# from datetime import datetime
# import psycopg2

# def compute_mvrv(frequency='hourly'):
#     conn = psycopg2.connect("dbname=mvrv user=postgres password=admin")
#     with conn:
#         with conn.cursor() as cur:  
#             # Get latest price
#             cur.execute("SELECT price_usd FROM btc_price ORDER BY timestamp DESC LIMIT 1")
#             price = cur.fetchone()[0]

#             # Get total circulating supply
#             total_supply = 19_700_000  # You can automate this with an API

#             market_cap = price * total_supply

#             # Realized cap
#             cur.execute("SELECT amount_btc, last_moved FROM btc_utxo")
#             utxos = cur.fetchall()

#             realized_cap = 0
#             for amt, moved in utxos:
#                 cur.execute("SELECT price_usd FROM btc_price WHERE timestamp <= %s ORDER BY timestamp DESC LIMIT 1", (moved,))
#                 row = cur.fetchone()
#                 moved_price = row[0] if row else price
#                 realized_cap += amt * moved_price

#             mvrv = market_cap / realized_cap if realized_cap > 0 else None

#             now = datetime.utcnow()
#             cur.execute("INSERT INTO mvrv_ratio (timestamp, market_cap, realized_cap, mvrv, frequency) VALUES (%s, %s, %s, %s, %s)",
#                         (now, market_cap, realized_cap, mvrv, frequency))
#     print(f"[✓] MVRV at {now}: {mvrv:.4f}")

from datetime import datetime
import psycopg2

def compute_mvrv(frequency='hourly'):
    try:
        conn = psycopg2.connect("dbname=mvrv user=postgres password=admin")
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT price_usd FROM btc_price ORDER BY timestamp DESC LIMIT 1")
                price_row = cur.fetchone()
                if not price_row:
                    print("No BTC price data found.")
                    return
                price = price_row[0]

                total_supply = 19_700_000  
                market_cap = price * total_supply

                cur.execute("SELECT amount_btc, last_moved FROM btc_utxo")
                utxos = cur.fetchall()

                realized_cap = 0
                for amt, moved in utxos:
                    cur.execute("SELECT price_usd FROM btc_price WHERE timestamp <= %s ORDER BY timestamp DESC LIMIT 1", (moved,))
                    row = cur.fetchone()
                    moved_price = row[0] if row else price
                    realized_cap += amt * moved_price

                mvrv = market_cap / realized_cap if realized_cap > 0 else None

                now = datetime.utcnow()
                cur.execute("INSERT INTO mvrv_ratio (timestamp, market_cap, realized_cap, mvrv, frequency) VALUES (%s, %s, %s, %s, %s)",
                            (now, market_cap, realized_cap, mvrv, frequency))
        print(f"MVRV at {now}: {mvrv:.4f}")
    except Exception as e:
        print(f"Error in MVRV computation: {e}")
