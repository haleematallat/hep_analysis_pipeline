# HEP Analysis Pipeline

This project is a High Energy Physics (HEP) data analysis pipeline built using PySpark and Uproot. The pipeline is designed to read and process HEP data stored in ROOT files, convert it to Spark DataFrames, and perform large-scale distributed data analysis.

## Features
- Read HEP data from ROOT files using `uproot`.
- Process and convert data into PySpark DataFrames for efficient distributed processing.
- Modular design to easily extend and modify components.
- Example script for reading, processing, and analyzing HEP data.

## Requirements
- Python 3.x
- Virtual environment (optional, but recommended)
- PySpark
- Uproot
- Pandas
- Matplotlib
- Plotly
- Dash

## Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/haleematallat/hep_analysis_pipeline.git
cd hep_analysis_pipeline
```

### Step 2: Set up a virtual environment (optional but recommended)
```bash
python3 -m venv hep_env
source hep_env/bin/activate
```

### Step 3: Install dependencies
```bash
pip install pyspark uproot pandas matplotlib plotly dash
```

### Step 4: Create or obtain a ROOT file
If you don't already have a `data.root` file, you can create a simple example using `uproot` with the provided script:
```bash
python3 create_root_file.py
```

This will generate a file named `data.root` with random event data.

## Usage

### Run the PySpark-based HEP Data Analysis Pipeline

```bash
python3 pipeline_manager.py
```

This will:
- Load data from a ROOT file (default: `data.root`).
- Convert the data to a PySpark DataFrame.
- Process and analyze the data (add your own analysis logic in the script).

### Example ROOT Data Processing
- The `pyspark_executor.py` handles Spark session creation.
- `io_handlers.py` loads ROOT data into Pandas DataFrames using `uproot`.
- `converters.py` converts Pandas DataFrames to PySpark DataFrames for distributed processing.

## Project Structure
- **create_root_file.py**: Generates a sample `data.root` file with random data.
- **pyspark_executor.py**: Handles the Spark session for processing data.
- **io_handlers.py**: Reads ROOT files using `uproot`.
- **converters.py**: Converts ROOT data from Pandas DataFrames to PySpark DataFrames.
- **pipeline_manager.py**: Main script to run the data analysis pipeline.

## Contributing
Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

