from Util import *
#from Movimentação import *
COTA = 2500


def van_gogh():
    planta()
    colhe()
    colheita_final()

def planta():
    area = get_world_size()
    for i in range(area):
        if get_ground_type() == Grounds.Grassland:
            till()
        plant(Entities.Sunflower)
        move(North)
    return True
    
def colhe():
    area = get_world_size()
    max = 15
    while num_items(Items.Power) < COTA:
        flag = True
        for i in range(area):
            if can_harvest() and measure() >= max:
                max = measure()
                harvest()
                plant(Entities.Sunflower)
                #regar(1)
                flag = False
            move(North)
        if flag:
            max -= 1
    return True

def colheita_final(): 
    area = get_world_size()
    value = 15
    while value >= 7 :
        for i in range(area):
            if can_harvest() and measure() >= value:
               harvest()
            move(North)
        value -= 1
    return True

ret_origem()
spawna(van_gogh)
