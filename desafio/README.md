# Projeto Final ⏳

## Parte 1 

- Criando código Python que carrega arquivos CSV para a Nuvem utilizando técnicas de ETL.

1. O seguinte código python implementa o processso de upload dos dois arquivos disponibilizados do tipo csv (movies.csv e series.csv) para um bucket S3 na AWS utilizando a lib boto3 e seguindo o padrão de exemplo **S3:\\data-lake-da-livia\Raw\Local\CSV\Series\2024\02\19\series.csv** para salvamento dos dados.

- [Código Python](parte_1/upload_aws/upload_s3.py)

Para funcionanmento do código, deve ser inserido no arquivo *chaves_aws.py* as suas respectivas credenciais AWS. Assim como no primeiro código, deve ser alterado o nome do bucket para o seu de referência. 

- [Código Python - Chaves_AWS](parte_1/upload_aws/chaves_aws.py)

Complementar, os arquivos abaixo auxiliam na criação da imagem docker:

- [Dockerfile](parte_1/upload_aws/Dockerfile)
- [Requirements](parte_1/upload_aws/requirements.txt)

Para realizar o upload dos arquivos, foi criada uma pasta chamada *dados* que armazenava os dois arquivos, movies.csv e series.csv, para compartilhamento no volume do Docker.

2. Logo após foi criado a imagem docker utilizando o comado `docker build -t upload-s3 .`, excecutando localmente o container *up-dados-s3* através do comando `docker run --name up-dados-s3 -v dados:/app/arquivos_csv upload-s3`

> Criando imagem upload-s3 no Docker
![Criando imagem](parte_1/capturas/criando-imagem.png)

> Executando container Docker
![Executando container](parte_1/capturas/up-dados.png)

> Upload dos arquivos nas respectivas pastas no bucket S3  
![Console AWS - Ambas as pastas](parte_1/capturas/bucketS3.png)
![Console AWS - Arquivo Movies](parte_1/capturas/salvo-movies.png)
![Console AWS - Arquivo Series](parte_1/capturas/salvo-series.png)