from vec_lib import Vector2D
import math

class entity:
    def __init__(self, radius: float , position:Vector2D,  position_old: Vector2D, acceleration: Vector2D= Vector2D(0,0), mass: float =1.0 ):
        self.acceleration = acceleration
        self.position = position
        self.position_old = position_old
        self.mass = mass
        self.radius = radius
        
    def update(self,dt:float =1.0): #verlet integration
        vel = self.position - self.position_old
        self.position_old = self.position
        self.position = self.position + vel + self.acceleration * (dt**2) 
        self.acceleration = Vector2D(0,0)

    def accelerate(self, a: Vector2D):  #new acceleration in next frame
        self.acceleration = self.acceleration + a

    def WallCollision(self, x_max:float , y_max:float, x_min:float, y_min:float,dt:float =1.0, e:float=1):
        u = (self.position - self.position_old)* (1/dt)
        m = self.mass
        if (self.position.x > x_max):
            temp = self.position.x
            self.position.x = x_max
            self.position_old.x = self.position.x + (temp - self.position_old.x)
        if (self.position.x < x_min):
            temp = self.position.x
            self.position.x = x_min
            self.position_old.x = self.position.x + (temp - self.position_old.x)

        if (self.position.y > y_max):
            temp=self.position.y
            self.position.y = y_max
            self.position_old.y = self.position.y + (temp - self.position_old.y) 
            # self.acceleration.y = self.acceleration.y + ((-u.y * e) - u.y)/dt

        if (self.position.y < y_min):
            temp=self.position.y
            self.position.y = y_min
            self.position_old.y = self.position.y + (temp - self.position_old.y) 

    def Collision(self, other: 'entity', e: float=0):
        m1 = self.mass  
        m2 = other.mass
        u1 = (self.position - self.position_old)  
        u2 = (other.position - other.position_old) 
        x1 = self.position
        x2 = other.position
        x1_old = self.position_old
        x2_old = other.position_old
        n = Vector2D.norm(other.position - self.position)
        if Vector2D.ab(self.position - other.position) <= (self.radius + other.radius):            
            error= (self.radius + other.radius) - (self.position - other.position).ab() 

            if (error > 0):
                self.position = self.position - n*(error/2)
                other.position = other.position + n*(error/2)
            
            self.position_old = self.position - ((x1 - x1_old)*m1 + (x2 - x2_old)*m2 + (x2 + x1_old - x1 - x2_old) * m2 * e ) * (1/(m1 + m2))
            other.position_old = other.position - ((x2 - x2_old)*m2 + (x1 - x1_old)*m1 + (x1 + x2_old - x2 - x1_old) * m1 * e ) * (1/(m1 + m2))

    def Link(self,other:'entity',d:float=7,type="free"):  #type can be free, pin
        dist = (self.position - other.position).ab()
        difference = dist - d
        normal = (self.position - other.position).norm()
        delta = normal * (difference)
        if type == "free":
            self.position = self.position - delta * 0.5
            other.position = other.position + delta * 0.5
        if type == "pin":
            other.position = other.position + delta
        
            
            
        
            

                
            



        
