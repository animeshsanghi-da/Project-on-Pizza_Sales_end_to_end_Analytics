CREATE DATABASE IF NOT EXISTS pizza_db;
USE pizza_db;

CREATE TABLE pizza_sales (
    pizza_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    unique_order INT NOT NULL,
    pizza_name_id VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    order_time TIME NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    pizza_size VARCHAR(10) NOT NULL,
    pizza_category VARCHAR(50) NOT NULL,
    pizza_name VARCHAR(100) NOT NULL,
    order_weeknum INT NOT NULL,
    order_day VARCHAR(5) NOT NULL,
    order_month  VARCHAR(5) NOT NULL,
    order_hour VARCHAR(10) NOT NULL
);