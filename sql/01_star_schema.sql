-- Dimension: Gender
CREATE TABLE dim_genders (
    gender_id SERIAL PRIMARY KEY,
    gender TEXT UNIQUE
);

-- Dimension: Age Ranges
CREATE TABLE dim_age_ranges (
    age_range_id SERIAL PRIMARY KEY,
    age_min INT,
    age_max INT,
    age_label TEXT
);

-- Fact: Customers
CREATE TABLE fact_customers (
    customer_id INT PRIMARY KEY,
    gender_id INT,
    age_range_id INT,
    age INT,
    annual_income FLOAT,
    spending_score FLOAT,
    segment INT,
    FOREIGN KEY (gender_id) REFERENCES dim_genders(gender_id),
    FOREIGN KEY (age_range_id) REFERENCES dim_age_ranges(age_range_id)
);
