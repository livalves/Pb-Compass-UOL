FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/
COPY upload_s3.py /app/
COPY chaves_aws.py /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade boto3

VOLUME /app/arquivos_csv

CMD ["python", "upload_s3.py"]
