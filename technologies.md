# Technologies Used

## BigQuery
- Fully-managed enterprise data warehouse used to store and query structured fraud analytics data.

## IAM Conditions
- Fine-grained access control policy used to allow conditional access based on request context like time and day.

## Google Cloud CLI (`gcloud`)
- Command-line interface used to configure and apply conditional IAM policies programmatically.

## Expression Language
- Used conditional logic with `request.time.getHours("UTC")` and `request.time.getDayOfWeek()` to enforce weekday and hourly restrictions.
