CREATE DATABASE IF NOT EXISTS trabalho_bd;
use trabalho_bd;



CREATE TABLE administrador (
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) PRIMARY KEY NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);


CREATE TABLE cinema (
    cnpj VARCHAR(18) PRIMARY KEY NOT NULL,
    nome varchar(50) NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    codigo_admin VARCHAR(15) NOT NULL,
    FOREIGN KEY (codigo_admin)
        REFERENCES administrador (cpf)
);

CREATE TABLE cliente (
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    vacinado BOOL NOT NULL
);

CREATE TABLE sala (
	codigo INT PRIMARY KEY AUTO_INCREMENT,
    codigo_cinema VARCHAR(18) NOT NULL,
    sessao_3d BOOL  NOT NULL,
    sessao_normal BOOL NOT NULL,
    sessao_platinum BOOL NOT NULL,
    FOREIGN KEY (codigo_cinema)
        REFERENCES cinema (cnpj)
);

CREATE TABLE assento (
    codigo INT PRIMARY KEY NOT NULL,
    fileira CHAR NOT NULL,
    numero INT NOT NULL,
    estado_conservacao VARCHAR(100) NOT NULL,
    adaptada BOOL NOT NULL,
    reservado BOOL NOT NULL,
    codigo_sala INT NOT NULL,
    FOREIGN KEY (codigo_sala)
        REFERENCES sala (codigo)
);

CREATE TABLE filme (
    codigo INT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    ano_lancamento INT NOT NULL,
    nome_diretor VARCHAR(100) NOT NULL,
    poster_img LONGBLOB,
    duracao_min INT NOT NULL,
    elenco VARCHAR(255) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    sinopse VARCHAR(2000) NOT NULL
);

CREATE TABLE exibicao (
    codigo INT PRIMARY KEY NOT NULL,
    codigo_filme INT NOT NULL,
    codigo_sala INT NOT NULL,
    codigo_cinema VARCHAR(18),
    audio VARCHAR(50) NOT NULL,
    legenda VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    FOREIGN KEY (codigo_filme)
        REFERENCES filme (codigo),
    FOREIGN KEY (codigo_sala)
        REFERENCES sala (codigo),
	FOREIGN KEY (codigo_cinema)
		REFERENCES cinema(cnpj)
);


CREATE TABLE reserva (
    codigo INT PRIMARY KEY NOT NULL,
    codigo_exibicao INT NOT NULL,
    codigo_cliente VARCHAR(15) NOT NULL,
    codigo_administrador VARCHAR(14) NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL,
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
    imagem LONGBLOB NOT NULL,
    autor VARCHAR(14),
    FOREIGN KEY (autor)
        REFERENCES administrador (cpf)
);

CREATE TABLE avaliacao (
    codigo INT PRIMARY KEY NOT NULL,
    nota INT NOT NULL,
    comentario VARCHAR(255),
    codigo_filme INT NOT NULL,
    codigo_cliente VARCHAR(14) NOT NULL,
    FOREIGN KEY (codigo_filme)
        REFERENCES filme (codigo),
    FOREIGN KEY (codigo_cliente)
        REFERENCES cliente (cpf)
);

# Administrador
INSERT INTO administrador(nome, cpf, email, senha) VALUES("Pedro de Torres Maschio", "819.166.051-25", "190018763@aluno.unb.br", "yonyk7aCRmig@5%FR");
INSERT INTO administrador(nome, cpf, email, senha) VALUES("Marcus Vinicius Abrantes", "799.062.168-16", "190034084@aluno.unb.br", "d*p8tvAyLB4#s8Xto");
INSERT INTO administrador(nome, cpf, email, senha) VALUES("Joao Antonio da Silva", "841.641.513-74", "joao@gmail.com", "wjwwTM^vZTFUT8hc!");
INSERT INTO administrador(nome, cpf, email, senha) VALUES("Maria de Souza Marques", "331.360.501-00", "maria@gmail.com", "&xYUgb@XUF67MJVwM");
INSERT INTO administrador(nome, cpf, email, senha) VALUES("Patrícia Beltrão Nogueira", "678.203.532-44", "patricia@gmail.com", "B7k!KpkBgUhvG&y75");


# Cinema
INSERT INTO cinema(cnpj, nome, endereco, cep, numero, cidade, estado, codigo_admin) VALUES("18.236.582/0001-75", "Cinema Premium", "Rua Fictícia, Quadra 3", "72322-403", 4, "Brasília", "Distrito Federal", "819.166.051-25");
INSERT INTO cinema(cnpj, nome, endereco, cep, numero, cidade, estado, codigo_admin) VALUES("35.658.462/0001-85", "Cinema Brasília", "Rua Fictícia, Quadra 4", "73215-000", 0, "Brasília", "Distrito Federal", "819.166.051-25");
INSERT INTO cinema(cnpj, nome, endereco, cep, numero, cidade, estado, codigo_admin) VALUES("81.276.435/0001-65", "Cinema Capital", "Rua Fictícia, Quadra 5", "73005-591", 11, "Brasília", "Distrito Federal", "678.203.532-44");
INSERT INTO cinema(cnpj, nome, endereco, cep, numero, cidade, estado, codigo_admin) VALUES("82.263.132/0001-70", "Cinema Deluxe", "Rua Fictícia, Quadra 6", "74262-009", 9, "Brasília", "Distrito Federal", "678.203.532-44");
INSERT INTO cinema(cnpj, nome, endereco, cep, numero, cidade, estado, codigo_admin) VALUES("91.106.222/0001-49", "Cinema Brasil", "Rua Fictícia, Quadra 7", "72392-003", 13, "Brasília", "Distrito Federal", "799.062.168-16");


# Cliente
INSERT INTO cliente(nome, cpf, email, senha, data_nascimento, sexo, vacinado) VALUES("Carla de Souza Marques", "788.325.518-53", "carla@gmail.com", "TfR3nK!qs$2HM*4v@", "1978-09-30", "Feminino", True);
INSERT INTO cliente(nome, cpf, email, senha, data_nascimento, sexo, vacinado) VALUES("Marcos Pereira de Abreu", "194.613.624-71", "marcos@gmail.com", "sK9cJhT9!48o72d2*", "2009-04-01", "Masculino", False);
INSERT INTO cliente(nome, cpf, email, senha, data_nascimento, sexo, vacinado) VALUES("Joana Farias Gomes", "830.701.851-00", "joana@gmail.com", "%bSZaaSTwPS8a3CtT", "2013-01-30", "Feminino", False);
INSERT INTO cliente(nome, cpf, email, senha, data_nascimento, sexo, vacinado) VALUES("Ana Paula Beltrão", "095.354.581-40", "ana@gmail.com", "yh6pj3!@6PPa%4$Km", "1960-12-15", "Feminino", True);
INSERT INTO cliente(nome, cpf, email, senha, data_nascimento, sexo, vacinado) VALUES("Antonio César Gomes", "158.586.433-10", "antonio@gmail.com", "kj9^Wyg36q4$Exsr2", "1991-07-24", "Masculino", True);


# Sala
INSERT INTO sala(codigo_cinema) VALUES("18.236.582/0001-75");
INSERT INTO sala(codigo_cinema) VALUES("18.236.582/0001-75");
INSERT INTO sala(codigo_cinema) VALUES("81.276.435/0001-65");
INSERT INTO sala(codigo_cinema) VALUES("91.106.222/0001-49");
INSERT INTO sala(codigo_cinema) VALUES("35.658.462/0001-85");


# Assento
INSERT INTO assento VALUES(1, "A", 1, "Bem conservado", True, 1);
INSERT INTO assento VALUES(2, "F", 1, "Pequenos rasgos no encosto", False, 1);
INSERT INTO assento VALUES(3, "F", 2, "Range constantemente", False, 4);
INSERT INTO assento VALUES(4, "C", 5, "Bem conservado", True, 4);
INSERT INTO assento VALUES(5, "G", 7, "Bem conservado", True, 4);


# Filme
INSERT INTO filme VALUES(1, "A Outra História Americana", 1998, "Tony Kaye", LOAD_FILE("/var/lib/mysql-files/american-history-x.jpg"), 119, "Edward Norton, Fairuza Balk, Avery Brooks etc.", "Crime/Drama", "Derek (Edward Norton) busca vazão para suas agruras tornando-se líder de uma gangue de racistas. A violência o leva a um assassinato, e ele é condenado pelo crime. Três anos mais tarde, ele sai da prisão e tem que convencer seu irmão (Edward Furlong), que está prestes a assumir a liderança do grupo, a não trilhar o mesmo caminho.");
INSERT INTO filme VALUES(2, "Um Sonho de Liberdade", 1994, "Frank Darabont", LOAD_FILE("/var/lib/mysql-files/um-sonho-de-liberdade.jpg"), 142, "Tim Robbins, Morgan Freeman, Bob Gunton etc.", "Crime/Drama", "Em 1946, Andy Dufresne (Tim Robbins), um jovem e bem sucedido banqueiro, tem a sua vida radicalmente modificada ao ser condenado por um crime que nunca cometeu, o homicídio de sua esposa e do amante dela. Ele é mandado para uma prisão que é o pesadelo de qualquer detento, a Penitenciária Estadual de Shawshank, no Maine. Lá ele irá cumprir a pena perpétua. Andy logo será apresentado a Warden Norton (Bob Gunton), o corrupto e cruel agente penitenciário, que usa a Bíblia como arma de controle e ao Capitão Byron Hadley (Clancy Brown) que trata os internos como animais. Andy faz amizade com Ellis Boyd Redding (Morgan Freeman), um prisioneiro que cumpre pena há 20 anos e controla o mercado negro da instituição.");
INSERT INTO filme VALUES(3, "O Homem que Copiava", 2003, "Jorge Furtado", LOAD_FILE("/var/lib/mysql-files/o-homem-que-copiava.jpg"), 123, "Leandra Leal, Luana Piovani, Lázaro Ramos etc.", "Romance/Comédia", "Em O Homem que Copiava, André (Lázaro Ramos) é um jovem de 20 anos que trabalha na fotocopiadora da papelaria Gomide, localizada em Porto Alegre. André mora com a mãe e tem uma vida comum, basicamente vivendo de casa para o trabalho e realizando sempre as mesmas atividades. Num dia André se apaixona por Sílvia (Leandra Leal), uma vizinha, a qual passa a observar com os binóculos em seu quarto. Decidido a conhecê-la melhor, André descobre que ela trabalha em uma loja de roupas e, para conseguir uma aproximação, tenta de todas as formas conseguir 38 reais para comprar um suposto presente para sua mãe.");
INSERT INTO filme VALUES(4, "Triângulo do Medo", 2009, "Christopher Smith", LOAD_FILE("/var/lib/mysql-files/triangulo-do-medo.jpg"), 99, "Melissa George, Liam Hemsworth, Michael Dorman etc.", "Horror/Suspense", "Quando Jess embarca em um veleiro com um grupo de amigos para o alto mar, ela tem o pressentimento de algo está errado. Sua suspeita se realiza quando eles vão parar no meio de uma tempestade e para sobreviverem, todos são forçados a embarcar em um misterioso e aparentemente desocupado transatlântico. Ao caminhar pelos corredores, Jess tem a sensação de que já esteve no local antes e repara que o relógio do navio está parado. Estranhas coisas começam a acontecer e eles percebem que não estão sozinhos: alguém está caçando-os, um por um, e Jess, sem saber, está com a chave para encerrar todo esse terror.");
INSERT INTO filme VALUES(5, "Réquiem para um Sonho", 2000, "Darren Aronofsky", LOAD_FILE("/var/lib/mysql-files/requiem-para-um-sonho.jpg"), 102, "Jennifer Connelly, Jared Leto, Marlon Wayans etc.", "Drama/Terror psicológico", "Uma visão frenética, perturbada e única sobre pessoas que vivem em desespero e ao mesmo tempo cheio de sonhos. Harry Goldfarb (Jared Leto) e Marion Silver (Jennifer Connelly) formam um casal apaixonado, que tem como sonho montar um pequeno negócio e viverem felizes para sempre. Porém, ambos são viciados em heroína, o que faz com que repetidamente Harry penhore a televisão de sua mãe (Ellen Burstyn), para conseguir dinheiro. Já Sara, mãe de Harry, viciada em assistir programas de TV. Até que um dia recebe um convite para participar do seu show favorito, o 'Tappy Tibbons Show', que transmitido para todo o país. Para poder vestir seu vestido predileto, Sara começa a tomar pílulas de emagrecimento, receitadas por seu médico. Só que, aos poucos, Sara começa a tomar cada vez mais pílulas até se tornar uma viciada neste medicamento.");


# Exibição
INSERT INTO exibicao(codigo, codigo_filme, codigo_sala, codigo_cinema, audio, legenda, data, horario) VALUES(1, 1, 1, "18.236.582/0001-75", "Português", "N/A", "2021-10-18", "15:00:00");
INSERT INTO exibicao(codigo, codigo_filme, codigo_sala, codigo_cinema, audio, legenda, data, horario) VALUES(2, 1, 1, "35.658.462/0001-85", "Inglês", "Português", "2021-10-19", "15:00:00");
INSERT INTO exibicao(codigo, codigo_filme, codigo_sala, codigo_cinema, audio, legenda, data, horario) VALUES(3, 3, 2, "91.106.222/0001-49", "Francês", "Português", "2021-10-20", "19:15:00");
INSERT INTO exibicao(codigo, codigo_filme, codigo_sala, codigo_cinema, audio, legenda, data, horario) VALUES(4, 4, 5, "91.106.222/0001-49", "Português", "Inglês", "2021-10-22", "22:10:00");
INSERT INTO exibicao(codigo, codigo_filme, codigo_sala, codigo_cinema, audio, legenda, data, horario) VALUES(5, 5, 4, "35.658.462/0001-85", "Português", "Inglês", "2021-10-21", "14:00:00");


# Reserva
INSERT INTO reserva(codigo, codigo_exibicao, codigo_cliente, codigo_administrador, data, hora) VALUES(1, 1, "788.325.518-53", "819.166.051-25", "2021-10-18", "16:03:31");
INSERT INTO reserva(codigo, codigo_exibicao, codigo_cliente, codigo_administrador, data, hora) VALUES(2, 2, "194.613.624-71", "819.166.051-25", "2021-10-18", "08:05:13");
INSERT INTO reserva(codigo, codigo_exibicao, codigo_cliente, codigo_administrador, data, hora) VALUES(3, 3, "194.613.624-71", "819.166.051-25", "2021-10-20", "17:03:47");
INSERT INTO reserva(codigo, codigo_exibicao, codigo_cliente, codigo_administrador, data, hora) VALUES(4, 4, "095.354.581-40", "819.166.051-25", "2021-10-18", "16:13:31");
INSERT INTO reserva(codigo, codigo_exibicao, codigo_cliente, codigo_administrador, data, hora) VALUES(5, 5, "095.354.581-40", "819.166.051-25", "2021-10-25", "20:40:33");


# Artigo
INSERT INTO artigo(codigo, titulo, texto, imagem, autor) VALUES (1, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet nulla malesuada pellentesque elit. Faucibus ornare suspendisse sed nisi lacus sed. Sit amet nisl suscipit adipiscing. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Arcu odio ut sem nulla pharetra. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Nulla pellentesque dignissim enim sit amet venenatis urna. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.", LOAD_FILE("/var/lib/mysql-files/imagem-artigo.png"), "799.062.168-16");
INSERT INTO artigo(codigo, titulo, texto, imagem, autor) VALUES (2, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet nulla malesuada pellentesque elit. Faucibus ornare suspendisse sed nisi lacus sed. Sit amet nisl suscipit adipiscing. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Arcu odio ut sem nulla pharetra. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Nulla pellentesque dignissim enim sit amet venenatis urna. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.", LOAD_FILE("/var/lib/mysql-files/imagem-artigo.png"), "799.062.168-16");
INSERT INTO artigo(codigo, titulo, texto, imagem, autor) VALUES (3, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet nulla malesuada pellentesque elit. Faucibus ornare suspendisse sed nisi lacus sed. Sit amet nisl suscipit adipiscing. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Arcu odio ut sem nulla pharetra. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Nulla pellentesque dignissim enim sit amet venenatis urna. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.", LOAD_FILE("/var/lib/mysql-files/imagem-artigo.png"), "799.062.168-16");
INSERT INTO artigo(codigo, titulo, texto, imagem, autor) VALUES (4, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet nulla malesuada pellentesque elit. Faucibus ornare suspendisse sed nisi lacus sed. Sit amet nisl suscipit adipiscing. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Arcu odio ut sem nulla pharetra. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Nulla pellentesque dignissim enim sit amet venenatis urna. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.", LOAD_FILE("/var/lib/mysql-files/imagem-artigo.png"), "799.062.168-16");
INSERT INTO artigo(codigo, titulo, texto, imagem, autor) VALUES (5, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet nulla malesuada pellentesque elit. Faucibus ornare suspendisse sed nisi lacus sed. Sit amet nisl suscipit adipiscing. Malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Arcu odio ut sem nulla pharetra. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Nulla pellentesque dignissim enim sit amet venenatis urna. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate.", LOAD_FILE("/var/lib/mysql-files/imagem-artigo.png"), "799.062.168-16");


# Avaliação
INSERT INTO avaliacao(codigo, nota, comentario, codigo_filme, codigo_cliente) VALUES(1, 10, "Excelente Filme", 1, "788.325.518-53");
INSERT INTO avaliacao(codigo, nota, comentario, codigo_filme, codigo_cliente) VALUES(2, 8, "Excelente Filme", 1, "194.613.624-71");
INSERT INTO avaliacao(codigo, nota, comentario, codigo_filme, codigo_cliente) VALUES(3, 7, "Excelente Filme", 2, "830.701.851-00");
INSERT INTO avaliacao(codigo, nota, comentario, codigo_filme, codigo_cliente) VALUES(4, 3, "Filme Muito Ruim", 4, "788.325.518-53");
INSERT INTO avaliacao(codigo, nota, comentario, codigo_filme, codigo_cliente) VALUES(5, 10, "Excelente Filme", 5, "095.354.581-40");

# Uma view que exibe todos os filmes em exibição no período noturno

CREATE VIEW filmes_noturnos AS
    SELECT
        *
    FROM
        exibicao
    WHERE
        exibicao.horario >= '18:00:00';

SELECT
    *
FROM
    filmes_noturnos;


# Procedure reserva_em_intervalo permite obter todas as reservas realizadas por um cliente entre duas datas.
# pode ser útil para criar uma página de histórico no perfil do cliente, por exemplo.

DELIMITER $$
CREATE PROCEDURE reserva_em_intervalo(IN quantidade INT, IN codigo_cliente VARCHAR(15), IN data_inicial DATE, IN data_final DATE)
BEGIN
	SELECT
    *
FROM
    reserva
WHERE
    reserva.codigo_cliente = codigo_cliente
        AND reserva.data >= data_inicial
        AND reserva.data <= data_final;
END $$
DELIMITER ;

# Chamada
#CALL reserva_em_intervalo(3, "095.354.581-40", "2021-10-18", "2021-10-25");
