CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(255),
    segment VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_product (
    product_id VARCHAR(50) PRIMARY KEY,
    category VARCHAR(100),
    sub_category VARCHAR(100),
    product_name TEXT
);

CREATE TABLE IF NOT EXISTS dim_region (
    region_id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_key DATE PRIMARY KEY,
    year INT,
    quarter INT,
    month INT,
    month_name VARCHAR(20),
    day INT
);

CREATE TABLE IF NOT EXISTS sales_fact (
    sales_id SERIAL PRIMARY KEY,

    order_id VARCHAR(50),

    customer_id VARCHAR(50),

    product_id VARCHAR(50),

    date_key DATE,

    sales FLOAT,

    quantity INT,

    discount FLOAT,

    profit FLOAT
);