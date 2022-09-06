-- creates an index on a table using two columns as key
CREATE INDEX idx_name_first_score ON names (name(1), score)
