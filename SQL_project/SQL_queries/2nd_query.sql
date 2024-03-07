-- Selecting period, category, first name, last name, and counting rows
SELECT
    fc.PERIOD,
    ua."GenClick Cleansed" AS Category,
    u."First Name",
    u."Last Name",
    COUNT(*) AS Row_Count
FROM
    FISCAL_CALENDAR fc
INNER JOIN
    USER_ACTIONS ua ON DATE(ua.Date) = DATE(fc.LAST_DAY)
INNER JOIN
    USERS u ON ua."Unique Visitor ID" = u."User ID" 
WHERE
    (u."Last Name" = 'Edwards' OR u."Last Name" = 'Harris')
    AND 
    fc.PERIOD LIKE '%JUN%'
GROUP BY
    fc.PERIOD,
    ua."GenClick Cleansed",
    u."First Name",
    u."Last Name"
ORDER BY
    Row_Count DESC;
-- The query returns 17 rows