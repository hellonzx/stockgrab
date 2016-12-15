import requests

class grab(object):
    url = 0

    def __init__(self, url):
        self.url = url    #'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssi_ssfx_flzjtj?daima=sh601688'
    
    def grab_network(self):
        print "sub function"
        response = requests.get(self.url)
        content = requests.get(self.url).content
        print "response headers:", response.headers
        print "response content:", content


