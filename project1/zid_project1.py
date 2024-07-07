""" zid_project1.py

"""
import json
import os

import toolkit_config as cfg

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
PRJDIR = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'toolkit')
ROOTDIR = os.path.join(PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')
# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {'Volume': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}
# ----------------------------------------------------------------------------
#   Please complete the body of this function, so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
        Each non-empty line of the file is guaranteed to have the following format:

        "XXXX"="YYYY"

        where:
            - XXXX represents an exchange.
            - YYYY represents a ticker.

        This function should return a dictionary, where each key is a properly formatted
        ticker, and each value the properly formatted exchange corresponding to the ticker.

        Parameters
        ----------
        pth : str
            Full path to the location of the TICKERS.txt file.

        Returns
        -------
        dict
            A dictionary with format {<tic> : <exchange>} where
                - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
                - Each value (<exchange>) is a string containing the exchange for this ticker.

        Notes
        -----
        The keys and values of the dictionary returned must conform with the following rules:
            - All characters are in lower case
            - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
            - No spaces
            - No empty tickers or exchanges

        """


    stock_tickers = {}

    with open(pth, 'r') as file:
        for l in file:
            l = l.strip()

            if not l:
                continue

            if '=' in l:
                exchange, ticker = l.split('=')

                # Format
                exchange = ''.join(filter(str.isalpha, exchange)).lower()
                ticker = ''.join(filter(str.isalpha, ticker)).lower()

                # Non-empty
                if exchange and ticker:
                    stock_tickers[ticker] = exchange

    return stock_tickers

#TESTING
pth = TICPATH
if __name__ == "__main__":
    tics = get_tics(pth)
    print(tics)

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """

    location = os.path.join(DATDIR, f"{tic}.dat")

    # To Read the file
    file = open(location, 'r')
    element = file.readlines()
    file.close()

    # To create a list with each line as an individual element
    element = [line.strip() for line in element]

    return element
# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    info = {}
    start = 0

    for c in COLUMNS:
        width = COLWIDTHS[c]
        info[c] = line[start:start + width].strip()
        start += width

    return info

def process_dat_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line_to_dict(line))
    return data

def process_all_dat_files_in_folder(folder_path):
    all_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.dat'):
            file_path = os.path.join(folder_path, filename)
            data = process_dat_file(file_path)
            all_data[filename] = data
    return all_data

#TESTING
data_folder_path = DATDIR
all_data = process_all_dat_files_in_folder(data_folder_path)

for filename, data in all_data.items():
    print(f"Data from {filename}:")
    for i in data[:5]:
        print(i)
    print("\n")
# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    if tickers_lst is not None:
        # Rule 1: Check if tickers_lst is an empty list
        if not tickers_lst:
            raise Exception("tickers_lst is an empty list.")

        # Rule 2: Check if tickers_lst contains a ticker not in tic_exchange_dic
        for ticker in tickers_lst:
            if ticker.lower() not in tic_exchange_dic:
                raise Exception(f"Ticker '{ticker}' is not a valid key in tic_exchange_dic.")

# TESTING
if __name__ == "__main__":
    # Example dictionary obtained by get_tics
    tic_exchange_dic = {'tsm': 'nyse', 'aal': 'nasdaq'}

    # Example tickers list to verify
    tickers_lst = ['aal', 'tsm']

    try:
        verify_tickers(tic_exchange_dic, tickers_lst)
        print("No exceptions, All the tickers are valid.")
    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If col_lst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    if col_lst is not None:
        # Rule 1: Check if there is an empty list
        if not col_lst:
            raise Exception("col_lst is an empty list.")

        # Rule 2: Raise exception is columns name are not found or incorrect
        for col in col_lst:
            if col not in COLUMNS:
                raise Exception(f"Column '{col}' is not found in COLUMNS.")


# TESTING
if __name__ == "__main__":
    columns_lst = ['Volume', 'Date', 'Adj Close']

    try:
        verify_cols(columns_lst)
        print("No exceptions, All the column names are verified.")
    except Exception as e:
        print(e)

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(ticker):
    """Reads the .dat file for the given ticker and returns the lines."""
    file_path = os.path.join(DATDIR, f"{ticker}_prc.dat")  # Updated to match file naming convention
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return file.readlines()


def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for

          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """

    # Verify tickers and columns

    if tickers_lst is not None:
        verify_tickers(tic_exchange_dic, tickers_lst)
    else:
        tickers_lst = list(tic_exchange_dic.keys())

    if col_lst is not None:
        verify_cols(col_lst)
    else:
        col_lst = COLUMNS

    data_dict = {}
    for ticker in tickers_lst:
        try:
            lines = read_dat(ticker)
        except FileNotFoundError as e:
            print(e)
            continue
        ticker_data = []
        for line in lines:
            line_data = line_to_dict(line)
            filtered_data = {col: line_data[col] for col in col_lst}
            ticker_data.append(filtered_data)
        data_dict[ticker.lower()] = {
            'exchange': tic_exchange_dic[ticker.lower()],
            'data': ticker_data
        }

    return data_dict

# TESTING
if __name__ == "__main__":
    # Print the list of .dat files in the data directory
    print("Listing all .dat files in the data directory:")
    for filename in os.listdir(DATDIR):
        if filename.endswith('.dat'):
            print(filename)

    # Example dictionary returned by get_tics
    tic_exchange_dic = {'aapl': 'nasdaq', 'baba': 'nyse'}

    # Example tickers list to verify
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']

    try:
        verify_tickers(tic_exchange_dic, tickers_lst)
        print("All tickers are valid.")
    except Exception as e:
        print(e)

    try:
        verify_cols(col_lst)
        print("All columns are valid.")
    except Exception as e:
        print(e)

    # Create data dictionary
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    print(data_dict)

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """

    with open(pth, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)

# ----------------------------------------------------------------------------
#    Please put your answers for the last question here:
# ----------------------------------------------------------------------------
    """
                    ***** Step 10 – Open Ended Questions *****



Configuration is required in step 1 due to the following reasons:
1) Portability: The paths will work in various kinds of operating systems like mac, Linux, or windows. The code will no
   longer be restricted to function on one specific system.
2) User Friendly: os.path.expanduser('~') ensures that the script runs correctly irrespective of the user.
3) Automatic subdirectory updates: If the root directory changes, the subdirectories will adjust accordingly. Which 
   means we do not need to update each subdirectory if the base directory changes.
4) Prevents Issues: When the script is moved to a new environment the issues due to that portability are prevented.
5) Structure : Configuration helps in achieving a well defined directory structure
6) Collaboration : Many users can follow the script to build on the project or complete work on research and it also
   simplifies the work flow.

Therefore, with the help of configuration, the script is flexible, adaptable to various operating systems, and 
easier to maintain in the event of modifications due of configuration.

------------------------------------------------------------------------------

2)  We will carefully examine both hypotheses and consider the consequences of the provided observations to assess the
 two alternative hypotheses based on the observed data.

 EVALUATION :
 
Hypotheses 1:Investors’ evaluations of those firms?

According to this hypothesis the investor assessment of the companies are reflected in the writings of journalists.It 
basically implies that reporters are able to capture and communicate the sentiment and opinions of the investment 
community as a whole.

• Short-term Impact: If articles with negative words represent investors' assessments, the sudden drop in stock 
returns may be the result of investors' responses to the negative articulation expressed in the articles. Because of 
the unfavourable sentiment, investors might sell off their stocks, which would cause a brief decline in stock prices in
the short term.

• Long-term Effect: Providing there is no long-term reversal, it indicates that investors' original negative assessment 
holds up over time or that the negative views is long-lasting. This would imply that the negative tone of the articles 
reflected actual investor concerns and had a long-term effect on stock prices.

Hypothesis 2: Valuable information beyond firm fundamentals?

According to this hypothesis, articles written by journalists provide valuable information that goes beyond basic 
financial knowledge and organisational fundamentals. It implies that journalists offer facts or perspectives that the 
market had not previously taken into account.

• Short-term Impact: A rapid fall in stock returns would mean that investors are rapidly incorporating new, important 
information into their assessment of the companies if articles with negative words indicated it. This would imply that 
the market is responding to the fresh information that journalists have provided. 

• Long-term Effect: The lack of a reversal over time implies that the newly acquired information provided by the 
journalists was accurate and had an ongoing effect on the market's evaluation of the firm.  This would suggest that the
negative tone expressed in the articles is based on genuine issues or concerns that the stock prices had not previously
taken into account.

------------------------------------------------------------------------------

Upon evaluating both the hypothesis, 
Hypothesis 2: Valuable information beyond firm fundamentals would be more likely true.

Short-term Response: The short-term decline in stock returns brought on by unfavourable sentiment can be explained by 
both the two theories. However, considering the long term effect is how we can conclude that hypothesis 2 is more likely 
to be true. 

Long-term Consistency: The absence of a long-term reversal is a strong indicative of a long-lasting impact on the market 
based on the information the journalists provided.  In the long run, when market reactions shift or new information 
is available,one could expect some correction or reversal if the articles simply reflected investors' judgements 
(Hypothesis 1). 

Nonetheless, the consistent decline indicates that the negative viewpoints in the articles offered new, insightful 
viewpoints that precisely represented fundamental problems with the firm, hence strengthening Hypothesis 2.Based on the 
observed information, it is therefore more likely that the assumption that journalists' articles contain valuable 
information beyond basic fundamentals is true.This implies that the articles' critical language offered fresh 
perspectives that prompted a reconsideration of the firm's prospects and a prolonged decline in stock returns.

------------------------------------------------------------------------------
Short-Run Predictability for Trading Volume

1. Immediate Impact: As the articles include insightful information, the market's quick response to it may cause huge
fluctuations in trading volume. Based on the new knowledge, investors might buy or sell stocks quickly, which would 
lead to increase in trade volume.

2. Article-Driven Trading: Trading volume is probably going to have a strong short-term correlation with the 
perspective that the articles convey. Higher sell volumes would result from negative articles, whereas higher buy
volumes would result from good pieces.

3. Predictability: Short-term rises or declines in trade volume can be predicted by examining the articles' viewpoint 
(for example,An article that has a lot of negative words, for instance, would probably forecast a spike in trading as 
investors would quickly sell the stocks). 

4.Historical Patterns: Based on the content of new articles, historical data on trading volumes' responses to previous
articles can be utilised to create forecast models for trading volumes in the future.

In summary, the hypothesis that journalists’ articles provide valuable information beyond firm fundamentals supports the
fact that trading in the short term can be predicted by the content of the articles as the investors react to newly 
available information. 

    """

# ----------------------------------------------------------------------------
#   Test functions:
#   The purpose of these functions is to help you test the functions above as
#   you write them.
#   IMPORTANT:
#   - These functions are optional, you do not have to use them
#   - These functions do not count as part of your assessment (they will not
#     be marked)
#   - You can modify these functions as you wish, or delete them altogether.
# ----------------------------------------------------------------------------
def _test_get_tics():
    """ Test function for the `get_tics` function. Will print the tickers as
    returned by the `get_tics` function.
    """
    pth = TICPATH
    tics = get_tics(pth)
    print(tics)


def _test_read_dat():
    """ Test function for the `read_dat` function. Will read the lines of the
    first ticker in `TICPATH` and print the first line in the list.
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    tic = tics[0]
    lines = read_dat(tic)
    # Print the first line in the file
    print(f'The first line in the dat file for {tic} is:')
    print(lines[0])


def _test_line_to_dict():
    """ Test function for the `read_dat` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Read the lines of the ".dat" file for the first ticker
    - Convert the first line of this file to a dictionary
    - Print this dictionary
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    lines = read_dat(tics[0])
    dic = line_to_dict(lines[0])
    print(dic)


def _test_create_data_dict():
    """ Test function for the `create_data_dict` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Call `create_data_dict` using
        - tickers_lst =  ['aapl', 'baba']
        - col_lst = ['Date', 'Close']
    - Print out the dictionary returned, but only the first 3 items of the data list for each ticker for brevity

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)



def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')


# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test functions
    # _test_get_tics()
    # _test_read_dat()
    # _test_line_to_dict()
    # _test_create_data_dict()
    # _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass





