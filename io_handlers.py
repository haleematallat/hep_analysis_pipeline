import uproot
import pandas as pd

class ROOTReader:
    def __init__(self, file_path):
        self.file = uproot.open(file_path)

    def read_tree(self, tree_name="events;1"):
        # Extract relevant branches: Muon kinematic data
        branches = ["Muon_Px", "Muon_Py", "Muon_Pz", "Muon_E", "NMuon"]
        tree = self.file[tree_name]
        data = tree.arrays(branches, library="pd")  # Convert to pandas DataFrame
        return data

