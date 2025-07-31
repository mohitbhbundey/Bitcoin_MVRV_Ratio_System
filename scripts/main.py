from fetch_price import fetch_btc_price
from fetch_utxo import simulate_utxo
from compute_mvrv import compute_mvrv

# if __name__ == "__main__":
print("→ Fetching BTC Price...")
fetch_btc_price()

print("→ Simulating UTXOs...")
simulate_utxo()

print("→ Computing MVRV...")
compute_mvrv("hourly")
    