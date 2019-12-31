import datetime
from datetime import date, timedelta
import calendar
from calendar import monthrange

# Function to input a valid date and send range if valid

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


# Function to find range between dates and print output
def find_range(start_date,end_date,start_month,end_month,start_year,end_year):
    month_end_sdate = calendar.monthrange(start_year,start_month)[1]
    month_end_edate = calendar.monthrange(end_year,end_month)[1]

    sday = []
    eday = []
    start_flag = False
    end_flag = False
    # Check if the dates are of same year
    if start_year == end_year:
        # Check if whole year
        if start_date == 1 and start_month == 1 and end_date == 31 and end_month == 12:
            print("transactions",start_year,"*")
        
        # Check if the dates ranges between two months
        elif end_month - start_month <= 1 and start_date != 1 and end_date != month_end_edate:
            sdate = date(start_year, start_month, start_date)   # start date
            edate = date(end_year, end_month, end_date) # end date
            delta = edate - sdate
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

            if end_date != month_end_edate:
                sdate = date(start_year,end_month,1)
                edate = date(end_year, end_month, end_date)
                delta = edate - sdate
                for i in range(delta.days + 1):
                    day = sdate + timedelta(days=i)
                    eday.append(day)
            else:
                end_flag = True
                 
            if start_flag and not end_flag:
                if start_month == 1 and end_month > 9:
                    print("transactions",start_year,"0*")
                else:
                    for month in range(start_month,end_month):
                        print("transactions",start_year,"-",month,"-*")
                for i in eday:
                    print("transactions",i)

            elif end_flag:
                if not start_flag:
                    for i in sday:
                        print("transactions",i)
                    for month in range(start_month+1,end_month+1):
                        print("transactions",start_year,"-",month,"-*")   
                else:
                    if start_month > 9 and end_month == 12: 
                        print("transactions",start_year,"1*")
                
            elif start_flag and end_flag:
                for month in range(start_month,end_month+1):
                    print("transactions",start_year,"-",month,"-*")
                
            else:
                for i in sday:
                    print("transactions",i)  
                for month in range(start_month+1,end_month):
                    print("transactions",start_year,"-",month,"-*")
                for i in eday:
                    print("transactions",i) 
                 
        
    else:
        end_date1 = 31
        end_month1 = 12
        end_year1 = start_year
        find_range(start_date,end_date1,start_month,end_month1,start_year,end_year1)
        
        if end_year - start_year > 1:
            for i in range(start_year+1,end_year):
                print("transactions",i,"*")
        
        start_date1 = 1
        start_month1 = 1
        start_year1 = end_year
        
        find_range(start_date1,end_date,start_month1,end_month,start_year1,end_year)


# Input taking base Name
base_name = input('Enter Base Name\n')
input_validDate()
# find_range(start_date,end_date,start_month,end_month,start_year,end_year)