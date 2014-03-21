#!/src/bin/python
import modulo
t_upla=(1e1,1e2,1e3,1e4,1e5,1e6,1e7)
lista=[]

def mostrar(lista):
  for l in lista:
    dif=modulo.PI-l
    print ' PI35DT: %.35f lista: %f PI35DT-lista: %f ' % (modulo.PI,l,dif)
    
for i in t_upla:
   y=modulo.aproximacion(i)
   lista=lista+[y]

  

 
mostrar(lista) 
#El numero maximo de elementos de la t_upla es 7.
#Al introducir el elemento 100000000 ya se porduce error de memoria.

#La expresion .pyc es el acrónimo de "Compiled Python script file"