-- This script shows all elements without the empty name
SELECT score, name FROM second_table
WHERE name IS NOT NULL;
