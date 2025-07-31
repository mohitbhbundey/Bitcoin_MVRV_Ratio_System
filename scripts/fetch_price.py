# import requests
# from datetime import datetime
# import psycopg2

# def fetch_btc_price():
#     res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
#     price = res.json()["bitcoin"]["usd"]
#     now = datetime.utcnow()

#     # DB insert
#     conn = psycopg2.connect("dbname=mvrv user=postgres password=admin host=localhost")
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute("INSERT INTO btc_price (timestamp, price_usd) VALUES (%s, %s)", (now, price))
#     print(f"[✓] BTC Price at {now}: ${price}")




import requests
from datetime import datetime
import psycopg2

def fetch_btc_price():
    try:
        res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=10)
        res.raise_for_status()
        price = res.json()["bitcoin"]["usd"]
        now = datetime.utcnow()
    except Exception as e:
        print(f"Failed to fetch BTC price: {e}")
        return

    try:
        conn = psycopg2.connect("dbname=mvrv user=postgres password=admin host=localhost")
        with conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO btc_price (timestamp, price_usd) VALUES (%s, %s)", (now, price))
        print(f"BTC Price at {now}: ${price}")
    except Exception as e:
        print(f"Failed to store BTC price in DB: {e}")

