# Bitcoin_MVRV_Ratio_System
Developed a system to calculate Bitcoin’s MVRV ratio by collecting real-time price and UTXO data, storing it efficiently in PostgreSQL, and computing market and realized values hourly and daily. The system ensures fault tolerance and provides a Streamlit dashboard for clear visualization of MVRV trends.

Key Features
- Fetches Bitcoin price from primary and fallback APIs.
- Simulates and stores UTXO data (for MVP/testing).
- Calculates MVRV ratio (Market Cap / Realized Cap).
- Supports hourly and daily updates.
- Optional visualization via Streamlit dashboard.
- Basic fault tolerance with try/except and logging.
Project Components
1. Data Collection:
   - Fetches Bitcoin price from API.
   - Simulates UTXO records with timestamps and amounts.

2. Database Storage:
   - PostgreSQL used to store price, UTXO, and MVRV ratio.

3. Computation:
   - Calculates Market Cap and Realized Cap.
   - Computes MVRV = Market Cap ÷ Realized Cap.

4. Visualization (Optional):
   - Streamlit dashboard to plot MVRV trends.
Basic Workflow
1. Fetch Bitcoin price and insert into btc_price table.
2. Insert UTXO data into btc_utxo table.
3. Compute MVRV and insert into mvrv_ratio table.
4. (Optional) Visualize MVRV in dashboard.
Tools & Technologies
- Python 3.10+
- PostgreSQL / psycopg2
- Requests (API calls)
- APScheduler (scheduling hourly/daily tasks)
- Streamlit & Pandas (dashboard & analysis)
