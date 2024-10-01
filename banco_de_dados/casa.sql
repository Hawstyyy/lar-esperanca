-- Active: 1726092351703@@192.168.100.52@3306@laresperanca

create database laresperanca;
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
    id_paciente INT,
    Foreign Key (id_funcionario) REFERENCES funcionario(id_funcionario),
    Foreign Key (id_estado_risco) REFERENCES estado_risco(id_estado_risco),
    Foreign Key (id_paciente) REFERENCES paciente(id_paciente)
);

CREATE TABLE intercorrencia(
    id_intercorrencia INT PRIMARY KEY AUTO_INCREMENT,
    id_funcionario INT,
    id_sinal_vital INT,
    texto TEXT,
    data_intercorrencia DATE,
    Foreign Key (id_funcionario) REFERENCES funcionario(id_funcionario),
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

INSERT INTO paciente (id_paciente, nome_paciente) VALUES 
(1, 'Paciente 1'),
(2, 'Paciente 2'),
(3, 'Paciente 3'),
(4, 'Paciente 4'),
(5, 'Paciente 5'),
(6, 'Paciente 6'),
(7, 'Paciente 7'),
(8, 'Paciente 8'),
(9, 'Paciente 9'),
(10, 'Paciente 10'),
(11, 'Paciente 11'),
(12, 'Paciente 12'),
(13, 'Paciente 13'),
(14, 'Paciente 14'),
(15, 'Paciente 15'),
(16, 'Paciente 16'),
(17, 'Paciente 17'),
(18, 'Paciente 18'),
(19, 'Paciente 19'),
(20, 'Paciente 20'),
(21, 'Paciente 21'),
(22, 'Paciente 22'),
(23, 'Paciente 23'),
(24, 'Paciente 24'),
(25, 'Paciente 25'),
(26, 'Paciente 26'),
(27, 'Paciente 27'),
(28, 'Paciente 28'),
(29, 'Paciente 29'),
(30, 'Paciente 30'),
(31, 'Paciente 31'),
(32, 'Paciente 32'),
(33, 'Paciente 33'),
(34, 'Paciente 34'),
(35, 'Paciente 35'),
(36, 'Paciente 36'),
(37, 'Paciente 37'),
(38, 'Paciente 38'),
(39, 'Paciente 39'),
(40, 'Paciente 40'),
(41, 'Paciente 41'),
(42, 'Paciente 42'),
(43, 'Paciente 43'),
(44, 'Paciente 44'),
(45, 'Paciente 45'),
(46, 'Paciente 46'),
(47, 'Paciente 47'),
(48, 'Paciente 48'),
(49, 'Paciente 49'),
(50, 'Paciente 50'),
(51, 'Paciente 51'),
(52, 'Paciente 52'),
(53, 'Paciente 53'),
(54, 'Paciente 54'),
(55, 'Paciente 55'),
(56, 'Paciente 56');

INSERT INTO sinal_vital (temperatura, pressao_sistolica, pressao_diastolica, pressao_cardiaca, saturacao, id_estado_risco, id_paciente) VALUES
(36.5, 120, 80, 70, 98.0, 1, 1),   -- Paciente 1 - Normal
(37.5, 130, 85, 75, 95.0, 2, 2),   -- Paciente 2 - Risco
(36.8, 125, 80, 72, 97.5, 1, 3),   -- Paciente 3 - Normal
(37.2, 140, 90, 78, 94.5, 2, 4),   -- Paciente 4 - Risco
(36.9, 122, 78, 68, 99.0, 1, 5),   -- Paciente 5 - Normal
(37.1, 135, 83, 74, 95.5, 2, 6),   -- Paciente 6 - Risco
(36.7, 118, 76, 70, 97.8, 1, 7),   -- Paciente 7 - Normal
(37.3, 145, 92, 81, 91.0, 2, 8),   -- Paciente 8 - Risco
(36.4, 120, 80, 72, 98.5, 1, 9),   -- Paciente 9 - Normal
(37.4, 150, 95, 85, 89.5, 2, 10),  -- Paciente 10 - Risco
(36.6, 126, 82, 73, 96.0, 1, 11),  -- Paciente 11 - Normal
(37.2, 140, 88, 76, 92.0, 2, 12),  -- Paciente 12 - Risco
(36.5, 121, 79, 71, 97.0, 1, 13),  -- Paciente 13 - Normal
(37.0, 135, 84, 78, 94.0, 2, 14),  -- Paciente 14 - Risco
(36.8, 123, 77, 72, 98.5, 1, 15),  -- Paciente 15 - Normal
(37.1, 145, 89, 75, 90.0, 2, 16),  -- Paciente 16 - Risco
(36.9, 127, 81, 73, 95.0, 1, 17),  -- Paciente 17 - Normal
(37.3, 150, 93, 82, 88.0, 2, 18),  -- Paciente 18 - Risco
(36.4, 119, 75, 70, 98.0, 1, 19),  -- Paciente 19 - Normal
(37.5, 155, 96, 85, 87.0, 2, 20),  -- Paciente 20 - Risco
(36.6, 128, 82, 74, 96.5, 1, 21),  -- Paciente 21 - Normal
(37.4, 142, 90, 77, 91.5, 2, 22),  -- Paciente 22 - Risco
(36.7, 126, 78, 71, 97.0, 1, 23),  -- Paciente 23 - Normal
(37.2, 145, 92, 79, 89.0, 2, 24),  -- Paciente 24 - Risco
(36.8, 120, 79, 73, 98.0, 1, 25),  -- Paciente 25 - Normal
(37.3, 150, 95, 81, 90.5, 2, 26),  -- Paciente 26 - Risco
(36.5, 124, 80, 72, 97.0, 1, 27),  -- Paciente 27 - Normal
(37.1, 138, 89, 75, 91.0, 2, 28),  -- Paciente 28 - Risco
(36.9, 130, 82, 70, 96.0, 1, 29),  -- Paciente 29 - Normal
(37.4, 148, 94, 78, 88.5, 2, 30),  -- Paciente 30 - Risco
(36.6, 123, 78, 73, 97.5, 1, 31),  -- Paciente 31 - Normal
(37.3, 140, 90, 76, 92.0, 2, 32),  -- Paciente 32 - Risco
(36.7, 125, 80, 72, 96.5, 1, 33),  -- Paciente 33 - Normal
(37.2, 145, 92, 78, 89.5, 2, 34),  -- Paciente 34 - Risco
(36.4, 120, 79, 75, 98.0, 1, 35),  -- Paciente 35 - Normal
(37.5, 150, 95, 81, 90.5, 2, 36),  -- Paciente 36 - Risco
(36.8, 128, 82, 74, 97.0, 1, 37),  -- Paciente 37 - Normal
(37.1, 138, 88, 76, 92.0, 2, 38),  -- Paciente 38 - Risco
(36.9, 124, 80, 72, 96.5, 1, 39),  -- Paciente 39 - Normal
(37.3, 152, 96, 80, 88.0, 2, 40),  -- Paciente 40 - Risco
(36.6, 125, 82, 71, 97.0, 1, 41),  -- Paciente 41 - Normal
(37.0, 140, 89, 74, 93.0, 2, 42),  -- Paciente 42 - Risco
(36.8, 126, 81, 73, 97.5, 1, 43),  -- Paciente 43 - Normal
(37.4, 145, 92, 78, 90.5, 2, 44),  -- Paciente 44 - Risco
(36.5, 120, 80, 70, 98.0, 1, 45),  -- Paciente 45 - Normal
(37.5, 155, 95, 85, 87.0, 2, 46),  -- Paciente 46 - Risco
(36.6, 121, 79, 72, 97.0, 1, 47),  -- Paciente 47 - Normal
(37.2, 138, 90, 76, 92.0, 2, 48),  -- Paciente 48 - Risco
(36.9, 126, 80, 71, 98.5, 1, 49),  -- Paciente 49 - Normal
(37.3, 150, 93, 78, 89.5, 2, 50),  -- Paciente 50 - Risco
(36.4, 119, 75, 70, 98.0, 1, 51),  -- Paciente 51 - Normal
(37.5, 155, 96, 85, 87.0, 2, 52),  -- Paciente 52 - Risco
(36.6, 122, 78, 69, 98.0, 1, 53),  -- Paciente 53 - Normal
(37.1, 140, 88, 74, 91.0, 2, 54),  -- Paciente 54 - Risco
(36.8, 123, 77, 72, 97.0, 1, 55),  -- Paciente 55 - Normal
(37.4, 150, 95, 83, 90.0, 2, 56);  -- Paciente 56 - Risco


select count(*) from paciente;