import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
import io
import pandas as pd

# Embedding the base data
csv_data = """
﻿Series,Base Year,Year,CPI - IW,CPI – IW (Food and Beverages),CPI - AL,CPI All India General Index Rural,CPI All India General Index Urban,CPI All India General Index Combined,CPI All India Combined: Food and beverages
Base  Year 1982 = 100,1982,1989-90,173,177,,,,,
Base  Year 1982 = 100,1982,1990-91,193,199,,,,,
Base  Year 1982 = 100,1982,1991-92,219,230,,,,,
Base  Year 1982 = 100,1982,1992-93,240,254,,,,,
Base  Year 1982 = 100,1982,1993-94,258,272,,,,,
Base  Year 1982 = 100,1982,1994-95,284,304,,,,,
Base  Year 1982 = 100,1982,1995-96,313,337,,,,,
Base  Year 1982 = 100,1982,1996-97,342,369,,,,,
Base  Year 1982 = 100,1982,1997-98,366,388,,,,,
Base  Year 1982 = 100,1982,1998-99,414,445,,,,,
Base  Year 1982 = 100,1982,1999-00,428,446,,,,,
Base  Year 1982 = 100,1982,2000-01,444,453,,,,,
Base  Year 1982 = 100,1982,2001-02,463,466,,,,,
Base  Year 1982 = 100,1982,2002-03,482,477,,,,,
Base  Year 1982 = 100,1982,2003-04,500,495,,,,,
Base  Year 1982 = 100,1982,2004-05,520,506,,,,,
Base Year 2001 = 100,2001,2005-06,117,115,,,,,
Base Year 2001 = 100,2001,2006-07,125,126,,,,,
Base Year 2001 = 100,2001,2007-08,133,136,,,,,
Base Year 2001 = 100,2001,2008-09,145,153,,,,,
Base Year 2001 = 100,2001,2009-10,163,176,,,,,
Base Year 2001 = 100,2001,2010-11,180,194,,,,,
Base Year 2001 = 100,2001,2011-12,195,206,,,,,
Base Year 2001 = 100,2001,2012-13,215,230,,,,,
Base Year 2001 = 100,2001,2013-14,236,259,,,,,
Base Year 2001 = 100,2001,2014-15,251,276,,,,,
Base Year 2001 = 100,2001,2015-16,265,293,,,,,
Base Year 2001 = 100,2001,2016-17,276,305,,,,,
Base Year 2001 = 100,2001,2017-18,284,310,,,,,
Base Year 2001 = 100,2001,2018-19,300,312,,,,,
Base Year 2001 = 100,2001,2019-20,323,335,,,,,
Base Year 2016 = 100,2016,2020-21,118,118,,,,,
Base Year 2016 = 100,2016,2021-22,124,124,,,,,
Base Year 2016 = 100,2016,2022-23,131,131,,,,,
Base  Year 1960-61 = 100,1960-61,1989-90,,,747,,,,
Base  Year 1960-61 = 100,1960-61,1990-91,,,803,,,,
Base  Year 1960-61 = 100,1960-61,1991-92,,,958,,,,
Base  Year 1960-61 = 100,1960-61,1992-93,,,1076,,,,
Base  Year 1960-61 = 100,1960-61,1993-94,,,1114,,,,
Base  Year 1960-61 = 100,1960-61,1994-95,,,1247,,,,
Base Year 1986-87 = 100,1986-87,1995-96,,,234,,,,
Base Year 1986-87 = 100,1986-87,1996-97,,,256,,,,
Base Year 1986-87 = 100,1986-87,1997-98,,,264,,,,
Base Year 1986-87 = 100,1986-87,1998-99,,,293,,,,
Base Year 1986-87 = 100,1986-87,1999-00,,,306,,,,
Base Year 1986-87 = 100,1986-87,2000-01,,,305,,,,
Base Year 1986-87 = 100,1986-87,2001-02,,,309,,,,
Base Year 1986-87 = 100,1986-87,2002-03,,,319,,,,
Base Year 1986-87 = 100,1986-87,2003-04,,,331,,,,
Base Year 1986-87 = 100,1986-87,2004-05,,,340,,,,
Base Year 1986-87 = 100,1986-87,2005-06,,,353,,,,
Base Year 1986-87 = 100,1986-87,2006-07,,,380,,,,
Base Year 1986-87 = 100,1986-87,2007-08,,,409,,,,
Base Year 1986-87 = 100,1986-87,2008-09,,,450,,,,
Base Year 1986-87 = 100,1986-87,2009-10,,,513,,,,
Base Year 1986-87 = 100,1986-87,2010-11,,,564,,,,
Base Year 1986-87 = 100,1986-87,2011-12,,,611,,,,
Base Year 1986-87 = 100,1986-87,2012-13,,,672,,,,
Base Year 1986-87 = 100,1986-87,2013-14,,,750,,,,
Base Year 1986-87 = 100,1986-87,2014-15,,,800,,,,
Base Year 1986-87 = 100,1986-87,2015-16,,,835,,,,
Base Year 1986-87 = 100,1986-87,2016-17,,,870,,,,
Base Year 1986-87 = 100,1986-87,2017-18,,,889,,,,
Base Year 1986-87 = 100,1986-87,2018-19,,,907,,,,
Base Year 1986-87 = 100,1986-87,2019-20,,,980,,,,
Base Year 1986-87 = 100,1986-87,2020-21,,,1034,,,,
Base Year 1986-87 = 100,1986-87,2021-22,,,1075,,,,
Base Year 1986-87 = 100,1986-87,2022-23,,,1148,,,,
Base Year 2012 = 100,2012,2011-12,,,,92.8,93.8,93.3,92.9
Base Year 2012 = 100,2012,2012-13,,,,102.7,102.3,102.5,103.3
Base Year 2012 = 100,2012,2013-14,,,,112.6,111.8,112.2,115.6
Base Year 2012 = 100,2012,2014-15,,,,119.5,118.1,118.9,123.1
Base Year 2012 = 100,2012,2015-16,,,,126.1,123,124.7,129.4
Base Year 2012 = 100,2012,2016-17,,,,132.4,127.9,130.3,135.2
Base Year 2012 = 100,2012,2017-18,,,,137.2,132.5,135,138.1
Base Year 2012 = 100,2012,2018-19,,,,141.3,137.7,139.6,139.1
Base Year 2012 = 100,2012,2019-20,,,,147.3,145.1,146.3,147.5
Base Year 2012 = 100,2012,2020-21,,,,156.1,154.4,155.3,158.3
Base Year 2012 = 100,2012,2021-22,,,,164.5,163.1,163.8,
Base Year 2012 = 100,2012,2022-23,,,,175.8,173.5,174.7,

"""

data = pd.read_csv(io.StringIO(csv_data))

class CPIApp(QWidget):
    def __init__(self):
        super().__init__()
        # Load the dataset here to ensure self.data is available for all methods
        self.data = pd.read_csv(io.StringIO(csv_data))
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Former Year Input
        layout.addWidget(QLabel("Enter Former Year (format YYYY or YYYY-YY):"))
        self.formerYearInput = QLineEdit(self)
        self.formerYearInput.setPlaceholderText("e.g., 2020 or 2020-21")
        layout.addWidget(self.formerYearInput)
        
        # Latter Year Input
        layout.addWidget(QLabel("Enter Latter Year (format YYYY or YYYY-YY):"))
        self.latterYearInput = QLineEdit(self)
        self.latterYearInput.setPlaceholderText("e.g., 2021 or 2021-22")
        layout.addWidget(self.latterYearInput)
        
        # CPI Measure Selection
        layout.addWidget(QLabel("Select a CPI Measure:"))
        self.cpiMeasureSelect = QComboBox(self)
        measures = self.data.columns[3:].tolist()  # Adjust based on your actual data
        self.cpiMeasureSelect.addItems(measures)
        layout.addWidget(self.cpiMeasureSelect)
        
        # Known Year Input
        layout.addWidget(QLabel("Is the known year former or latter"))
        self.knownYearInput = QLineEdit(self)
        self.knownYearInput.setPlaceholderText("e.g., former")
        layout.addWidget(self.knownYearInput)
        
        # Known Value Input
        layout.addWidget(QLabel("Enter Known CPI Value:"))
        self.knownValueInput = QLineEdit(self)
        self.knownValueInput.setPlaceholderText("e.g., 120.5")
        layout.addWidget(self.knownValueInput)
        
        # Calculate Button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.clicked.connect(self.onCalculate)
        layout.addWidget(self.calculateButton)
        
        # Result Output
        self.resultOutput = QLineEdit(self)
        self.resultOutput.setReadOnly(True)  # Makes the output selectable and copyable, but not editable
        self.resultOutput.setPlaceholderText("Result will be shown here")
        layout.addWidget(self.resultOutput)
        
        self.setLayout(layout)
        self.setWindowTitle("Inflation Adjustor")
        
    def onCalculate(self):
        try:
            former_year_int = int(self.formerYearInput.text()[:4])  # Assuming input is in YYYY format
            latter_year_int = int(self.latterYearInput.text()[:4])
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Year must be in YYYY format.")
            return

        if former_year_int >= latter_year_int:
            QMessageBox.warning(self, "Input Error", "The former year must come before the latter year.")
            return
        
        former_year = self.formerYearInput.text()
        latter_year = self.latterYearInput.text()
        
        cpi_measure = self.cpiMeasureSelect.currentText()
        
        known_year = self.knownYearInput.text().lower()  # Normalize the case to make comparison case-insensitive
        if known_year not in ['former', 'latter']:
            QMessageBox.warning(self, "Input Error", "Known year must be 'former' or 'latter'.")
            return
        
        try:
            known_value = float(self.knownValueInput.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid number.")
            return
        
        # Call your calculation logic here and update the resultOutput with the result
        self.calculate_cpi(former_year, latter_year, cpi_measure, known_year, known_value)
        
        # result = self.calculate_cpi(former_year, latter_year, cpi_measure, known_year, known_value)
        # self.resultOutput.setText(f"{result}")

        # Placeholder to show where the result is set
        #self.resultOutput.setText("Calculation result placeholder")

    
    # helper function for calculate_cpi()
    def determine_linking_factor(self, cpi_measure, base_year_former, base_year_latter):
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
    def adjust_value_using_linking_factor(self, value, former_value, latter_value, linking_factor, adjust_to_latter=True):
        """
        Adjusts a CPI value using the linking factor. If adjusting to latter base year, multiplies by the linking factor;
        if adjusting to former, divides by the linking factor.
        """
        if adjust_to_latter:
            return value * (latter_value / former_value) * linking_factor
        else:
            return value * (former_value / latter_value) / linking_factor
    
    
    def calculate_cpi(self, former_year, latter_year, cpi_measure, known_year, known_value):
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
        
        data = self.data
        
        # Filter data for the specific CPI measure being not null
        data_filtered = data[data[cpi_measure].notnull()]
        
        # Extract rows for the former and latter years with cpi_measure populated
        row_former = data_filtered[data_filtered['Year'].str.contains(former_year)]
        row_latter = data_filtered[data_filtered['Year'].str.contains(latter_year)]

        # Check for missing data in either year
        if row_former.empty or row_latter.empty:
            self.resultOutput.setText("Data Not Available. Sorry")
            return

        base_year_former = row_former['Base Year'].values[0]
        base_year_latter = row_latter['Base Year'].values[0]

        # Proceed directly if base years are the same
        if base_year_former == base_year_latter:
            former_value = row_former[cpi_measure].values[0]
            latter_value = row_latter[cpi_measure].values[0]
            
            if known_year == 'former':
                adjusted_value = known_value * (latter_value / former_value)
                self.resultOutput.setText(f"{adjusted_value}")
            else:
                adjusted_value = known_value * (former_value / latter_value)
                self.resultOutput.setText(f"{adjusted_value}")

        else:
            # Base years are different, determine the linking factor
            linking_factor = self.determine_linking_factor(cpi_measure, base_year_former, base_year_latter)
            former_value = row_former[cpi_measure].values[0]
            latter_value = row_latter[cpi_measure].values[0]
            
            if linking_factor is None:
                self.resultOutput.setText("Unable. Linking Factor Not Available.")
                return
            
            # Adjust the CPI value using the linking factor
            if known_year == 'former':
                # Adjust to latter's base year
                adjusted_value = self.adjust_value_using_linking_factor(known_value, former_value, latter_value, linking_factor, adjust_to_latter=True)
                self.resultOutput.setText(f"{adjusted_value}")
            else:
                # Adjust to former's base year
                adjusted_value = self.adjust_value_using_linking_factor(known_value, former_value, latter_value, linking_factor, adjust_to_latter=False)
                self.resultOutput.setText(f"{adjusted_value}")    
            
def main():
    app = QApplication(sys.argv)
    ex = CPIApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()