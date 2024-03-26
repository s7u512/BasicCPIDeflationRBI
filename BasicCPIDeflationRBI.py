import pandas as pd

# Load the dataset
file_path = './rbi_consumer_price_index.csv'
data = pd.read_csv(file_path)

# Function to list CPI measures and get user selection
def choose_cpi_measure(data):
    measures = data.columns[3:]  # Assuming the first three columns are not CPI measures
    print("\nChoose a CPI measure by entering the corresponding number:")
    for i, measure in enumerate(measures, 1):
        print(f"{i}. {measure}")
    while True:
        try:
            selection = int(input()) - 1
            if 0 <= selection < len(measures):
                return measures[selection]
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Please enter a number.")

# Function to get input for year and check if it's within the dataset range
def get_year_input(prompt, data):
    while True:
        year = input(prompt)
        if data['Year'].str.contains(year).any():
            return year
        else:
            print("Year not found in the dataset. Please try again.")

def calculate_or_splice(data, former_year, latter_year, cpi_measure, known_year, known_value):
    """
    Checks for missing data, compares base years, and calculates the unknown CPI value if possible.
    If data is missing, indicates so without suggesting splicing. If base years are different,
    indicates that splicing is required.

    :param data: DataFrame containing the CPI data.
    :param former_year: The former year in the comparison.
    :param latter_year: The latter year in the comparison.
    :param cpi_measure: The CPI measure to use for calculation.
    :param known_year: Indicates which year ('former' or 'latter') has the known value.
    :param known_value: The known CPI value.
    :return: A flag indicating whether splicing is required (True if required, False otherwise).
    """
    # Extract rows for the former and latter years
    row_former = data[data['Year'].str.contains(former_year)]
    row_latter = data[data['Year'].str.contains(latter_year)]
    splicing_required = False

    # Check for missing data in either year
    if row_former.empty or row_latter.empty or \
       pd.isna(row_former[cpi_measure].values[0]) or \
       pd.isna(row_latter[cpi_measure].values[0]):
        print("Data missing for one or both of the years. Cannot proceed.")
    else:
        # Both years have data, now check if base years are the same
        if row_former['Base Year'].values[0] == row_latter['Base Year'].values[0]:
            former_value = row_former[cpi_measure].values[0]
            latter_value = row_latter[cpi_measure].values[0]

            # Calculate the unknown value based on the known value and the CPI ratio
            if known_year == 'former':
                result = known_value * (latter_value / former_value)
                print(f"Calculated CPI for the latter year: {result}")
            else:
                result = known_value * (former_value / latter_value)
                print(f"Calculated CPI for the former year: {result}")
        else:
            # Base years are different, splicing is required
            print("Different base years, need to splice.")
            splicing_required = True

    return splicing_required
    
# helper function for splice_cpi_values()
def determine_linking_factor(cpi_measure, base_year_former, base_year_latter):
    """
    Returns the linking factor based on the CPI measure and the transition between base years.
    """
    # Example implementation, expand based on available linking factors
    if cpi_measure == "CPI - IW":
        if base_year_former == "1982" and base_year_latter == "2001":
            return 4.63
        elif base_year_former == "2001" and base_year_latter == "2016":
            return 2.88
    elif cpi_measure == "CPI - AL":
        if base_year_former == "1960-61" and base_year_latter == "1986-87":
            return 5.89
    # Add more conditions as needed
    return None

# helper function for splice_cpi_values()
def adjust_value_using_linking_factor(value, linking_factor, adjust_to_latter=True):
    """
    Adjusts a CPI value using the linking factor. If adjusting to latter base year, multiplies by the linking factor;
    if adjusting to former, divides by the linking factor.
    """
    if adjust_to_latter:
        return value * linking_factor
    else:
        return value / linking_factor

# This function would only kick in if splicing_required = True
def splice_cpi_values(data, former_year, latter_year, cpi_measure, known_year, known_value):
    # Determine the base years for former and latter years
    base_year_former = data[data['Year'].str.contains(former_year)]['Base Year'].values[0]
    base_year_latter = data[data['Year'].str.contains(latter_year)]['Base Year'].values[0]
    
    # Determine the appropriate linking factor based on CPI measure and base years
    linking_factor = determine_linking_factor(cpi_measure, base_year_former, base_year_latter)
    
    
    if linking_factor is None:
        print("Unable to determine the linking factor for the given CPI measure and base years.")
        return
    
    # Retrieve the CPI values for former and latter years
    row_former = data[data['Year'].str.contains(former_year)]
    row_latter = data[data['Year'].str.contains(latter_year)]
    cpi_value_former = row_former[cpi_measure].values[0]
    cpi_value_latter = row_latter[cpi_measure].values[0]
    
    # Adjust the known value using the linking factor
    if known_year == 'former':
        # If the known value is in the former year, adjust it to the latter year's base year before calculating
        adjusted_value = known_value * linking_factor
        # Calculate the CPI value for the latter year using the ratio of CPI values from the data
        calculated_value = adjusted_value * (cpi_value_latter / cpi_value_former)
        print(f"Spliced CPI for the latter year ({latter_year}) is: {calculated_value}")
    else:
        # If the known value is in the latter year, adjust it to the former year's base year before calculating
        adjusted_value = known_value / linking_factor
        # Calculate the CPI value for the former year using the ratio of CPI values from the data
        calculated_value = adjusted_value * (cpi_value_former / cpi_value_latter)
        print(f"Spliced CPI for the former year ({former_year}) is: {calculated_value}")
    
    return calculated_value


def main(data):
    print("CPI Data Analysis Tool")
    former_year = get_year_input("Enter Former Year (format YYYY or YYYY-YY): ", data)
    latter_year = get_year_input("Enter Latter Year (format YYYY or YYYY-YY): ", data)

    cpi_measure = choose_cpi_measure(data)
    
    while True:
        known_year = input("Which is the known value year? Enter 'former' or 'latter': ").lower()
        if known_year in ['former', 'latter']:
            break
        else:
            print("Invalid input. Please enter 'former' or 'latter'.")

    while True:
        try:
            known_value = float(input("Enter the known CPI value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    splicing_required = calculate_or_splice(data, former_year, latter_year, cpi_measure, known_year, known_value)
    
    if splicing_required:
        splice_cpi_values(data, former_year, latter_year, cpi_measure, known_year, known_value)

if __name__ == "__main__":
    main(data)
