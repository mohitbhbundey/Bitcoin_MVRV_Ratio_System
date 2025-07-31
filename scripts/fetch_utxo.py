import random
from datetime import datetime, timedelta
import psycopg2

def simulate_utxo(n=5000):
    try:
        conn = psycopg2.connect("dbname=mvrv user=postgres password=admin")
        with conn:
            with conn.cursor() as cur:
                for _ in range(n):
                    tx_id = f"tx{random.randint(1, int(1e6))}"
                    amount = round(random.uniform(0.0001, 1.5), 6)
                    last_moved = datetime.utcnow() - timedelta(days=random.randint(0, 1800))
                    cur.execute("INSERT INTO btc_utxo (tx_id, amount_btc, last_moved) VALUES (%s, %s, %s)",
                                (tx_id, amount, last_moved))
        print(f"Inserted {n} simulated UTXOs.")
    except Exception as e:
        print(f"Error simulating UTXOs: {e}")
