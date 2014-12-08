import datetime 


def reformat_subway_dates(date1):
    '''
    The dates in the subway data are formatted in the format month-day-year.
    The dates in the weather underground data are formatted year-month-day.
    
    this function takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    
    '''
    a=datetime.datetime.strptime(date1,"%m-%d-%y")
    
    
    date_formatted=a.strftime('%Y-%m-%d')
    
    
    return date_formatted

