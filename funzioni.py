# Per prima cosa importo la libreria math per utilizzare il pgreco 
# nel calcolo della circonferenza del cerchio
import math

#Ho creato la funzione per il calcolo  del perimetro del quadrato
def quadrato():
    
    x=float (input("\nInserisce il lato del quadrato:"))
    y=x**2

    print ("Il perimetro del quadrato è",y)

#Ho creato la funzione per il calocolo della circonferenza del cerchio
def circonferenza():

    x= float (input("\nInserire lunghezza del raggio:"))
    y= 2*math.pi*x

    print ("La circonferenza del cerchio è:",y)

#Ho creato la funzione per il calcolo del perimetro del rettangolo
def rettangolo():

     b= float (input("\nInserire la base del rettangolo:"))
     h= float (input("\nInserire l'altezza del rettangolo:"))
     y= b*h
     
     print("Il periemetro del rettangolo è:",y)
