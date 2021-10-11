import pygame
from pygame import gfxdraw
from pygame import draw
import os
import time as t
from math import atan2, cos, degrees, radians, sin, tan, sqrt, pi
import math


# Game presets
start_time = t.time()
fps = 123456
width, height = 590, 470

# Centers window
x, y = 1360 - width, 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("draw arrows")
# font = pygame.font.Font('freesansbold.ttf', 15)

whitest      = (204, 234, 234)
white        = (160, 160, 160)
grey         = ( 27,  27,  27)  # (27, 75, 75)
black        = (  0,   0,   0)
red          = (225,  40,  40)
green        = ( 10, 200,  27)
yellow       = (255, 230,   0)
darkyellow   = (218, 168,   5)
velvet       = (232,  20,  20)
bluish_white = (179, 255, 251)
tastyellow   = (255, 230,   0)


def Move(rotation, steps, position):
    """Return coordinate position of an amount of steps in a direction."""
    xPosition = cos(radians(rotation)) * steps + position[0]
    yPosition = sin(radians(rotation)) * steps + position[1]
    return (xPosition, yPosition)

def DrawThickLine(point1, point2, thickness, color):
    angle = degrees(atan2(point1[1] - point2[1], point1[0] - point2[0]))

    vertices = list()
    vertices.append(Move(angle-90, thickness, point1))
    vertices.append(Move(angle+90, thickness, point1))
    vertices.append(Move(angle+90, thickness, point2))
    vertices.append(Move(angle-90, thickness, point2))

    gfxdraw.aapolygon(screen, vertices, color)
    gfxdraw.filled_polygon(screen, vertices, color)


# def arrow(color,line_color, start, end, thickness):
#     x, y = start[0], start[1]
#     X, Y = end[0], end[1]

#     theta = math.atan2(y-Y, X-x)
    
#     pygame.draw.circle(screen, color, (x, y), thickness)
#     DrawThickLine(start, end, thickness, line_color)
#     # now we draw the triangle
#     length = math.sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2) # of arrow
#     height = length//6 # of tri
#     if length < 150: # lower cap on height 
#         height = 150//6
#     elif length > 288: # upper cap on height
#         height = 288//6



#     base = height*math.tan(math.radians(32))


#     bx, by = X - height*cos(theta), Y + height*sin(theta)
#     x1, y1 = bx-base*sin(theta), by - base*cos(theta)
#     x2, y2 = bx+base*sin(theta), by + base*cos(theta)
#     pygame.gfxdraw.aapolygon(screen, [(X+20*cos(theta),Y-20*sin(theta)), (x1,y1), (x2,y2)], color)
#     pygame.gfxdraw.filled_polygon(screen, [(X+20*cos(theta),Y-20*sin(theta)), (x1,y1), (x2,y2)] , color)


# def circle(color, radius, x, y):
#     pygame.draw.circle(screen, color, (x, y), radius)



def arrow(color,line_color, start, end, thickness):
    x, y = start[0], start[1]
    X, Y = end[0], end[1]

    theta = math.atan2(y-Y, X-x)
    
    pygame.draw.circle(screen, color, (x, y), thickness)
    DrawThickLine(start, end, thickness, line_color)
    # now we draw the triangle
    frac = 8 # height as a fraction of lenght. 6 means height is 6th of lenght
    length = math.sqrt((start[0]-end[0])**2 + (start[1]-end[1])**2) # of arrow
    height = length//frac # of tri
    lcap = 60 # lower cap
    ucap = 186 # upper cap
    if length < lcap: # lower cap on height 
        height = lcap//frac
    elif length > ucap: # upper cap on height
        height = ucap//frac



    base = height*math.tan(math.radians(32))


    bx, by = X - height*cos(theta), Y + height*sin(theta)
    x1, y1 = bx-base*sin(theta), by - base*cos(theta)
    x2, y2 = bx+base*sin(theta), by + base*cos(theta)
    pygame.gfxdraw.aapolygon(screen, [(X+5*cos(theta),Y-5*sin(theta)), (x1,y1), (x2,y2)], color)
    pygame.gfxdraw.filled_polygon(screen, [(X+5*cos(theta),Y-5*sin(theta)), (x1,y1), (x2,y2)] , color)

def aacirlce(rad, x, y, color, thickness):
    layers = thickness
    increment = 0.3
    for i in range(int(layers/increment)+3):
        gfxdraw.aacircle(screen, x, y, int(rad-(i*increment)), color)
    

    # gfxdraw.circle(screen, x, y, rad, color)



m_x, m_y = 200, 160
r_x, r_y = 250, 80
left_hold = False

# points = [(0,0), (0,1)]

if __name__ == "__main__":
    while True:
        
        screen.fill(grey)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # leftclick
                    r_x, r_y = pygame.mouse.get_pos()
                    left_hold = True

                if event.button == 3:  # rightclick
                    pass
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    left_hold = False

     
        if left_hold:
            m_x, m_y = pygame.mouse.get_pos()
        arrow(yellow, yellow, (r_x, r_y), (m_x, m_y), 2)
        aacirlce(100, m_x, m_y, red, 3)
            # points.append((m_x, m_y))
            # circle(red, 4, m_x, m_y)
            # pygame.draw.lines(screen, red, False, points, 8)
        
        
        
        pygame.display.update()
        clock.tick(fps)






