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
    window = pygame.display.set_mode((288,512))

    #music
    """pygame.mixer.init()
    pygame.mixer.music.load("resource\\soundtrack.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()"""

    #background
    bkg_image = pygame.image.load('bg.jpg')


    #base
    base_image = pygame.image.load('wall.png')
    var_x=0

    #bird
    bird_img = pygame.image.load('plane.png')

    bird_rect = bird_img.get_rect(center=(75, 512/2))
    g_force = 0.3

    #pipes
    pipe_img = pygame.image.load('pillar.png')

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
                random_pipe_height = [200, 250, 300, 350, 400]
                pipes = pipe_img.get_rect(midtop=(290, random.choice(random_pipe_height)))
                list_of_pipe.append(pipes)


        #game basic
        window.blit(bkg_image, (0, 0))

        #collition detection
        collision(list_of_pipe,bird_rect)

        #pipe movement
        pipe_movement(window,list_of_pipe,pipe_img)

        #base movement
        var_x-=1
        base_movement(window,base_image,var_x)
        if var_x<=-200:
            var_x=0

        #bird movement
        bird_new_pos+=g_force
        bird_rect.centerx+=bird_new_pos
        bird_movement(window,bird_img,bird_rect)

        #updating
        clock.tick(60)
        pygame.display.update()

    pygame.quit()


if __name__ =="__main__":
    game_build()

