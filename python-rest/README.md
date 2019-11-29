Dataset description:

Beginning from the zero o'clock on the start date, contains OHLCV price data for cryptocurrencies hourly. In the link below, there are my examples with 10000 data rows for bitcoin, ethereum, ripple, litecoin respectively beginning on 2019-01-01.

Dataset link:

`coinapi-sdk\python-rest\coinapi_rest_v1\dataset`

To run: Python >= 3

```bash
git clone https://github.com/Chen0092/coinapi-sdk.git
cd coinapi-sdk/python-rest/coinapi_rest_v1
# edit hrs_price_data.py to change currency type, period, date and row limitations  
python hrs_price_data.py YOUR_API_KEY
```

To get one key:

 https://www.coinapi.io/pricing?apikey 

To read more:

 https://docs.coinapi.io/#latest-data

 https://www.coinapi.io/integration 