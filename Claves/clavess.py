class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data

class lista:
    def __init__(self):
        self.head=None
        self.last=None

    def put(self, data):
        if self.head != None:
            node= Node(data)
            self.head= node
            self.last= node
        else:
            aux= self.head
            while aux:
                if aux.next == None:
                    node= Node(data)
                    aux.next= node
                    node.prev= aux
                    self.last= node
                aux= aux.next
    
    def pop(self):
        if self.head != None:
            aux1=self.head
            aux= self.head.next
            self.head= aux
            aux.prev=None
            return aux1
        else:
            print("No hay codigo en la lista")
            return None

    def contraer(self):
        if self.head != None:
            text=self.head.data
            aux=self.head.next
            while aux:
                text= text+aux.data
                aux= aux.next
            return text
        else:
            print("no hay nada en la lista")
            return None
    
 


def cenitpolar(codigo):
    codigo.lower()
    if codigo != None:
        codigo.replace("c","P")
        codigo.replace("e","O")
        codigo.replace("n","L")
        codigo.replace("i","A")
        codigo.replace("t","R")
        codigo.replace("p","C")
        codigo.replace("o","E")
        codigo.replace("l","N")
        codigo.replace("a","I")
        codigo.replace("r","T")
        codigo.lower()
        print(codigo)
    else:
        print("Codigo invalido")

cenitpolar("hola")

s="hola"
s.replace("c","P",100)
s.replace("e","O",100)
s.replace("n","L",100)
s.replace("i","A",100)
s.replace("t","R",100)

s.lower()
print(s)
        