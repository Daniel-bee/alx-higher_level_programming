-- list
UPDATE second_table SET score = 12, name = 'Aria' WHERE name = 'George';
INSERT INTO second_table (id, name, score) VALUES (2, "Aria", 18);
SELECT score, name FROM second_table ORDER BY score DESC;
