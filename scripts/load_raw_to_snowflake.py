import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# ---------- Snowflake Connection ----------
conn = snowflake.connector.connect(
    user="ROSHNIADNANI",
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account="aqbiijp-ff48046",
    warehouse="COMPUTE_WH",
    database="ECOMMERCE_DB",
    schema="RAW",
    role="ACCOUNTADMIN"
)

DATA_PATH = "data/raw"

files = {
    "olist_orders_dataset.csv": "ORDERS",
    "olist_order_items_dataset.csv": "ORDER_ITEMS",
    "olist_order_payments_dataset.csv": "ORDER_PAYMENTS",
    "olist_customers_dataset.csv": "CUSTOMERS",
    "olist_products_dataset.csv": "PRODUCTS",
    "olist_sellers_dataset.csv": "SELLERS",
    "product_category_name_translation.csv": "PRODUCT_CATEGORY_TRANSLATION"
}

for file, table in files.items():
    print(f"\nLoading {file} → RAW.{table}")

    df = pd.read_csv(f"{DATA_PATH}/{file}")

    # Normalize column names
    df.columns = [c.upper() for c in df.columns]

    # 🔥 CRITICAL: NaN → NULL
    df = df.where(pd.notnull(df), None)

    # Load using Snowflake's native bulk loader
    success, nchunks, nrows, _ = write_pandas(
        conn,
        df,
        table_name=table,
        auto_create_table=True,
        overwrite=True
    )

    print(f"Loaded {nrows} rows into RAW.{table}")

conn.close()

print("\n✅ ALL FILES LOADED SUCCESSFULLY INTO SNOWFLAKE RAW SCHEMA")
