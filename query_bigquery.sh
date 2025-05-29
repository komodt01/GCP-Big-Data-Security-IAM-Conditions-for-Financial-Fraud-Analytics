#!/bin/bash
gcloud auth application-default login
gcloud config set project PROJECT_ID
gcloud bigquery query "SELECT * FROM \`project.dataset.table\` LIMIT 10"