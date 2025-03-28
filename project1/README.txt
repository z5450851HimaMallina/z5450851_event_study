Combining Data from Multiple Sources

Project Objective

The goal of this project is to develop the foundational skills necessary for data acquisition, cleaning, and merging. Finance research often requires assembling datasets from various sources, and in this project, you I have combined stock price data distributed across multiple files. The output will be a single JSON file containing the combined data.

This project will helpful to test the following skills:
	•	Handling different file formats and structures
	•	Writing general code that can adapt to different file formats and sources
	•	Importing, cleaning, and merging data
	•	Using Python functions to read and process large data files
	•	Storing the combined data in JSON format for further analysis

Files Included
	•	project_desc.pdf: Provides additional project details and instructions.
	•	README.txt: This file, which explains the project.
	•	TICKERS.txt: Contains a list of tickers and their corresponding exchanges.
	•	zid_project1.py: Contains all the functions that are required to complete this project. You will need to implement specific parts of this file.
	•	data/: Contains multiple .dat files with stock price data for various tickers. Each ticker from TICKERS.txt will have a corresponding .dat file.

Project Workflow

Step 1: Setting the location of files and folders

Set the correct paths for the project folder, data sub-folder, and TICKERS.txt file using the os module to ensure the code works on different systems.

Step 2: Defining Source Data Format

Define the column names and widths for the source data files based on the README.txt file. This will help in extracting the correct data fields from the .dat files.

Step 3: Implement the get_tics function

Writing a function that reads the TICKERS.txt file, formats the tickers, and returns a list of tickers.

Step 4: Implement the read_dat function

Writing a function that reads a stock price data file for a given ticker and returns its contents as a list of lines.

Step 5: Implement the line_to_dict function

Writing a function that converts a single line of data from the .dat file into a dictionary, mapping the column names to their values.

Step 6: Implement the verify_tickers function

Writing a function that verifies if the tickers provided are valid by checking them against the dictionary returned by get_tics.

Step 7: Implement the verify_cols function

Writing a function that verifies the column names against the predefined COLUMNS list and raises an exception if any of the columns are invalid.

Step 8: Implement the create_data_dict function

Writing a function that combines the data from multiple .dat files into a single dictionary, where each ticker has its own data.

Step 9: Implement the create_json function

Writing a function that saves the combined data dictionary into a JSON file.

Step 10: Evaluation and Analysis

Write an analysis explaining how stock returns can be influenced by journalists’ articles, and discuss the relationship between the short-run predictability of trading volume and stock returns.

⸻
 






# ---------------------------------------------------------------------------- 
#   About this file
# ---------------------------------------------------------------------------- 

This file contains information about the price DAT files. These files contain
fixed-width data for the following columns: 

  - 'Volume': The total number of shares traded on the day (in millions)

  - 'Date': The calendar day of this data. Each date is represented as 
            a four-digit year, a two-digit month, and a two-digit day 
            separated by hyphens. This is YYYY-MM-DD format.

  - 'Adj Close': The closing price of the stock, adjusted for dividends, 
            splits, and other events.

  - 'Close': The closing price at which the stock trades on the day, 
            unadjusted for dividends, splits, and other events.

  - 'Open': The initial price at which the stock trades for the day, 
            unadjusted for dividends, splits, and other events.

  - 'High': The highest price at which the stock trades for the day, 
            unadjusted for dividends, splits, and other events.

The data is in a fixed-width format. Instead of using delimiters, such as
a comma, to separate the data columns, data is simply presented as text,
with one data field leading directly to the next. For example, if the first
piece of information in a row is a four-character word (e.g. "blue"), the
next piece of information is a four-character number (e.g. "3.14"), and the
third piece of information is a one-character Boolean value (e.g. "t" for
true), the row will be presented as "blue3.14t". All data would need to meet
this format with no item shorter or longer than its specified length.

Identification of information in the file requires knowing the ordering
of the columns and the width of each column. Each line in your actual
stock price DAT file has exactly 80 characters. The information for the
first column starts at the beginning of the line and stops after the `n`
characters, where `n` is the width of the first column. The information for
the second column starts immediately after the first, stopping after `m`
characters. Thus, the second column contains information from character
`n+1` through `n+m`. The remaining columns follow this logic.

For instance, assume that the first column in the `DAT` files contains is
`Volume` and, based on the information you are given, the width of that column
is `14`. This means that the data for this column starts at the beginning of
the line and continue up to and including the 14th character in that line.
The data for the next column begins immediately after the 14th character,
with the 15th character in the line.

For specific DAT files, there's following information:

Column Name:
    column position : The order of this column in the file starting with 1. 
                      That is, the first column has column position 1, the 
                      second column has column position 2, and so on. 

    dtype :           The Pandas data type for this column

    width :           The number of characters in this column

# ---------------------------------------------------------------------------- 
#   Column information
# ---------------------------------------------------------------------------- 

Volume:
  column position: 1
  dtype: int64
  width: 14

Date:
  column position: 2
  dtype: datetime64
  width: 11

Adj Close:
  column position: 3
  dtype: float64
  width: 19

Close:
  column position: 4
  dtype: float64
  width: 10

Open:
  column position: 5
  dtype: float64
  width: 6

High:
  column position: 6
  dtype: float64
  width: 20

Contact
For inquiries or collaborations, feel free to connect with me on [www.linkedin.com/in/himarohinimallina] or check out more of my work on (https://github.com/z5450851HimaMallina).

Thank you 
