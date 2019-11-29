from coinapi_rest_v1 import CoinAPIv1
import datetime, sys, csv

class DataCollector:
	def __init__(self, api, asset_id, period_id, start_date, lim):
		self.api = api
		self.asset_id = asset_id
		self.period_id = period_id
		self.start_date = start_date
		self.lim = lim

	def perform(self):
		csv_path = './dataset/'+self.asset_id+'_'+self.period_id+'_'+self.start_date+'.csv'
		f = open(csv_path,'w',encoding='utf-8',newline='')
		csv_writer = csv.writer(f)
		csv_writer.writerow(['Period Start','Period end','Time open','Time close','Price open',
							 'Price close','Price low','Price high','Volume traded','Trades count'])

		ohlcv_historical = self.api.ohlcv_historical_data('BITSTAMP_SPOT_'+self.asset_id+'_USD', {'period_id': self.period_id, 
                                                                                            'time_start': self.start_date, 'limit': self.lim})

		for period in ohlcv_historical:
			csv_writer.writerow([period['time_period_start'], period['time_period_end'],period['time_open'],
			period['time_close'],period['price_open'],period['price_close'],period['price_low'],
			period['price_high'],period['volume_traded'],period['trades_count']])

test_key = sys.argv[1]

api = CoinAPIv1(test_key)
'''
assets = ['BTC','ETH','XRP','LTC']
'''
assets = ['XRP','LTC']
period_id = '1HRS'
'''
start_dates = [datetime.date(2010, 7, 17).isoformat(),datetime.date(2015, 8, 7).isoformat(),
               datetime.date(2013, 11, 25).isoformat(),datetime.date(2013, 5, 19).isoformat()]
'''
start_dates = [datetime.date(2013, 11, 25).isoformat(),datetime.date(2013, 5, 19).isoformat()]
lim = '100000' 

for i, asset_id in enumerate(assets):
	dc = DataCollector(api, asset_id, period_id, start_dates[i], lim)
	dc.perform()
