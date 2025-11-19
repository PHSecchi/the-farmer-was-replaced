def arar():
    size = get_world_size()
    for i in range(size):
        till()
        move(North)
       
def nutrir(umi = 0.5):
    if get_water() < umi:
        use_item(Items.Water)
        use_item(Items.Fertilizer)

def colhe():
    size = get_world_size()
    for i in range(size):
        harvest()
        move(North)


def spawna(action):
    size = get_world_size()
    for i in range(size):
        spawn_drone(action)
        if i == (size -1):
            action()
        move(East)

def ret_origem():
    while get_pos_x() != 0:
        move(West)
    while get_pos_y() != 0:
        move(South)
        
 