import requests
import pandas as pd
from datetime import date, timedelta

'''
input: 2 datetime.date arguments for specifying query range
output: A JSON array of query result
'''
def get_AAPL_history(startDate, endDate):
    assert startDate < endDate
    rpost = requests.post(
        "https://cn.investing.com/instruments/HistoricalDataAjax",
        data={
            "curr_id": "6408",
            "header": "AAPL历史数据",
            "st_date": startDate.strftime('%Y/%m/%d'),
            "end_date": endDate.strftime('%Y/%m/%d'),
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4)\
                AppleWebKit/537.36 (KHTML, like Gecko)",
            "Host": "cn.investing.com",
            "X-Requested-With": "XMLHttpRequest",
        },
    )
    table = pd.read_html(rpost.text)
    assert len(table) > 0
    return table[0].to_json()
