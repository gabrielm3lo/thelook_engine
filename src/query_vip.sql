WITH clientes_compras AS (
    SELECT 
        user_id AS cliente_id,
        SUM(sale_price) AS total_gasto
    FROM `thelook_ecommerce.order_items`
    WHERE status = 'Complete'
    GROUP BY user_id
)
SELECT 
    cliente_id, 
    total_gasto
FROM clientes_compras
WHERE total_gasto > 500
ORDER BY total_gasto DESC;