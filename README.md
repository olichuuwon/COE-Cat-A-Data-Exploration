# COE Cat A Data Exploration

This is a Streamlit application for exploring COE (Certificate of Entitlement) Category A price history interactively.

## Features

- Upload CSV file with COE data
- Interactive date filtering
- Line chart visualization with tooltips
- Data preview table

## Requirements

- Python 3.x
- streamlit
- pandas
- altair

## How to Run

1. Install dependencies: `pip install streamlit pandas altair`
2. Run the app: `streamlit run main.py`
3. Upload the `coe_catA_full_clean.csv` file in the app

## Data Format

The CSV file should contain:

- `date`: Date column (parseable as datetime)
- `Cat_A`: Numeric price values for COE Category A
