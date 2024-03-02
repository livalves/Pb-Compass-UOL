CREATE VIEW dim_cliente AS
	SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
	FROM Cliente
	
CREATE VIEW dim_vendedor AS
	SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
	FROM Vendedor
	
CREATE VIEW dim_combustivel AS
	SELECT DISTINCT idCombustivel, tipoCombustivel
	FROM Combustivel
	
CREATE VIEW dim_carro AS
	SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
	FROM Carro
	
CREATE VIEW dim_tempo AS
	SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega
	FROM Locacao
	
CREATE VIEW fato_locacao AS
	SELECT DISTINCT idLocacao, idCliente, idVendedor, idCarro, kmCarro, qtdDiaria, vlrDiaria
	FROM Locacao

	