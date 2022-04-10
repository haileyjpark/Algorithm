# Write your MySQL query statement below
SELECT C.Name AS Customers
FROM Customers AS C
LEFT JOIN Orders AS O ON C.Id = O.CustomerID
WHERE O.ID IS NULL