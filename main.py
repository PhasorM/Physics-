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
for i in range(0):
    #(self, radius: float , position:Vector2D,  position_old: Vector2D,  acceleration: Vector2D = (0,0), mass: float =1.0 )
    r=20
    v_in = Vector2D(random.randint(-5,5),random.randint(-5,5))
    pos=Vector2D(random.randint(r,a-r),random.randint(r,b-r))
    old_pos= pos - v_in * dt
    #ac = Vector2D(0,0)
    l.append(entity(r,
    pos, 
    old_pos,
    ac))
l1=[]
h=200
for i in range(0,2):
    #(self, radius: float , position:Vector2D,  position_old: Vector2D,  acceleration: Vector2D = (0,0), mass: float =1.0 )
    r=10
    v_in = Vector2D(0,0)
    pos=Vector2D(h,300)
    old_pos= pos - v_in * dt
    if (i==0):
        ac = Vector2D(0,0)
    else : 
        ac = Vector2D(0,0.98)
    l1.append(entity(r,
    pos,
    old_pos,
    ac))
    h=h+25

l=l1+l


substeps = 8
while running:
    for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255, 255, 255), (0, 300-r), (800, 300-r), 1)
    
    
    
    for i in range(len(l)):
        for s in range(substeps):
            l[i].WallCollision(a-r,b-r,r,r,dt/substeps)
            l[i].accelerate(ac)        
            for j in range(i+1,len(l)):
                l[i].Collision(l[j],1)
            
            l[i].update(dt/substeps)
            
            pygame.draw.circle(screen, (255, 0, 0), (int(l[i].position.x), int(l[i].position.y)), r)
    

    screen.blit
    pygame.display.update()

