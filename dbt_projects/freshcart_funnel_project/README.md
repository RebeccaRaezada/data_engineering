# FreshCart Funnel Analysis (dbt)

This project models a signup-to-purchase funnel by user signup week, using dbt best practices.

## Funnel Steps
- Signup
- Browse
- Add to Cart
- Purchase

## Models
- `stg_user_events`: cleaned raw event logs
- `int_user_funnels`: user-level funnel flags + signup cohort
- `fct_user_funnel_by_week`: aggregated funnel by signup week

## Usage
```bash
dbt run
dbt test
dbt docs generate
```
