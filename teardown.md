# Teardown Instructions

To remove the conditional access policy from the project:

```bash
gcloud projects remove-iam-policy-binding bigquery-fraud-detection \
  --member="user:k_omodt@msn.com" \
  --role="roles/bigquery.dataViewer"
```
