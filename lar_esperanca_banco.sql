-- Active: 1726756977448@@db4free.net@3306@laresperanca
use laresperanca;


CREATE Table funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(15),
    senha VARCHAR(70),
    nome_completo VARCHAR(100),
    rg VARCHAR(15),
    endereco VARCHAR(100),
    data_nascimento DATE
);

CREATE Table estado_risco (
    id_estado_risco INT PRIMARY KEY AUTO_INCREMENT,
    estado VARCHAR(30)
);

CREATE Table paciente (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    nome_paciente VARCHAR(100),
    id_funcionario int,
    status_paciente BOOLEAN,
    Foreign Key (id_funcionario) REFERENCES funcionario(id_funcionario)
);

CREATE TABLE remedio (
    id_remedio INT PRIMARY KEY AUTO_INCREMENT,
    nome_remedio VARCHAR(100)
);

CREATE TABLE receita (
    id_receita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente int,
    id_remedio int,
    status_remedio BOOLEAN,
    horario_inicial TIME,
    intervalo_remedio TINYINT,
    Foreign Key (id_paciente) REFERENCES paciente(id_paciente),
    Foreign Key (id_remedio) REFERENCES remedio(id_remedio)
);

CREATE Table sinal_vital (
    id_sinal_vital INT PRIMARY KEY AUTO_INCREMENT,
    temperatura FLOAT,
    pressao_diastolica SMALLINT,
    pressao_sistolica SMALLINT,
    pressao_cardiaca SMALLINT,
    saturacao FLOAT,
    id_estado_risco INT,
    id_funcionario INT,
    Foreign Key (id_funcionario) REFERENCES funcionario(id_funcionario),
    Foreign Key (id_estado_risco) REFERENCES estado_risco(id_estado_risco)
);

CREATE TABLE intercorrencia(
    id_intercorrencia INT PRIMARY KEY AUTO_INCREMENT,
    id_funcionario INT,
    id_paciente INT,
    id_sinal_vital INT,
    texto TEXT,
    data_intercorrencia DATE,
    Foreign Key (id_funcionario) REFERENCES funcionario(id_funcionario),
    Foreign Key (id_paciente) REFERENCES paciente(id_paciente),
    Foreign Key (id_sinal_vital) REFERENCES sinal_vital(id_sinal_vital)
);

INSERT INTO estado_risco VALUES 
(null, 'Normal'),
(null, 'Risco');

describe sinal_vital;