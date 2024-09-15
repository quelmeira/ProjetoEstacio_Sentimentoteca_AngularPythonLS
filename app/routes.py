from app import app, db
from flask import jsonify, request
from app.models import Pensamento

@app.route('/pensamentos', methods=['GET', 'POST'])
def get_pensamentos():
    if request.method == 'GET':
        pensamentos = Pensamento.query.all()
        return jsonify([pensamento.as_dict() for pensamento in pensamentos])
    elif request.method == 'POST':
        data = request.get_json()
        new_pensamento = Pensamento(
            conteudo=data['conteudo'],
            autoria=data['autoria'],
            modelo=data['modelo'],
            favorito=data.get('favorito', False)
        )
        db.session.add(new_pensamento)
        db.session.commit()
        return jsonify(new_pensamento.as_dict()), 201

@app.route('/pensamentos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_pensamento(id):
    pensamento = Pensamento.query.get(id)
    if not pensamento:
        return jsonify({'error': 'Pensamento not found'}), 404
    if request.method == 'GET':
        return jsonify(pensamento.as_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        pensamento.conteudo = data.get('conteudo', pensamento.conteudo)
        pensamento.autoria = data.get('autoria', pensamento.autoria)
        pensamento.modelo = data.get('modelo', pensamento.modelo)
        pensamento.favorito = data.get('favorito', pensamento.favorito)
        db.session.commit()
        return jsonify(pensamento.as_dict())
    elif request.method == 'DELETE':
        db.session.delete(pensamento)
        db.session.commit()
        return jsonify({'message': 'Pensamento deleted'}), 200
