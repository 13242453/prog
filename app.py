from flask import Flask, render_template, request, jsonify
from avl_tree import AVLTree

app = Flask(__name__)
tree = AVLTree()

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Insertar nodo
@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    value = int(data.get('value'))
    tree.root = tree.insert(tree.root, value)
    response = {
        "inorder": tree.inorder(tree.root),
        "count": tree.nodeCount,
        "height": tree.get_height(tree.root),
        "balanced": abs(tree.get_balance(tree.root)) <= 1
    }
    return jsonify(response)

# Eliminar nodo
@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    value = int(data.get('value'))
    tree.root = tree.delete(tree.root, value)
    response = {
        "inorder": tree.inorder(tree.root),
        "count": tree.nodeCount,
        "height": tree.get_height(tree.root),
        "balanced": abs(tree.get_balance(tree.root)) <= 1
    }
    return jsonify(response)

# Limpiar árbol
@app.route('/clear', methods=['POST'])
def clear():
    global tree
    tree = AVLTree()
    return jsonify({"status": "cleared"})

if __name__ == '__main__':
    app.run(debug=True)
