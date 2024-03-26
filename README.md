# BasicCPIDeflationRBI

Simple python script based on manually prepared data from CPI values published by RBI [here](https://www.rbi.org.in/scripts/AnnualPublications.aspx?head=Handbook%20of%20Statistics%20on%20Indian%20Economy)

## Example

Just run it in a terminal. Any python with pandas installed should work.

```bash
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

## Please help improve the code.
