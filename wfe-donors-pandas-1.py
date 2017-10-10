import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

df = pd.read_csv('/Users/joanhealy1/Documents/MW_donors.csv', parse_dates=[0], dayfirst=True)
#print(df)

# Convert date to datetime and then sort dataframe by date
df['Date'] = pd.to_datetime(df['Funding Date'], dayfirst=True,)
date = df.sort_values(by='Date')
print(date[['Date']])

date.to_csv('test-pandas_2.csv', sep='\t')

# Convert to local time, store as an index
#date1 = pd.DatetimeIndex(pd.to_datetime(df['Date'])).tz_localize('UTC').tz_convert('Europe/Dublin')
date1 = pd.DatetimeIndex(date['Date']).tz_localize('UTC').tz_convert('Europe/Dublin')
print('this is date1')
print(date1)

# Get the time only
just_time = date1 - date1.normalize()
print(just_time)

# remove the commas from each amount number
date['Amount'] = date['Amount'].str.replace(',', '')
print(date[['Amount']])

# Just get amount, no relics from conversion. Then convert into integer for plotting.
date['Rubbish'], date['Amount'] = date['Amount'].str.split('¬', 1).str
date['Amount']  = pd.to_numeric(date.Amount, errors='coerce').fillna(0).astype(np.int64)
print(date[['Amount']])

# Plot on graph
plt.figure()
plt.plot(date1, date['Amount'] )
plt.xticks(rotation='vertical')
plt.subplots_adjust(bottom=0.15)
plt.show()














