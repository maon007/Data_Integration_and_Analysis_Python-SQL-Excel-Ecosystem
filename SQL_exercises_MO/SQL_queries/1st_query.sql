-- Selecting unique visitor ID, first name, last name, and counting occurrences
SELECT
    ua."Unique Visitor ID",
    u."First Name" ,
    u."Last Name" ,
    COUNT(ua."Unique Visitor ID") AS User_Count
FROM
    USERS u
INNER JOIN
    USER_ACTIONS ua ON u."User ID" = ua."Unique Visitor ID"
GROUP BY
    ua."Unique Visitor ID",
    u."First Name" ,
    u."Last Name" 
ORDER BY
    User_Count DESC
LIMIT 10; -- Limiting the output to the top 10 users by action count