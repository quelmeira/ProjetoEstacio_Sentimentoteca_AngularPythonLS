CREATE DATABASE IF NOT EXISTS gestao_alunos;

USE gestao_alunos;

CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    turma VARCHAR(50),
    contato_responsavel VARCHAR(100),
    endereco VARCHAR(255),
    email VARCHAR(100)
);

CREATE TABLE educadores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    especialidade VARCHAR(100)
);

CREATE TABLE interacoes_emocionais (
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_id INT,
    educador_id INT,
    data_interacao DATE NOT NULL,
    tipo_interacao ENUM('Positiva', 'Negativa', 'Neutra') NOT NULL,
    descricao TEXT NOT NULL,
    feedback_educador TEXT,
    acao_recomendada TEXT,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE,
    FOREIGN KEY (educador_id) REFERENCES educadores(id) ON DELETE CASCADE
);

CREATE TABLE projetos_futuros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_id INT,
    interacao_id INT,
    nome_projeto VARCHAR(100),
    descricao TEXT,
    data_inicio DATE,
    data_conclusao DATE,
    status ENUM('Planejado', 'Em Andamento', 'Concluído'),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE,
    FOREIGN KEY (interacao_id) REFERENCES interacoes_emocionais(id) ON DELETE CASCADE
);

INSERT INTO alunos (nome, data_nascimento, turma, contato_responsavel, endereco, email)
VALUES 
('João Silva', '2010-05-12', '5A', 'Maria Silva, (11) 91234-5678', 'Rua das Flores, 123', 'maria@exemplo.com'),
('Ana Souza', '2009-09-22', '6B', 'Carlos Souza, (11) 93456-7890', 'Av. Paulista, 456', 'carlos@exemplo.com');

INSERT INTO educadores (nome, email, telefone, especialidade)
VALUES 
('Marcos Oliveira', 'marcos@escola.com', '(11) 98765-4321', 'Psicologia'),
('Patrícia Lima', 'patricia@escola.com', '(11) 99876-5432', 'Pedagogia');

INSERT INTO interacoes_emocionais (aluno_id, educador_id, data_interacao, tipo_interacao, descricao, feedback_educador, acao_recomendada)
VALUES 
(1, 1, '2024-09-14', 'Positiva', 'Aluno mostrou grande interesse em ajudar colegas', 'Parabéns pelo comportamento', 'Promover atividades colaborativas'),
(2, 2, '2024-09-14', 'Negativa', 'Aluno tem se mostrado desmotivado nas aulas', 'Incentivar participação ativa', 'Sessões com psicólogo escolar');
