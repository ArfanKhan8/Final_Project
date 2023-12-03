from pyspark.sql import SparkSession, Row
from pyspark.ml import PipelineModel
from pyspark.sql.types import *
import json
import re

class NewsPredictor:

    def __init__(self) -> None:
        self.create_spark_session()
        self.load_data()
        self.create_dataframe()
        self.predict()


    def create_spark_session(self):
        # Create a Spark session
        self.spark = SparkSession.builder.appName("NewsPredictor").getOrCreate()

    def load_model(self):
        # Load the saved model
        saved_model_path = "./fake_news_model"
        self.loaded_model = PipelineModel.load(saved_model_path)


    def load_data(self, data:str):
        # Assuming 'new_data' is a PySpark DataFrame with the same structure as your training data
        # You can load your new data or create it as needed
        self.data = re.sub('\W+',' ', data )

    def create_dataframe(self):
        self.schema = StructType([StructField("text", StringType(), True)])
        self.df = self.spark.createDataFrame(([self.data]),StringType()).toDF('text') 


    def predict(self):
        # Make predictions on the new data
        predictions = self.loaded_model.transform(self.df)

        # Show the predictions
        # predictions.show()
        print(predictions.collect()[0][5])

        # Stop the Spark session
        self.spark.stop()