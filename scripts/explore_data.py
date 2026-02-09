import pandas as pd

print("SCRIPT STARTED")

DATA_PATH = "data/raw"

files = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv"
]

for file in files:
    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    df = pd.read_csv(f"{DATA_PATH}/{file}")

    print("\nColumns:")
    for col in df.columns:
        print(f" - {col}")

    print("\nSample rows:")
    print(df.head(3))

print("\nSCRIPT FINISHED")
