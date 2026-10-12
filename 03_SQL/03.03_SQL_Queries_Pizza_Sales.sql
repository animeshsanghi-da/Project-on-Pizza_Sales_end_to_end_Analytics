USE pizza_db;
SELECT * FROM pizza_sales;
SELECT COUNT(*) FROM pizza_sales;

--------------------------------------
-- KPI METRICS:-
--------------------------------------

-- 1. Total Revenue:
SELECT 
	CAST(SUM(total_price) AS DECIMAL (10,2)) AS Total_Revenue
FROM pizza_sales;

-- 2. Average Order Value
SELECT 
	CAST(SUM(total_price) / COUNT(DISTINCT order_id) AS DECIMAL (5,2)) 
		AS Avg_Order_Value, 
    MAX(total_price) AS Maximum_Order_Value, 
    MIN(total_price) AS Minimum_Order_Value 
FROM pizza_sales;

-- 3. Total Pizzas Sold 
SELECT SUM(quantity) AS Total_Pizzas_Sold FROM pizza_sales;

-- 4. Total Orders 
SELECT COUNT(DISTINCT(order_id)) AS Total_Orders FROM pizza_sales;

-- 5. Average Pizzas Per Order
SELECT 
	CAST(SUM(quantity) / COUNT(DISTINCT(order_id)) AS DECIMAL (10,2))
		AS Average_Pizzas_per_Order
FROM pizza_sales;

--------------------------------------
-- TRENDS FOR TOTAL ORDERS:-
--------------------------------------

-- 6. Hourly Trend for Total Pizzas Sold:
SELECT order_hour, SUM(quantity) AS Total_Pizzas_Sold 
FROM pizza_sales
GROUP BY order_hour
ORDER BY order_hour;

-- 7. Weekly Trend for Orders:
SELECT 
	order_weeknum AS Week_Number_of_2015,
    COUNT(DISTINCT(order_id)) AS Total_Orders
FROM pizza_sales
GROUP BY order_weeknum
ORDER BY order_weeknum;

--------------------------------------
-- PERCENTAGE OF SALES:-
--------------------------------------

-- 8. Percentage of Sales by Pizza Category:
SELECT 
	pizza_category,
    CAST(SUM(total_price) / 100000 AS DECIMAL(10,2)) AS Total_Revenue_in_Lakh,
    CAST(SUM(total_price) * 100 / (SELECT SUM(total_price) FROM pizza_sales) AS DECIMAL(10,2)) AS PCT
FROM pizza_sales
GROUP BY pizza_category
ORDER BY Total_Revenue_in_Lakh DESC;

-- 9. Percentage  of Sales by Pizza Size:
SELECT 
	pizza_size,
    CAST(SUM(total_price) / 100000 AS DECIMAL(10,2)) AS Total_Revenue_in_Lakh,
    CAST(SUM(total_price) * 100 / (SELECT SUM(total_price) FROM pizza_sales) AS DECIMAL(10,2)) AS PCT
FROM pizza_sales
GROUP BY pizza_size
ORDER BY Total_Revenue_in_Lakh DESC;

-- 10. Total Pizzas Sold by Pizza Category:
SELECT 
	pizza_category,
    SUM(quantity) AS Total_Quantity_Sold
FROM pizza_sales
GROUP BY pizza_category
ORDER BY Total_Quantity_Sold DESC;

--------------------------------------
-- BEST AND WORST SELLERS:-
--------------------------------------

-- 11. Top 5 Pizzas by Revenue:
SELECT 
	pizza_name,
    CAST(SUM(total_price) AS DECIMAL (10,2)) AS Total_Revenue 
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Revenue DESC
LIMIT 5;

-- 12. Bottom 5 Pizzas by Revenue:
SELECT 
	pizza_name,
    CAST(SUM(total_price) AS DECIMAL (10,2)) AS Total_Revenue 
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Revenue ASC
LIMIT 5;

-- 13. Top 5 Pizzas by Quantity:
SELECT 
	pizza_name,
    SUM(quantity) AS Total_Pizzas_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Pizzas_Sold DESC
LIMIT 5;

-- 14. Bottom 5 Pizzas by Quantity:
SELECT 
	pizza_name,
    SUM(quantity) AS Total_Pizzas_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Pizzas_Sold ASC
LIMIT 5;

-- 15. Top 5 Pizzas by Total Orders:
SELECT 
	pizza_name,
    COUNT(DISTINCT(order_id)) AS Total_Orders
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Orders DESC
LIMIT 5;

-- 16. Bottom 5 Pizzas by Total Orders:
SELECT 
	pizza_name,
    COUNT(DISTINCT(order_id)) AS Total_Orders
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Orders ASC
LIMIT 5;