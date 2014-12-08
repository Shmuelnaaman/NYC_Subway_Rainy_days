import pandas
import pandasql

def avg_min_temperature(filename):
    '''
    This function run a SQL query on a dataframe of
    weather data.  The SQL query return  the average 
    meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    
    
    Here I convert dates to days of the week via the 'strftime' keyword in SQL.
    
    You can see the weather data below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)

    q = """
    SELECT  avg(cast (meantempi as integer)) 
    FROM weather_data 
    WHERE cast(strftime('%w', date) as integer) IN(0,6)
    GROUP BY cast(strftime('%w', date) as integer) IN(0,6)
    """
    
    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends
