# Alpha Vantage Python Reference

## Install
```python
pip install alpha_vantage
```


## Usage
For usage in this repo, store your alpha vantage key (obtained for free on their
website) in the standard config style under:
```
[AlphaVantage]
key = YOUR_KEY_HERE
```

## Time Series Methods
```python
ts.get_batch_stock_quotes()
ts.get_daily()
ts.get_daily_adjusted()
ts.get_intraday()
ts.get_monthly()
ts.get_monthly_adjusted()
ts.get_weekly()
ts.get_weekly_adjusted()
ts.indexing_type()
ts.key()
ts.map_to_matype()
ts.output_format()
ts.proxy()
ts.retries()
ts.set_proxy()
ts.treat_info_as_error()
```
