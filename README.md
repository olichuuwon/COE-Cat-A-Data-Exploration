# COE Cat A Data Exploration

This is a Streamlit application for exploring COE (Certificate of Entitlement) Category A price history interactively.

## Features

- Interactive date filtering
- Line chart visualization with tooltips
- Data preview table
- Loads included COE data automatically

## Requirements

- Python 3.x
- streamlit
- pandas
- altair

## How to Run

### Local Development

1. Install dependencies: `pip install streamlit pandas altair`
2. Run the app: `streamlit run main.py`
3. The app loads the included `coe_catA_full_clean.csv` file automatically

### Docker

1. Build the Docker image (linux/amd64 platform only): `docker build --platform linux/amd64 -t coe-cat-a-explorer .`
2. Run the container: `docker run -p 8501:8501 coe-cat-a-explorer`
3. Open your browser to `http://localhost:8501`
4. The app loads the included `coe_catA_full_clean.csv` file automatically

## Data Format

The CSV file should contain:

- `date`: Date column (parseable as datetime)
- `Cat_A`: Numeric price values for COE Category A
