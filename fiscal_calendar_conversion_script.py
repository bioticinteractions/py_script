"""
help creating fiscal year calendars since they are particularly strange.
you can read all about 4-4-5 and 4-5-4 retail calendar months.
"""
from fiscal_calendar_conversion import fiscal_calendar
from fiscal_calendar_conversion import fy_dates
import datetime as dt
import pandas as pd
import csv
import json
import numpy as np
import re

pd.set_option('display.width', 1500)
pd.set_option('display.max_columns', 17)

fiscal_year_input = 2012

fy_dict = fy_dates(fiscal_year_input)
date_start = fy_dict.get('date_start')
date_stop = fy_dict.get('date_stop')
generic_fy = fiscal_calendar(date_start=date_start, date_stop=date_stop)

# set up for loop
all_fy_df = pd.DataFrame()
dict_keys = xrange(2010, 2017+1)
for i in dict_keys:
    fy_dict = fy_dates(i)
    start = fy_dict.get('date_start')
    stop = fy_dict.get('date_stop')

    temp_df = fiscal_calendar(date_start=start, date_stop=stop, output='df')
    all_fy_df = all_fy_df.append(temp_df)

    print 'the fiscal year is {}'.format(i)
    print 'the start date is {}'.format(start)
    print 'the stop date is {}'.format(stop)

print all_fy_df.head(10)
print all_fy_df.tail(10)


