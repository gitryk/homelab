from google.cloud import storage
import datetime

def generate_signed_url(bucket_name, blob_name, expiration_seconds=3600, method='GET'):
    """Generates a v4 signed URL for downloading a blob.
    Note that this method requires a service account key to authenticate.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # GCS 서비스 어카운트를 이용하여 Signed URL 생성
    # Workload Identity를 통해 이 컨테이너는 자동으로 인증됨
    # 해당 서비스 어카운트가 Signed URL을 생성할 권한을 가져야 함

    # v4 Signed URL은 특정 HTTP Method와 만료 시간을 가짐
    expiration = datetime.timedelta(seconds=expiration_seconds)

    url = blob.generate_signed_url(
        version="v4",
        expiration=expiration,
        method=method, # 'GET', 'PUT', 'DELETE' 등
        # content_type="application/octet-stream" # PUT 요청 시 필요
    )

    print(f"The signed URL for {blob_name} is: {url}")
    print(f"It will expire in {expiration_seconds} seconds.")
    return url

if __name__ == "__main__":
    bucket_name = "test-tryk-bucket" # 실제 버킷 이름
    blob_name = "test.png" # 실제 파일 이름
    generate_signed_url(bucket_name, blob_name)
