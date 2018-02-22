import boto3

bucket = 'dash-cache-images'


# Upload local file to S3
def upload(byte_stream):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    print('S3 Client Initiated')

    s3.upload_file(byte_stream, bucket, file_key)
    # s3.Bucket('review-app-jh').put_object(Key=filename, Body=data)

    print('S3 Upload Completed')

    return s3, file_key


# This wraps the upload and URL creation for the Graph
def add_and_upload_simple(byte_stream):
    s3, uploaded_file_id = upload(byte_stream)
    url = gen_URL(bucket, uploaded_file_id, s3)
    return url


# Generate URL from object ID
def gen_URL(bucket, key, s3):
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        }
    )
    return url
