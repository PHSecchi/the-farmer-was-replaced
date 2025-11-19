from Util import *
#from Movimentação import *
QTD = 1500000


def planta():
    area = get_world_size()
    for i in range(area):
        if get_ground_type() == Grounds.Grassland:
            till()
            plant(Entities.Carrot)
        move(North)
    return True    

def colheita_final(): 
    area = get_world_size()
    for i in range(area):
        harvest()
        move(North)
    return True

def cenoura():
    planta()
    cota = QTD + num_items(Items.Carrot)
    quick_print('Cota de cenoura:', cota)
    while cota > num_items(Items.Carrot): 
        if can_harvest():
            harvest()
            plant(Entities.Carrot)
        move(North)
    colheita_final()
    return True
    
ret_origem()
spawna(cenoura)