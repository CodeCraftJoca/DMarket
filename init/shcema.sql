CREATE DATABASE IF NOT EXISTS dmarket_database;

CREATE TABLE IF NOT EXISTS `dmarket_database`. `users` (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL
    last_name VARCHAR(255 NOT NULL)
    age BIGINT NOT NULL
    primary key (id)
)