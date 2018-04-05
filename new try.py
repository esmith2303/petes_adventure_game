import pygame, sys, time, math
from Graphics.textures import *
from globalcamera import Globals
from mapengine import *
from Scripts.NPC import *
from Scripts.Player import *


pygame.init()


cSec = 0
cFrame = 0
FPS = 0


terrain = Map_Engine.load_map("Ponds.map")

fps_font = pygame.font.Font("/home/pi/Desktop/RPG/Sofia-Regular.otf", 20)

sky = pygame.image.load("sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, (100, 100, 100))
    window.blit(fps_overlay, (0, 0))

def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 500, 700
    window_title = "Mad skills leet RPG game"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_height, window_width), pygame.HWSURFACE|pygame.DOUBLEBUF)


def count_fps():
    global delta_time, cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            delta_time = 1 / FPS

create_window()

player = Player("Petelol")
player_w, player_h = player.width, player.height
player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
player_y = ((window_height / 2 - player_h / 2 - Globals.camera_x) / Tiles.Size)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "west"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "east"

        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0


    #Logic
    if Globals.camera_move == 1:
        if not Tiles.Blocked_Pos((round(player_x), math.floor(player_y))):
            Globals.camera_y += 100 * delta_time
    elif Globals.camera_move == 2:
        if not Tiles.Blocked_Pos((round(player_x), math.ceil(player_y))):
            Globals.camera_y -= 100 * delta_time
    elif Globals.camera_move == 3:
        if not Tiles.Blocked_Pos((math.floor(player_x), round(player_y))):
            Globals.camera_x += 100 * delta_time
    elif Globals.camera_move == 4:
        if not Tiles.Blocked_Pos((math.ceil(player_x), round(player_y))):
            Globals.camera_x -= 100 * delta_time


    player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
    player_y = ((window_height / 2 - player_h / 2 - Globals.camera_x) / Tiles.Size)        
    

    #Render Graphics
    window.blit(Sky, (0, 0))
    
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    player.render(window, (window_width / 2 - player_w / 2,
                           window_height / 2 - player_h / 2))

    show_fps()
                
    pygame.display.update()
                
    count_fps()
                


pygame.quit()
sys.exit
