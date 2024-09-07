from pyspark_executor import PySparkExecutor
from io_handlers import ROOTReader
from converters import EventConverter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class PipelineManager:
    def __init__(self):
        self.executor = PySparkExecutor()

    def load_data(self, input_file):
        reader = ROOTReader(input_file)
        events = reader.read_events()
        converter = EventConverter(self.executor.spark)
        return converter.to_spark(events)

    def analyze_data(self, spark_df):
        # Convert Spark DataFrame to Pandas for analysis
        pandas_df = spark_df.toPandas()

        # Example columns (these may differ based on your ROOT file structure)
        pt1 = pandas_df['pt1']
        pt2 = pandas_df['pt2']
        eta1 = pandas_df['eta1']
        eta2 = pandas_df['eta2']
        phi1 = pandas_df['phi1']
        phi2 = pandas_df['phi2']
        
        # Calculate invariant mass
        def calculate_invariant_mass(pt1, pt2, eta1, eta2, phi1, phi2):
            mass1 = 0.105  # muon mass in GeV/c^2, example
            mass2 = 0.105  # muon mass in GeV/c^2, example
            
            E1 = np.sqrt(pt1**2 + mass1**2)
            E2 = np.sqrt(pt2**2 + mass2**2)
            px1 = pt1 * np.cos(phi1)
            py1 = pt1 * np.sin(phi1)
            pz1 = pt1 * np.sinh(eta1)
            px2 = pt2 * np.cos(phi2)
            py2 = pt2 * np.sin(phi2)
            pz2 = pt2 * np.sinh(eta2)
            
            # Calculate invariant mass
            E_total = E1 + E2
            px_total = px1 + px2
            py_total = py1 + py2
            pz_total = pz1 + pz2
            invariant_mass = np.sqrt(E_total**2 - (px_total**2 + py_total**2 + pz_total**2))
            return invariant_mass

        invariant_mass = calculate_invariant_mass(pt1, pt2, eta1, eta2, phi1, phi2)
        
        # Add invariant mass to the DataFrame
        pandas_df['invariant_mass'] = invariant_mass

        # Plot the invariant mass distribution
        plt.hist(invariant_mass, bins=50, histtype='step', label='Invariant Mass (GeV/c^2)')
        plt.xlabel('Invariant Mass (GeV/c^2)')
        plt.ylabel('Events')
        plt.title('Invariant Mass Distribution')
        plt.legend()
        plt.show()

        # Plot the pt distribution
        plt.hist(pt1, bins=50, histtype='step', label='pt1')
        plt.hist(pt2, bins=50, histtype='step', label='pt2')
        plt.xlabel('Transverse Momentum (GeV/c)')
        plt.ylabel('Events')
        plt.title('Transverse Momentum Distribution')
        plt.legend()
        plt.show()

    def run_analysis(self, input_file):
        data = self.load_data(input_file)
        self.analyze_data(data)

    def shutdown(self):
        self.executor.shutdown()

if __name__ == "__main__":
    manager = PipelineManager()
    manager.run_analysis("DY1011.root")  # Path to your ROOT file
    manager.shutdown()

