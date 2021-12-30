import requests
from google.cloud import storage

def hello_pubsub_write_file(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
                        event. The `@type` field maps to
                         `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
                        The `data` field maps to the PubsubMessage data
                        in a base64-encoded string. The `attributes` field maps
                        to the PubsubMessage attributes if any is present.
         context (google.cloud.functions.Context): Metadata of triggering event
                        including `event_id` which maps to the PubsubMessage
                        messageId, `timestamp` which maps to the PubsubMessage
                        publishTime, `event_type` which maps to
                        `google.pubsub.topic.publish`, and `resource` which is
                        a dictionary that describes the service API endpoint
                        pubsub.googleapis.com, the triggering topic's name, and
                        the triggering event type
                        `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
    Returns:
        None. The output is written to Cloud Logging.
    """
    import base64

    print("""This Function was triggered by messageId {} published at {} to {}
    """.format(context.event_id, context.timestamp, context.resource["name"]))

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')

        # request_json = request.get_json()
        url = "https://www.six-group.com/exchanges/downloads/indexdata/hsmi.csv"
        r = requests.get(url, allow_redirects=True)

        BUCKET_NAME = 'wm-financial-data'
        #BLOB_STR = '{"blob": "some json"}'
        BLOB_STR = r.content
        BLOB_NAME = 'test-blob.txt'

        upload_blob(BUCKET_NAME, BLOB_STR, BLOB_NAME)
    else:
        name = 'World'

    print('Write {}!'.format(name))

def upload_blob(bucket_name, blob_str, blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.upload_from_string(blob_str)

    print('File {} uploaded to {}.'.format(
        blob_name,
        bucket_name))
