from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import sys

keyword = str(sys.argv[1])
begin_date=dt.date(2019,12,31)
end_date=dt.date(2020,1,1)

print(f'Memulai pencarian tweet dengan keyword {keyword}...')
tweets = query_tweets(keyword, limit=1, begindate=begin_date, enddate=end_date, lang='id')[:1]

df=pd.DataFrame(t.__dict__ for t in tweets)

columns_fix = ['screen_name','username','timestamp','text','likes','retweets','replies']
df_fix = df.loc[:, df.columns.isin(columns_fix)]

df_fix.to_csv(f'./tweets/{keyword}.csv', sep=',', encoding='utf-8', index=False)

print(f'Pencarian tweet dengan keyword {keyword} telah selesai.')