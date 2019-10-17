#TAOP86
#Matilda Engstroem Ericsson, Emily Berghaell

import numpy as np
import time
import sys
import copy

e=1 #diskonteringsfaktor

prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'

npzfile = np.load("extrdata/floc2.npz")
npzfile.files

#Skalärer:
mojliga_fabriker=npzfile['m'] #antal mojliga platser for lokalisering av anlaggning/fabrik.
antal_kunder=npzfile['n'] #antal kunder.

#Kolumnvektorer:
kapacitet_fabrik=npzfile['s'] #kapacitet hos anlaggning i.
kostnad_fabrik=npzfile['f'] #fasta kostnader att oppna anlaggning pa plats i.
efterfragan_kund=npzfile['d'] #efterfragan hos kund j.

#Array, 2D
transportkostnad=npzfile['c'] #transportkostnad per enhet till kund j fran plats i.
#rad i c motsvarar kund. kolumn i c motsvarar anlaggning
#c.item(anlaggning, kund) for att fa transportkostnad ish



print('(mojliga fabriker) m:', mojliga_fabriker, ' (antal kunder) n:', antal_kunder)
print( '(kapaciet) s:', kapacitet_fabrik)
print('(efterfragan) d:', efterfragan_kund)
print('(kostnad anlaggning) f:', kostnad_fabrik)
print('(transportkostnad) c:', transportkostnad)

t1=time.time()
x=np.zeros((mojliga_fabriker, antal_kunder), dtype=np.int)
y=np.zeros((mojliga_fabriker), dtype=np.int)


c_kapacitet_fabrik=copy.deepcopy(kapacitet_fabrik)
c_transportkostnad=copy.deepcopy(transportkostnad)
c_efterfragan_kund=copy.deepcopy(efterfragan_kund)
c_kostnad_fabrik=copy.deepcopy(kostnad_fabrik)

    #Vi bestammer att vi vill hitta den dyraste fabriken forst
    #Vi vill ocksa ta den kund med hogst efterfragan

total_kostnad = 0

while sum(c_efterfragan_kund)>0:
    # find facility, find customer, send, at min cost
    # set x and y
    # deduct from ss (c_kapacitet_fabrik) and dd (c_efterfragan_kund),
    # --------

    storst_kund = c_efterfragan_kund.max()
    index_kund = c_efterfragan_kund.argmax()

    dyrast_fabrik = c_kostnad_fabrik.max()
    index_fabrik = c_kostnad_fabrik.argmax()

    print("Störst kund: ", storst_kund, "index ", index_kund)
    print("Dyrast fabrik: ",dyrast_fabrik, "index ", index_fabrik)


    #yi = 1 om en anlaggning finns på plats i, 0 annars
    #aka. vi berattar att vi byggt den fabriken
    y.itemset(index_fabrik, 1)

    print("y: ", y)

    #xij = transporterad mangd fran anlaggning pa plats i till kund j

    kapacitet = c_kapacitet_fabrik.item(index_fabrik)

    print("Kapacitet fabrik efter: ", c_kapacitet_fabrik)

    onskad_mangd = c_efterfragan_kund.item(index_kund)

    if (kapacitet >= onskad_mangd):
        transporterad_mangd = onskad_mangd
        kapacitet = kapacitet - onskad_mangd
        onskad_mangd = 0
        # fortsatt till nasta kund
    else:
        transporterad_mangd = kapacitet
        onskad_mangd = onskad_mangd - kapacitet
        # fortsatt till nasta fabrik

#    transporterad_mangd = transport_mangd(kapacitet, onskad_mangd)

    c_kapacitet_fabrik.itemset(index_fabrik, kapacitet)
    c_efterfragan_kund.itemset(index_kund, onskad_mangd)

    x.itemset((index_fabrik, index_kund), transporterad_mangd)

    print("x: ", x)



    print("Kapacitet fabrik efter: ", c_kapacitet_fabrik)
    print("Efterfragan kund: ", c_efterfragan_kund)

    if(onskad_mangd == 0):
        print("Nasta kund")
        c_efterfragan_kund = np.delete(c_efterfragan_kund, index_kund)
    else:
        #bygg en till fabrik
        print("Bygg en till fabrik")

        c_kapacitet_fabrik = np.delete(c_kapacitet_fabrik, index_fabrik)
        c_kostnad_fabrik = np.delete(c_kostnad_fabrik, index_fabrik)


print("All efterfragan uppfylld!")
#transport_kostnad = cc.item(index_fabrik, index_kund)
#fast_kostnad = ff.item(index_fabrik)

#total_kostnad = transport_kostnad + fast_kostnad

#print("Transport kostnad: ", transport_kostnad)
#print("Fast kostnad: ", fast_kostnad)

#transport_kostnad = 0
#fast_kostnad = 0
#ff = np.delete(ff, index_fabrik)
#print("ff: ", ff)

    #




elapsed = time.time() - t1
print('Tid: '+ str('%.4f' % elapsed))

cost= sum(sum(np.multiply(transportkostnad, x))) + e * np.dot(kostnad_fabrik, y)
print( 'Problem:',prob,' Totalkostnad: '+str(cost))
print( 'y:',y)
print('Antal byggda fabriker: (', sum(y),'av', mojliga_fabriker, ')')


# Om kundens efterfragan uppfylls, return True
# Om inte, och ny fabtik behover byggas, return False
def transport_mangd(kapacitet, onskad_mangd):
    if (kapacitet >= onskad_mangd):
        transporterad_mangd = onskad_mangd
        kapacitet = kapacitet - onskad_mangd
        onskad_mangd = 0
        # fortsatt till nasta kund
        return transporterad_mangd
    else:
        transporterad_mangd = kapacitet
        onskad_mangd = onskad_mangd - kapacitet
        # fortsatt till nasta fabrik
        return transporterad_mangd