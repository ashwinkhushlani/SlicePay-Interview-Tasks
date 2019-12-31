import datetime
from datetime import date, timedelta
import calendar
from calendar import monthrange

# Function to take base Name

def input_baseName():
    base_name = input('Enter Base Name\n')
    basename_isvalid(base_name)

# Function to check if basename is valid
def basename_isvalid(base_name):
    # If base name is not Transaction / Transactions take input again else Take Start Date and End Date
    if base_name.lower() == 'transactions' or base_name.lower() == 'transaction':
        print("base_name", base_name)
        input_validDate()
        
    else:
        print('Invalid Base Name')
        input_baseName()

# Function to input a valid date and send range if valid
def input_validDate():
    isValidDate = True
    
    try :
        # Input Start Date and End Date
        start_date_entry = input('Enter a start_date in YYYY-MM-DD format\n')
        end_date_entry = input('Enter a end_date in YYYY-MM-DD format\n')
        start_year, start_month, start_date = map(int, str(start_date_entry).split('-'))
        end_year, end_month, end_date = map(int, str(end_date_entry).split('-'))
        datetime.datetime(int(start_year),int(start_month),int(start_date))
        datetime.datetime(int(end_year),int(end_month),int(end_date))
    
    except ValueError :
        # If input date is not valid set isValidDate to False
        isValidDate = False

    if(isValidDate) :
        # If date is valid send it to Find Range function
        find_range(start_date,end_date,start_month,end_month,start_year,end_year)
    else :
        # If Date is invalid, take input again
        input_validDate()


# Function to find range between dates and print transactions output
def find_range(start_date,end_date,start_month,end_month,start_year,end_year):

    month_end_sdate = calendar.monthrange(start_year,start_month)[1] # Variable to store last date of Start Month
    month_end_edate = calendar.monthrange(end_year,end_month)[1] # Variable to store last date of End Month

    sday = [] # Transaction Dates of Starting month
    eday = [] # Transaction Dates for Ending month
    
    start_flag = False # Variables which defines if start date is 1 
    end_flag = False # Variables which defines if end date is 30/31 (depending on month)
    
    # Check if the dates are of same year
    if start_year == end_year:
        # Check if start date and end date is whole year
        if start_date == 1 and start_month == 1 and end_date == 31 and end_month == 12:
            print("transactions",start_year,"*")
        
        # Check if the dates ranges between two months
        elif end_month - start_month <= 1 and start_date != 1 and end_date != month_end_edate:
            sdate = date(start_year, start_month, start_date)   # start date
            edate = date(end_year, end_month, end_date) # end date
            delta = edate - sdate
            # Find Range between 2 dates and Print the same
            for i in range(delta.days + 1):
                day = sdate + timedelta(days=i)
                print(day)
            
        else:
            # Check if the start month does not start from 01 then give all the dates of the start month from start date 
            if start_date != 1:
                sdate = date(start_year, start_month, start_date)
                edate = date(start_year,start_month,month_end_sdate)
                delta = edate - sdate
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    sday.append(day)

            # If start date of start month is 1 set flag to true
            else:
                start_flag = True

            # Check if the end month does not ends at 30/31(depending on month) then give all the dates of the end month from 1st of month till end date  
            if end_date != month_end_edate:
                sdate = date(start_year,end_month,1)
                edate = date(end_year, end_month, end_date)
                delta = edate - sdate
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    eday.append(day)
            
            # If date of end month is 31/30 set flag to true
            else:
                end_flag = True
            
            # If Date starts with 1 but not ends at 30/31
            if start_flag and not end_flag:
                # If Range consists of all months from 01-01 to 30-10
                if start_month == 1 and end_month > 9:
                    print("transactions",start_year,"0*")
                else:
                    for month in range(start_month,end_month):
                        print("transactions",start_year,"-",month,"-*")
                # Print the range of all days of end month
                for i in eday:
                    print("transactions",i)

            # If End date is 30/31
            elif end_flag:
                # If start date is not 01
                if not start_flag:
                    # Print Range of Dates in Start Month 
                    for i in sday:
                        print("transactions",i)
                    # Print all whole months between start month and end month 
                    for month in range(start_month+1,end_month+1):
                        print("transactions",start_year,"-",month,"-*")   
                # If Start date is 1 and end month is 12
                else:
                    if start_month > 9 and end_month == 12: 
                        print("transactions",start_year,"1*")
            
            # If start month and end month is starting from 01 and ending at 30/31 
            elif start_flag and end_flag:
                # Print All the months between given range
                for month in range(start_month,end_month+1):
                    print("transactions",start_year,"-",month,"-*")
            
            # If Date is not starting from 1 and ending at 30/31
            else:
                # Print Transactions Dates of First Month
                for i in sday:
                    print("transactions",i)  
                # Print all the Months ranging between Dates
                for month in range(start_month+1,end_month):
                    print("transactions",start_year,"-",month,"-*")
                # Print Transactions Dates of End Month
                for i in eday:
                    print("transactions",i) 
                 
    # If Difference between dates is more than a year
    else:
        # Divide first year and call find_range
        end_date1 = 31
        end_month1 = 12
        end_year1 = start_year
        find_range(start_date,end_date1,start_month,end_month1,start_year,end_year1)
        # Print all years in between
        if end_year - start_year > 1:
            for i in range(start_year+1,end_year):
                print("transactions",i,"*")
        # Divide Last Year and call find_range
        start_date1 = 1
        start_month1 = 1
        start_year1 = end_year
        
        find_range(start_date1,end_date,start_month1,end_month,start_year1,end_year)

input_baseName()