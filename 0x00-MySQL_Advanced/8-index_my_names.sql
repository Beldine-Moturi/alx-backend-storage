-- creates an index on a table using the first letter of a column value
CREATE INDEX idx_name_first on names (name (1));
