import boto3
from datetime import datetime
from chaves_aws import aws_access_key_id, aws_secret_access_key, aws_session_token

BUCKET_NAME = "data-lake-livia"
DATE = datetime.now().strftime('%Y/%m/%d')

LOCAL_FILE_NAME_MOVIES = "/app/arquivos_csv/movies.csv"
LOCAL_FILE_NAME_SERIES = "/app/arquivos_csv/series.csv"

AWS_FILE_KEY_MOVIES = f"Ram/Local/CSV/Movies/{DATE}/movies.csv"
AWS_FILE_KEY_SERIES = f"Ram/Local/CSV/Series/{DATE}/series.csv"

def main(): 
    client = boto3.client('s3', 
                            aws_access_key_id = aws_access_key_id,
                            aws_secret_access_key = aws_secret_access_key,
                            aws_session_token = aws_session_token)
    
    try:
        client.put_object(Bucket=BUCKET_NAME, Key=AWS_FILE_KEY_MOVIES, Body=LOCAL_FILE_NAME_MOVIES)
        client.put_object(Bucket=BUCKET_NAME, Key=AWS_FILE_KEY_SERIES, Body=LOCAL_FILE_NAME_SERIES)
        print(f"Sucesso! Os arquivos foram salvos no bucket S3")
    except Exception as e:
        print(f"Erro durante o upload: {e}")

if __name__ == '__main__':
    main()
