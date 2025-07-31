import psycopg2

schema = """
CREATE TABLE IF NOT EXISTS btc_price (
    timestamp TIMESTAMPTZ PRIMARY KEY,
    price_usd NUMERIC
);

CREATE TABLE IF NOT EXISTS btc_utxo (
    tx_id TEXT,
    amount_btc NUMERIC,
    last_moved TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS mvrv_ratio (
    timestamp TIMESTAMPTZ PRIMARY KEY,
    market_cap NUMERIC,
    realized_cap NUMERIC,
    mvrv NUMERIC,
    frequency TEXT
);
"""

conn = psycopg2.connect("dbname=mvrv user=postgres password=admin host=localhost")
with conn:
    with conn.cursor() as cur:
        cur.execute(schema)
print("Tables created successfully.")
