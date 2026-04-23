import time
import hmac
import hashlib
import requests
from config import API_KEY, API_SECRET, BASE_URL


class BinanceClient:

    def _sign(self, params):
        query = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = hmac.new(
            API_SECRET.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, symbol, side, order_type, quantity, price=None):

        url = BASE_URL + "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": self.get_server_time()
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": API_KEY
        }

        response = requests.post(url, headers=headers, params=params)

        return response.json()
    
    def get_server_time(self):
      url = BASE_URL + "/fapi/v1/time"
      response = requests.get(url)
      return response.json()['serverTime']
    
    def get_order(self, symbol, order_id):
      url = BASE_URL + "/fapi/v1/order"

      params = {
        "symbol": symbol,
        "orderId": order_id,
        "timestamp": self.get_server_time()
    }

      params["signature"] = self._sign(params)

      headers = {
        "X-MBX-APIKEY": API_KEY
    }

      response = requests.get(url, headers=headers, params=params)
      return response.json()
    