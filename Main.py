#TAOP86
#Matilda Engstroem Ericsson, Emily Berghaell

import numpy as np
import time
import sys
import copy

e=1 #diskonteringsfaktor

prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'

npzfile = np.load("extrdata/floc1.npz") #den kan ladda!
npzfile.files
m=npzfile['m'] #antal mojliga platser for lokalisering av anlaggning/fabrik. skalärer
n=npzfile['n'] #antal kunder. skalärer

s=npzfile['s'] #kapacitet hos anlaggning i. kolumnvektor
f=npzfile['f'] #fasta kostnader att oppna anlaggning pa plats i. kolumnvektor

c=npzfile['c'] #transportkostnad per enhet till kund j fran plats i. array 2D
#rad i c motsvarar kund. kolumn i c motsvarar anlaggning
#c.item(anlaggning, kund) for att fa transportkostnad ish

d=npzfile['d'] #efterfragan hos kund j. kolumnvektor

#print 'm:',m,' n:',n
#print 's:',s
#print 'd:',d
#print 'f:',f
#print 'c:',c

t1=time.time()
x=np.zeros((m,n),dtype=np.int)
y=np.zeros((m),dtype=np.int)

#yi = 1 om en anlaggning finns på plats i, 0 annars

#xij = transporterad mangd fran anlaggning pa plats i till kund j

ss=copy.deepcopy(s)
cc=copy.deepcopy(c)
dd=copy.deepcopy(d)
ff=copy.deepcopy(f)

    #Vi bestammer att vi vill hitta den dyraste fabriken forst
    #Vi vill ocksa ta den kund med hogst efterfragan

print(dd)
print(ff)

total_kostnad = 0

#while sum(dd)>0:
    # find facility, find customer, send, at min cost
    # set x and y
    # deduct from ss and dd,
    # --------

storst_kund = dd.max()
index_kund = dd.argmax()

dyrast_fabrik = ff.max()
index_fabrik = ff.argmax()



print(storst_kund)
print(index_kund)
print(dyrast_fabrik)
print(index_fabrik)

transport_kostnad = cc.item(index_fabrik, index_kund)
fast_kostnad = ff.item(index_fabrik)

total_kostnad = transport_kostnad + fast_kostnad

print(transport_kostnad)
print(fast_kostnad)

transport_kostnad = 0
fast_kostnad = 0
ff = np.delete(ff, index_fabrik)
print(ff)

    #




elapsed = time.time() - t1
print('Tid: '+ str('%.4f' % elapsed))

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print( 'Problem:',prob,' Totalkostnad: '+str(cost))
print( 'y:',y)
print('Antal byggda fabriker:',sum(y),'(av',m,')')
