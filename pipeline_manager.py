from io_handlers import ROOTReader
from physics_analysis import calculate_invariant_mass
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os

class PipelineManager:
    def __init__(self, file_path):
        self.reader = ROOTReader(file_path)
        self.output_dir = "output_plots"
        os.makedirs(self.output_dir, exist_ok=True)  # Ensure output directory exists

    def run_analysis(self):
        # Read the tree data
        data = self.reader.read_tree("events;1")

        # Extract muon kinematic data (these are lists of arrays due to variable-length structure)
        muon_px = data["Muon_Px"].to_numpy()
        muon_py = data["Muon_Py"].to_numpy()
        muon_pz = data["Muon_Pz"].to_numpy()
        muon_E = data["Muon_E"].to_numpy()
        n_muons = data["NMuon"].to_numpy()

        # Invariant mass calculation for muon pairs (consider events with at least 2 muons)
        inv_masses = []
        for event in range(len(n_muons)):
            if n_muons[event] >= 2:  # Only consider events with at least 2 muons
                px1, py1, pz1, E1 = muon_px[event][0], muon_py[event][0], muon_pz[event][0], muon_E[event][0]
                px2, py2, pz2, E2 = muon_px[event][1], muon_py[event][1], muon_pz[event][1], muon_E[event][1]
                inv_mass = calculate_invariant_mass(px1, py1, pz1, E1, px2, py2, pz2, E2)
                inv_masses.append(inv_mass)

        # Save invariant mass distribution and statistics
        self.plot_invariant_mass(inv_masses)

        # Plot and save transverse momentum distribution for the first muon
        self.plot_transverse_momentum(muon_px, muon_py, n_muons)

    def plot_invariant_mass(self, inv_masses):
        # Convert to numpy array
        inv_masses = np.array(inv_masses)

     
        plt.figure(figsize=(8, 6))
        n, bins, patches = plt.hist(inv_masses, bins=50, density=True, histtype='step', label='Invariant Mass (GeV/c^2)', color='darkblue')

        # Fit a Gaussian to the invariant mass data
        mu, std = norm.fit(inv_masses)

      
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'r--', linewidth=2, label=f'Gaussian Fit: mean={mu:.2f}, std={std:.2f}')

        plt.xlabel('Invariant Mass (GeV/c^2)')
        plt.ylabel('Probability Density')
        plt.title('Invariant Mass Distribution with Gaussian Fit')
        plt.legend(loc='upper right')

        # Add grid
        plt.grid(True, linestyle='--', alpha=0.7)

        # Save plot
        plot_path = os.path.join(self.output_dir, "invariant_mass_distribution.png")
        plt.savefig(plot_path)
        print(f"Invariant Mass plot saved to {plot_path}")

        # Save results to a text file
        result_path = os.path.join(self.output_dir, "invariant_mass_results.txt")
        with open(result_path, "w") as f:
            f.write(f"Gaussian Fit Results:\n")
            f.write(f"Mean: {mu:.2f} GeV/c^2\n")
            f.write(f"Standard Deviation: {std:.2f} GeV/c^2\n")
        print(f"Invariant Mass results saved to {result_path}")

        # Show the plot
        plt.show()

    def plot_transverse_momentum(self, muon_px, muon_py, n_muons):
        # Calculate transverse momentum for each muon
        muon_pt = []
        for event in range(len(n_muons)):
            if n_muons[event] >= 1:  # Check if there is at least 1 muon in the event
                for i in range(n_muons[event]):  # Loop over all muons in the event
                    pt = np.sqrt(muon_px[event][i]**2 + muon_py[event][i]**2)
                    muon_pt.append(pt)

        plt.figure(figsize=(8, 6))
        plt.hist(muon_pt, bins=50, histtype='step', label='Muon pt', color='darkgreen')

    
        plt.xlabel('Transverse Momentum (GeV/c)')
        plt.ylabel('Number of Muons')
        plt.title('Muon pt Distribution')
        plt.legend(loc='upper right')

        plt.grid(True, linestyle='--', alpha=0.7)

        # Save plot
        plot_path = os.path.join(self.output_dir, "muon_pt_distribution.png")
        plt.savefig(plot_path)
        print(f"Transverse Momentum plot saved to {plot_path}")

        # Show the plot
        plt.show()

if __name__ == "__main__":
    pipeline = PipelineManager("data/dy.root")
    pipeline.run_analysis()

