from pyspark.sql import SparkSession

class PySparkExecutor:
    def __init__(self, app_name="HEP_Analysis"):
        self.spark = SparkSession.builder.appName(app_name).getOrCreate()

    def process_data(self, data_rdd):
        # Implement data processing logic using Spark RDDs or DataFrames
        pass

    def shutdown(self):
        self.spark.stop()

if __name__ == "__main__":
    executor = PySparkExecutor()
    data = executor.spark.range(1000).toDF("number")
    data.show()
    executor.shutdown()

