#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title TSB Kasko Car Insurance Valuation
# @raycast.mode inline

# Optional parameters:
# @raycast.icon 🚗
# @raycast.refreshTime 1h
# @raycast.packageName Finance

# Documentation:
# @raycast.description Fetches the suggested insurance payout value of an automobile from Turkiye Sigortalar Birligi (TSB)
# @raycast.author Alp Sayin
# @raycast.authorURL https://github.com/alpsayin

import sys

import requests
import traceback
from pprint import pprint
import json

invoke_path = sys.argv[0]

DEFAULT_YEAR = 2017
DEFAULT_BRAND = 'HONDA'
DEFAULT_TYPE = 'CIVIC HB SPORT 1.5 182 OV'

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en;q=0.5",
    "Connection": "keep-alive",
    "Content-Length": "36",
    "Content-Type": "application/json;charset=utf-8",
    "DNT": "1",
    "Host": "tsb.org.tr",
    "Origin": "https://www.tsb.org.tr",
    "Referer": "https://www.tsb.org.tr/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0",
}


def main(year=DEFAULT_YEAR, brand_name=DEFAULT_BRAND, type_name=DEFAULT_TYPE):
    url = 'https://tsb.org.tr/api/tr/insurance_data/'

    post_data = {'year': year, 'brand_name': brand_name, 'type_name': type_name}
    try:
        result = requests.post(url, headers=headers, data=json.dumps(post_data))
    except requests.exceptions.ConnectionError as ce:
        print('ConnectionError!')
        print('---')
        pprint(ce)
        return

    if result.status_code != 200:
        print(f'HTTP {result.status_code}')
        # print(result.text)
        return

    # pprint(result.text)

    kasko_dict = dict()
    try:
        kasko_dict = json.loads(result.text)
    except Exception as exc:
        print('Data parse error')
        print('---')
        pprint(result.text)
        print(f'{exc}')
        traceback.print_exc()
        return

    try:
        result = int(kasko_dict['insurance']['insurance_value'])
    except Exception as exc:
        print('Number parse error')
        print('---')
        pprint(kasko_dict)
        print(f'{exc}')
        traceback.print_exc()
        return

    end_char = '  '
    print(f'{year} {brand_name} {type_name} → {result:,} TL', end=end_char)


if __name__ == '__main__':
    main()
