-- 1. Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ; (ponto e vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:

-- CodLivro
-- Titulo
-- CodAutor
-- NomeAutor
-- Valor
-- CodEditora
-- NomeEditora

select 
	cod as CodLivro,
	titulo as Titulo,
	autor as CodAutor,
	autor.nome as NomeAutor,
	valor as Valor,
	editora as CodEditora,
	editora.nome as NomeEditora
from livro
left join autor on livro.autor = autor.codautor 
left join editora on livro.editora = editora.codeditora  
order by valor desc  
limit 10


-- 2. Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. Utilizar o caractere | (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:

-- CodEditora
-- NomeEditora
-- QuantidadeLivros

select 
	codeditora as CodEditora,
	nome as NomeEditora,
	count(livro.cod) as QuantidadeLivros
from editora
inner join livro on editora.codeditora = livro.editora  
group by nome
order by QuantidadeLivros desc
limit 5
