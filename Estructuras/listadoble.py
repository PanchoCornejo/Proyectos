class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insert_last(self, element):
        if self.empty():
            self.head = Node(element)
            self.tail = self.head
        else:
            node  = Node(element)
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node

    def insert_first(self, element):
        if self.empty():
            self.head = Node(element)
            self.tail = self.head
        else:
            node = Node(element)
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node

    def print_list(self):
        if self.empty():
             print("Lista vacia")
        else:
            self.bubbleSort()
            temp = self.head
            i = 1
            while True:
                print("Nodo {} contiene el número {}".format(i, temp.data))
                temp = temp.next_node
                i += 1
                if temp == None:
                    break

    def _find(self,valor):
        aux= self.head
        while True:
            if aux.data==valor:
                return aux
            elif aux.next_node== None:
                return None
            aux= aux.next_node

    def delete(self,node):
        valorr=node.data
        nodito=self._find(valorr)
        if nodito==None:
            print("No existe")
        else:
            t=nodito.prev_node
            x=nodito.next_node
            t.next_node=x
            x.prev_node=t
            print("fue borrado")

    def _delete(self,valuee):
        noditox=self._find(valuee)
        if noditox==None:
            print("No existe")
        else:
            o=noditox.prev_node
            l=noditox.next_node
            o.next_node=l
            l.prev_node=o
            print("fue borrado") 

    def bubbleSort(self):
        if self.empty():
            print("Esta Vacia")
        first=self.head
        second=self.head.next_node
        while True:
            if second==None:
                break
            
            elif first.data>second.data:
                q=first.prev_node
                first.prev_node=second
                first.next_node=second.next_node
                second.next_node=first
                second.prev_node=q

                first=first.next_node
                second=second.next_node
            else:
                first=first.next_node
                second=second.next_node

lista = ListaDoblementeEnlazada()
lista.insert_last(4)
lista.insert_last(2)
lista.insert_last(6)
lista.insert_first(1)
lista.print_list()
print(lista.head.data)
print(lista.tail.data)

        

