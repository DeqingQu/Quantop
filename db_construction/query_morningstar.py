import requests
import csv
import json
import sys
import urllib.parse


class QueryKeyRatios:

    TIMEOUT_SEC = 120
    API_BASE_URL = 'http://financials.morningstar.com/ajax'

    @staticmethod
    def __access_api(handler, url_suffix):

        url = QueryKeyRatios.API_BASE_URL + '/' + handler + '?' + url_suffix

        try:
            res = requests.get(url, timeout=QueryKeyRatios.TIMEOUT_SEC)
        except requests.exceptions.Timeout:
            print(url, file=sys.stderr)
            print('Timeout in QueryKeyRatios for URL: ' + url, file=sys.stderr)
            return None
        except BaseException as e:
            print(url, file=sys.stderr)
            print('%s received in QueryKeyRatios for URL: %s' % (e, url), file=sys.stderr)
            return None
        status_code = res.status_code
        if status_code != 200:
            print(url, file=sys.stderr)
            print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
            return None
        return res.text

    @staticmethod
    def query_key_ratios(ticker, region='GBR', culture='en_US', currency='USD'):
        key_ratios = {}
        if not isinstance(ticker, str):
            return key_ratios
        response = QueryKeyRatios.__access_api("exportKR2CSV.html",
                                               "callback=?&t={t}&region={reg}&culture={cult}&cur={cur}".format(
                                                   t=ticker, reg=region, cult=culture, cur=currency
                                               ))
        if response is not None:
            print("not none")
        return response


if __name__ == '__main__':
    print(QueryKeyRatios.query_key_ratios("TSLA"))