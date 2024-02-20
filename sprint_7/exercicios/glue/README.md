## Lab AWS Glue 

- Construindo um processo de ETL simplificado utilizando o serviço AWS Glue.

1. Preparando os dados de origem
- No serviço S3 da AWS foi criado o bucket *sprint-lab* para armazenamento dos dados. 

![Criando bucket no S3](capturas/criando-bucket.png)

2. Configurando conta para utilizar o AWS Glue
- Foi adicionado o usuário *adm-livia.alves* para acesso ao serviço AWS Glue, assim como, foi configurado o acesso ao S3.

![Adicionando usuário ao Glue](capturas/adicionando-usuario.png)
![Configurando Glue](capturas/configurando-s3.png)

3. Criando IAM Role para os jobs do AWS Glue
- Foi criado a role chamada *AWSGlueServiceRole-Lab4* com as permissões necessárias.

![Criação da role](capturas/role-criada.png)
![Permissões da role](capturas/permissoes-role.png)

4. Configurando as permissões no AWS LakeFormation
- Foi criado o database chamado *glue-lab*, e logo adicionado o usuário como administrador principal do data lake.

![Criando database](capturas/criando-banco.png)
![Permissões de usuário](capturas/permissoes-banco.png)

- Em seguida, foi configurado a role de permissões para o database criado.

![Configurando role](capturas/adicionando-role.png)
![Role adicionada](capturas/role-adicionada.png)

5. Criando novo job no AWS Glue
- Tentativa de criação do job para processamento do arquivo *nomes.csv* com spark, foi iniciado a configuração dos detalhes do job. 

![Registro de erro nas permissões](capturas/erro-job.png)

- Em seguida, foi realizado a tentativa de configuração do path para leitura do arquivo csv e armazenamento dos resultados.

![Acesso negado ao configurar path](capturas/erro-path.png)
![Tentando rodar job](capturas/rodando-job.png)

- Sem execuções de jobs devido as permissões.

![Verificando jobs](capturas/verificando-jobs.png)


