def van_gogh():
    planta_girassois()
    colhe_girassois()

def planta_girassois(qnt = 15000):
    area = get_world_size()
    for i in range(area):
        if get_ground_type() == Grounds.Grassland:
            till()
            plant(Entities.Sunflower)
        move(North)
    return True
    
def colhe_girassois():
    area = get_world_size()
    max = 15
    while True:
        flag = True
        for i in range(area):
            if can_harvest() and measure() >= max:
                max = measure()
                harvest()
                plant(Entities.Sunflower)
                regar(1)
                flag = False
            move(North)
        if flag:
            max -= 1
        quick_print(max)
    return True
    
def regar(umi = 0.5):
    if get_water() < umi:
        use_item(Items.Water)
        use_item(Items.Fertilizer) 