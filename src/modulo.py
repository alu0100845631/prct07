#!/src/bin/python
PI=3.1415926535897931159979634685441852
import sys
 
def aproximacion(n):
  n=int n
  if(n!=0):
   suma=0
   for i in range(1,n+1):
     x_i=(i-0.5)/float(n)
     fx_i=4/(1+x_i**2)
     b=i/float(n)
     a=b-(1/float(n))
     suma=suma+fx_i
   pi=suma/n
   return pi

if __name__ == "__main__":     
 
 if(len(sys.argv)==3):
   n= int(sys.argv[1])
   m=int(sys.argv[2])

 else:
   print'La forma de uso es: "modulo.py, n, m", por lo que se utilizaran los valores por defecto.'
   n=10
   m=10
     
 l=[]

 for j in range(1, m+1):
   pi=aproximacion(j*m)
   l=l+[pi]
 print l

 
 for z in range(0, m):
   npi=l[z]
   dif=PI-npi
 print ' PI35DT: %.35f lista: %f PI35DT-lista: %f ' % (PI,npi,dif)
  
