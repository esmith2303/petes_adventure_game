import pygame

pygame.init()

class Tiles:

    Size = 32

    Blocked = []
    
    Blocked_Types = ["2", "3"]

    def Blocked_Pos(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False
    
    def load_texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface


    Grass = load_texture("grass.jpg", Size)

    Stone = load_texture("stone.jpg", Size)

    Water = load_texture("water.jpg", Size)

    Texture_Tags = {"1": Grass, "2": Stone, "3": Water}
        
