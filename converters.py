from pyspark.sql import SparkSession

class EventConverter:
    def __init__(self, spark_session=None):
        self.spark = spark_session or SparkSession.builder.getOrCreate()

    def to_pandas(self, root_data):
        return root_data  # The data is already in pandas format from uproot

    def to_spark(self, root_data):
        pandas_df = self.to_pandas(root_data)
        return self.spark.createDataFrame(pandas_df)

