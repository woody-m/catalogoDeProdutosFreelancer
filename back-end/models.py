import sqlite3
import os
from flask import g

DB_PATH = os.path.join(os.path.dirname(__file__), "database", "database.db")

def get_connection():
    """Retorna a conexão ativa com o banco, usando g para reusar por request."""
    db = getattr(g, "_database", None)
    if db is None:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        db = g._database = sqlite3.connect(DB_PATH)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    """Cria a tabela produtos se não existir"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco REAL NOT NULL
            )
        """)
        db.commit()


