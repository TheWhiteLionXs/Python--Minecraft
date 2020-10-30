#+++++++++++++++++++++++++++++++PYTHON MINECRAFT+++++++++++++++++++++++++++++++#
#Connect Minecraft with Python.
from mcpi import block
from mcpi.minecraft import Minecraft
#Inportar librerias
import time
import math
#-------------------------------------CODE--------------------------------------#
mc = Minecraft.create()
#Crear un bucle
while True:
#Obtener las coordenadas del jugador.
    x, y, z = mc.player.getTilePos()
#Obtener el bloque de la cordenada del jugador.
    b = mc.getBlock(x, y-1, z)
    mc.postToChat(b)
    time.sleep(1)
