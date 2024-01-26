# Lab AWS Lambda

- Criação de uma função lambda e de uma camada com o auxílio da imagem Docker.

1. Criando a função pelo console aws

![Criando função](capturas/criando-funcao.png)

2. Atualizando o código lambda_function.py

![Atualizando código](capturas/atualizando-codigo.png)

3. Realizando o teste para verificação do erro esperado

![Testando código](capturas/erro-esperado.png)

4. Criando imagem docker para implementação da camada com adaptação para suporte do python 3.12

![Criando imagem docker](capturas/criando-imagem.png)

5. Configurando pastas a partir do prompt

![Configurando pastas](capturas/configurando-pastas.png)

6. Compactando os arquivos criados

![Compactando arquivos](capturas/compactando-arquivos.png)

7. Copiando o arquivo compactado para a máquina local 

![Copiando arquivos localmente](capturas/arquivo-copiado.png)

8. Criando um novo bucket para armazenamento do arquivo compactado

![Criando bucket](capturas/novo-bucket.png)

9. Criando camada com a nova imagem 

![Criando camada](capturas/criando-camada.png)

10. Adicionando camada a função lambda

![Adicionando camada](capturas/adicionando-camada.png)

11. Atualizando consulta com o nome do bucket criado no lab S3 que armazena o arquivo nomes.csv

![Atualizando consulta](capturas/atualizando-funcao.png)

12. Função finalizada e funcionando 

![Testando função](capturas/finalizado.png)



