/*
PROJECT: E-Commerce Revenue Analytics
PURPOSE:
This analytics file defines executive-ready KPI queries built on top of
dbt-modeled fact and dimension tables in Snowflake.

DATA NOTE:
The underlying dataset is historical (2016–2018). All queries are written
exactly as they would be in production and are reusable without modification
when connected to live data sources.
*/

-- =========================================================
-- KPI 1: Monthly Revenue Trend (USD)
-- Business Question:
-- How has revenue evolved over time?
-- =========================================================
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    ROUND(SUM(oi.price + oi.freight_value) * 0.20, 2) AS revenue_usd
FROM MART.FACT_ORDERS o
JOIN MART.FACT_ORDER_ITEMS oi
  ON o.order_id = oi.order_id
GROUP BY 1
ORDER BY 1;


-- =========================================================
-- KPI 2: Month-over-Month Revenue Growth (%)
-- Business Question:
-- Are we accelerating or slowing down?
-- =========================================================
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
        SUM(oi.price + oi.freight_value) * 0.20 AS revenue_usd
    FROM MART.FACT_ORDERS o
    JOIN MART.FACT_ORDER_ITEMS oi
      ON o.order_id = oi.order_id
    GROUP BY 1
)
SELECT
    month,
    ROUND(revenue_usd, 2) AS revenue_usd,
    ROUND(
        100 * (revenue_usd - LAG(revenue_usd) OVER (ORDER BY month))
        / NULLIF(LAG(revenue_usd) OVER (ORDER BY month), 0),
        2
    ) AS mom_growth_pct
FROM monthly_revenue
ORDER BY month;
