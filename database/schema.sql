CREATE TABLE dim_customer(
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    segment VARCHAR(100)
);

CREATE TABLE dim_product(
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(50),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    product_name TEXT
);

CREATE TABLE dim_region(
    region_key SERIAL PRIMARY KEY,
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(100)
);

CREATE TABLE dim_date(
    date_key DATE PRIMARY KEY,
    year INT,
    quarter INT,
    month INT,
    month_name VARCHAR(20),
    day INT
);

CREATE TABLE sales_fact(
    sales_key SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    date_key DATE,
    sales FLOAT,
    quantity INT,
    discount FLOAT,
    profit FLOAT
);