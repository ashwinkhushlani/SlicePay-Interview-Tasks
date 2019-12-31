# Slice Pay Date Range Assignment

This is a Program to calculate the range of transactions between two given dates.

Examples-
    baseName- transactions

    startDate- 2019-01-01
    endDate- 2019-12-31
    ------------------------------------------
    Output- transactions-2019*

    baseName- transactions
    startDate- 2019-01-09
    endDate- 2019-01-11
    ------------------------------------------
    Output -
    transactions-2019-01-09,transactions-2019-01-10,transactions-2019-01-11
    
## Requirements

``` Python 3 or above```

## Run Code

```
To run code type python3 transactions.py in console.
Input base name i.e transactions in our case
Type start date and End Date in format YYYY-MM-DD
```

# Algorithm

``` 
1. Take Base Name, if base name is valid take Start Date and End Date else take Base Name again.
2. Take Start Date and End Date, if both dates are valid call find_range function to find transactions between two dates.
3. Check if both the dates are of same year
    - If yes Print the ranges of dates and months
4. If Dates are of 2 consecutives year
    - Divide the dates and call find_range function.
    - Start Date and end date of Starting year, Start Date and end Date of Ending Year.
5. If difference between 2 dates is more than a year.
    - Divide the dates and call find_range function.
    - Start Date and end date of Starting year, Start Date and end Date of Ending Year.
    - Print the range of years between Start Year and End Year
```