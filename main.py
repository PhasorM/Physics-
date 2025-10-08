import pygame 
import math
from objects import entity
from vec_lib import Vector2D
import random
pygame.init()
a = 800
b = 600
print("Dimensions set to: " + str(a) + "x" + str(b))
screen = pygame.display.set_mode((a, b))
pygame.display.set_caption("My Game Window")  
running = True
l = []
dt=0.1
ac=Vector2D(0,0.98)
for i in range(30):
    r=10
    v_in = Vector2D(5,random.randint(-5,5))
    pos=Vector2D(random.randint(r,a-r),random.randint(r,int(b/4)))
    old_pos= pos - v_in * dt
    l.append(entity(r,
    pos, 
    old_pos))
l1=[]
h=-100
d=10
number= 30
for i in range(number):
    r=5
    v_in = Vector2D(0,0)
    pos=Vector2D(h,300)
    old_pos= pos

    l1.append(entity(r,
    pos,
    old_pos))
    h=h+d
    print(h)
end_pos = h + (number - 1)*d
l=l1+l

substeps =2
trajectory = []
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
    screen.fill((0,0,0))
    
    for j in range(substeps):
        for i in range(len(l)):
            l[i].accelerate(ac)
            l[i].WallCollision(a-r,b-r,r,r,dt/substeps,0.9)
            for k in range(i+1,len(l)):
                if (not( i <= len(l1)-1 and k <= len(l1)-1)):
                    l[i].Collision(l[k],0.9)
            l[i].update(dt/substeps)
            if (i<=len(l1)-1):        
                pygame.draw.circle(screen, (255, 0, 0), (int(l[i].position.x), int(l[i].position.y)), l[i].radius)
            else:
                pygame.draw.circle(screen, (0, 255, 0), (int(l[i].position.x), int(l[i].position.y)), l[i].radius)
        l1[0].position=Vector2D(h,300)
        l1[len(l1)-1].position=Vector2D(end_pos,300)
        for iterations in range(5):
            for i in range(len(l1)-1):
                # dist = (l1[i].position - l1[i+1].position).ab()
                # difference = dist - d
                # normal = (l1[i].position - l1[i+1].position).norm()
                # delta = normal * (difference)
                if (i != 0 or i!= len(l1)-2):
                    # l1[i].position = l1[i].position - delta * 0.5
                    # l1[i+1].position = l1[i+1].position + delta * 0.5
                    l[i].Link(l[i+1],d,"free")
                elif (i == 0):
                    # l1[i+1].position = l1[i+1].position + delta
                    l[i].Link(l[i+1],d,"pin")
                elif (i == len(l1)-1):
                    # l1[i-1].position = l1[i-1].position + delta
                    l[i].Link(l[i-1],d,"pin")
        
    pygame.display.update()
        




