from VanGogh import *
clear()

area = get_world_size()
for i in range(area):
    spawn_drone(van_gogh)
    if i == (area -1):
        van_gogh()
    move(East)
