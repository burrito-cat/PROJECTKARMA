import pygame
import os

RESOLUTION_X = 640
RESOLUTION_Y = 640

pygame.init()
screen = pygame.display.set_mode((RESOLUTION_X,RESOLUTION_Y))
clock = pygame.time.Clock()
running = True

game_folder = os.path.dirname(__file__)

def get_path(x: str):

    #in: le chemin relatif d'une file
    #function: prends le chemin absolu du jeu et y ajoute le chemin relatif
    #out: le path absolu
    #cela permet d'eviter des problemes 
    return os.path.join(game_folder, x)



class Player:
    def __init__(self, x, y):
        
        #on initialise idleimage qui est notre cas de base. il ne sera jamais modifie.
        # self.image sera ce qui va etre afficher, donc on le modifie.
        self.idleimage = pygame.image.load(get_path('assets/tempwalkcycle_0003.png')).convert_alpha()
        self.image = self.idleimage
        self.idleimage = pygame.transform.scale(self.image,
            (self.image.get_width() * 4,
            self.image.get_height() * 4)
        )
        self.rect = pygame.Rect(x, y, 100, 50)

        self.speed = 3

        #on charge toutes les frames de l'anim walkcycle et on les resize pour pas qu'on reset la taille a chaque fois. 
        #A terme, faudra que ca devienne une fonction global pour toutes les animations.
        #Je le fait pas de suite car je ne sais pas trop si la scale va changer en fonction des differents assets (ex: perso vs arriere plan)

        self.current_frame = 0
        self.frames = []
        self.frame_speed = 10
        self.frame_state = 0


        for i in range(1, 6):
            path = get_path(f'assets/tempwalkcycle_000{i}.png')
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img,
                (img.get_width() * 4, 
                 img.get_height() * 4)
            )
            self.frames.append(img)




    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, keys):
        is_moving = False

        #Mouvement
        if keys[pygame.K_a]:
            is_moving = True    
            self.rect.x -= self.speed
            #si on bouge vers la gauche, le sprite devrait s'inverser pour marcher.
            self.moving_left = True
        if keys[pygame.K_d]:
            is_moving = True
            self.rect.x += self.speed
        if keys[pygame.K_s]:
            is_moving = True
            self.rect.y += self.speed
        if keys[pygame.K_w]:
            is_moving = True
            self.rect.y -= self.speed
        

        #Animation
        # Pour eviter qu'on change de sprite de la walk cycle tout les frames, j'ai ajoute
        # un compteur (frame_state) qui, quand il est divisible par la rapidite voulue de l'animation
        # (frame_speed), ensuite va a la prochaine sprite dans. donc si frame_speed = 10, on aura 
        # 1 sprite toutes les 10 frames de mouvements.
        if is_moving:
            self.frame_state += 1
            if self.frame_state%self.frame_speed == 0:
                self.frame_state = 0
                self.current_frame += 1
                if self.current_frame >= len(self.frames):
                    self.current_frame = 0
                



                if keys[pygame.K_a]:
                    self.image = pygame.transform.flip(self.frames[self.current_frame], True, False)
                else:
                    self.image = self.frames[self.current_frame]
        #si on bouge pas on met l'etat idle.
        else:

            self.image = self.idleimage
                    
                    


    def roll():
        pass
    def interact():
        pass    
    def attack():
        pass

    
player1 = Player(50, 50)




while running:
    #close window quand on appuie sur la croix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255,255,255))
    



    player1.move(pygame.key.get_pressed())
    player1.draw(screen)


    pygame.display.flip()
    clock.tick(60) #capper a 60 fps



pygame.quit()