# Data Sweeper 📀

## Overview
**Data Sweeper** is a Streamlit-based application that allows users to upload CSV and Excel files, perform data cleaning operations, visualize data, and convert files between formats.

## Features
- Upload multiple CSV or Excel files 📂
- Preview uploaded files in a dataframe table 📋
- Perform data cleaning:
  - Remove duplicates ✅
  - Fill missing values with mean 🛠️
- Select specific columns for processing 🎯
- Visualize data with bar charts 📊
- Convert files between CSV and Excel formats 🔄
- Download processed files easily ⬇️

## Installation
To use Data Sweeper locally, follow these steps:

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/data-sweeper.git
   cd data-sweeper
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the Streamlit app with:
```sh
streamlit run app.py
```

## Requirements
- Python 3.x
- Streamlit
- Pandas

Ensure all dependencies are installed via:
```sh
pip install -r requirements.txt
```

## Contributing
Feel free to fork this project and submit pull requests to improve functionality! 🚀

## License
This project is licensed under the MIT License.

