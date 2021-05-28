# Description
Create a GCP cloud function and use a http request as trigger

# Setup
1. Install Google Cloud-SDK
2. Activate Cloud Functions and Cloud Build APIs
3. Update gcloud components: > gcloud components update

# Deployment
## Deploy
Go to ~/helloworld and execute the following command:

> gcloud functions deploy hello_http --runtime python38 --trigger-http --allow-unauthenticated

## Trigger
Open your browser and trigger cloud function using the following url:

https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello_http.cloudfunctions.net/hello_http?name=Matthias

## Check logs
Go to ~/helloworld and execute the following command:

> gcloud functions logs read hello_http