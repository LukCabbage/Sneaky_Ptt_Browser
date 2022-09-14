import requests
import urllib


url_tinyurl = "http://tinyurl.com/api-create.php"


def url_shortener(url_original):
    url_for_shortener = url_tinyurl + "?" \
          + urllib.parse.urlencode({"url": url_original})  # 百分比編碼（percentage-encoding）將保留字元進行編碼
    shorted_url = requests.get(url_for_shortener)  # get result from tinyurl
    print(shorted_url.text)



