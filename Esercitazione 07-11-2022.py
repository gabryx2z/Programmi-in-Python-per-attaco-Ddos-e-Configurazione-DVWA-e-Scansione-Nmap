#Il nostro obbiettivo è quello di effettuare delle operazioni di calcolo su delle figure geometriche
#per prima cosa importo dal modulo che ho creato con il nome di  "funzioni" , le funzioni appunto
#per il calcolo del perimetro del quadro, del rettangolo e la circonferenza del cerchio

from funzioni import quadrato
from funzioni import circonferenza
from funzioni import rettangolo

#Ho dato come input una scelta iniziale che con la funzioni if fa scegliere all'utente l'operazione di cui necessità
scelta =  int(input("Ciao, quale operezione vuoi fare?\n\n Perimentro quadrato (1)\n\n Circonferenza cerchio (2)\n\n perimentro rettangolo (3)\n\n"))
 
if (scelta==1):
    quadrato()

elif (scelta==2):
 circonferenza()

elif (scelta==3):
    rettangolo()
#In fine ho inserito un  else nel caso in cui si inserisca un valore diverso da 1,2 o 3
#facendo comparire a schermo la scritta valore non valido
else:
 print ("\nvalore inserito non valido\n")



