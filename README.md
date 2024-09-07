
# HEP Analysis Pipeline

This project provides a high-energy physics (HEP) data analysis pipeline built using **PySpark**, **uproot**, **awkward-pandas**, **numpy**, and **matplotlib**. The pipeline is designed for analyzing event-level data from particle physics experiments, such as ROOT files from CERN Open Data, focusing on muon-related processes like the Drell-Yan process. It calculates physical quantities such as invariant mass and transverse momentum and generates informative plots.

## Table of Contents
- [Project Structure](#project-structure)
- [Description of Dataset](#description-of-dataset)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Pipeline](#running-the-pipeline)
- [Using Your Own Data](#using-your-own-data)
- [Adding Your Own Functions](#adding-your-own-functions)
- [Design Choices](#design-choices)
  - [Why PySpark?](#why-pyspark)
  - [Why awkward-pandas?](#why-awkward-pandas)
  - [Why uproot?](#why-uproot)
- [Other Languages](#other-languages)

---

## Project Structure

The main files in this repository are:

- **`pipeline_manager.py`**  
  This is the main entry point of the pipeline. It manages the reading of ROOT files, analysis of data, and plotting of results. It uses other helper modules like `io_handlers.py` and `physics_analysis.py`.

- **`io_handlers.py`**  
  This file contains the `ROOTReader` class, which handles reading the ROOT files using the `uproot` and `awkward-pandas` libraries, converting them into easily manipulated `pandas` DataFrames. These tools simplify the handling of complex, jagged data structures, which are common in particle physics experiments.

- **`physics_analysis.py`**  
  This file contains functions for calculating physical quantities, such as the invariant mass of particle pairs. You can extend this file with additional physics analysis functions as needed.

- **`output_plots/`**  
  This directory stores the generated plots from running the pipeline, including invariant mass and transverse momentum histograms.

- **`data/`**  
  A placeholder for your own data files (e.g., `.root` files). You can place your own files here and modify the pipeline to analyze them.

---

## Description of Dataset

The data used in this pipeline comes from the **CERN Open Data Portal**. The example dataset is designed for analyzing events related to the **Drell-Yan process**, where a virtual photon or Z boson decays into a pair of muons. This is a common process used to study the production of heavy particles such as the Z boson.

- **Example dataset**: [[Drell-Yan to Muons]](https://opendata.cern.ch/record/206)
- **ROOT File**: Contains the kinematic information for each event, such as:
  - `Muon_Px`, `Muon_Py`, `Muon_Pz`, `Muon_E`: The momentum and energy components of muons.
  - `NMuon`: Number of muons per event.
  - **Other potential branches**: Data for jets, electrons, photons, and other physics objects depending on the dataset.

This pipeline processes the data to compute key physical quantities such as the **invariant mass** of muon pairs and the **transverse momentum** of individual muons. The dataset is structured in such a way that each event can contain multiple muons, and the muons' kinematic information is stored as jagged arrays, which are handled efficiently using the `awkward-pandas` library.

---

## Requirements

The following libraries are required for this project:

- `uproot` (for reading ROOT files)
- `awkward-pandas` (for handling jagged arrays and converting them to pandas DataFrames)
- `pandas` (for DataFrame operations)
- `numpy` (for numerical calculations)
- `matplotlib` (for plotting)
- `scipy` (for Gaussian fitting and additional statistics)

To install the required libraries, run:

```bash
pip install uproot awkward-pandas pandas numpy matplotlib scipy
```

If you're using a virtual environment (recommended), make sure it is activated before installing these packages.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/haleematallat/hep_analysis_pipeline.git
cd hep_analysis_pipeline
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to keep project dependencies isolated:
```bash
python3 -m venv hep_env
source hep_env/bin/activate  # On macOS/Linux
```

### 3. Install the Required Libraries

Make sure you're inside the project directory, then install the required dependencies:
```bash
pip install -r requirements.txt
# Or manually install using:
pip install uproot awkward-pandas pandas numpy matplotlib scipy
```

---

## Running the Pipeline

The pipeline is designed to analyze ROOT files containing particle physics event data and calculate physics observables like **invariant mass** and **transverse momentum**. Here’s how to run the pipeline:

1. **Ensure you have your data file** (e.g., `dy.root` containing muon kinematics). You can download such data from [CERN Open Data Portal](http://opendata.cern.ch/record/2007).
   
2. **Run the pipeline** using the following command:
   ```bash
   python3 pipeline_manager.py
   ```

3. **Output**:  
   The pipeline will:
   - Calculate the **invariant mass** of muon pairs and plot the results.
   - Calculate the **transverse momentum** distribution for muons.
   - Save the plots in the `output_plots/` folder:
     - `invariant_mass_distribution.png`
     - `muon_pt_distribution.png`
   - The Gaussian fit results (mean and standard deviation of the invariant mass) will be saved in a text file:
     - `output_plots/invariant_mass_results.txt`

---

## Using Your Own Data

You can easily replace the example data with your own ROOT files and modify the pipeline accordingly.

1. **Replace the Data File**:  
   Copy your ROOT file into the `data/` directory and update the path in `pipeline_manager.py`:
   ```python
   pipeline = PipelineManager("data/your_data_file.root")
   ```

2. **Ensure Your Data Structure**:  
   The pipeline expects your ROOT file to have branches like `Muon_Px`, `Muon_Py`, `Muon_Pz`, and `Muon_E`. If your data contains different branches (e.g., electron data or jet data), modify the `ROOTReader` class in `io_handlers.py` to extract the relevant branches.

3. **Run the Pipeline**:  
   After updating the data file, run the pipeline as described above:
   ```bash
   python3 pipeline_manager.py
   ```



## Adding Your Own Functions

You can extend the pipeline to calculate other physics quantities or analyze other types of particles (e.g., electrons, jets). To do this:

1. **Add Your Function to `physics_analysis.py`**:  
   Add your own custom function for calculating a new physics quantity. For example, to calculate transverse energy (`E_T`):
   ```python
   def calculate_transverse_energy(px, py):
       return np.sqrt(px**2 + py**2)
   ```

2. **Update `pipeline_manager.py`** to Call Your Function:  
   Call your new function in the analysis section of the pipeline:
   ```python
   et = calculate_transverse_energy(px, py)
   ```

3. **Plot and Save Your Results**:  
   Use `matplotlib` to visualize and save the results. You can follow the existing examples in `pipeline_manager.py`.



## Design Choices

### Why PySpark?

**PySpark** was chosen for its scalability and ability to handle large datasets efficiently. In HEP experiments, datasets can grow to terabytes in size. **PySpark** allows for distributed data processing, which can help when analyzing massive amounts of particle collision data. Although the current pipeline operates on local data, using **PySpark** sets a foundation for future scalability if more significant event data is used.

**Key reasons for using PySpark**:
- **Scalability**: PySpark enables distributed processing, which is beneficial for analyzing large datasets.
- **Integration with Hadoop or cloud clusters**: In large HEP experiments, datasets are often stored and processed on clusters. PySpark allows for easy integration with these big data infrastructures.
- **Interoperability**: PySpark works seamlessly with other Python libraries, making it easy to integrate Spark’s distributed power with libraries like `numpy`, `pandas`, and `matplotlib`.

### Why awkward-pandas?

`awkward-pandas` is used to handle the jagged arrays (or irregularly shaped arrays) that are common in ROOT files. Jagged arrays occur when different events have a different number of particles (e.g., some events have 2 muons, while others have only 1). This library seamlessly converts `awkward` arrays (used by `uproot`) into `pandas` DataFrames, making them easier to process.

### Why uproot?

`uproot` is chosen over `PyROOT` because it’s lightweight, fast, and works well with the broader scientific Python ecosystem (like `pandas` and `numpy`). It allows ROOT data to be easily manipulated in Python without requiring a full ROOT

 installation.

### Flexibility in Analysis

The pipeline is designed to be easily adaptable. By modifying the functions in `physics_analysis.py`, users can add new analyses (e.g., jet studies, electron analysis) or compute other physical observables (e.g., missing transverse energy).



## Other Languages

This project is developed entirely in **Python**. All the major components—data handling, physics calculations, and plotting—are written in Python using libraries like `uproot`, `awkward-pandas`, `pandas`, and `matplotlib`.

If you wish to integrate this pipeline with other languages (e.g., C++ or Java for more intensive computational tasks), PySpark can be extended to call Java or Scala functions. However, this current version focuses solely on Python for simplicity and ease of use.




## Contributing
Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request with your improvements.

## License

This project is licensed under the terms of the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/). 
