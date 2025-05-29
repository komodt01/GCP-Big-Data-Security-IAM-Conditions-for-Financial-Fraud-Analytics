## IAM Conditions Setup (Time-based)

This policy restricts BigQuery access to weekdays (Mon–Fri) between 08:00 and 17:59 UTC:

```bash
gcloud projects add-iam-policy-binding bigquery-fraud-detection \
  --member="user:k_omodt@msn.com" \
  --role="roles/bigquery.dataViewer" \
  --condition="title=WorkWeekAccessOnly,expression=request.time.getHours('UTC') >= 8 && request.time.getHours('UTC') < 18 && request.time.getDayOfWeek() >= 1 && request.time.getDayOfWeek() <= 5,description=Allow BigQuery access only Mon–Fri during 08:00–17:59 UTC"
```
