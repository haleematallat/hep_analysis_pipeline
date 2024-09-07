from pyspark_executor import PySparkExecutor
from io_handlers import ROOTReader
from converters import EventConverter

class PipelineManager:
    def __init__(self):
        self.executor = PySparkExecutor()

    def load_data(self, input_file):
        reader = ROOTReader(input_file)
        events = reader.read_events()
        converter = EventConverter(self.executor.spark)
        return converter.to_spark(events)

    def analyze_data(self, spark_df):
        # Placeholder for data analysis logic
        return spark_df

    def run_analysis(self, input_file):
        data = self.load_data(input_file)
        analyzed_data = self.analyze_data(data)
        analyzed_data.show()

    def shutdown(self):
        self.executor.shutdown()

if __name__ == "__main__":
    manager = PipelineManager()
    manager.run_analysis("DY1011.root")
    manager.shutdown()

