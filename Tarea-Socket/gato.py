import socket
import threading
import sys
import pickle

class Node:
    def __init__(self, data, pos):
        self.pos = pos
        self.data = data
        self.next_node = None
        self.prev_node = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insertt(self, element,pos):
        if self.empty():
            self.head = Node(element,pos)
            self.tail = self.head
        else:
            aux=self.head
            count=0
            while aux:
                if aux.pos==pos:
                    print("no se puede agregar")
                    count+=1
                    break
                else:
                    aux=aux.next_node
            if count==0:
                node  = Node(element,pos)
                self.tail.next_node = node
                node.prev_node = self.tail
                self.tail = node

    def getjugada(self,pos):
        aux= self.head
        while aux:
            if aux.pos==pos:
                return aux.data
            else:
                aux=aux.next_node

    def vaciar(self):
        self.head=None
        self.tail=None



class Servidor():
    """docstring for Servidor"""
    def __init__(self, host="172.16.32.111", port=4000):

        self.clientes = []

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)
        self.matriz = Lista()

        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)
        
        aceptar.daemon = True
        aceptar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            msg = input('->')
            if msg == 'salir':
                self.sock.close()
                sys.exit()
            else:
                pass

    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg.encode())
            except:
                self.clientes.remove(c)
    
    def msg_to_jugador(self, msg, cliente):
        for c in self.clientes:
            try:
                if c == cliente:
                    c.send(msg.encode())
            except:
                self.clientes.remove(c)

    def aceptarCon(self):
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass

    def procesarCon(self):
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data.decode()=="x1":
                            self.matriz.insertt("X",1)
                            self.evaluar(c)
                        elif data.decode()=="x2":
                            self.matriz.insertt("X",2)
                            self.evaluar(c)
                        elif data.decode()=="x3":
                            self.matriz.insertt("X",3)
                            self.evaluar(c)
                        elif data.decode()=="x4":
                            self.matriz.insertt("X",4)
                            self.evaluar(c)
                        elif data.decode()=="x5":
                            self.matriz.insertt("X",5)
                            self.evaluar(c)
                        elif data.decode()=="x6":
                            self.matriz.insertt("X",6)
                            self.evaluar(c)
                        elif data.decode()=="x7":
                            self.matriz.insertt("X",7)
                            self.evaluar(c)
                        elif data.decode()=="x8":
                            self.matriz.insertt("X",8)
                            self.evaluar(c)
                        elif data.decode()=="x9":
                            self.matriz.insertt("X",9)
                            self.evaluar(c)
                        elif data.decode()=="o1":
                            self.matriz.insertt("O",1)
                            self.evaluar(c)
                        elif data.decode()=="o2":
                            self.matriz.insertt("O",2)
                            self.evaluar(c)
                        elif data.decode()=="o3":
                            self.matriz.insertt("O",3)
                            self.evaluar(c)
                        elif data.decode()=="o4":
                            self.matriz.insertt("O",4)
                            self.evaluar(c)
                        elif data.decode()=="o5":
                            self.matriz.insertt("O",5)
                            self.evaluar(c)
                        elif data.decode()=="o6":
                            self.matriz.insertt("O",6)
                            self.evaluar(c)
                        elif data.decode()=="o7":
                            self.matriz.insertt("O",7)
                            self.evaluar(c)
                        elif data.decode()=="o8":
                            self.matriz.insertt("O",8)
                            self.evaluar(c)
                        elif data.decode()=="o9":
                            self.matriz.insertt("O",9)
                            self.evaluar(c) 
                        elif data!=None and data.decode() != "x1" and data.decode() !=  "x2" and data.decode() != "x3" and data.decode() != "x4" and data.decode() !=  "x5" and data.decode() != "x6" and data.decode() != "x7" and data.decode() != "x8" and data.decode() != "x9" and data.decode() != "o1" and data.decode() !=  "o2" and data.decode() != "o3" and data.decode() != "o4" and data.decode() !=  "o5" and data.decode() != "o6" and data.decode() != "o7" and data.decode() != "o8" and data.decode() != "o9":
                            rr=data.decode()
                            jj=str(rr)
                            self.msg_to_all(jj,c)
                    except:
                        pass

    def evaluar(self,c):
        xx1=self.matriz.getjugada(1)
        xx2=self.matriz.getjugada(2)
        xx3=self.matriz.getjugada(3)
        xx4=self.matriz.getjugada(4)
        xx5=self.matriz.getjugada(5)
        xx6=self.matriz.getjugada(6)
        xx7=self.matriz.getjugada(7)
        xx8=self.matriz.getjugada(8)
        xx9=self.matriz.getjugada(9)
        if xx1!= None and xx2 != None and xx3 != None and xx1==xx2==xx3 or xx4!= None and xx5 != None and xx6 != None and xx4==xx5==xx6 or xx7!= None and xx8 != None and xx9 != None and xx7==xx8==xx9 or xx1!= None and xx4 != None and xx7 != None and xx1==xx4==xx7 or xx2!= None and xx5 != None and xx8 != None and xx2==xx5==xx8 or xx3!= None and xx6 != None and xx9 != None and xx3==xx6==xx9 or xx7!= None and xx5 != None and xx3 != None and xx7==xx5==xx3 or xx1!= None and xx5 != None and xx9 != None and xx1==xx5==xx9:
            print("Alguien a Ganado Felicitaciones")
            self.mostrar(c)
            self.msg_to_all("Has Perdido! Vuelve a intentarlo",c)
            self.msg_to_jugador("Felicitaciones has Ganado",c)
            #ahora tengo que reiniciar el juego
            self.matriz.vaciar()

        elif xx1 != None and xx2 != None and xx3 != None and xx4 != None and xx5 != None and xx6 != None and xx7 != None and xx8 != None and xx9 != None:
            empate= str("Empate, vuelve a intentarlo")
            print("Se a Empatado, lo intentaremos de nuevo")
            self.mostrar(c)
            self.msg_to_all(empate,c)
            self.msg_to_jugador(empate,c)
            #ahora tengo que reiniciar el juego
            self.matriz.vaciar()
        else:
            #como no pasa nada solo paso
            print("Se ingreso una jugada :D")
            self.mostrar(c)
    
    def mostrar(self,c):
        oo1=self.matriz.getjugada(1)
        oo2=self.matriz.getjugada(2)
        oo3=self.matriz.getjugada(3)
        oo4=self.matriz.getjugada(4)
        oo5=self.matriz.getjugada(5)
        oo6=self.matriz.getjugada(6)
        oo7=self.matriz.getjugada(7)
        oo8=self.matriz.getjugada(8)
        oo9=self.matriz.getjugada(9)
        print("oo1 vale {}".format(oo1))
        print("oo2 vale {}".format(oo2))
        print("oo3 vale {}".format(oo3))
        print("oo4 vale {}".format(oo4))
        print("oo5 vale {}".format(oo5))
        print("oo6 vale {}".format(oo6))
        print("oo7 vale {}".format(oo7))
        print("oo8 vale {}".format(oo8))
        print("oo9 vale {}".format(oo9))
        y=str(" \n {}|{}|{}".format(oo1,oo2,oo3))
        x=str(" {}|{}|{}".format(oo4,oo5,oo6))
        w=str(" {}|{}|{}".format(oo7,oo8,oo9))
        self.msg_to_all(w,c)
        self.msg_to_all(x,c)
        self.msg_to_all(y,c)

s = Servidor()