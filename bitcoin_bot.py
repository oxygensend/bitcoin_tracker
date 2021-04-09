import requests
import time
from requests.exceptions import ConnectionError
class Bitcoin_tracker():
    """Taking currency values from api data"""

    def __init__(self, chat_id,wait_time, threshold):
        self.api_key = '9ee3c484-46ff-4628-b074-7b4ced9642da'
        self.bot_token = '1643630027:AAFbQraFKVCqlyt53tY4ySrxjfxsFTjVxFw'
        self.chat_id =  chat_id
        self.threshold = threshold
        self.wait_time = wait_time

    def run(self):
        
        while True:
            try:
                btc_usd = self.get_btc_price() 
                usd = self.get_usd_price()
                btc_pln = btc_usd * usd
                if btc_pln < self.threshold:
                    self.send_message(msg=f'BTC Price USD: {btc_usd}\nBTC Price PLN: {btc_pln}') 
                    time.sleep(self.wait_time/2)
                    continue
                self.send_message(msg=f'BTC Price USD: {btc_usd}\nBTC Price PLN: {btc_pln}') 
                time.sleep(self.wait_time)
            except ConnectionError:
                time.sleep(10)


            
            

    def get_btc_price(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key
        }
        response = requests.get(url, headers=headers)
        crypto_json = response.json()
        bitcoin_price  = crypto_json['data'][0]
        return bitcoin_price['quote']['USD']['price']

    def get_usd_price(self):
        url = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/today/'
        headers = {
            'Accepts': 'application/json'
        }
        response = requests.get(url, headers=headers)
        usd = response.json()
        return usd['rates'][0]['bid']

    def send_message(self,msg):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={msg}"
        requests.get(url)


instance = Bitcoin_tracker(chat_id='1709304356',wait_time=3600, threshold=214000)
instance.run()
