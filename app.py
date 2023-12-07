from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from predictor import NewsPredictor

app = Flask(__name__)

@app.route('/')
def index():
    result = 2
    return render_template('news_scraper.html', result =result)

@app.route('/fetch', methods=['GET','POST'])
def fetch():
    result = 2
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
            paragraphs_to_string =" ".join(paragraphs) 
            predictor = NewsPredictor(paragraphs_to_string)
            result = predictor.predict()
        except Exception as e:
            return render_template('news_scraper.html', error=str(e))

        return render_template('news_scraper.html', header_description=header_description, paragraphs=paragraphs,news_url = link, result = result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)
