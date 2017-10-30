import datetime as dt
import pandas as pd
import json
import csv

def fiscal_calendar(date_start, date_stop, output = 'df'):
    num_days = date_stop - date_start
    
    fy_date_list = [date_start + dt.timedelta(days = i) for i in range(num_days.days + 1)]
    fy_date_seq = range(1, num_days.days + 2)
    fy_date_list_mod = [i%7 for i in fy_date_seq]
    num_weeks = fy_date_list_mod.count(0)
    
    fy_weeks = []
    t_week = 1
    for i in range(len(fy_date_seq) - 1):
        t_mod = fy_date_list_mod[i]
        t_date_0 = dt.datetime(1944, 1, 1).date()
        t_date = fy_date_list[i]
        
        if t_mod == 0:
            fy_weeks += 7*[t_week/7]
            t_week += 1
        else:
            t_week += 1
    
        if t_week == len(fy_date_seq):
            fy_weeks += 7*[num_weeks]
    
    fy_weeks = [k if k <= 52 else 52 for k in fy_weeks]

    fy_year = int(fy_date_list[60].strftime('%Y'))
    fy_month_num = [int(s.strftime('%m')) for s in fy_date_list]
    
    fy_month = [2,3,4,5,6,7,8,9,10,11,12,1]
    fy_2016 = [4,4,5,4,4,5,4,4,5,4,5,4]
    fy_2017 = [4,4,5,4,4,5,4,4,5,4,5,5]
    fy_2018 = [4,4,5,4,4,5,4,4,5,4,5,4]
    
    if fy_year == 2016:
        fy_year_key = fy_2016
    elif fy_year == 2017:
        fy_year_key = fy_2017
    elif fy_year == 2018:
        fy_year_key = fy_2018
    else:
        fy_year_key = []

    fy_month_num = [[i]*j*7 for i,j in zip(fy_month, fy_year_key)]
    fy_month_num = [x for y in fy_month_num for x in y]
    fy_month_abb = [s.strftime('%b').upper() for s in fy_date_list]
    fy_date = [s.strftime('%Y-%m-%d') for s in fy_date_list]

    if output == 'dict':
       # dict
       zip_list = zip(fy_date, fy_month_num, fy_weeks, [fy_year]*len(fy_month_num))
       fiscal_year = {d[0]:{'month': d[1], 'week_of_year': d[2], 'year': d[3]} for d in zip_list}

    if output == 'df':
        # dataframe
        fiscal_year = pd.DataFrame(
                 {'date': fy_date,
                  'year': fy_year,
                  'month': fy_month_num,
                  'week_of_year': fy_weeks,
                 }
        )
    print fiscal_year.head(30)

    return fiscal_year

date_start = dt.datetime(2017, 1, 29).date()
date_stop = dt.datetime(2018, 2, 3).date()
 
date_start = dt.datetime(2018, 2, 4).date()
date_stop = dt.datetime(2019, 2, 2).date()

fy_2016 = fiscal_calendar(date_start = date_start, date_stop = date_stop, output = 'df')
