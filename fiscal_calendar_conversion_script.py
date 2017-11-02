"""
help creating fiscal year calendars since they are particularly strange.
you can read all about 4-4-5 and 4-5-4 retail calendar months.
"""
from fiscal_calendar_conversion import fiscal_calendar
from fiscal_calendar_conversion import fy_dates
import datetime as dt
import pandas as pd

pd.set_option('display.width', 1500)
pd.set_option('display.max_columns', 17)

# set up for loop
all_fy_df = pd.DataFrame()
dict_keys = xrange(2010, 2018+1)
for i in dict_keys:
    # grab dict value using year as key
    fy  = fy_dates(i)

    # get start and stop date lists
    start_date = fy.get('date_start')
    stop_date = fy.get('date_stop')

    # create datetime.datetime.date object from list
    start = dt.datetime(start_date[0], start_date[1], start_date[2]).date()
    stop = dt.datetime(stop_date[0], stop_date[1], stop_date[2]).date()

    # create calendar from start and end dates
    temp_df = fiscal_calendar(date_start=start, date_stop=stop, output='df')
    all_fy_df = all_fy_df.append(temp_df)

    print 'the fiscal year is {}'.format(i)
    print 'the start date is {}'.format(start)
    print 'the stop date is {}'.format(stop)
    print ''

print all_fy_df.head(10)
print all_fy_df.tail(10)

