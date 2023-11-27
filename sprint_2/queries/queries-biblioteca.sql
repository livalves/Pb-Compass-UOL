-- SQL Biblioteca por Livia Alves 

-- 1- Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

select * from livro  
where publicacao > '2014-12-31'
order by cod


-- 2- Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente. Atenção às colunas esperadas no resultado final:  titulo, valor.

select 
	titulo,
	valor
from livro
order by valor desc  
limit 10


-- 3-  Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select 
	count(livro.cod) as quantidade,
	nome,
	endereco.estado,
	endereco.cidade 
from editora
inner join livro on editora.codeditora = livro.editora  
left join endereco on editora.endereco = endereco.codendereco 
group by nome
order by quantidade desc
limit 5


-- 4- Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

select 
	nome,
	codautor,
	nascimento,
	count(livro.cod) as quantidade
from autor
left join livro 
	on autor.codautor = livro.autor 
group by nome
order by nome


-- 5- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

select 
	distinct nome
from autor 
left join livro 
	on autor.codautor = livro.autor 
where livro.editora = 
	(
		select 
			editora.codeditora
		from editora
		left join endereco 
			on editora.endereco = endereco.codendereco 
		where endereco.estado not in ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
	)
group by nome 
having count(livro.cod) > 0
order by nome 


-- 6- Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

select 
	codautor,
	nome,
	COUNT(livro.cod) as quantidade_publicacoes 
from autor 
left join livro 
on autor.codautor = livro.autor 
group by nome 
order by quantidade_publicacoes desc
limit 1


-- 7- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

select 
	nome
from autor 
left join livro 
	on autor.codautor = livro.autor 
where livro.autor is null
order by nome 


