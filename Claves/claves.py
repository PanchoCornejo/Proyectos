class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data

class lista:
    def __init__(self,codigo):
        self.head=None
        self.last=None
        self.codigo=codigo
        for i in codigo:
            if self.head == None:
                nodex= Node(i)
                self.head= nodex
                self.last= nodex
                nodex.prev=None
                nodex.next=None
            else:
                nodex= Node(i)
                self.last.next=nodex
                nodex.prev=self.last
                self.last=nodex

    def push(self, data):
        print("entro un push")
        if self.head == None:
            print("no habia nadie mas")
            nodex= Node(data)
            self.head= nodex
            self.last= nodex
            nodex.prev=None
            nodex.next=None
        else:
            print("buscare un espacio para mi")
            aux= self.head
            intento=1
            while aux!= None:
                print("intento:{}".format(intento))
                if aux.next == None:
                    nodex= Node(data)
                    aux.next= nodex
                    nodex.prev= aux
                    self.last= nodex
                    nodex.next=None
                    aux=aux.next
                    intento= intento+1
                else:
                    aux = aux.next
                    intento= intento+1
    
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
                print("esto es text: {}".format(text))
                aux= aux.next
            return text
        else:
            print("no hay nada en la lista")
            return None
    
    def mostrar(self):
        if self.head != None:
            aux = self.head
            while aux:
                print(str(aux.data))
                aux=aux.next
        else:
            print("no hay elementos")
    
    def mostrartext(self):
        if self.head != None:
            text=self.head.data
            aux=self.head.next
            while aux:
                text= text+aux.data
                aux= aux.next
            print("Codigo:{}".format(text))
        else:
            print("no hay nada en la lista")
            return None

        
    def cenitpolar(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "c":
                    aux.data= "p"
                elif aux.data == "e":
                    aux.data= "o"
                elif aux.data == "n":
                    aux.data= "l"
                elif aux.data == "i":
                    aux.data= "a"
                elif aux.data == "t":
                    aux.data= "r"
                elif aux.data == "p":
                    aux.data= "c"
                elif aux.data == "o":
                    aux.data= "e"
                elif aux.data == "l":
                    aux.data= "n"
                elif aux.data == "a":
                    aux.data= "i"
                elif aux.data == "r":
                    aux.data= "t"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def ratonfeliz(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "r":
                    aux.data= "f"
                elif aux.data == "a":
                    aux.data= "e"
                elif aux.data == "t":
                    aux.data= "l"
                elif aux.data == "o":
                    aux.data= "i"
                elif aux.data == "n":
                    aux.data= "z"
                elif aux.data == "f":
                    aux.data= "r"
                elif aux.data == "e":
                    aux.data= "a"
                elif aux.data == "l":
                    aux.data= "t"
                elif aux.data == "i":
                    aux.data= "o"
                elif aux.data == "z":
                    aux.data= "n"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def BP(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "b":
                    aux.data= "p"
                elif aux.data == "a":
                    aux.data= "o"
                elif aux.data == "d":
                    aux.data= "w"
                elif aux.data == "e":
                    aux.data= "e"
                elif aux.data == "n":
                    aux.data= "l"
                elif aux.data == "p":
                    aux.data= "b"
                elif aux.data == "o":
                    aux.data= "a"
                elif aux.data == "w":
                    aux.data= "d"
                elif aux.data == "e":
                    aux.data= "e"
                elif aux.data == "l":
                    aux.data= "n"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def AEIOU(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "a":
                    aux.data= "1"
                elif aux.data == "e":
                    aux.data= "2"
                elif aux.data == "i":
                    aux.data= "3"
                elif aux.data == "o":
                    aux.data= "4"
                elif aux.data == "u":
                    aux.data= "5"
                elif aux.data == "1":
                    aux.data= "a"
                elif aux.data == "2":
                    aux.data= "e"
                elif aux.data == "3":
                    aux.data= "i"
                elif aux.data == "4":
                    aux.data= "o"
                elif aux.data == "5":
                    aux.data= "u"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def Lapiznegro(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "l":
                    aux.data= "n"
                elif aux.data == "a":
                    aux.data= "e"
                elif aux.data == "p":
                    aux.data= "g"
                elif aux.data == "i":
                    aux.data= "r"
                elif aux.data == "z":
                    aux.data= "o"
                elif aux.data == "n":
                    aux.data= "l"
                elif aux.data == "e":
                    aux.data= "a"
                elif aux.data == "g":
                    aux.data= "p"
                elif aux.data == "r":
                    aux.data= "i"
                elif aux.data == "o":
                    aux.data= "z"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def JulioCesar(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "j":
                    aux.data= "c"
                elif aux.data == "u":
                    aux.data= "e"
                elif aux.data == "l":
                    aux.data= "s"
                elif aux.data == "i":
                    aux.data= "a"
                elif aux.data == "o":
                    aux.data= "r"
                elif aux.data == "c":
                    aux.data= "j"
                elif aux.data == "e":
                    aux.data= "u"
                elif aux.data == "s":
                    aux.data= "l"
                elif aux.data == "a":
                    aux.data= "i"
                elif aux.data == "r":
                    aux.data= "o"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def Orquidea(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "o":
                    aux.data= "1"
                elif aux.data == "r":
                    aux.data= "2"
                elif aux.data == "q":
                    aux.data= "3"
                elif aux.data == "u":
                    aux.data= "4"
                elif aux.data == "i":
                    aux.data= "5"
                elif aux.data == "d":
                    aux.data= "6"
                elif aux.data == "e":
                    aux.data= "7"
                elif aux.data == "a":
                    aux.data= "8"
                elif aux.data == "1":
                    aux.data= "o"
                elif aux.data == "2":
                    aux.data= "r"
                elif aux.data == "3":
                    aux.data= "q"
                elif aux.data == "4":
                    aux.data= "u"
                elif aux.data == "5":
                    aux.data= "i"
                elif aux.data == "6":
                    aux.data= "d"
                elif aux.data == "7":
                    aux.data= "e"
                elif aux.data == "8":
                    aux.data= "a"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def agujerito(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "a":
                    aux.data= "1"
                elif aux.data == "g":
                    aux.data= "2"
                elif aux.data == "u":
                    aux.data= "3"
                elif aux.data == "j":
                    aux.data= "4"
                elif aux.data == "e":
                    aux.data= "5"
                elif aux.data == "r":
                    aux.data= "6"
                elif aux.data == "i":
                    aux.data= "7"
                elif aux.data == "t":
                    aux.data= "8"
                elif aux.data == "o":
                    aux.data= "9"
                elif aux.data == "1":
                    aux.data= "a"
                elif aux.data == "2":
                    aux.data= "g"
                elif aux.data == "3":
                    aux.data= "u"
                elif aux.data == "4":
                    aux.data= "j"
                elif aux.data == "5":
                    aux.data= "e"
                elif aux.data == "6":
                    aux.data= "r"
                elif aux.data == "7":
                    aux.data= "i"
                elif aux.data == "8":
                    aux.data= "t"
                elif aux.data == "9":
                    aux.data= "o"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def murcielago(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "m":
                    aux.data= "0"
                elif aux.data == "u":
                    aux.data= "1"
                elif aux.data == "r":
                    aux.data= "2"
                elif aux.data == "c":
                    aux.data= "3"
                elif aux.data == "i":
                    aux.data= "4"
                elif aux.data == "e":
                    aux.data= "5"
                elif aux.data == "l":
                    aux.data= "6"
                elif aux.data == "a":
                    aux.data= "7"
                elif aux.data == "g":
                    aux.data= "8"
                elif aux.data == "o":
                    aux.data= "9"
                elif aux.data == "0":
                    aux.data= "m"
                elif aux.data == "1":
                    aux.data= "u"
                elif aux.data == "2":
                    aux.data= "r"
                elif aux.data == "3":
                    aux.data= "c"
                elif aux.data == "4":
                    aux.data= "i"
                elif aux.data == "5":
                    aux.data= "e"
                elif aux.data == "6":
                    aux.data= "l"
                elif aux.data == "7":
                    aux.data= "a"
                elif aux.data == "8":
                    aux.data= "g"
                elif aux.data == "9":
                    aux.data= "o"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def sufamelico(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "s":
                    aux.data= "u"
                elif aux.data == "u":
                    aux.data= "s"
                elif aux.data == "f":
                    aux.data= "a"
                elif aux.data == "a":
                    aux.data= "f"
                elif aux.data == "m":
                    aux.data= "e"
                elif aux.data == "e":
                    aux.data= "m"
                elif aux.data == "l":
                    aux.data= "i"
                elif aux.data == "i":
                    aux.data= "l"
                elif aux.data == "c":
                    aux.data= "o"
                elif aux.data == "o":
                    aux.data= "c"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")
    
    def dametupico(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "d":
                    aux.data= "a"
                elif aux.data == "a":
                    aux.data= "d"
                elif aux.data == "m":
                    aux.data= "e"
                elif aux.data == "e":
                    aux.data= "m"
                elif aux.data == "t":
                    aux.data= "u"
                elif aux.data == "u":
                    aux.data= "t"
                elif aux.data == "p":
                    aux.data= "i"
                elif aux.data == "i":
                    aux.data= "p"
                elif aux.data == "c":
                    aux.data= "o"
                elif aux.data == "o":
                    aux.data= "c"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def parelinofu(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "p":
                    aux.data= "a"
                elif aux.data == "a":
                    aux.data= "p"
                elif aux.data == "r":
                    aux.data= "e"
                elif aux.data == "e":
                    aux.data= "r"
                elif aux.data == "l":
                    aux.data= "i"
                elif aux.data == "i":
                    aux.data= "l"
                elif aux.data == "n":
                    aux.data= "o"
                elif aux.data == "o":
                    aux.data= "n"
                elif aux.data == "f":
                    aux.data= "u"
                elif aux.data == "u":
                    aux.data= "f"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def Inversa(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "a":
                    aux.data= "z"
                elif aux.data == "b":
                    aux.data= "y"
                elif aux.data == "c":
                    aux.data= "x"
                elif aux.data == "d":
                    aux.data= "w"
                elif aux.data == "e":
                    aux.data= "v"
                elif aux.data == "f":
                    aux.data= "u"
                elif aux.data == "g":
                    aux.data= "t"
                elif aux.data == "h":
                    aux.data= "s"
                elif aux.data == "i":
                    aux.data= "r"
                elif aux.data == "j":
                    aux.data= "k"
                elif aux.data == "k":
                    aux.data= "p"
                elif aux.data == "l":
                    aux.data= "o"
                elif aux.data == "m":
                    aux.data= "ñ"
                elif aux.data == "n":
                    aux.data= "n"
                elif aux.data == "ñ":
                    aux.data= "m"
                elif aux.data == "o":
                    aux.data= "l"
                elif aux.data == "p":
                    aux.data= "k"
                elif aux.data == "q":
                    aux.data= "j"
                elif aux.data == "r":
                    aux.data= "i"
                elif aux.data == "s":
                    aux.data= "h"
                elif aux.data == "t":
                    aux.data= "g"
                elif aux.data == "u":
                    aux.data= "f"
                elif aux.data == "v":
                    aux.data= "e"
                elif aux.data == "w":
                    aux.data= "d"
                elif aux.data == "x":
                    aux.data= "c"
                elif aux.data == "y":
                    aux.data= "b"
                elif aux.data == "z":
                    aux.data= "a"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def Media(self):
        if self.head != None:
            aux= self.head
            while aux:
                if aux.data == "a":
                    aux.data= "n"
                elif aux.data == "b":
                    aux.data= "o"
                elif aux.data == "c":
                    aux.data= "p"
                elif aux.data == "d":
                    aux.data= "q"
                elif aux.data == "e":
                    aux.data= "r"
                elif aux.data == "f":
                    aux.data= "s"
                elif aux.data == "g":
                    aux.data= "t"
                elif aux.data == "h":
                    aux.data= "u"
                elif aux.data == "i":
                    aux.data= "v"
                elif aux.data == "j":
                    aux.data= "w"
                elif aux.data == "k":
                    aux.data= "x"
                elif aux.data == "l":
                    aux.data= "y"
                elif aux.data == "m":
                    aux.data= "z"
                elif aux.data == "n":
                    aux.data= "a"
                elif aux.data == "o":
                    aux.data= "b"
                elif aux.data == "p":
                    aux.data= "c"
                elif aux.data == "q":
                    aux.data= "d"
                elif aux.data == "r":
                    aux.data= "e"
                elif aux.data == "s":
                    aux.data= "f"
                elif aux.data == "t":
                    aux.data= "g"
                elif aux.data == "u":
                    aux.data= "h"
                elif aux.data == "v":
                    aux.data= "i"
                elif aux.data == "w":
                    aux.data= "j"
                elif aux.data == "x":
                    aux.data= "k"
                elif aux.data == "y":
                    aux.data= "l"
                elif aux.data == "z":
                    aux.data= "m"
                else:
                    pass
                aux=aux.next
        else:
            print("no hay codigo")

    def corredora(self,orden):
        if self.head != None:
            aux=self.head
            while aux:
                if aux.data=="a":
                    aux.data=1+orden
                elif aux.data=="b":
                    aux.data=2+orden
                elif aux.data=="c":
                    aux.data=3+orden
                elif aux.data=="d":
                    aux.data=4+orden
                elif aux.data=="e":
                    aux.data=5+orden
                elif aux.data=="f":
                    aux.data=6+orden
                elif aux.data=="g":
                    aux.data=7+orden
                elif aux.data=="h":
                    aux.data=8+orden
                elif aux.data=="i":
                    aux.data=9+orden
                elif aux.data=="j":
                    aux.data=10+orden
                elif aux.data=="k":
                    aux.data=11+orden
                elif aux.data=="l":
                    aux.data=12+orden
                elif aux.data=="m":
                    aux.data=13+orden
                elif aux.data=="n":
                    aux.data=14+orden
                elif aux.data=="ñ":
                    aux.data=15+orden
                elif aux.data=="o":
                    aux.data=16+orden
                elif aux.data=="p":
                    aux.data=17+orden
                elif aux.data=="q":
                    aux.data=18+orden
                elif aux.data=="r":
                    aux.data=19+orden
                elif aux.data=="s":
                    aux.data=20+orden
                elif aux.data=="t":
                    aux.data=21+orden
                elif aux.data=="u":
                    aux.data=22+orden
                elif aux.data=="v":
                    aux.data=23+orden
                elif aux.data=="w":
                    aux.data=24+orden
                elif aux.data=="x":
                    aux.data=25+orden
                elif aux.data=="y":
                    aux.data=26+orden
                elif aux.data=="z":
                    aux.data=27+orden
                else:
                    pass
                aux=aux.next
            aux=self.head
            while aux:
                if aux.data==1:
                    aux.data="a"
                elif aux.data==2:
                    aux.data="b"
                elif aux.data==3:
                    aux.data="c"
                elif aux.data==2:
                    aux.data="b"
                elif aux.data==3:
                    aux.data="c"
                elif aux.data==4:
                    aux.data="b"
                elif aux.data==5:
                    aux.data="c"
                elif aux.data==6:
                    aux.data="b"
                elif aux.data==7:
                    aux.data="c"
                elif aux.data==8:
                    aux.data="b"
                elif aux.data==9:
                    aux.data="c"
                elif aux.data==10:
                    aux.data="b"
                elif aux.data==11:
                    aux.data="c"
                elif aux.data==12:
                    aux.data="b"
                elif aux.data==13:
                    aux.data="c"
                elif aux.data==14:
                    aux.data="b"
                elif aux.data==15:
                    aux.data="c"
                elif aux.data==16:
                    aux.data="b"
                elif aux.data==17:
                    aux.data="c"
                elif aux.data==18:
                    aux.data="b"
                elif aux.data==19:
                    aux.data="c"
                elif aux.data==20:
                    aux.data="b"
                elif aux.data==21:
                    aux.data="c"
                elif aux.data==22:
                    aux.data="b"
                elif aux.data==23:
                    aux.data="c"
                elif aux.data==24:
                    aux.data="b"
                elif aux.data==25:
                    aux.data="c"
                elif aux.data==26:
                    aux.data="b"
                elif aux.data==27:
                    aux.data="c"
                elif aux.data==28:
                    aux.data="b"
                elif aux.data==29:
                    aux.data="c"
                elif aux.data==30:
                    aux.data="b"
                elif aux.data==31:
                    aux.data="c"
                elif aux.data==32:
                    aux.data="b"
                elif aux.data==33:
                    aux.data="c"
                elif aux.data==34:
                    aux.data="b"
                elif aux.data==35:
                    aux.data="c"
                elif aux.data==36:
                    aux.data="b"
                elif aux.data==37:
                    aux.data="c"
                elif aux.data==38:
                    aux.data="b"
                elif aux.data==39:
                    aux.data="c"
                elif aux.data==40:
                    aux.data="b"
                elif aux.data==41:
                    aux.data="c"
                elif aux.data==42:
                    aux.data="b"
                elif aux.data==43:
                    aux.data="c"
                elif aux.data==44:
                    aux.data="b"
                elif aux.data==45:
                    aux.data="c"
                elif aux.data==46:
                    aux.data="b"
                elif aux.data==47:
                    aux.data="c"
                elif aux.data==48:
                    aux.data="b"
                elif aux.data==49:
                    aux.data="c"
                elif aux.data==50:
                    aux.data="b"
                elif aux.data==51:
                    aux.data="c"
                elif aux.data==52:
                    aux.data="b"
                elif aux.data==53:
                    aux.data="c"
                elif aux.data==54:
                    aux.data="b"
                else:
                    pass
        else:
            print("no hay codigo")
    
    def Grafico(self): #arrevez
        if self.head != None:
            aux=self.head
            while aux:
                if aux.data=="A1" or aux.data=="a1":
                    aux.data="a"
                elif aux.data=="A2" or aux.data=="a2":
                    aux.data="b"
                elif aux.data=="A3" or aux.data=="a3":
                    aux.data="c"
                elif aux.data=="A4" or aux.data=="a4":
                    aux.data="d"
                elif aux.data=="A5" or aux.data=="a5":
                    aux.data="e"
                elif aux.data=="A6" or aux.data=="a6":
                    aux.data="f"
                elif aux.data=="A7" or aux.data=="a7":
                    aux.data="g"
                elif aux.data=="A8" or aux.data=="a8":
                    aux.data="h"
                elif aux.data=="A9" or aux.data=="a9":
                    aux.data="i"
                elif aux.data=="B1" or aux.data=="b1":
                    aux.data="j"
                elif aux.data=="B2" or aux.data=="b2":
                    aux.data="k"
                elif aux.data=="B3" or aux.data=="b3":
                    aux.data="l"
                elif aux.data=="B4" or aux.data=="b4":
                    aux.data="m"
                elif aux.data=="B5" or aux.data=="b5":
                    aux.data="n"
                elif aux.data=="B6" or aux.data=="b6":
                    aux.data="ñ"
                elif aux.data=="B7" or aux.data=="b7":
                    aux.data="o"
                elif aux.data=="B8" or aux.data=="b8":
                    aux.data="p"
                elif aux.data=="B9" or aux.data=="b9":
                    aux.data="q"
                elif aux.data=="C1" or aux.data=="c1":
                    aux.data="r"
                elif aux.data=="C2" or aux.data=="c2":
                    aux.data="s"
                elif aux.data=="C3" or aux.data=="c3":
                    aux.data="t"
                elif aux.data=="C4" or aux.data=="c4":
                    aux.data="u"
                elif aux.data=="C5" or aux.data=="c5":
                    aux.data="v"
                elif aux.data=="C6" or aux.data=="c6":
                    aux.data="w"
                elif aux.data=="C7" or aux.data=="c7":
                    aux.data="x"
                elif aux.data=="C8" or aux.data=="c8":
                    aux.data="y"
                elif aux.data=="C9" or aux.data=="c9":
                    aux.data="z"
                # falta el caso si es alrrevez
                else:
                    pass
        else:
            print("no hay codigo")
    
    def Morse(self): #hay que mirar los espacios
        if self.head != None:
            aux=self.head
            while aux:
                if aux.data == "a":
                    aux.data= ".-"
                elif aux.data == "b":
                    aux.data= "-.."
                elif aux.data == "c":
                    aux.data= "-.-."
                elif aux.data == "d":
                    aux.data= "-.."
                elif aux.data == "e":
                    aux.data= "."
                elif aux.data == "f":
                    aux.data= "..-."
                elif aux.data == "g":
                    aux.data= "--."
                elif aux.data == "h":
                    aux.data= "...."
                elif aux.data == "i":
                    aux.data= ".."
                elif aux.data == "j":
                    aux.data= ".---"
                elif aux.data == "k":
                    aux.data= "-.-"
                elif aux.data == "l":
                    aux.data= ".-.."
                elif aux.data == "m":
                    aux.data= "--"
                elif aux.data == "n":
                    aux.data= "-."
                elif aux.data == "ñ":
                    aux.data= ""
                elif aux.data == "o":
                    aux.data= "---"
                elif aux.data == "p":
                    aux.data= ".--."
                elif aux.data == "q":
                    aux.data= "--.-"
                elif aux.data == "r":
                    aux.data= ".-."
                elif aux.data == "s":
                    aux.data= "..."
                elif aux.data == "t":
                    aux.data= "-"
                elif aux.data == "u":
                    aux.data= "..-"
                elif aux.data == "v":
                    aux.data= "...-"
                elif aux.data == "w":
                    aux.data= ".--"
                elif aux.data == "x":
                    aux.data= "-..-"
                elif aux.data == "y":
                    aux.data= "-.--"
                elif aux.data == "z":
                    aux.data= "--.."
                elif aux.data == "1":
                    aux.data= ".----"
                elif aux.data == "2":
                    aux.data= "..---"
                elif aux.data == "3":
                    aux.data= "...--"
                elif aux.data == "4":
                    aux.data= "....-"
                elif aux.data == "5":
                    aux.data= "....."
                elif aux.data == "6":
                    aux.data= "-...."
                elif aux.data == "7":
                    aux.data= "--..."
                elif aux.data == "8":
                    aux.data= "---.."
                elif aux.data == "9":
                    aux.data= "----."
                elif aux.data == "0":
                    aux.data= "-----"
                elif aux.data == ".-":
                    aux.data= "a"
                elif aux.data == "-..":
                    aux.data= "b"
                elif aux.data == "-.-.":
                    aux.data= "c"
                elif aux.data == "-..":
                    aux.data= "d"
                elif aux.data == ".":
                    aux.data= "e"
                elif aux.data == "..-.":
                    aux.data= "f"
                elif aux.data == "--.":
                    aux.data= "g"
                elif aux.data == "....":
                    aux.data= "h"
                elif aux.data == "..":
                    aux.data= "i"
                elif aux.data == ".---":
                    aux.data= "j"
                elif aux.data == "-.-":
                    aux.data= "k"
                elif aux.data == ".-..":
                    aux.data= "l"
                elif aux.data == "--":
                    aux.data= "m"
                elif aux.data == "-.":
                    aux.data= "n"
                elif aux.data == "":
                    aux.data= ""
                elif aux.data == "---":
                    aux.data= "o"
                elif aux.data == ".--.":
                    aux.data= "p"
                elif aux.data == "--.-":
                    aux.data= "q"
                elif aux.data == ".-.":
                    aux.data= "r"
                elif aux.data == "...":
                    aux.data= "s"
                elif aux.data == "-":
                    aux.data= "t"
                elif aux.data == "..-":
                    aux.data= "u"
                elif aux.data == "...-":
                    aux.data= "v"
                elif aux.data == ".--":
                    aux.data= "w"
                elif aux.data == "-..-":
                    aux.data= "x"
                elif aux.data == "-.--":
                    aux.data= "y"
                elif aux.data == "--..":
                    aux.data= "z"
                elif aux.data == ".----":
                    aux.data= "1"
                elif aux.data == "..---":
                    aux.data= "2"
                elif aux.data == "...--":
                    aux.data= "3"
                elif aux.data == "....-":
                    aux.data= "4"
                elif aux.data == ".....":
                    aux.data= "5"
                elif aux.data == "-....":
                    aux.data= "6"
                elif aux.data == "--...":
                    aux.data= "7"
                elif aux.data == "---..":
                    aux.data= "8"
                elif aux.data == "----.":
                    aux.data= "9"
                elif aux.data == "-----":
                    aux.data= "0"
        else:
            print("no hay codigo")



    
            
            

## Main             

        

clave= lista("pancho")
clave.corredora(2)
clave.mostrartext()




