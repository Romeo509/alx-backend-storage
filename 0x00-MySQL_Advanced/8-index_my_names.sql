-- Create index idx_name_first on the first letter of the name column

USE holberton; -- Ensure you are using the correct database

-- Drop the index if it exists (optional, to ensure idempotency)
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create the index on the first letter of the name column
CREATE INDEX idx_name_first ON names (LEFT(name, 1));

-- Optionally, you can verify the index creation
SHOW INDEX FROM names;
