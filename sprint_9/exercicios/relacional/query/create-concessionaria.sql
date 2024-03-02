CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY NOT NULL,
    nomeCliente VARCHAR(100) NOT NULL,
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);


CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15) NOT NULL,
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);


CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20) NOT NULL
);


CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR(50) NOT NULL,
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);


CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idVendedor INT,
    idCarro INT,
    kmCarro INT,
    dataLocacao DATETIME NOT NULL,
    horaLocacao TIME,
    qtdDiaria INT NOT NULL,
    vlrDiaria DECIMAL(18,2) NOT NULL,
    dataEntrega DATE NOT NULL,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro)
);


