# bitcoin_tracker
Bot to informing what is the bitcoin's price per hour
The aim of this bot is to informing what is the newest bitcoin's price.
Bot sends a message in Telegram aplication per hour with price in USD and PLN.

To run this script automatically with system booting follow this code:

1.Create a new file in systemd directory with .service suffix
  `vim /etc/systemd/system/btc_tracker.service`

with following code
![image](https://user-images.githubusercontent.com/74931215/114176229-2a7eb800-993b-11eb-95e2-3ee4f25d4d76.png)

2.Reload changes
  `systemctl daemon-reload`

3. Try if everything works
 `service btc_tracker start`
 `systemctl status btc_tracker.service`
 `service btc_tracker stop`

4. Mark this script as enable
  `service btc_tracker enable`

