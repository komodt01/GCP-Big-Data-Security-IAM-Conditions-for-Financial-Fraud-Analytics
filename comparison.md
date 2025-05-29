# Technology Comparison: GCP vs AWS vs Azure

| Feature                        | GCP (This Project)                          | AWS                              | Azure                                  |
|-------------------------------|---------------------------------------------|-----------------------------------|-----------------------------------------|
| IAM Conditions                | Yes (project-level, using `request.time`)   | Yes (Conditions in IAM policies) | Yes (Condition Access in Role Assignments) |
| Time-based access             | ✅ Supported via `request.time.getHours()`   | ✅ With IAM policy condition keys | ✅ With Azure Condition Access Policies |
| IP-based access (native)      | ❌ Only via Access Context Manager           | ✅ CIDR blocks via policy         | ✅ Named location and IP conditions     |
| Access Context Manager (ACM)  | ✅ Advanced perimeters, needs org-level      | N/A                               | N/A                                     |
