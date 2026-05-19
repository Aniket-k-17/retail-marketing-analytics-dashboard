-- =========================================
-- RETAIL & MARKETING ANALYTICS SQL QUERIES
-- =========================================


-- 1️⃣ TOP 10 CITIES BY TOTAL ORDERS

SELECT 
    c.customer_city,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_city
ORDER BY total_orders DESC
LIMIT 10;



-- 2️⃣ TOTAL REVENUE GENERATED

SELECT 
    ROUND(SUM(p.payment_value), 2) AS total_revenue
FROM payments p;



-- 3️⃣ MONTHLY REVENUE TREND

SELECT 
    strftime('%Y-%m', o.order_purchase_timestamp) AS order_month,
    ROUND(SUM(p.payment_value), 2) AS monthly_revenue
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
GROUP BY order_month
ORDER BY order_month;



-- 4️⃣ TOP 10 STATES BY REVENUE

SELECT 
    c.customer_state,
    ROUND(SUM(p.payment_value), 2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY total_revenue DESC
LIMIT 10;



-- 5️⃣ MOST USED PAYMENT TYPES

SELECT 
    payment_type,
    COUNT(*) AS usage_count
FROM payments
GROUP BY payment_type
ORDER BY usage_count DESC;



-- 6️⃣ ORDER STATUS DISTRIBUTION

SELECT 
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;



-- 7️⃣ TOP 10 CUSTOMERS BY SPENDING

SELECT 
    c.customer_unique_id,
    ROUND(SUM(p.payment_value), 2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY total_spent DESC
LIMIT 10;



-- 8️⃣ AVERAGE ORDER VALUE

SELECT 
    ROUND(AVG(payment_value), 2) AS avg_order_value
FROM payments;



-- 9️⃣ TOTAL CUSTOMERS BY STATE

SELECT 
    customer_state,
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;



-- 🔟 TOP PRODUCT CATEGORIES BY SALES

SELECT 
    pr.product_category_name,
    ROUND(SUM(p.payment_value), 2) AS total_sales
FROM products pr
JOIN order_items oi
ON pr.product_id = oi.product_id
JOIN payments p
ON oi.order_id = p.order_id
GROUP BY pr.product_category_name
ORDER BY total_sales DESC
LIMIT 10;



-- 1️⃣1️⃣ AVERAGE FREIGHT COST

SELECT 
    ROUND(AVG(freight_value), 2) AS avg_freight_cost
FROM order_items;



-- 1️⃣2️⃣ REVENUE CONTRIBUTION BY PAYMENT TYPE

SELECT 
    payment_type,
    ROUND(SUM(payment_value), 2) AS total_revenue
FROM payments
GROUP BY payment_type
ORDER BY total_revenue DESC;



-- 1️⃣3️⃣ TOP CITIES BY REVENUE

SELECT 
    c.customer_city,
    ROUND(SUM(p.payment_value), 2) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments p
ON o.order_id = p.order_id
GROUP BY c.customer_city
ORDER BY total_revenue DESC
LIMIT 10;



-- 1️⃣4️⃣ TOTAL ORDERS PER YEAR

SELECT 
    strftime('%Y', order_purchase_timestamp) AS order_year,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY order_year
ORDER BY order_year;



-- 1️⃣5️⃣ CUSTOMER PURCHASE FREQUENCY

SELECT 
    c.customer_unique_id,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
ORDER BY total_orders DESC