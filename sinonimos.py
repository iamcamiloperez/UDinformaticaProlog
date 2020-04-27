from pyswip import Prolog

prolog = Prolog()
prolog.consult('sinonimos')
palabra = 'terminar'

solucion = list(prolog.query("P=%s,sinonimo_de(P, S)" % palabra, maxresult=-1))
for sinonimo in range(0,len(solucion)):
    print(solucion[sinonimo]['S'])
