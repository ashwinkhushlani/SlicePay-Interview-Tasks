# SlicePay Interview Assignments
## Requirements

``` Python 3 or above```

## Date Range Assignment (transactions.py)

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


## Run Code

```
Navigate to SlicePay directory.
Check transactions.py is in the same directory where you are.
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

## ATM Notes Problem (atm_notes.py)

``` 
Consider an ATM machine which have currency notes from 100 to 1000 (i.e 100,101,102...999,1000)
Given an amount, you have to tell the minimum number of notes with the amount required to be dispenced

Example : 
Input:
Amount to be withdrawn = 2001

Output

1 note of 1000
1 note of 901
1 note of 100
```

## Run Code

```
Navigate to SlicePay directory.
Check atm_notes.py is in the same directory where you are.
To run code type python3 atm_notes.py in console.

```

# Algorithm

```
Pseudo Code
Note: We are assuming that all the notes from 100 - 1000 are available in the machine

1. Start the Program
2. Take the input( i.e amount which needs to be dispatched )
3. Check if the entered amount is valid i.e it should be >= 100 and <= 10,000
4. If the amount it Invalid, return and print the error message.
5. Else 
          - if amount is less than 1000, return 1 currency note of the same amount.
          - else divide the number in the with base of 10.
            For example: 2000 will be divided as:
                                   2000
                                   /     \
                                1000   1000
                                1000 will be divides as:
                                 /    \
                             900   100

6. If the number cannot be further divided, leave that node and start bifurcating the other node.
7. Keep dividing the number until the child nodes sums up to parent node and is a valid note available.
8. If there are any leaf nodes which is not a valid node and cannot be further divided. Add that amount to another leaf node.
9. Finally, count the currency notes in leaf and print the ouput.

Example:
Input = 2001

Solution
                                  2001                                // Bifurcating 2001
                                  /      \
                             1000     1001                        // Since 1000 is a valid note we wont be bifurcating it further and will consider 1001
                                          /      \
                                      1000   1                       // Since 1 is not a valid currency note, we have to bifurcate 1000
                                       /     \
                                  900    100                        // We can stop diving as we have now the leaf nodes which are valid currencies and add up to the parent node.

Finally, take the count of all the notes in the currency. If there are any invalid notes add it to one of the other leaf node
In the above example 
1 can either be added to 100 or 900. Let us add to 100 
So the Notes to be given becomes

Output 
1* 101
1*900
1*1000
```