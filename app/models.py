# app/models.py

from app import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date)
    turma = db.Column(db.String(50))
    contato_responsavel = db.Column(db.String(100))
    endereco = db.Column(db.String(255))
    email = db.Column(db.String(100))

class Educador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    especialidade = db.Column(db.String(100))

class InteracaoEmocional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    educador_id = db.Column(db.Integer, db.ForeignKey('educador.id'), nullable=False)
    data_interacao = db.Column(db.Date, nullable=False)
    tipo_interacao = db.Column(db.Enum('Positiva', 'Negativa', 'Neutra'), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    feedback_educador = db.Column(db.Text)
    acao_recomendada = db.Column(db.Text)
    aluno = db.relationship('Aluno', backref=db.backref('interacoes_emocionais', lazy=True))
    educador = db.relationship('Educador', backref=db.backref('interacoes_emocionais', lazy=True))

class ProjetoFuturo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    interacao_id = db.Column(db.Integer, db.ForeignKey('interacao_emocional.id'))
    nome_projeto = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.Date)
    data_conclusao = db.Column(db.Date)
    status = db.Column(db.Enum('Planejado', 'Em Andamento', 'Concluído'))
    aluno = db.relationship('Aluno', backref=db.backref('projetos_futuros', lazy=True))
    interacao = db.relationship('InteracaoEmocional', backref=db.backref('projetos_futuros', lazy=True))
