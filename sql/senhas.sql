CREATE DATABASE IF NOT EXISTS senhas;

CREATE TABLE IF NOT EXISTS `senhas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `senha` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
);

CREATE TABLE IF NOT EXISTS `senhas_chamadas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `senha` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
);
