import datetime as dt
import pandas as pd

def fiscal_calendar(date_start, date_stop, output = 'df'):
    # calculate difference in days between two dates
    num_days = date_stop - date_start
   
    # create list of dates between the two input dates
    fy_date_list = [date_start + dt.timedelta(days = i) for i in range(num_days.days + 1)]

    # create list with each day
    fy_date_seq = range(1, num_days.days + 2)

    # calculate where weeks end given list dates
    fy_date_list_mod = [i%7 for i in fy_date_seq]

    # count how many numbers where x mod 7 = 0
    num_weeks = fy_date_list_mod.count(0)
   
    # calculate number of fiscal weeks
    fy_weeks = []
    t_week = 1
    for i in range(len(fy_date_seq) - 1):
        t_mod = fy_date_list_mod[i]
        #t_date_0 = dt.datetime(1944, 1, 1).date()
        #t_date = fy_date_list[i]
        if t_mod == 0:
            fy_weeks += 7*[t_week/7]
            t_week += 1
        else:
            t_week += 1
        if t_week == len(fy_date_seq): # for last row, add extra week
            fy_weeks += 7*[num_weeks]

    # convert calendar date to calendar month integer
    cy_month_num = [int(s.strftime('%m')) for s in fy_date_list]

    # convert calendar date to calendar year
    cy_year = [int(s.strftime('%Y')) for s in fy_date_list]

    # grab day from date
    cy_day = [int(d.strftime('%d')) for d in fy_date_list]
   
    # grab fiscal year (to be safe get year of date 60 rows in
    fy_year = int(fy_date_list[60].strftime('%Y'))

    # make sure all weeks over 52 count as 52 (except for year 2012, which has 53)
    if fy_year != 2012:
        fy_weeks = [k if k <= 52 else 52 for k in fy_weeks]
    else:
        fy_weeks = [k if k <= 53 else 53 for k in fy_weeks]

    # order of the calendar months for the fiscal year: feb first, jan last
    fy_month = [2,3,4,5,6,7,8,9,10,11,12,1]

    # set number of months given the fiscal year
    ends_in_5 = [2012, 2017]
    if fy_year in ends_in_5:
        fy_year_key = [4,4,5,4,4,5,4,4,5,4,5,5]
    else: 
        fy_year_key = [4,4,5,4,4,5,4,4,5,4,5,4]
   
    # create list of weeks in a given fiscal month
    fy_month_week = [[x]*7 for y in fy_year_key for x in range(1, y+1)]
    fy_month_week = [x for y in fy_month_week for x in y]

    # create list of fiscal months
    fy_month_num = [[i]*j*7 for i,j in zip(fy_month, fy_year_key)]
    fy_month_num = [x for y in fy_month_num for x in y]

    # create month abbreviation
    fy_month_abb = [s.strftime('%b').upper() for s in fy_date_list]

    # create list of dates as strings
    fy_date = [s.strftime('%Y-%m-%d') for s in fy_date_list]

    # output type
    if output == 'dict':
       # dict
       zip_list = zip(fy_date, fy_month_num, fy_weeks, [fy_year]*len(fy_month_num))
       fiscal_year = {d[0]:{'month': d[1], 'week_of_year': d[2], 'year': d[3]} for d in zip_list}

    if output == 'df':
        # dataframe
        fiscal_year = pd.DataFrame(
                 {'date': fy_date,
                  'fiscal_year': fy_year,
                  'fiscal_month': fy_month_num,
                  'fiscal_week_of_year': fy_weeks,
                  'fiscal_week_of_month': fy_month_week,
                  'cy_year': cy_year,
                  'cy_month_num': cy_month_num,
                  'cy_day': cy_day
                 }
        )

    # make sure to print a few lines to check
    #print fiscal_year.head(10)

    return fiscal_year

def fy_dates(year):
    
    fy_dict = {
        2010: {"date_start": [2010,1, 31], "date_stop": [2011, 1, 29]},
        2011: {"date_start": [2011,1, 30], "date_stop": [2012, 1, 28]},
        2012: {"date_start": [2012,1, 29], "date_stop": [2013, 2, 2]},
        2013: {"date_start": [2013,2, 3], "date_stop": [2014, 2, 1]},
        2014: {"date_start": [2014,2, 2], "date_stop": [2015, 1, 31]},
        2015: {"date_start": [2015,2, 1], "date_stop": [2016, 1, 30]},
        2016: {"date_start": [2016,1, 31], "date_stop": [2017, 1, 28]},
        2017: {"date_start": [2017,1, 29], "date_stop": [2018, 2, 3]},
        2018: {"date_start": [2018,2, 4], "date_stop": [2019, 2, 2]}
    }

    temp_dates = fy_dict.get(year)

    return temp_dates

