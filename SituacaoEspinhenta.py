from Verifica_Cacto import *
from RetornaOrigem import *



def teste():
    flag = True
    ord = False
    while ord == False:
        ord = True
        for i in range (get_world_size()):
            if verif_cacto() ==  False:
                ord = False
            move(North)
    ord = False



ret_origem()
area = get_world_size()
for i in range(get_world_size()):
    spawn_drone(teste)
    if i == (area -1):
        teste()
    move(East)
