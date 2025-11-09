##💼 Catálogo de Produtos para Freelancers

Projeto web full-stack para cadastro, listagem e gerenciamento de freelancers e serviços. O sistema permite que freelancers cadastrem seus serviços e usuários possam visualizar, editar e excluir registros.  

---

## 🛠 Tecnologias Utilizadas

- **Front-end:** HTML, CSS, JavaScript  
- **Back-end:** Python (Flask)  
- **Banco de Dados:** SQLite  
- **Arquitetura:** MVC (Model-View-Controller)  
- **Controle de Versão:** Git / GitHub  

---

## ⚙ Funcionalidades

- 📝 **Cadastro de Freelancers e Serviços** (Create)  
- 📋 **Listagem de Freelancers e Serviços** (Read)  
- ✏️ **Edição de Dados** (Update)  
- 🗑 **Exclusão de Registros** (Delete)  
- 🔍 Pesquisa de serviços e freelancers  
- 💻 Protótipo e fluxos de telas  

---

## 📁 Estrutura do Projeto

catalogo de produtos freelancer/
├── back-end/ # Código do servidor (Flask)
│ ├── app.py
│ ├── models.py
│ ├── controllers/
│ └── database/ # Banco SQLite
├── front-end/ # HTML, CSS, JS
├── documentação/ # Plano, testes, feedback
├── modelagem/ # Diagramas UML
├── protótipo/ # Protótipos de telas
├── venv/ # Ambiente virtual Python
└── .gitignore

## 🚀 Como Rodar o Projeto
Clone o repositório:
git clone https://github.com/SEU_USUARIO/NOME_REPO.git

Entre na pasta do projeto:
cd "Catalogo de Produtos Freelancer/back-end"

Ative o ambiente virtual:
source venv/bin/activate

Instale as dependências (se necessário):
pip install -r requirements.txt

Execute o Flask:
python3 app.py

Acesse no navegador:
http://127.0.0.1:5000

📄 Documentação
Plano de projeto: documentação/plano_de_projeto.docx
Dicionário de dados: documentação/dicionario_de_dados.docx
Testes e validação: documentação/testes.md
Feedbacks dos usuários: documentação/feedback.md

👩‍💻 Autor
Bruna Siquiera Lopes
Email: bwoodymila@gmail.com

⭐ Observações
O projeto segue o padrão MVC para organizar o back-end.
O banco de dados SQLite é criado automaticamente ao rodar o Flask.
A pasta venv/ e o banco app.db estão no .gitignore para manter o repositório limpo.
