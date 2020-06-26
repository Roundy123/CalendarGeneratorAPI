import pandas as pd
from datetime import datetime, timedelta

def generate_calendar(start_date, end_date):
    # todo - if time specified as well as date
    # todo - hire Adam!

    days = (end_date - start_date).days + 1
    half_hours_per_day = 48

    # The original function used nested for loops and took 56.15 seconds to do 1 year (17568 lines). Using the merge method reduced this to 0.76 seconds!

    times = []
    for halfhour in range(half_hours_per_day):
        # Adding datetime(2020,1,1) below just as an easy way to convert from timedelta to datetime. We could pick any random date as long as it starts at midnight.
        time = datetime(2020,1,1) + timedelta(minutes=0, seconds=0) + timedelta(minutes=30*halfhour)
        time = time.strftime("%H:%M")
        times.append(time)
    
    dates = []
    for day in range(days):
        date = start_date + timedelta(days=day)
        date = date.strftime("%Y%m%d")
        dates.append(date)

    times = pd.DataFrame(times, columns=['Time'])
    dates = pd.DataFrame(dates, columns=['Date'])

    # add columns with equal values for cartesian product join/merge
    times['key'] = 1
    dates['key'] = 1
    dates_times = dates.merge(times, left_on='key', right_on='key')
    dates_times.drop(['key'], axis=1, inplace=True)

    period = [n for n in range(1,len(dates_times) + 1)]
    dates_times['Period'] = period

    return dates_times.to_dict('records')