--1
SELECT id, title, description, status_id
FROM tasks
WHERE user_id = 111;

--2
SELECT id, title, description, status_id
FROM tasks
WHERE status_id = (
    SELECT id
    FROM status
    WHERE name = 'new'
);

--3
UPDATE tasks
SET status_id = (
    SELECT id
    FROM status
    WHERE name = 'in progress'
)
WHERE id = 103;

--4
SELECT id, fullname, email
FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM tasks
);

--5
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Назва завдання', 'Опис завдання', 27, 111);

--6
SELECT id, title, description, status_id, user_id
FROM tasks
WHERE status_id NOT IN (29);

--7
DELETE FROM tasks
WHERE id = 108;

--8 Знайти користувачів з певною електронною поштою. 
SELECT id, fullname, email
FROM users
WHERE email LIKE 'stephanie54@example.net';

--9
UPDATE users
SET fullname = 'new name'
WHERE id = 115;

--10
SELECT status_id, COUNT(*) AS task_count
FROM tasks
GROUP BY status_id;


--11
SELECT t.id, t.title, t.description, t.status_id, t.user_id
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';


--12
SELECT id, title, status_id, user_id
FROM tasks
WHERE description IS NULL OR description = '';

--13
SELECT u.id AS user_id, u.fullname AS user_name, t.id AS task_id, t.title AS task_title
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

--14
SELECT u.id AS user_id, u.fullname AS user_name, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id, u.fullname;






