-- Top customers by revenue
SELECT CustomerID, SUM(TotalPrice) AS revenue
FROM sales
GROUP BY CustomerID
ORDER BY revenue DESC
LIMIT 10;

-- Monthly revenue
SELECT strftime('%Y-%m', InvoiceDate) AS month,
SUM(TotalPrice) AS revenue
FROM sales
GROUP BY month;