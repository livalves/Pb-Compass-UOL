import json
import boto3
import requests
from datetime import datetime

def lambda_handler(event, context):
    
    cod_genre = 53
    api_tmdb_key = '' 
    params = "primary_release_date.gte=1990-01-01&primary_release_date.lte=1999-12-31"
    # params = "primary_release_date.gte=2000-01-01&primary_release_date.lte=2009-12-31"
    # params = "primary_release_date.gte=2010-01-01&primary_release_date.lte=2019-12-31"
    # params = "primary_release_date.gte=2020-01-01&primary_release_date.lte=2024-01-31"
    url_tmdb = f"https://api.themoviedb.org/3/discover/movie?api_key={api_tmdb_key}&with_genres={cod_genre}&{params}"
    
    BUCKET_NAME = "data-lake-livia"
    DATE = datetime.now().strftime('%Y/%m/%d')
    HOURS = datetime.now().strftime('%H%M%S')
    
    AWS_FILE_KEY = f"Ram/tmdb/json/{DATE}/data_{cod_genre}-{HOURS}.json"

    response = requests.get(url_tmdb)
    data_tmdb = response.json()
    JSON_DATA_TMDB = json.dumps(data_tmdb, indent=4)
    
    client = boto3.client('s3', 
                            aws_access_key_id = '',
                            aws_secret_access_key = '',
                            aws_session_token = '')
    
    client.put_object(Bucket=BUCKET_NAME, Key=AWS_FILE_KEY, Body=JSON_DATA_TMDB)
 
    return {
        'statusCode': 200,
        'body': 'Ingestao realizada no bucket S3!'
    }
    