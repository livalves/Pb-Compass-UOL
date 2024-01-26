# Lab AWS S3

- Criação de um bucket do Amazon S3 que funcione como hospedagem de conteúdo estático.

1. Criando o bucket no S3

![Criando bucket](capturas/criando-bucket.png)

2. Configurando para hospedagem e atribuindo o index e o arquivo de erro

![Configurando Index](capturas/configurando-index.png)

3. Realizando alterações para que o bucket possa ter acesso público

![Configurando acesso público](capturas/acesso-publico.png)

4. Para acesso, foi configurado as políticas do bucket para torná-lo disponível 

![Alterando as políticas](capturas/mudando-politicas.png)

5. Adicionando os arquivos necessários para o site, foi adicionado o arquivo csv na pasta dados e o arquivo index.html

![Adicionando arquivos](capturas/adicionando-arquivos.png)

6. Adicionando o arquivo de 404.html solicitado, logo nomeado como error.html, nome já escolhido inicialmente nas configurações do bucket

![Adicionando o arquivo de erro](capturas/arquivo-error.png)

7. Após a realização das etapas, o site está funcionando através do acesso ao endpoint 

![Hospedagem do site estático funcionando](capturas/finalizado.png)