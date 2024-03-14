import pygame
import datetime as dt


def rotate_arrow():
    minute = dt.datetime.now().minute
    second = dt.datetime.now().second

    minute_angle = (minute * 60)
    second_angle = second * 60 

    rotated_arrow = pygame.transform.rotate(m_arrow, -minute_angle)
    return rotated_arrow
pygame.init()



surface = pygame.Surface((200,200))
screen = pygame.display.set_mode((700, 500))


clock = pygame.image.load(r"C:\Users\PC\Desktop\Python\lab1\LAB7\img\mainclock.png")
m_arrow = pygame.image.load(r"C:\Users\PC\Desktop\Python\lab1\LAB7\img\rightarm.png")
s_arrow = pygame.image.load(r"C:\Users\PC\Desktop\Python\lab1\LAB7\img\leftarm.png")
clock = pygame.transform.scale(clock, (700, 500))
m_arrow = pygame.transform.scale(m_arrow, (700, 500))
s_arrow = pygame.transform.scale(s_arrow, (45, 500))

angle_m = 310
angle_s = 360
pivot_point = (350, 250)

running = True
while (running):
    
    screen.blit(clock, (0, 0))
    arrow = rotate_arrow()

    screen.blit(arrow, (350 - arrow.get_width() / 2, 250 - arrow.get_height() / 2))
    #rotated_image = pygame.transform.rotate(m_arrow, angle_m)
    #rect1 = rotated_image.get_rect(center=pivot_point)

    #rotated_image2 = pygame.transform.rotate(s_arrow, angle_s)
    #rect2 = rotated_image2.get_rect(center=pivot_point)
    # Отображение повернутого изображения
    #screen.blit(rotated_image, rect1.topleft)
    #screen.blit(rotated_image2, rect2.topleft)

    pygame.display.update()
    angle_m -= 0.5
    angle_s -= 0.677
    if angle_s <= 0:
        angle_s = 360
    if angle_m <= 0:
        angle_m = 360

    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()