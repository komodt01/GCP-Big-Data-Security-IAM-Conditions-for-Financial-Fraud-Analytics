# Test IAM Access
import google.auth
from google.cloud import bigquery

client = bigquery.Client()
query = "SELECT COUNT(*) FROM `project.dataset.table`"
print(client.query(query).result())