import uproot

class ROOTReader:
    def __init__(self, file_path):
        self.file = uproot.open(file_path)

    def read_events(self, tree_name="Events"):
        return self.file[tree_name].arrays(library="pd")  # Returns a pandas DataFrame

if __name__ == "__main__":
    reader = ROOTReader("DY1011.root")
    events = reader.read_events()
    print(events.head())
