from grab import *

def main():
    print("main")
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssi_ssfx_flzjtj?daima=sh601688'
    grabobj = grab(url)
    grabobj.grab_network()

if __name__=='__main__':
    main()
