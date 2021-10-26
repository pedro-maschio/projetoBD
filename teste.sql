BEGIN;
--
-- Create model Filme
--
CREATE TABLE "cinema_app_filme" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(200) NOT NULL, "ano_lancamento" integer NOT NULL, "nome_diretor" varchar(200) NOT NULL, "poster_img" varchar(100) NOT NULL, "duracao_min" integer NOT NULL, "elenco" varchar(100) NOT NULL, "genero" varchar(50) NOT NULL, "sinopse" varchar(200) NOT NULL);
--
-- Create model Sala
--
CREATE TABLE "cinema_app_sala" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "numero_assentos" integer NOT NULL);
--
-- Create model Exibicao
--
CREATE TABLE "cinema_app_exibicao" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "audio" varchar(50) NOT NULL, "legenda" varchar(50) NOT NULL, "data" date NOT NULL, "hora" time NOT NULL, "codigo_filme_id" bigint NULL REFERENCES "cinema_app_filme" ("id") DEFERRABLE INITIALLY DEFERRED, "codigo_sala_id" bigint NULL REFERENCES "cinema_app_sala" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Artigo
--
CREATE TABLE "cinema_app_artigo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(100) NOT NULL, "texto" text NOT NULL, "artigo_img" varchar(100) NOT NULL, "author_id" bigint NULL REFERENCES "register_administrador" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "cinema_app_exibicao_codigo_filme_id_406a1fe3" ON "cinema_app_exibicao" ("codigo_filme_id");
CREATE INDEX "cinema_app_exibicao_codigo_sala_id_b4c244ed" ON "cinema_app_exibicao" ("codigo_sala_id");
CREATE INDEX "cinema_app_artigo_author_id_00d8d441" ON "cinema_app_artigo" ("author_id");
COMMIT;
