import pygame, random

def quiteGame():
    print('Your Score is :', score)
    pygame.quit()

def base_movement(window, base_img, var_x):
    window.blit(base_img,(var_x,512-75))
    #second window
    window.blit(base_img,(var_x+288,512-75))

def plane_movement(window,plane_img,plane_rect):
    window.blit(plane_img,plane_rect)

def pipe_movement(window,pipes,pipe_img):
    for pipe in pipes:
        pipe.centerx -= 5

    for pipe in pipes:
        window.blit(pipe_img,pipe)

def collision(pipes,plane_rect):
    for pipe in pipes:
        if pipe.colliderect(plane_rect):
            print('collusion')
            quiteGame()


    if plane_rect.bottom<=0:
        print('exceeded upper limit')
        quiteGame()



    if plane_rect.bottom>= 512-75:
        print('exceeded lower limit')
        quiteGame()


def game_build():
    global score
    score=0
    pygame.init()
    window = pygame.display.set_mode((288, 512))

    #music
    """pygame.mixer.init()
    pygame.mixer.music.load("resource\\soundtrack.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()"""

    #background
    bkg_image = pygame.image.load('bg.jpg')


    #base
    base_image = pygame.image.load('wall.jpg')
    var_x=0

    #plane
    plane_img = pygame.image.load('plane.png')

    plane_rect = plane_img.get_rect(center=(288/2, 512/2))
    g_force = 0.3
    plane_new_pos = 0

    #pipes
    pipe_img = pygame.image.load('vertical-line.png')

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
                    plane_new_pos =0
                    plane_new_pos-=8

            if event.type==TIMER:
                random_pipe_height = [200, 250, 300, 350, 400]
                pipes = pipe_img.get_rect(midtop=(290, random.choice(random_pipe_height)))
                list_of_pipe.append(pipes)


        #game basic
        window.blit(bkg_image, (0, 0))

        #collition detection
        collision(list_of_pipe,plane_rect)

        #pipe movement
        pipe_movement(window,list_of_pipe,pipe_img)

        score=score+1

        #base movement
        var_x-=1
        base_movement(window,base_image,var_x)
        if var_x<=-288:
            var_x=0

        #plane movement
        plane_new_pos+=g_force
        plane_rect.centery+=plane_new_pos
        plane_movement(window,plane_img,plane_rect)

        #updating
        clock.tick(50)
        pygame.display.update()
    quiteGame()



game_build()

