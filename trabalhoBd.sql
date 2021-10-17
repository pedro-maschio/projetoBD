CREATE DATABASE IF NOT EXISTS trabalho_bd;
use trabalho_bd;

CREATE TABLE administrador (
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(15) PRIMARY KEY NOT NULL,
    email VARCHAR(70) UNIQUE NOT NULL,
    senha VARCHAR(500) NOT NULL
);

CREATE TABLE cinema (
    cnpj VARCHAR(50) PRIMARY KEY NOT NULL,
    nome varchar(50) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    numero VARCHAR(5) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    codigo_admin VARCHAR(15) NOT NULL,
    FOREIGN KEY (codigo_admin)
        REFERENCES administrador (cpf)
);

CREATE TABLE cliente (
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(15) NOT NULL PRIMARY KEY,
    data_nascimento DATE NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    vacinado BOOL NOT NULL
);

CREATE TABLE sala (
    codigo VARCHAR(5) PRIMARY KEY NOT NULL,
    saida_emergencia BOOL NOT NULL
);

CREATE TABLE assento (
    codigo VARCHAR(3) PRIMARY KEY NOT NULL,
    estado_conservacao VARCHAR(100) NOT NULL,
    adaptada BOOL NOT NULL,
    codigo_sala VARCHAR(5) NOT NULL,
    FOREIGN KEY (codigo_sala)
        REFERENCES sala (codigo)
);

CREATE TABLE filme (
    codigo INT PRIMARY KEY NOT NULL,
    nome VARCHAR(50) NOT NULL,
    ano_lancamento INT NOT NULL,
    nome_diretor VARCHAR(50) NOT NULL,
    audio VARCHAR(50) NOT NULL,
    legenda VARCHAR(50) NOT NULL,
    poster_img LONGBLOB NOT NULL,
    duracao_min INT NOT NULL,
    elenco VARCHAR(200) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    sinopse VARCHAR(200) NOT NULL
);

CREATE TABLE exibicao (
    codigo INT PRIMARY KEY NOT NULL,
    codigo_filme INT NOT NULL,
    codigo_sala VARCHAR(5) NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    FOREIGN KEY (codigo_filme)
        REFERENCES filme (codigo),
    FOREIGN KEY (codigo_sala)
        REFERENCES sala (codigo)
);

CREATE TABLE reserva (
    codigo INT PRIMARY KEY NOT NULL,
    codigo_exibicao INT NOT NULL,
    codigo_cliente VARCHAR(15) NOT NULL,
    codigo_administrador VARCHAR(15) NOT NULL,
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (codigo_exibicao)
        REFERENCES exibicao (codigo),
    FOREIGN KEY (codigo_administrador)
        REFERENCES administrador (cpf),
    FOREIGN KEY (codigo_cliente)
        REFERENCES cliente (cpf)
);

CREATE TABLE artigo (
    codigo INT PRIMARY KEY NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    texto TEXT NOT NULL,
    imagem BLOB NOT NULL,
    autor VARCHAR(15),
    FOREIGN KEY (autor)
        REFERENCES administrador (cpf)
);

CREATE TABLE avaliacao (
    codigo INT PRIMARY KEY NOT NULL,
    nota INT NOT NULL,
    comentario VARCHAR(255),
    filme_codigo INT NOT NULL,
    cliente_codigo VARCHAR(15) NOT NULL,
    FOREIGN KEY (filme_codigo)
        REFERENCES filme (codigo),
    FOREIGN KEY (cliente_codigo)
        REFERENCES cliente (cpf)
);

