import pygame, random
def base_movement(window, base_img, var_x):
    window.blit(base_img,(var_x,512-75))
    #second window
    window.blit(base_img,(var_x+200,512-75))

def bird_movement(window,bird_img,bird_rect):
    window.blit(bird_img,bird_rect)

def pipe_movement(window,pipes,pipe_img):
    for pipe in pipes:
        pipe.conterx -=5

    for pipe in pipes:
        window.blit(pipe_img,pipe)

def collision(pipes,bird_rect):
    for pipe in pipes:
        if pipe.colliderect(bird_rect):
            print('collected')

    if bird_rect.bottom<=-10:
        print('exceeded upper limit')

    if bird_rect.bottom>=512-75:
        print('exceeded lower limit')

def game_build():
    pygame.init()
    windows = pygame.display.set_mode((288,512))

    #music
    """pygame.mixer.init()
    pygame.mixer.music.load("resource\\soundtrack.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()"""

    #background
    bkg_image = pygame.image.load('resource\\background-night.png')


    #base
    base_image = pygame.image.load('resource\\base.png')
    var_x=0

    #bird
    bird_img = pygame.image.load('resource\\rebird-midflag.png')

    bird_rect = bird_img.get_rect(center=(75, 512/2))
    g_force = 0.3

    #pipes
    pipe_img = pygame.image.load('resource\\pipe-red.png')

    list_of_pipe=[]

    TIMER = pygame.USEREVENT
    pygame.time.set_timer(TIMER,1000)

    #main loop
    clock = pygame.time.Clock()
    running = True

    while running:
        #event loop
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_new_pos = 0
                    bird_new_pos-=8

            if event.type==TIMER:
                random_pipe_height = [200,250,300,350,400]

