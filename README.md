# Financial Data Engineering & Volatility Portfolio Analysis
### Objective

In financial environments, valuable insights are rarely limited by modelling techniques they are limited by data quality, fragmentation, and poor pipelines. Market data is often scattered across files, formats, and systems, making even basic analysis unreliable without a strong data engineering foundation.

This project was built to address that real-world problem. It delivers an end-to-end financial data pipeline that first solves the problem of fragmented stock price data and then applies that clean, structured data to a volatility-based portfolio strategy. Together, the two components reflect how data engineering directly enables better financial analysis and investment decisions.

### Project-1: Building Market Data Pipeline

<img width="520" alt="image" src="https://github.com/user-attachments/assets/4af33ff0-e882-4384-a59b-a13c30cd0ffb" />

The first phase focuses on a core industry problem: combining stock price data from multiple sources into a single, trusted dataset. Rather than assuming clean inputs, the pipeline is designed to handle inconsistent files, validate metadata, and enforce structure at every stage. Using Python, the solution extracts ticker information from a central configuration file, reads individual price datasets, validates column formats and ticker mappings, and consolidates everything into a unified JSON output. 

Each step mirrors real ETL workflows used in financial systems, where data reliability is as important as data availability. The pipeline is modular, portable, and deliberately avoids hardcoded paths or assumptions. This makes it easy to extend to new tickers, exchanges, or time periods without rewriting core logic. By the end of this phase, fragmented raw files are transformed into a clean, analysis-ready dataset that can be confidently reused across downstream analytics and modelling tasks.

At its core, this project demonstrates how strong data engineering practices turn messy market data into a dependable analytical asset.

### Project-1 Structure
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

### Key Functionality
The project enables users to:
- Read stock ticker information from a text file
- Extract stock price data from multiple files
- Verify and validate input data
- Combine stock price information into a comprehensive JSON file

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

### Requirements
- Python 3.x
- Standard Python libraries (os, json)

### Usage
1. Ensure all project files are in the correct directory structure
2. Run the `zid_project1.py` script
3. The script will generate a JSON file with combined stock data

### Notes
- The project is designed to be portable across different computing environments
- Avoid hardcoding specific paths or ticker names

### Potential Research Applications
- Stock price analysis
- Financial data aggregation
- Comparative stock performance studies


## Project 2 - Volatility-Driven Portfolio Strategy Analysis

With a reliable data foundation in place, the second phase applies the pipeline output to a practical financial use case: evaluating whether stock volatility can be used as a systematic investment signal. This component builds a complete analytical workflow, calculating daily and monthly returns, measuring stock-level volatility, and constructing volatility-sorted portfolios. Stocks are grouped based on their volatility characteristics, and equal-weighted as well as long–short portfolios are created to compare performance across risk profiles.Rather than focusing on a single time snapshot, the analysis spans multiple market cycles, allowing portfolio behaviour to be evaluated across different economic conditions. The workflow emphasizes repeatability and transparency, ensuring that results are driven by data and methodology rather than manual intervention.This phase highlights how clean engineering upstream directly enables rigorous financial analysis downstream, bridging the gap between raw market data and investment insights.

### Project-2 Structure

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

### Workflow 

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

### Analysis Approach

**Time Period**: 2000-12-29 to 2021-08-31

**Methodology**: 
  - Tertile portfolio sorting based on volatility
  - Equal-weighted portfolio construction
  - Comparative performance analysis

### Key Insights

- Investigate the relationship between stock volatility and returns
- Test the hypothesis of volatility-based investment strategies
- Provide empirical evidence for investment decision-making

### Analytical Techniques

- Descriptive Statistics
- Portfolio Sorting
- Return Calculation
- Hypothesis Testing
- Performance Metrics Computation

### Skills 
- End-to-end ETL pipeline design (Extract, Transform, Load)
- Data Engineering
- Advanced Python Programming
- Statistical Analysis
- Data validation, integrity checks, and schema enforcement
- Modular and reusable pipeline architecture
- Portable, environment-agnostic code design

### Why This Project Matters

What makes this project stand out is not a single model or metric, but the end-to-end ownership of the data lifecycle. From ingestion and validation to portfolio construction and performance evaluation, every step is designed with real financial environments in mind.

Together, these elements reflect how modern analytics teams operate where engineering discipline and financial reasoning work hand in hand.

### Conclusion

This project showcases how disciplined data engineering enables meaningful financial insights. By treating data quality as a first-class problem and linking it directly to investment analysis, the project reflects the kind of thinking required in data-driven financial and analytics roles where reliable decisions begin long before modelling starts.

### Contact
For inquiries or collaborations, feel free to connect with me on [www.linkedin.com/in/himarohinimallina] or check out more of my work on (https://github.com/z5450851HimaMallina).

Thank you
