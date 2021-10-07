create database if not exists trabalho_bd;
use trabalho_bd;

create table administrador (
	nome varchar(50) not null,
    cpf varchar(15) primary key not null,
    email varchar(70) unique not null,
    senha varchar(500) not null
);


create table cinema (
	cnpj varchar(50) primary key not null,
    endereco varchar(50) not null,
    cep varchar(20) not null,
    numero varchar(5) not null,
    cidade varchar(50) not null,	
    estado varchar(50) not null,
    codigo_admin varchar(15) not null,
    
    foreign key(codigo_admin) references administrador(cpf)
);

create table cliente (
	nome varchar(50) not null,
    cpf varchar(15) not null primary key,
    data_nascimento date not null,
    sexo varchar(10) not null,
    vacinado bool not null
);

create table sala (
	codigo varchar(5) primary key not null,
    numero_assentos int not null,
    saida_emergencia bool not null
);

create table assento (
	numero int primary key not null,
    fileira int not null,
	estado_conservacao varchar(100) not null,
    adaptada bool not null,
    codigo_sala varchar(5) not null,
    
    foreign key(codigo_sala) references sala(codigo)
);

create table filme (
	codigo int primary key not null,
	nome varchar(50) not null,
    ano_lancamento int not null,
    nome_diretor varchar(50) not null,
    audio varchar(50) not null,
    legenda varchar(50) not null,	
    poster_img longblob not null,
    duracao_min	 int not null,
    elenco varchar(200) not null,
    genero varchar(50) not null,
    sinopse varchar(200) not null
);

create table exibicao (
	codigo int primary key not null,
    codigo_filme int not null,
    codigo_sala varchar(5) not null,
    horario datetime not null,
    foreign key(codigo_filme) references filme(codigo),
    foreign key(codigo_sala) references sala(codigo)
);

create table reserva (
	codigo int primary key not null,
    codigo_exibicao int not null,
    codigo_cliente varchar(15) not null,
    codigo_administrador varchar(15) not null,
    horario_reserva datetime not null,
    
    foreign key(codigo_exibicao) references exibicao(codigo),
    foreign key(codigo_administrador) references administrador(cpf),
    foreign key(codigo_cliente) references cliente(cpf)
);

create table artigo (
	codigo int primary key not null,
    titulo varchar(200) not null,
    texto text not null,
    imagem blob not null,
    autor varchar(15),
    
    foreign key(autor) references administrador(cpf)
);

create table avaliacao (
	codigo int primary key not null,
    nota int not null,
    comentario varchar(255),
    filme_codigo int not null,
    cliente_codigo varchar(15) not null,
    
    foreign key(filme_codigo) references filme(codigo),
    foreign key(cliente_codigo) references cliente(cpf)
);

