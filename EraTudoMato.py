from Util import*
QTD = 5000000

def ceifador():
    cota = QTD + num_items(Items.Hay)
    quick_print('Cota de grama:', cota)
    while num_items(Items.Hay) < cota:
        harvest()
        move(North)
clear() 
spawna(ceifador)
