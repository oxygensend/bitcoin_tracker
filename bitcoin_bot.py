import requests
import time
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError
class Bitcoin_tracker():
    """Taking currency values from api data"""

    def __init__(self, chat_id,wait_time, threshold):
        self.api_key = '9ee3c484-46ff-4628-b074-7b4ced9642da'
        self.bot_token = '1643630027:AAFbQraFKVCqlyt53tY4ySrxjfxsFTjVxFw'
        self.chat_id =  chat_id
        self.threshold = threshold
        self.wait_time = wait_time
        self.n = 0

    def run(self):
    
        while True:
            try:
                btc_usd = round(self.get_btc_price(),2)
                usd = self.get_usd_price()
                btc_pln = round(btc_usd * usd,2)
                if btc_pln < self.threshold:
                    self.send_message(msg=f'BTC Price USD: {btc_usd}\nBTC Price PLN: {btc_pln}') 
                    time.sleep(self.wait_time/2)
                    continue
                self.send_message(msg=f'BTC Price USD: {btc_usd}\nBTC Price PLN: {btc_pln}') 
                time.sleep(self.wait_time)
                self.n=0
            except ConnectionError:
                time.sleep(10)
                self.n+=1
                if(self.n >= 180):
                    sys.exit()
                    


            
            

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
        url_today = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/today/'
        url_average = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/'
        headers = {
            'Accepts': 'application/json'
        }
        try: # There is posibility that today's date can be available with with delay
            response = requests.get(url_today, headers=headers)
            usd = response.json()
        except JSONDecodeError:
            response = requests.get(url_average, headers=headers)
            usd = response.json()

        return usd['rates'][0]['bid']

    def send_message(self,msg):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={msg}"
        requests.get(url)


instance = Bitcoin_tracker(chat_id='1709304356',wait_time=3600, threshold=214000)
instance.run()
