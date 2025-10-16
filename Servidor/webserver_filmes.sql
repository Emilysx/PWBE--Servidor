-- Criar banco de dados
CREATE DATABASE webserver_filmes;
USE webserver_filmes;

-- TABELAS PRINCIPAIS

CREATE TABLE Ator (
    id_ator INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255),
    nacionalidade VARCHAR(255),
    genero ENUM('Masculino', 'Feminino', 'Outro', 'Não Informar') NOT NULL
);

CREATE TABLE Diretor (
    id_diretor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255),
    nacionalidade VARCHAR(255),
    genero ENUM('Masculino', 'Feminino', 'Outro', 'Não Informar') NOT NULL
);

CREATE TABLE Produtora (
    id_produtora INT AUTO_INCREMENT PRIMARY KEY,
    produtora VARCHAR(255) NOT NULL
);

CREATE TABLE Pais (
    id_pais INT AUTO_INCREMENT PRIMARY KEY,
    pais VARCHAR(255) NOT NULL
);

CREATE TABLE Linguagem (
    id_linguagem INT AUTO_INCREMENT PRIMARY KEY,
    linguagem VARCHAR(255) NOT NULL
);

CREATE TABLE Genero (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    genero VARCHAR(255) NOT NULL
);

CREATE TABLE Filme (
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    tempo_duracao TIME,
    ano YEAR,
    poster VARCHAR(255),
    id_linguagem INT,
    FOREIGN KEY (id_linguagem) REFERENCES Linguagem(id_linguagem)
);

-- TABELAS INTERMEDIÁRIAS

CREATE TABLE Filme_Ator (
    id_filme_ator INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    id_ator INT NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
    FOREIGN KEY (id_ator) REFERENCES Ator(id_ator)
);

CREATE TABLE Filme_Diretor (
    id_filme_diretor INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    id_diretor INT NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
    FOREIGN KEY (id_diretor) REFERENCES Diretor(id_diretor)
);

CREATE TABLE Filme_Produtora (
    id_filme_produtora INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    id_produtora INT NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
    FOREIGN KEY (id_produtora) REFERENCES Produtora(id_produtora)
);

CREATE TABLE Filme_Pais (
    id_filme_pais INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    id_pais INT NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
    FOREIGN KEY (id_pais) REFERENCES Pais(id_pais)
);

CREATE TABLE Filme_Genero (
    id_filme_genero INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    id_genero INT NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
    FOREIGN KEY (id_genero) REFERENCES Genero(id_genero)
);

-- INSERTS

-- Linguagem
INSERT INTO Linguagem (linguagem) VALUES
('Inglês'), ('Português'), ('Espanhol'), ('Francês'), ('Alemão'),
('Italiano'), ('Japonês'), ('Chinês'), ('Russo'), ('Coreano'),
('Árabe'), ('Hindi'), ('Holandês'), ('Sueco'), ('Turco'),
('Grego'), ('Tailandês'), ('Vietnamita'), ('Polonês'), ('Dinamarquês');

-- Filme
INSERT INTO Filme (titulo, tempo_duracao, ano, poster, id_linguagem) VALUES
('Divertida Mente 2', '01:36:00', 2024, 'http://www.impawards.com/2024/posters/inside_out_two_ver15_xlg.jpg', 1),
('Super Mario Bros: O Filme', '01:32:00', 2023, 'https://cdn.awsli.com.br/800x800/1610/1610163/produto/208807923/poster-super-mario-bros-o-filme-i-f04111d3.jpg', 1),
('Encanto', '01:42:00', 2021, 'https://br.web.img3.acsta.net/pictures/21/09/29/18/02/2861381.jpg', 2),
('O Menino e a Garça', '02:04:00', 2023, 'https://ingresso-a.akamaihd.net/prd/img/movie/o-menino-e-a-garca/654da114-f4e6-4929-aa37-176f44b84bc7.webp', 7),
('Homem-Aranha no Aranhaverso', '01:57:00', 2018, 'https://www.sonypictures.com.br/sites/brazil/files/2023-06/1400x2100.jpg', 1),
('Elementos', '01:41:00', 2023, 'https://br.web.img3.acsta.net/pictures/22/11/17/20/58/0132283.jpg', 1),
('Soul', '01:40:00', 2020, 'https://apostiladecinema.com.br/wp-content/uploads/2021/01/soul-poster-scaled.jpg', 1),
('Red: Crescer é uma Fera', '01:40:00', 2022, 'https://ingresso-a.akamaihd.net/prd/img/movie/red-crescer-e-uma-fera/ff8826af-fead-443a-917d-215bcee486e2.jpg', 1),
('Viva: A Vida é uma Festa', '01:49:00', 2017, 'https://br.web.img3.acsta.net/pictures/17/12/07/11/33/0502209.jpg', 2),
('Frozen 2', '01:43:00', 2019, 'https://ingresso-a.akamaihd.net/img/cinema/cartaz/22550-cartaz.jpg', 1),
('Zootopia', '01:48:00', 2016, 'https://ingresso-a.akamaihd.net/img/cinema/cartaz/14839-cartaz.jpg', 1),
('Os Incríveis 2', '01:58:00', 2018, 'https://pbs.twimg.com/media/DgOW5tlWsAEzwla.jpg', 1),
('Toy Story 4', '01:40:00', 2019, 'https://m.media-amazon.com/images/I/81haAVSwaWL._UF894,1000_QL80_.jpg', 1),
('Procurando Dory', '01:37:00', 2016, 'https://br.web.img2.acsta.net/pictures/16/06/30/20/49/544752.jpg', 1),
('Luca', '01:35:00', 2021, 'https://br.web.img2.acsta.net/r_1280_720/pictures/21/04/28/15/52/1967183.jpg', 6),
('Moana', '01:47:00', 2016, 'https://m.media-amazon.com/images/I/A1JOaV3B6fL._AC_SL1500_.jpg', 2),
('Carros 3', '01:42:00', 2017, 'https://ingresso-a.akamaihd.net/img/cinema/cartaz/19186-cartaz.jpg', 1),
('O Rei do Show', '01:45:00', 2017, 'https://br.web.img2.acsta.net/pictures/17/11/14/20/38/1278231.jpg', 1),
('Lightyear', '01:45:00', 2022, 'https://ingresso-a.akamaihd.net/prd/img/movie/lightyear/799e6039-8200-4925-aeaa-98ef20a319bb.jpg', 1),
('O Bom Dinossauro', '01:33:00', 2015, 'https://ingresso-a.akamaihd.net/img/cinema/cartaz/13406-cartaz.jpg', 1);

-- Ator
INSERT INTO Ator (nome, sobrenome, nacionalidade, genero) VALUES
('Amy', 'Poehler', 'Americana', 'Feminino'),
('Chris', 'Pratt', 'Americano', 'Masculino'),
('Stephanie', 'Beatriz', 'Americana', 'Feminino'),
('Soma', 'Santoki', 'Japonesa', 'Feminino'),
('Shameik', 'Moore', 'Americano', 'Masculino'),
('Leah', 'Lewis', 'Americana', 'Feminino'),
('Jamie', 'Foxx', 'Americano', 'Masculino'),
('Rosalie', 'Chiang', 'Americana', 'Feminino'),
('Anthony', 'Gonzalez', 'Mexicano', 'Masculino'),
('Idina', 'Menzel', 'Americana', 'Feminino'),
('Ginnifer', 'Goodwin', 'Americana', 'Feminino'),
('Craig', 'T. Nelson', 'Americano', 'Masculino'),
('Tom', 'Hanks', 'Americano', 'Masculino'),
('Ellen', 'DeGeneres', 'Americana', 'Feminino'),
('Jacob', 'Tremblay', 'Canadense', 'Masculino'),
('Auli’i', 'Cravalho', 'Havaiana', 'Feminino'),
('Owen', 'Wilson', 'Americano', 'Masculino'),
('Hugh', 'Jackman', 'Australiano', 'Masculino'),
('Chris', 'Evans', 'Americano', 'Masculino'),
('Raymond', 'Ochoa', 'Americano', 'Masculino');

-- Diretor
INSERT INTO Diretor (nome, sobrenome, nacionalidade, genero) VALUES
('Kelsey', 'Mann', 'Americano', 'Masculino'),
('Aaron', 'Horvath', 'Americano', 'Masculino'),
('Byron', 'Howard', 'Americano', 'Masculino'),
('Hayao', 'Miyazaki', 'Japonês', 'Masculino'),
('Peter', 'Ramsey', 'Americano', 'Masculino'),
('Peter', 'Sohn', 'Americano', 'Masculino'),
('Pete', 'Docter', 'Americano', 'Masculino'),
('Domee', 'Shi', 'Chinesa', 'Feminino'),
('Lee', 'Unkrich', 'Americano', 'Masculino'),
('Chris', 'Buck', 'Americano', 'Masculino'),
('Rich', 'Moore', 'Americano', 'Masculino'),
('Brad', 'Bird', 'Americano', 'Masculino'),
('Josh', 'Cooley', 'Americano', 'Masculino'),
('Andrew', 'Stanton', 'Americano', 'Masculino'),
('Enrico', 'Casarosa', 'Italiano', 'Masculino'),
('Ron', 'Clements', 'Americano', 'Masculino'),
('Brian', 'Fee', 'Americano', 'Masculino'),
('Michael', 'Gracey', 'Australiano', 'Masculino'),
('Angus', 'MacLane', 'Americano', 'Masculino'),
('Peter', 'Sohn', 'Americano', 'Masculino');

-- Produtora
INSERT INTO Produtora (produtora) VALUES
('Pixar Animation Studios'),
('Illumination'),
('Walt Disney Animation Studios'),
('Studio Ghibli'),
('Sony Pictures Animation'),
('Pixar Animation Studios'),
('Pixar Animation Studios'),
('Pixar Animation Studios'),
('Pixar Animation Studios'),
('Walt Disney Animation Studios'),
('Walt Disney Animation Studios'),
('Pixar Animation Studios'),
('Pixar Animation Studios'),
('Pixar Animation Studios'),
('Pixar Animation Studios'),
('Walt Disney Animation Studios'),
('Pixar Animation Studios'),
('20th Century Fox'),
('Pixar Animation Studios'),
('Pixar Animation Studios');

-- País
INSERT INTO Pais (pais) VALUES
('Estados Unidos'),
('Japão'),
('México'),
('Canadá'),
('Austrália'),
('Reino Unido'),
('Itália'),
('França'),
('Espanha'),
('China'),
('Coreia do Sul'),
('Brasil'),
('Alemanha'),
('Dinamarca'),
('Argentina'),
('Suécia'),
('Noruega'),
('Nova Zelândia'),
('Irlanda'),
('Filipinas');

-- Gênero
INSERT INTO Genero (genero) VALUES
('Animação'),
('Aventura'),
('Comédia'),
('Drama'),
('Família'),
('Musical'),
('Fantasia'),
('Ficção Científica'),
('Romance'),
('Ação'),
('Mistério'),
('Histórico'),
('Biografia'),
('Terror'),
('Policial'),
('Suspense'),
('Guerra'),
('Esporte'),
('Documentário'),
('Musical');

-- Filme_Ator
INSERT INTO Filme_Ator (id_filme, id_ator) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),
(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20);

-- Filme_Diretor
INSERT INTO Filme_Diretor (id_filme, id_diretor) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),
(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20);

-- Filme_Produtora
INSERT INTO Filme_Produtora (id_filme, id_produtora) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),
(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20);

-- Filme_Pais
INSERT INTO Filme_Pais (id_filme, id_pais) VALUES
(1,1),(2,1),(3,1),(4,2),(5,1),(6,1),(7,1),(8,1),(9,3),(10,1),
(11,1),(12,1),(13,1),(14,1),(15,6),(16,1),(17,1),(18,5),(19,1),(20,1);

-- Filme_Genero
INSERT INTO Filme_Genero (id_filme, id_genero) VALUES
(1,1), (2,2), (3,5), (4,7), (5,2), (6,3), (7,4), (8,5), (9,6), (10,7),
(11,3), (12,1), (13,1), (14,5), (15,3), (16,2), (17,10), (18,6), (19,8), (20,5);