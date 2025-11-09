from flask import Flask, render_template, g
from models import init_db, get_connection
from controllers.produtos_controller import produtos_bp
import os

# Configura Flask com front-end e estáticos
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../front-end'),
    static_folder=os.path.join(os.path.dirname(__file__), '../front-end')
)

# Inicializa banco de dados
init_db()

# Registra blueprint da API de produtos
app.register_blueprint(produtos_bp, url_prefix="/produtos")

# Fecha conexão ao terminar request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# Rotas front-end
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/editar/<int:id>')
def editar(id):
    return render_template('editar.html', id=id)

# Roda servidor local
if __name__ == "__main__":
    print("Servidor rodando em http://127.0.0.1:5000/")
    app.run(host="127.0.0.1", port=5000, debug=True)


