class Nodo:
  def __init__(self,autor,titulo,ventas,nota,categoria,comentario):
    self.autor=autor
    self.titulo=titulo
    self.ventas=ventas
    self.nota=nota
    self.categoria=categoria
    self.comentario=comentario
    self.next=None
  def get_autor(self):
    return(self.autor)
  def get_titulo(self):
    return(self.titulo)
  def get_ventas(self):
    return(self.ventas)
  def get_nota(self):
    return(self.nota)
  def get_categoria(self):
    return(self.categoria)
  def get_comentario(self):
    return(self.comentario)
def str2num(key):
  return sum([ord(c) for c in key])
def hashstr(key,size):
  return str2num(key)%size
class Queue:
  def __init__(self):
    self.prim=None
    self.last=None
    self.cout=0
  def print_front(self):
    a=self.prim
    #print("tamaño",self.cout)
    print("--------------------------------------------------------")
    print("TITULO",a.get_titulo())
    print("autor:",a.get_autor(),"nota:",a.get_nota())
    print("ventas:",a.get_ventas(),"categoria:",a.get_categoria())
    print("comentario:",a.get_comentario())
    print("--------------------------------------------------------")
  def enqueue_pri_ventas(self,nodo):
    if(self.prim is None):
      self.prim=self.last=nodo
      self.cout=self.cout+1
      return
    if(self.last.next is None):
      if(nodo.get_ventas()==self.prim.get_ventas()):
        self.prim=self.last=nodo
        return
      if(nodo.get_ventas()>self.prim.get_ventas()):
        primero=self.prim
        self.last=primero
        primero.next=nodo
        self.prim=nodo
        self.cout=self.cout+1
        return
      else:
        nodo.next=self.prim
        self.last=nodo
        self.cout=self.cout+1
        return
    pos=self.last
    while(pos.next is not None):
      if(nodo.get_ventas()==get_ventas()):
        #lo remplazo
        nodo.next=pos.next
        parent.next=nodo
        return
      if(nodo.get_ventas()<pos.get_ventas()):
        nodo.next=pos
        parent.next=nodo
        self.cout=self.cout+1
        return
      parent=pos
      pos=pos.next 
    if(nodo.get_ventas()>pos.get_ventas()):
      pos.next=nodo
      self.prim=nodo
      self.cout=self.cout+1
    else:
      parent.next=nodo
      nodo.next=pos
      self.cout=self.cout+1
  def enqueue_pri_nota(self,nodo):
    if(self.prim is None):
      self.prim=self.last=nodo
      self.cout=self.cout+1
      return
    if(self.last.next is None):
      if(nodo.get_nota()==self.prim.get_nota()):
        self.prim=self.last=nodo
        return
      if(nodo.get_nota()>self.prim.get_nota()):
        primero=self.prim
        self.last=primero
        primero.next=nodo
        self.prim=nodo
        self.cout=self.cout+1
        return
      else:
        nodo.next=self.prim
        self.last=nodo
        self.cout=self.cout+1
        return
    pos=self.last
    while(pos.next is not None):
      if(nodo.get_nota()==pos.get_nota()):
        #lo remplazo
        nodo.next=pos.next
        parent.next=nodo
        return
      if(nodo.get_nota()<pos.get_nota()):
        nodo.next=pos
        parent.next=nodo
        self.cout=self.cout+1
        return
      parent=pos
      pos=pos.next 
    if(nodo.get_nota()>pos.get_nota()):
      pos.next=nodo
      self.prim=nodo
      self.cout=self.cout+1
    else:
      parent.next=nodo
      nodo.next=pos
      self.cout=self.cout+1
class Hash_ventas:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size
  def put(self,autor,titulo,ventas,nota,categoria,comentario):
    libro=Nodo(autor,titulo,ventas,nota,categoria,comentario)
    pos = hashstr(categoria,self.size)
    if self.list[pos] is not None:
      #Si existe esa cola solo la agrego ahi
      self.list[pos].enqueue_pri_ventas(libro)
    else:
      #Si no existe creo una cola y lo agrego
      self.list[pos]=Queue()
      self.list[pos].enqueue_pri_ventas(libro)
  def listado(self,categoria):
    pos = hashstr(categoria,self.size)
    if self.list[pos] is not None:#si existe
      aux=self.list[pos]
      aux.print_front()
    else:
      print("categoria no encontrada")
class Hash_nota:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size
  def put(self,autor,titulo,ventas,nota,categoria,comentario):
    libro=Nodo(autor,titulo,ventas,nota,categoria,comentario)
    pos = hashstr(autor,self.size)
    #print("pos",pos)
    if self.list[pos] is not None:
      #Si existe esa cola solo la agrego ahi
      self.list[pos].enqueue_pri_nota(libro)
    else:
      #Si no existe creo una cola y lo agrego
      self.list[pos]=Queue()
      self.list[pos].enqueue_pri_nota(libro)
  def compra_segura(self,autor):
    #ver si hay autor
    pos = hashstr(autor,self.size)
    if self.list[pos] is not None:#si existe
      aux=self.list[pos]
      aux.print_front()
    else:
      print("autor no encontrado")
class Hash:
  def __init__(self):
    self.H_nota=Hash_nota(100)
    self.H_ventas=Hash_ventas(100)
  def put_hash(self,autor,titulo,ventas,nota,categoria,comentario):
    self.H_nota.put(autor,titulo,ventas,nota,categoria,comentario)
    self.H_ventas.put(autor,titulo,ventas,nota,categoria,comentario)
    return
  def compra_segura_hash(self,autor):
    print("Busqueda por nota de",autor)
    self.H_nota.compra_segura(autor)
    return
  def listado_hash(self,categoria):
    print("Busqueda por ventas de",categoria)
    self.H_ventas.listado(categoria)
    return
H=Hash()
H.put_hash("pedro","rene y el pato",100,4,"fantasia","comentario")
H.put_hash("pedro","rene y el perro",70,6,"romance","comentario")
H.put_hash("luis","veranos rosa",2,65,"romance","comentario")
H.put_hash("luis","el/ella no te quiere",400,7,"fantasia","comentario")
H.compra_segura_hash("pedro")
H.compra_segura_hash("luis")
H.listado_hash("romance")
H.listado_hash("fantasia")