-- SQL Loja por Livia Alves 

-- 8 - Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

select 
	tbvendedor.cdvdd,
	tbvendedor.nmvdd
from tbvendedor 
left join tbvendas  
	on tbvendedor.cdvdd = tbvendas.cdvdd 
where tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd
order by count(tbvendas.cdven) desc
limit 1


-- 9 - Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

select 
	cdpro,
	nmpro
from tbvendas 
where status = 'Concluído' and dtven between '2014-02-03' and '2018-02-02' 
group by cdpro
order by count(cdven) desc
limit 1


-- 10 - A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

with vendas as (
	select 
		cdvdd,
		SUM(qtd*vrunt) as valor_total_vendas
	from tbvendas
	where status = 'Concluído'
	group by cdvdd 
)
select 
	tbvendedor.nmvdd as vendedor,
	valor_total_vendas,
	round((valor_total_vendas * tbvendedor.perccomissao * 0.01), 2) as comissao
from tbvendedor 
left join vendas  
	on tbvendedor.cdvdd = vendas.cdvdd 
group by tbvendedor.cdvdd
order by comissao desc


-- 11 - Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

select 
	cdcli,
	nmcli,
	SUM(qtd*vrunt) as gasto
from tbvendas
where status = 'Concluído'
group by nmcli
order by gasto desc
limit 1


-- 12 - Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

with vendas as (
	select 
		cdvdd,
		SUM(qtd*vrunt) as valor_total_vendas
	from tbvendas
	where status = 'Concluído' 
	group by cdvdd 
)
select 
	tbdependente.cddep,
	tbdependente.nmdep,
	tbdependente.dtnasc,
	valor_total_vendas
from tbvendedor 
inner join tbdependente on tbvendedor.cdvdd = tbdependente.cdvdd 
left join vendas on tbvendedor.cdvdd = vendas.cdvdd 
order by valor_total_vendas 
limit 1


-- 13 - Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

select 
	cdpro,
	nmcanalvendas,
	nmpro,
	SUM(qtd) as quantidade_vendas
from tbvendas 
where status = 'Concluído' and (nmcanalvendas = 'Ecommerce' or nmcanalvendas = 'Matriz')
group by cdpro, nmcanalvendas
order by quantidade_vendas
limit 10


-- 14 - Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
-- Observação: Apenas vendas com status concluído.

select 
	estado,
	round((avg(qtd*vrunt)), 2) as gastomedio
from tbvendas
where status = 'Concluído'
group by estado
order by gastomedio desc 


-- 15 - Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

select 
	cdven
from tbvendas
where deletado = 1 
order by cdven 


-- 16 - Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
-- Obs: Somente vendas concluídas.

select 
	estado,
	nmpro,
	round((avg(qtd)), 4) as quantidade_media
from tbvendas
where status = 'Concluído'
group by estado, nmpro 
order by estado, nmpro
