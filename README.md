## Project-1 & Project-2
### Project-1: Combining Data from Multiple Sources
Finance data often requires assembling datasets from various sources especially when dealing with stock prices.

<img width="520" alt="image" src="https://github.com/user-attachments/assets/4af33ff0-e882-4384-a59b-a13c30cd0ffb" />


## Project Overview
This project is designed to help combine stock price information from multiple sources by creating a robust and flexible data acquisition, cleaning, and merging pipeline in Python.

## Project Structure
```
project1/
│
├── zid_project1.py       # Main Python script for data processing
├── TICKERS.txt           # List of stock tickers and exchanges
├── README.txt            # Original README with data file specifications
│
└── data/
    └── <tic>_prc.dat     # Individual stock price data files
```

## Key Functionality
The project enables users to:
- Read stock ticker information from a text file
- Extract stock price data from multiple files
- Verify and validate input data
- Combine stock price information into a comprehensive JSON file

## Main Components

### Data Processing Steps
1. Set file and folder locations
2. Defined data source column formats
3. Read and process ticker information
4. Extract stock price data from individual files
5. Combined data into a single dictionary
6. Exported data to a JSON file

### Functions
- `get_tics()`: Reads and formats ticker information
- `read_dat()`: Reads stock price data files
- `line_to_dict()`: Converts file lines to dictionaries
- `verify_tickers()`: Validates ticker information
- `verify_cols()`: Validates column names
- `create_data_dict()`: Combines stock data
- `create_json()`: Exports data to JSON

## Requirements
- Python 3.x
- Standard Python libraries (os, json)

## Usage
1. Ensure all project files are in the correct directory structure
2. Run the `zid_project1.py` script
3. The script will generate a JSON file with combined stock data

## Notes
- The project is designed to be portable across different computing environments
- Avoid hardcoding specific paths or ticker names

## Potential Research Applications
- Stock price analysis
- Financial data aggregation
- Comparative stock performance studies

## Limitations
- Requires consistently formatted input files
- Depends on the specific structure of the input data files


## PROJECT 2
# Stock Volatility Portfolio Analysis 

## Project Overview

This project explores the fascinating relationship between stock volatility and returns through a comprehensive data analysis pipeline. By leveraging Python and financial data processing techniques, we investigate whether investors can generate significant returns by strategically investing in volatility-based portfolios.

## Key Technologies

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Git**: Collaborative version control
- **Financial Data Processing**: Advanced ETL techniques

## Research Objectives

Our project aims to:
- Construct portfolios based on stock volatility characteristics
- Analyze the potential of volatility-driven investment strategies
- Develop robust data engineering and financial analysis skills

## Project-2 Structure

```
project2/
├── config.py
├── zid_project2_etl.py
├── zid_project2_characteristics.py
├── zid_project2_main.py
├── zid_project2_portfolio.py
└── data/
    └── <stock price CSV files>
```

## Workflow 

### 1. Data Extraction & Transformation (ETL)
- Extract stock price data from CSV files
- Calculate daily and monthly stock returns
- Prepare data for analysis

### 2. Volatility Characteristics
- Compute monthly volatility for each stock
- Generate comprehensive financial metrics

### 3. Portfolio Construction
- Create equal-weighted portfolios
- Implement long-short portfolio strategy
- Analyze portfolio performance

## Analysis Approach

- **Time Period**: 2000-12-29 to 2021-08-31
- **Methodology**: 
  - Tertile portfolio sorting based on volatility
  - Equal-weighted portfolio construction
  - Comparative performance analysis

## Key Insights

- Investigate the relationship between stock volatility and returns
- Test the hypothesis of volatility-based investment strategies
- Provide empirical evidence for investment decision-making

## Analytical Techniques

- Descriptive Statistics
- Portfolio Sorting
- Return Calculation
- Hypothesis Testing
- Performance Metrics Computation

## Skills Developed

- Advanced Python Programming
- Financial Data Engineering
- Statistical Analysis
- Collaborative Software Development

## Research Methodology

1. **Data Collection**: Aggregate stock price data
2. **Preprocessing**: Clean and transform financial datasets
3. **Volatility Calculation**: Compute monthly stock volatilities
4. **Portfolio Construction**: Create volatility-based portfolios
5. **Performance Analysis**: Evaluate portfolio returns and statistical significance

## Collaborative Development

- **Version Control**: Git-based collaborative workflow
- **Team Coordination**: Shared GitHub repository
- **Continuous Integration**: Regular code reviews and merges

---


## Contact
For inquiries or collaborations, feel free to connect with me on [www.linkedin.com/in/himarohinimallina] or check out more of my work on (https://github.com/z5450851HimaMallina).

Thank you
