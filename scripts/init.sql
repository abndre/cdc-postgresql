CREATE DATABASE my_data_gold;

\c my_data_gold

CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(50),
  sobrenome VARCHAR(50),
  data_nascimento DATE
);

INSERT INTO usuarios (nome, sobrenome, data_nascimento) VALUES
  ('João', 'Silva', '1990-01-01'),
  ('Maria', 'Santos', '1995-05-10'),
  ('Pedro', 'Almeida', '1988-11-20');
