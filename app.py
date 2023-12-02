# from flask import Flask, render_template, request
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('news_scraper.html')

# @app.route('/fetch', methods=['POST'])
# def fetch():
#     if request.method == 'POST':
#         link = request.form.get('link')

#         try:
#             response = requests.get(link)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # paras = soup.find_all('p')
#             # paras_joined = ''
#             # for string in paras:
#             #     paras_joined.join( string.text)
#             content = soup.text()
#         except Exception as e:
#             return render_template('news_scraper.html', error=str(e))

#         return render_template('news_scraper.html', content=content)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('news_scraper.html')

@app.route('/fetch', methods=['GET','POST'])
def fetch():
    link = ''
    header_description = ''
    paragraphs = ''
    if request.method == 'POST':
        link = request.form.get('link')

        try:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            header_description = soup.title.string if soup.title else "No header found"
            paragraphs = [p.get_text() for p in soup.find_all('p')]
        except Exception as e:
            return render_template('news_scraper.html', error=str(e))

        return render_template('news_scraper.html', header_description=header_description, paragraphs=paragraphs,news_url = link)

if __name__ == '__main__':
    app.run(debug=True)
