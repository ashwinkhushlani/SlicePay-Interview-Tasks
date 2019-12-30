import datetime
from datetime import date, timedelta
import calendar
from calendar import monthrange
# Function to check if the date entered is correct

def input_validDate():
    isValidDate = True
    
    try :
        start_date_entry = input('Enter a start_date in YYYY-MM-DD format\n')
        end_date_entry = input('Enter a end_date in YYYY-MM-DD format\n')
        start_year, start_month, start_date = map(int, str(start_date_entry).split('-'))
        end_year, end_month, end_date = map(int, str(end_date_entry).split('-'))
        datetime.datetime(int(start_year),int(start_month),int(start_date))
        datetime.datetime(int(end_year),int(end_month),int(end_date))
    
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        find_range(start_date,end_date,start_month,end_month,start_year,end_year)
    else :
        input_validDate()


# Function to check if basename is valid
def basename_isvalid(base_name):
    if base_name.casefold() != "transactions" or base_name.lower() != "transaction":
        print("base_name", base_name)
        print('Invalid Base Name')

def find_range(start_date,end_date,start_month,end_month,start_year,end_year):
    month_end_date = calendar.monthrange(start_year,start_month)[1]
    sdate = date(start_year, start_month, start_date)   # start date
    edate = date(end_year, end_month, end_date) # end date
    year_start = 1
    year_end = 12

    if start_year == end_year:
        print("year is same")
        if start_month == year_start and end_month == year_end:
            print("month is same")
            if start_date == 1 and end_date == 31:
                print("date is same")
                print("transactions",start_year,"*")

    # delta = edate - sdate
    # for i in range(delta.days + 1):
    #     day = sdate + timedelta(days=i)
    #     print(day)

# Input taking base Name
base_name = input('Enter Base Name\n')
input_validDate()
# find_range(start_date,end_date,start_month,end_month,start_year,end_year)