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

# helper function for calculate_cpi()
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
    elif cpi_measure == "CPI – IW (Food and Beverages)":
        if base_year_former == "1982" and base_year_latter == "2001":
            return 4.58
        elif base_year_former == "2001" and base_year_latter == "2016":
            return 2.88    
    elif cpi_measure == "CPI - AL":
        if base_year_former == "1960-61" and base_year_latter == "1986-87":
            return 5.89
    # Add more conditions as needed
    return None


# helper function for calculate_cpi()
def adjust_value_using_linking_factor(value, former_value, latter_value, linking_factor, adjust_to_latter=True):
    """
    Adjusts a CPI value using the linking factor. If adjusting to latter base year, multiplies by the linking factor;
    if adjusting to former, divides by the linking factor.
    """
    if adjust_to_latter:
        return value * (latter_value / former_value) * linking_factor
    else:
        return value * (former_value / latter_value) / linking_factor

def calculate_cpi(data, former_year, latter_year, cpi_measure, known_year, known_value):
    """
    Calculates the unknown CPI value if base years are the same, or adjusts CPI values when splicing is required 
    due to different base years, taking into account only rows where the cpi_measure is populated.

    :param data: DataFrame containing the CPI data.
    :param former_year: The former year in the comparison.
    :param latter_year: The latter year in the comparison.
    :param cpi_measure: The CPI measure to use for calculation or adjustment.
    :param known_year: Indicates which year ('former' or 'latter') has the known value.
    :param known_value: The known CPI value.
    """
    # Filter data for the specific CPI measure being not null
    data_filtered = data[data[cpi_measure].notnull()]
    
    # Extract rows for the former and latter years with cpi_measure populated
    row_former = data_filtered[data_filtered['Year'].str.contains(former_year)]
    row_latter = data_filtered[data_filtered['Year'].str.contains(latter_year)]

    # Check for missing data in either year
    if row_former.empty or row_latter.empty:
        print("Data missing for one or both of the years. Cannot proceed.")
        return

    base_year_former = row_former['Base Year'].values[0]
    base_year_latter = row_latter['Base Year'].values[0]

    # Proceed directly if base years are the same
    if base_year_former == base_year_latter:
        former_value = row_former[cpi_measure].values[0]
        latter_value = row_latter[cpi_measure].values[0]
        
        if known_year == 'former':
            adjusted_value = known_value * (latter_value / former_value)
            print(f"{known_value} in {former_year} adjusted using {cpi_measure} for the year {latter_year} is: {adjusted_value}")
        else:
            adjusted_value = known_value * (former_value / latter_value)
            print(f"{known_value} in {latter_year} adjusted using {cpi_measure} for the year {former_year} is: {adjusted_value}")

    else:
        # Base years are different, determine the linking factor
        linking_factor = determine_linking_factor(cpi_measure, base_year_former, base_year_latter)
        former_value = row_former[cpi_measure].values[0]
        latter_value = row_latter[cpi_measure].values[0]
        
        if linking_factor is None:
            print("Unable to determine the linking factor for the given CPI measure and base years.")
            return
        
        # Adjust the CPI value using the linking factor
        if known_year == 'former':
            # Adjust to latter's base year
            adjusted_value = adjust_value_using_linking_factor(known_value, former_value, latter_value, linking_factor, adjust_to_latter=True)
            print(f"{known_value} in {former_year} adjusted using {cpi_measure} and linking factor {linking_factor} for the year {latter_year} is: {adjusted_value}")
        else:
            # Adjust to former's base year
            adjusted_value = adjust_value_using_linking_factor(known_value, former_value, latter_value, linking_factor, adjust_to_latter=False)
            print(f"{known_value} in {latter_year} adjusted using {cpi_measure} and linking factor {linking_factor} for the year {former_year} is: {adjusted_value}")


def main(data):
    print("Basic Inflation Adjuster Tool")
    while True:  # Start a loop to keep asking until the condition is met
        former_year = get_year_input("Enter Former Year (format YYYY or YYYY-YY): ", data)
        latter_year = get_year_input("Enter Latter Year (format YYYY or YYYY-YY): ", data)

        # Convert years to integers for comparison
        try:
            former_year_int = int(former_year[:4])  # Extract the first 4 characters to handle YYYY-YY format
            latter_year_int = int(latter_year[:4])  # Extract the first 4 characters to handle YYYY-YY format
        except ValueError:
            print("Error converting year inputs to integers. Please ensure the format is correct.")
            continue

        # Check if former year is before latter year
        if former_year_int < latter_year_int:
            break  # Exit the loop if the condition is met
        else:
            print("The former year must come before the latter year. Please re-enter both years.")

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
    
    calculate_cpi(data, former_year, latter_year, cpi_measure, known_year, known_value)

if __name__ == "__main__":
    main(data)
