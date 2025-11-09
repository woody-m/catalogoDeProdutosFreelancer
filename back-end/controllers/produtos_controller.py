from flask import Blueprint, request, jsonify
from models import get_connection

# Criando o Blueprint
produtos_bp = Blueprint("produtos", __name__)

@produtos_bp.route("/", methods=["GET"])
def listar_produtos():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM produtos")
    produtos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(produtos)

@produtos_bp.route("/", methods=["POST"])
def criar_produto():
    data = request.json or {}
    nome = data.get("nome")
    preco = data.get("preco")
    if not nome or preco is None:
        return jsonify({"erro": "nome e preco são obrigatórios"}), 400

    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO produtos (nome, descricao, preco) VALUES (?, ?, ?)",
        (nome, data.get("descricao"), preco)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": novo_id, "mensagem": "Produto criado com sucesso!"}), 201

@produtos_bp.route("/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    data = request.json or {}
    nome = data.get("nome")
    preco = data.get("preco")
    if not nome or preco is None:
        return jsonify({"erro": "nome e preco são obrigatórios"}), 400

    conn = get_connection()
    conn.execute(
        "UPDATE produtos SET nome=?, descricao=?, preco=? WHERE id=?",
        (nome, data.get("descricao"), preco, id)
    )
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Produto atualizado com sucesso!"})

@produtos_bp.route("/<int:id>", methods=["DELETE"])
def deletar_produto(id):
    conn = get_connection()
    conn.execute("DELETE FROM produtos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Produto removido com sucesso!"})

