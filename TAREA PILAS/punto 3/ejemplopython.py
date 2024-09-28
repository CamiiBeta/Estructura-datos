#primera funcion stack sera una lita
class Stack:
    def __init__(self):
        self.stack = [] 

    #agregar un elemento
    def push(self, elemento):
        self.stack.append(elemento)
        print(f"el elemento {elemento} fue agregado a la pila")

    #elimina el ultimo elemento de la pila
    def pop(self):
        if self.isEmpty():
            print("error: pila vacia")
            return None
        else:
            return self.stack.pop()

    #muestra el primer elemetno de la pila
    def top(self):
        if self.isEmpty():
            print("error: pila vacia")
            return None
        else:
            return self.stack[-1]

    #para saber el tamaño de la pila
    def size(self):
        return len(self.stack)

    #para saber si la pila esta vacia o no
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

pila1 = Stack()
pila1.push(10)
pila1.push(20)
pila1.push(30)
pila1.top()
pila1.pop()
pila1.size()
pila1.isEmpty()
