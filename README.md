# Pandas Mastery

**A comprehensive, hands-on guide to mastering Pandas for data manipulation, analysis, and visualization.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas 2.0+](https://img.shields.io/badge/pandas-2.0+-150458.svg?logo=pandas)](https://pandas.pydata.org/)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-notebook-F37626.svg?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributors](https://img.shields.io/github/contributors/InfinitePraveen/Pandas-Mastery)](https://github.com/InfinitePraveen/Pandas-Mastery/graphs/contributors)

---

## 📖 About This Repository

This repository documents my **complete learning journey** to mastering **Pandas**, the essential Python library for data science. It serves as a structured, example-driven guide, taking you from fundamental data structures to advanced topics like time series analysis and data visualization.

Whether you are a **beginner** taking your first steps in data science, a **student** solidifying your understanding, or an **experienced practitioner** in need of a quick reference, this resource is designed for you. Every concept is explored through executable Jupyter notebooks using real-world inspired datasets, embodying a "learning by doing" philosophy.

### 🎯 My Learning Philosophy

I believe the best way to learn is by doing. This repository is a reflection of that belief, containing not just code, but also practical exercises and my own handwritten notes. It documents a journey from theory to application, with a focus on building practical, job-ready skills.

---

## 📋 Table of Contents

- [Technical Requirements](#technical-requirements)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation and Usage](#installation--usage)
- [How to Use This Repository](#how-to-use-this-repository)
- [Key Topics Covered](#key-topics-covered)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## ⚙️ Technical Requirements

| Requirement | Version |
| :--- | :--- |
| **Python** | 3.8 or higher |
| **Pandas** | 2.0 or higher |
| **NumPy** | 1.24 or higher |
| **Jupyter Notebook** | Latest stable version |
| **Other Libraries** | See `requirements.txt` for full list |

---

## 📁 Repository Structure

The repository is organized into logical modules to ensure a smooth learning flow:

| Folder | Topic | Status | Key Notebooks |
| :--- | :--- | :--- | :--- |
| **`01 Basics`** | Pandas Fundamentals | ✅ Completed | `01_series_dataframe.ipynb`, `02_reading_writing_data.ipynb`, `03_inspecting_dataframes.ipynb` |
| **`02 Data Cleaning`** | Handling Messy Data | ✅ Completed | `01_handling_missing_values.ipynb`, `02_duplicates_outliers.ipynb`, `03_data_type_conversion.ipynb` |
| **`03 Data Selection`** | Filtering and Indexing | ✅ Completed | `01_selecting_columns_rows.ipynb`, `02_loc_iloc_differences.ipynb`, `03_conditional_filtering.ipynb` |
| **`04 Data Transformation`** | Manipulating Data | ✅ Completed | `01_apply_map_applymap.ipynb`, `02_creating_modifying_columns.ipynb`, `03_string_operations.ipynb` |
| **`05 Grouping and Aggregation`** | Summarizing Data | ✅ Completed | `01_groupby_basics.ipynb`, `02_aggregate_transform_filter.ipynb`, `03_pivot_tables_crosstab.ipynb` |
| **`06 Merging and Joining`** | Combining Datasets | ✅ Completed | `01_concatenation.ipynb`, `02_merging_dataframes.ipynb`, `03_joining_on_index.ipynb` |
| **`07 Time Series`** | Working with Dates | ✅ Completed | `01_datetime_indexing.ipynb`, `02_resampling_rolling.ipynb`, `03_time_zone_handling.ipynb` |
| **`08 Visualization`** | Plotting with Pandas | ✅ Completed | `01_line_bar_plots.ipynb`, `02_histogram_boxplot_scatter.ipynb`, `03_customization_subplots.ipynb` |
| **`09 Practical Assessment`** | Applied Problems | ✅ Completed | Real-world inspired exercises to test your skills |
| **`10 Experiments`** | Exploration and Testing | ✅ Completed | My personal sandbox for trying out new ideas and edge cases |
| **`11 HANDWRITTEN NOTES`** | Personal Study Notes | ✅ Completed | Scanned copies of my handwritten notes summarizing key concepts |

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system
- Basic knowledge of Python (variables, loops, functions, lists, dictionaries)
- Familiarity with NumPy is helpful but not required

### Installation and Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/InfinitePraveen/Pandas-Mastery.git
   cd Pandas-Mastery
   ```

2. **Set up a virtual environment (Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

   Navigate to the `notebooks/` directory and start with the `01 Basics` folder.

---

## 🚀 How to Use This Repository

1. **Follow the Modules in Order:** The modules are numbered for a logical progression. Start from `01 Basics` and work your way through.

2. **Read and Execute:** Open each Jupyter notebook, read the explanations, and execute the code cells. Experiment by changing the code and observing the results.

3. **Complete the Exercises:** The `09 Practical Assessment` folder contains problems that will test your understanding. Try to solve them independently.

4. **Refer to the Notes:** The handwritten notes in `11 HANDWRITTEN NOTES` provide a quick summary of key concepts and can be a great revision tool.

---

## 📚 Key Topics Covered

- **Core Data Structures:** `Series` and `DataFrame`
- **Data I/O:** Reading and writing data from/to CSV, Excel, and other formats
- **Data Cleaning:** Handling missing values, duplicates, outliers, and data type conversion
- **Data Selection and Filtering:** Using `loc`, `iloc`, and boolean indexing
- **Data Transformation:** Creating new columns, applying functions, and string operations
- **Data Aggregation:** Grouping data with `groupby()`, aggregation, and pivot tables
- **Data Combination:** Concatenating and merging DataFrames
- **Time Series Analysis:** Working with datetime indexes, resampling, and rolling windows
- **Data Visualization:** Creating various plots directly from Pandas

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy](https://numpy.org/)
- [Jupyter](https://jupyter.org/)
- All contributors and learners who find this resource helpful!

---

**Happy Coding!** 🐼✨
