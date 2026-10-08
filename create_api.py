from flask import Flask, request, jsonify

app = Flask(__name__) #essa função cria uma instância da classe Flask
                      #que é a aplicação web em si
                      #o parâmetro __name__ é usado para determinar o caminho do arquivo principal da aplicação.

livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
    },
    {
        "id": 2,
        "titulo": "1984",
        "autor": "George Orwell",
    },
    {
        "id": 3,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
    },
    {
        "id": 4,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling",
    }
]

#consultar(todos)
@app.route("/livros", methods=["GET"])
def cosultar():
    return jsonify(livros)

#consultar(id)
@app.route("/livros/<int:id>", methods=["GET"]) #<int:id> é um parâmetro de rota,
                                                #ele é usado para capturar o valor do id que vem na URL
def consultar_id(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)
    return jsonify({"mensagem": "Livro não encontrado"}), 404


#editar
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro(id):
    data = request.get_json() #get_json() é um método do objeto request que retorna os dados da requisição em formato JSON
    for livro in livros:
        if livro["id"] == id:
            livro.update(data)
            return jsonify(livro)
    return jsonify({"mensagem": "Livro não encontrado"}), 404

#criar
@app.route("/livros", methods=["POST"])
def criar_livro():
    novo = request.get_json()
    livros.append(novo)
    return jsonify(novo)

#excluir
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro excluído com sucesso"})

app.run(port=5000, host="localhost", debug=True)