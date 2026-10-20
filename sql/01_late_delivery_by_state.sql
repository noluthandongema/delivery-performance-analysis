-- Q2: Which customer states have the worst late-delivery rates?
--
-- An order counts as late when it reached the customer after the
-- estimated delivery date. Only delivered orders are included.

SELECT
    c.customer_state,
    COUNT(*) AS delivered_orders,
    SUM(CASE
            WHEN date(o.order_delivered_customer_date) > date(o.order_estimated_delivery_date)
            THEN 1 ELSE 0
        END) AS late_orders,
    ROUND(
        100.0 * SUM(CASE
                        WHEN date(o.order_delivered_customer_date) > date(o.order_estimated_delivery_date)
                        THEN 1 ELSE 0
                    END) / COUNT(*),
        1
    ) AS late_pct
FROM orders AS o
JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
GROUP BY c.customer_state
HAVING COUNT(*) >= 100          -- ignore states with very few orders
ORDER BY late_pct DESC;
