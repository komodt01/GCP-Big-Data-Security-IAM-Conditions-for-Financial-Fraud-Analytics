# Lessons Learned

- IP-based IAM conditions like `request.remoteIp` are not supported in standard GCP IAM policy bindings.
- `request.time.getHours()` and `getDayOfWeek()` are supported for fine-grained time-based access control.
- Conditional IAM expressions must be provided using `--condition="title=...,expression=...,description=..."`.
- Attempted formats using multiple flags or incorrect syntax failed due to parsing or unsupported features.
