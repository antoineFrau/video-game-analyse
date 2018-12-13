# Here is some tests ....
from pytrends.request import TrendReq
import pandas as pd
import datetime
pytrend = TrendReq()
start_at = "2018-10-25"
end_at = "2018-10-29"
timeframe = start_at + ' ' + end_at 
key = 'Read dead redemption 2'

pytrend.build_payload(kw_list=[key], timeframe=timeframe)
dict = {
    "cities": {},
    "evolutions": {}
}
# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
evolutions = interest_over_time_df.to_dict()[key]
for i in evolutions:
    d = i.strftime("%Y-%m-%d")
    dict['evolutions'][d] = evolutions[i]

print(dict)
# Interest by Region
interest_by_region_df = pytrend.interest_by_region(resolution='COUNTRY')
interest_by_region_df = interest_by_region_df[interest_by_region_df[key] != 0]
dict['cities'] = interest_by_region_df.to_dict()[key]
