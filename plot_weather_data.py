from pandas import *
from ggplot import *
import numpy as np
import pandas as pd


def plot_weather_data(turnstile_weather):
    ''' 
    Here I plot the variation in riders number as function of temperature and daily hour 
    and the avg riders for the most active Unit in different hours.
    '''

    #dataframe = pandas.read_csv('turnstile_data_master_with_weather.csv')
    dataframe =pd.DataFrame(turnstile_weather)

    dataframe.fillna(1)
  # Select Features (try different features!)
    # Add day of the week
    features = dataframe[['precipi','Hour','meantempi','meandewpti','rain','ENTRIESn_hourly','UNIT']] #, 'rain', 'precipi', 'Hour', 'meantempi'
    features.is_copy = False
    features['Dow1']= dataframe['DATEn'].apply (lambda x:datetime.strftime(datetime.strptime(x,"%Y-%m-%d"),"%w"))

    
    # Ridership by average temperture and daily hour

    Dyl_avg = dataframe.groupby(['Hour','meantempi'],as_index=False)['ENTRIESn_hourly'].agg([np.mean])
    UN_MX=  Dyl_avg.groupby(level=['Hour'],as_index=False).apply(lambda t: (t.ENTRIESn_hourly['mean']-t.ENTRIESn_hourly['mean'].mean())/t.ENTRIESn_hourly['mean'].std()).reset_index()

    qsec=(150*(UN_MX['mean']+1))
    
    plot=ggplot(UN_MX['mean'],aes(x=UN_MX['meantempi'] , y=UN_MX['Hour'])) + \
    geom_point(aes(size  = qsec)) + \
    scale_x_continuous(name="Temp [F]",breaks =range(80) , labels=range(80),size=20) +\
    scale_y_continuous(name="Time [Hours]",size=20) +\
    ggtitle("Hourly ENTRIES as function of Temp normalize by the hourly variation") + \
    xlim(53, 80) +\
    ylim(-2, 25)

     # max average per UNIT acording to the daily hour
    Dyl_avg = dataframe.groupby(['Hour','UNIT'],as_index=False)['ENTRIESn_hourly'].agg([np.mean]) 
    UN_MX=  Dyl_avg.groupby(level=['Hour'],as_index=False).apply(lambda t: t[t.ENTRIESn_hourly['mean']==t.ENTRIESn_hourly['mean'].max()]).reset_index()
    
       
    plot=ggplot(UN_MX['ENTRIESn_hourly'], aes(x=UN_MX.ENTRIESn_hourly.index, y='mean')) + \
    geom_bar(aes( weight = 'mean', fill='gray'),stat="identity") + \
    geom_text(aes(x=UN_MX.ENTRIESn_hourly.index, y='mean', label=UN_MX.UNIT,size=20),angle = 90) +  \
    scale_x_continuous(name="Time [Hours]",breaks =range(24) , labels=range(24),size=20) +\
    scale_y_continuous(name="Max avg ENTRIES")+\
    ggtitle("UNIT with Max Avg Enteries per time in day") + \
    xlim(-1, 24)+\
    ylim(-1, 30500)


    return plot
