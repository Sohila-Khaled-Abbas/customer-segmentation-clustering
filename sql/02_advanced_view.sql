CREATE OR REPLACE VIEW vw_customer_segmentation_enriched AS
WITH segment_avgs AS (
  SELECT
    segment,
    AVG(annual_income) AS avg_income_per_segment,
    AVG(spending_score) AS avg_spending_per_segment
  FROM
    fact_customers
  GROUP BY
    segment
),
ranked_customers AS (
  SELECT
    fc.customer_id,
    fc.segment,
    fc.annual_income,
    fc.spending_score,
    RANK() OVER (PARTITION BY fc.segment ORDER BY fc.spending_score DESC) AS spending_rank_in_segment,
    PERCENT_RANK() OVER (PARTITION BY fc.segment ORDER BY fc.spending_score) AS spending_percentile_in_segment
  FROM
    fact_customers fc
)
SELECT
  rc.*,
  sa.avg_income_per_segment,
  sa.avg_spending_per_segment,
  rc.annual_income - sa.avg_income_per_segment AS income_diff_from_segment_avg,
  rc.spending_score - sa.avg_spending_per_segment AS spending_diff_from_segment_avg
FROM
  ranked_customers rc
  JOIN segment_avgs sa
    ON rc.segment = sa.segment;
