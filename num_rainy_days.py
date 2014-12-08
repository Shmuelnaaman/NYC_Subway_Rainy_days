import pandas
import pandasql


def num_rainy_days(filename):
    '''
    This function run a SQL query on a dataframe of
    weather data.  The SQL query return one column and
    one row - a count of the number of days in the dataframe where
    the rain column is equal to 1 (i.e., the number of days it
    rained).  The dataframe is title 'weather_data'. the function 
    provide the SQL query.  
    
    in this function I interpreting numbers as integers or floats by using the cast
     option.  ( This is done by writing cast(column as integer)).
    
    weather data can be found :
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv

    To run this function type 
    num_rainy_days('weather_underground.csv')
    '''
    weather_data = pandas.read_csv(filename)
    
    q = """ SELECT  count(*)
    FROM weather_data 
    WHERE cast(rain as integer) =1 
    GROUP BY rain
    """
    
    #Execute your SQL command against the pandas frame
    #rainy_days=q
    rainy_days = (pandasql.sqldf(q.lower(), locals()))
    #print 'Number_of_rainy_dayes'+str(rainy_days)[15:]
    return 'Number_of_rainy_dayes'+str(rainy_days)[15:]