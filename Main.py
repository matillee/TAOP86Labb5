#TAOP86
#Matilda Engstroem Ericsson, Emily Berghaell

import numpy as np
import time
import sys
import copy

e=1 #diskonteringsfaktor

prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'

npzfile = np.load("extrdata/floc3.npz") #den kan ladda!
npzfile.files
m=npzfile['m'] #antal mojliga platser for lokalisering av anlaggning/fabrik
n=npzfile['n'] #antal kunder
s=npzfile['s'] #kapacitet hos anlaggning i
d=npzfile['d'] #efterfragan hos kund j
f=npzfile['f'] #fasta kostnader att oppna anlaggning pa plats i
c=npzfile['c'] #transportkostnad per enhet till kund j fran plats i
#print 'm:',m,' n:',n
#print 's:',s
#print 'd:',d
#print 'f:',f
#print 'c:',c

t1=time.time()
x=np.zeros((m,n),dtype=np.int)
y=np.zeros((m),dtype=np.int)

ss=copy.deepcopy(s)
dd=copy.deepcopy(d)
ff=copy.deepcopy(f)

    #Vi bestammer att vi vill hitta den dyraste fabriken forst
    #Vi vill ocksa ta den kund med hogst efterfragan

    #Vi vill alltsa sortera dd och ff sa storsta elementet ar forst.

sorted(dd, reverse=True)
sorted(ff, reverse=True)


print(dd)
print(ff)

# sedan vill hitta samma element i riktiga d i och f. Hitta index for dessa.

storst_kund = d.index(dd[0])
dyrast_fabrik = f.index(ff[0])

print(storst_kund)
print(dyrast_fabrik)

#while sum(dd)>0:
    # find facility, find customer, send, at min cost
    # set x and y
    # deduct from ss and dd,
    # --------



    #




elapsed = time.time() - t1
print 'Tid: '+str('%.4f' % elapsed)

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print 'Problem:',prob,' Totalkostnad: '+str(cost)
print 'y:',y
print 'Antal byggda fabriker:',sum(y),'(av',m,')'
