# BasicCPIDeflationRBI

Simple python script based on manually prepared data from CPI values published by RBI [here](https://www.rbi.org.in/scripts/AnnualPublications.aspx?head=Handbook%20of%20Statistics%20on%20Indian%20Economy)

The script can inflate or deflate values from one year to another. It can also use linkage factors if RBI has specified it, to calculate values between years with different base years.


## Requirements

Python with pandas installed.

Install python,
open terminal, type 
`pip install pandas`

## Usage

Place `BasicCPIDeflationRBI.py` and `rbi_consumer_price_index.csv` in the same directory.
Then just run the script in a terminal or command prompt. 

## Example

Example output to find how much has Rs.2000 in 2010-11 become in 2021-22 using CPI - IW is given below


```shell
CPI Data Analysis Tool
Enter Former Year (format YYYY or YYYY-YY): 2010-11
Enter Latter Year (format YYYY or YYYY-YY): 2021-22

Choose a CPI measure by entering the corresponding number:
1. CPI - IW
2. CPI – IW (Food and Beverages)
3. CPI - AL
4. CPI All India General Index Rural
5. CPI All India General Index Urban
6. CPI All India General Index Combined
7. CPI All India Combined: Food and beverages
1
Which is the known value year? Enter 'former' or 'latter': former
Enter the known CPI value: 2000
Different base years, need to splice.
Spliced CPI for the latter year (2021-22) is: 3968.0
````

## Contribute
Please help improve the code.

## License
This work is licensed under the GNU GPLv3 license. This work is free: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This work is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
