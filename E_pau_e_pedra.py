from Util import *
#from Movimentação import *
QTD = 5000000

def colheita_final(): 
    area = get_world_size()
    for i in range(area):
        harvest()
        move(North)
    return True

def madeira():
    cota = QTD + num_items(Items.Wood)
    quick_print('Cota de m:', cota)
    while cota > num_items(Items.Wood): 
        if can_harvest():
            harvest()
        x,y = get_pos_x(),get_pos_y()
        if (x+y)%2==0:
            plant(Entities.Tree)
        else : 
            plant(Entities.Bush)
        move(North)
    colheita_final()
    return True
    
ret_origem()
spawna(madeira)