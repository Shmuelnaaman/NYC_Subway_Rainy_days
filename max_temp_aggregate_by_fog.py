import pandas
import pandasql


def max_temp_aggregate_by_fog(filename):
    '''
    This function run a SQL query on a dataframe of
    weather data.  The SQL query  return two columns and
    two rows - whether it was foggy or not (0 or 1) and the max
    maxtempi for that fog value (i.e., the maximum max temperature
    for both foggy and non-foggy days).  
    
       
    You can see the weather data below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)

    q = """
    SELECT fog,  max(cast (maxtempi as integer)) 
    FROM weather_data 
    WHERE cast(fog as integer) = 0 
    OR cast(fog as integer) = 1
    GROUP BY fog 
        
    To run this function type 
    max_temp_aggregate_by_fog('weather_underground.csv')
    
    """
    
    #Execute your SQL command against the pandas frame
    Max_temp_fog = pandasql.sqldf(q.lower(), locals())

    return Max_temp_fog
