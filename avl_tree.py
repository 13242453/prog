# -----------------------------
# AVL Tree en Python
# -----------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    # Obtener altura
    def get_height(self, node):
        return node.height if node else 0

    # Obtener factor de balance
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Actualizar altura
    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left),
                                   self.get_height(node.right))

    # Rotaciones
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    # Insertar nodo
    def insert(self, node, value):
        if not node:
            self.nodeCount += 1
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node  # duplicado, no se inserta

        self.update_height(node)
        balance = self.get_balance(node)

        # Casos de rotación
        if balance > 1 and value < node.left.value:  # Izq-Izq
            return self.rotate_right(node)
        if balance < -1 and value > node.right.value:  # Der-Der
            return self.rotate_left(node)
        if balance > 1 and value > node.left.value:  # Izq-Der
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and value < node.right.value:  # Der-Izq
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Encontrar el valor máximo (para eliminar)
    def max_value_node(self, node):
        current = node
        while current.right:
            current = current.right
        return current

    # Eliminar nodo
    def delete(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            # Nodo encontrado
            if not node.left:
                self.nodeCount -= 1
                return node.right
            elif not node.right:
                self.nodeCount -= 1
                return node.left

            temp = self.max_value_node(node.left)
            node.value = temp.value
            node.left = self.delete(node.left, temp.value)

        if not node:
            return node

        self.update_height(node)
        balance = self.get_balance(node)

        # Rebalancear
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # Recorrido en orden
    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)
