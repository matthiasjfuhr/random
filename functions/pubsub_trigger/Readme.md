 Description
Create a GCP cloud function and use a pubsub topic as trigger

# Setup
1. Install Google Cloud-SDK
2. Activate Cloud Functions and Cloud Build APIs
3. Update gcloud components: > gcloud components update

# Deployment

## Topic
Create a pubsub topic:
> gcloud pubsub topics create test_topic

## Deploy
Go to ~/helloworld and execute the following command:

> gcloud functions deploy hello_pubsub --trigger-topic test_topic --runtime python38