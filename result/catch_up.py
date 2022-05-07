from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'),(700, 500))


#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('sprite1.png'),(100, 100))
sprite2 = transform.scale(image.load('sprite2.png'),(100, 100))
speed = 10

x1 = 100
y1 = 300
x2 = 300
y2 = 300

game = True
clock = time.Clock()
FPS = 60

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= 10
    if keys_pressed[K_RIGHT] and x1 < 610:
        x1 += 10
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1 < 410:
        y1 += 10

    if keys_pressed[K_a] and x2 > 5:
        x2 -= 10
    if keys_pressed[K_d] and x2 < 610:
        x2 += 10
    if keys_pressed[K_w] and y2 > 5:
        y2 -= 10
    if keys_pressed[K_s] and y2 < 410:
        y2 += 10

    display.update()
    clock.tick(FPS)
    


