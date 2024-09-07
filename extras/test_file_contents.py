import uproot

# Path to your ROOT file (update this path if needed)
file_path = "dy.root"

# Open the ROOT file
file = uproot.open(file_path)

# List all available keys (we know there is 'events;1')
print("File keys:", file.keys())

# Access the tree 'events;1'
tree = file['events;1']

# List the available branches in the 'events;1' tree
print("Branches in 'events;1':", tree.keys())

