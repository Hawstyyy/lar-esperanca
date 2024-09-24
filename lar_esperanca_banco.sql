-- Active: 1727181197773@@35.198.53.133@3306
use laresperanca;

CREATE Table funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    cpf VARCHAR(15) UNIQUE,
    usuario VARCHAR(20) UNIQUE,
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

INSERT INTO funcionario (cpf, usuario, senha, nome_completo, rg, endereco, data_nascimento)
VALUES
('123.456.789-00', 'joaos', SHA2('joaos1', 256), 'João Silva', '12.345.678-9', 'Rua A,123,Bairro X', '1990-01-01'),
('987.654.321-00', 'mariao', SHA2('maria1', 256), 'Maria Oliveira', '98.765.432-1', 'Rua B,456,Bairro Y', '1985-05-15'),
('555.666.777-88', 'carloss', SHA2('carlos1', 256), 'Carlos Souza', '55.666.777-8', 'Rua C,789,Bairro Z', '2000-09-09');

INSERT INTO paciente (nome_paciente, id_funcionario, status_paciente)
VALUES
('Ana Paula', 1, TRUE),
('Roberto Carlos', 2, TRUE),
('Fernanda Lima', 3, TRUE),
('Marcelo Gomes', 1, TRUE),
('Cláudia Souza', 2, TRUE),
('Bruno Silva', 3, TRUE);

INSERT INTO remedio (nome_remedio)
VALUES
('Paracetamol 500mg'),
('Paracetamol 750mg'),
('Ibuprofeno 200mg'),
('Ibuprofeno 400mg'),
('Aspirina 100mg'),
('Aspirina 500mg'),
('Amoxicilina 500mg'),
('Amoxicilina 875mg'),
('Omeprazol 20mg'),
('Omeprazol 40mg'),
('Simeticona 125mg'),
('Loratadina 10mg'),
('Dipirona 500mg'),
('Dipirona 1g'),
('Captopril 25mg'),
('Captopril 50mg'),
('Cloridrato de Metformina 500mg'),
('Cloridrato de Metformina 850mg'),
('Salbutamol 100mcg'),
('Salbutamol 200mcg'),
('Ranitidina 150mg'),
('Ranitidina 300mg'),
('Losartana 50mg'),
('Losartana 100mg'),
('Atorvastatina 10mg'),
('Atorvastatina 20mg'),
('Cetirizina 10mg'),
('Diclofenaco 50mg'),
('Diclofenaco 75mg'),
('Prednisona 20mg');

insert into sinal_vital (temperatura, pressao_sistolica, pressao_diastolica, pressao_cardiaca, saturacao, id_estado_risco, id_funcionario, id_paciente) values(0.5, 3, 4, 2, 1, 1, 1, 1);

insert into sinal_vital (temperatura, pressao_sistolica, pressao_diastolica, pressao_cardiaca, saturacao, id_estado_risco, id_funcionario, id_paciente) values(0.56, 3, 4, 2, 1, 1, 1, 1);