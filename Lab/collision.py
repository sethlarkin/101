# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:06:51 2016

@author: seth
"""
#Version 1.0
import math
import numpy as np
import numpy.random as rand
import numpy.linalg as linalg

from tkinter import Tk, Frame, Canvas


class Painter:
    def __init__(self, root, width=800, height=600, offset=5, min_radius=5, max_radius=10, num_balls=20, refresh_speed=5):

        # Draw frame etc
        self.app_frame = Frame(root)
        self.app_frame.pack()
        self.canvas = Canvas(self.app_frame, width = width, height = height)
        self.canvas_size = (int(self.canvas.cget('width')), int(self.canvas.cget('height')))
        self.canvas.pack()
        self.refresh_speed = refresh_speed
        
        # Work area
        self.min_x = offset
        self.max_x = width - offset
        self.min_y = offset
        self.max_y = height - offset

        self.num_balls = num_balls
        self.balls = []
        self.ball_handles = dict()        
        self.init_balls(max_radius, min_radius, num_balls)
        
        self.time = 0

        self.wall_collision_times = np.zeros(num_balls)
        self.init_wall_collision_times()

        self.ball_collision_times = np.zeros((num_balls,num_balls))
        self.init_ball_collision_times()
                
        self.draw()
        self.refresh()
        return

    def init_balls(self, max_radius, min_radius, num_balls):
        for i in np.arange(num_balls):
            while(True):
                radius = (max_radius - min_radius) * rand.random_sample() + min_radius

                ball_min_x = self.min_x + radius
                ball_max_x = self.max_x - radius
                x = (ball_max_x - ball_min_x)*rand.random_sample() + ball_min_x

                ball_min_y = self.min_y + radius
                ball_max_y = self.max_y - radius                
                y = (ball_max_y - ball_min_y)*rand.random_sample() + ball_min_y

                vx = rand.random_sample()
                vy = rand.random_sample()

                mass = rand.random_sample()
                new_ball = Ball(radius, x, y, vx, vy, mass)
                
                if not new_ball.check_overlap(self.balls):
                    self.balls.append(new_ball)
                    break

    def draw(self):
        #Draw walls
        self.canvas.create_line((self.min_x, self.min_y), (self.min_x, self.max_y), fill = "red")
        self.canvas.create_line((self.min_x, self.min_y), (self.max_x, self.min_y), fill = "red")
        self.canvas.create_line((self.min_x, self.max_y), (self.max_x, self.max_y), fill = "red")
        self.canvas.create_line((self.max_x, self.min_y), (self.max_x, self.max_y), fill = "red")
        #Draw balls        
        for b in self.balls:
            obj = self.canvas.create_oval(b.x - b.radius, b.y - b.radius, b.x + b.radius, b.y + b.radius)
            self.ball_handles[b] = obj
        self.canvas.update()

    def next_wall_collision_idx(self):
        collided = []
        for i in np.arange(self.num_balls):
            if self.wall_collision_times[i] <= self.time:
                collided.append(i)
        return collided

    def next_ball_collision_idx(self):
        min_i = 0
        min_j = 0
        collided = []
        # min_tij = float('inf')
        for i in np.arange(self.num_balls):
            for j in np.arange(i, self.num_balls):
                tij = self.ball_collision_times[i][j]
                if tij <= self.time:
                    collided.append((i, j))
        return collided 
        
    #CODE YOU NEED TO IMPLEMENT
    def init_wall_collision_times(self):
        for i in np.arange(self.num_balls):
            self.wall_collision_times[i]= self.balls[i].compute_wall_collision_time(self, self.min_x, self.max_x, self.min_y, self.max_y)
          

#    def update_wall_collision_time(self, i):
#
    def init_ball_collision_times(self):
        for i in np.arange(self.num_balls):
            for j in np.arange(self.num_balls):
                self.ball_collision_times[i] = self.balls[i].compute_ball_collision_time(self, other)
#
#    def update_ball_collision_time(self, i):


        
    #Do not update this 
    def refresh(self):
        wall_i = self.next_wall_collision_idx()
        ball_i = self.next_ball_collision_idx()
        # print wall_i, ball_i
        for i in wall_i:
            bi = self.balls[i]
            old_x = bi.x
            old_y = bi.y
            bi.collide_with_wall(self.min_x, self.max_x, self.min_y, self.max_y)
            self.canvas.move(self.ball_handles[bi], bi.x - old_x, bi.y - old_y)

        for (i,j) in ball_i:
            bi = self.balls[i]
            bj = self.balls[j]
            bi.collide_with_ball(bj)

        collided = wall_i
        for (i, j) in ball_i:
            collided.append(i)
            collided.append(j)

        collided = set(collided)
        # print collided
        
        for i in collided:
            self.update_ball_collision_time(i)
            self.update_wall_collision_time(i)

        not_collided = set(np.arange(self.num_balls)) - collided
        
        for i in not_collided:
            bi = self.balls[i]
            old_x = bi.x
            old_y = bi.y
            bi.move()
            self.canvas.move(self.ball_handles[bi], bi.x - old_x, bi.y - old_y)

        self.time += 1
        self.canvas.update()
        self.canvas.after(self.refresh_speed, self.refresh) #Calls the function again
                
class Ball:
    # radius is a float
    # position is a numpy array of size 2
    # velocity is a numpy array of size 2
    # mass is a float
    def __init__(self, radius, x, y, vx, vy,  mass):
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        return

    def calc_new_pos(self):
        return (self.x + self.vx, self.y + self.vy)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        return

    def check_overlap(self, others):
        for b in others:
            min_dist = b.radius + self.radius
            center_dist = math.sqrt((b.x - self.x)*(b.x - self.x) + \
                                    (b.y - self.y)*(b.y - self.y))
            if center_dist < min_dist:
                return True
        return False

    def collide_with_ball(self, other):
        # print "handing collision between:"
        # self.show_stats()
        # print " and "
        # other.show_stats()

        
        v1x = (2 * other.mass * other.vx + (self.mass - other.mass) * self.vx) / (self.mass + other.mass) 
        v1y = (2 * other.mass * other.vy + (self.mass - other.mass) * self.vy) / (self.mass + other.mass) 
        v2x = (2 * self.mass * self.vx + (self.mass - other.mass) * other.vx) / (self.mass + other.mass)
        v2y = (2 * self.mass * self.vy + (self.mass - other.mass) * other.vy) / (self.mass + other.mass)
        self.vx = v1x
        self.vy = v1y
        other.vx = v2x
        other.vy = v2y

        # self.vx = other.vy
        # self.vy = other.vx

        # other.vx = self.vy
        # other.vy = other.vx

        
        # dv_x = self.vx - other.vx
        # dv_y = self.vy - other.vy

        # dr_x = self.x - other.x
        # dr_y = self.y - other.y

        # sigma = self.radius + other.radius
        
        # dv_dr = dv_x * dr_x + dv_y * dr_y

        # J = 2.0 * self.mass * other.mass * dv_dr/((self.mass + other.mass)*sigma)
        # Jx = J * (self.x - other.x)/sigma
        # Jy = J * (self.y - other.y)/sigma
        # self.vx -= Jx/self.mass
        # self.vy -= Jy/self.mass

        # other.vx += Jx/other.mass
        # other.vx += Jx/other.mass
        # self.move()
        # other.move()

        return
    
    # Compute when the balls collide 
    # Say ball 1 is at p1 (p1 is center of the ball) with velocity v1 and ball 2 is at p2 with velocity v2.
    # After time t, ball 1 is at p1' and ball 2 is at p2'. 
    # So || p1' - p2' || = R where R is sum of radiuses of the two balls. 
    # This will result in a quadratic equation  of from ax^2 + bx +c 
    # where a = || v1 - v2 ||^2
    # b = (v1 - v2)^T (p1- p2)
    # c = || p1 - p2 ||^2  -  R^2

    def compute_ball_collision_time(self, other):
        delta_t = float("inf")
        
        dr_x = self.x - other.x
        dr_y = self.y - other.y
        
        dv_x = self.vx - other.vx
        dv_y = self.vy - other.vy

        dv_dv = dv_x * dv_x + dv_y * dv_y
        dr_dr = dr_x * dr_x + dr_y * dr_y
        dv_dr = dv_x * dr_x + dv_y * dr_y
        sigma = self.radius + other.radius

        d = dv_dr * dv_dr - dv_dv * (dr_dr - sigma * sigma) 
        
        # No solution 
        if dv_dr >= 0 or d < 0:
            return delta_t
        
        sol1 = (np.sqrt(d) - dv_dr)/dv_dv
        sol2 = (-np.sqrt(d) - dv_dr)/dv_dv
        if sol1 > 0 and sol2 > 0:
            delta_t = min(sol1, sol2)
        elif sol1 > 0:
            delta_t = sol1
        elif sol2 > 0:
            delta_t = sol2
        return delta_t
        # ax = self.x + self.vx * delta_t
        # ay = self.y + self.vy * delta_t

        # bx = other.x + other.vx * delta_t
        # by = other.y + other.vy * delta_t

        # c = (ax - bx)*(ax -bx) + (ay - by) *(ay - by)
        # assert(abs(c - sigma * sigma) < 1e-5)
    
    
    def collide_with_wall(self, min_x, max_x, min_y, max_y):
        self.move()
        if self.x - self.radius <= min_x:
            self.vx = -self.vx
            self.x = min_x + self.radius
            
        if self.radius + self.x >= max_x:
            self.vx = -self.vx
            self.x = max_x - self.radius 
            
        if self.y - self.radius <= min_y:
            self.vy = -self.vy
            self.y = min_y + self.radius

        if self.radius + self.y >= max_y:
            self.vy = -self.vy
            self.y = max_y - self.radius

        return

    def compute_wall_collision_time(self, min_x, max_x, min_y, max_y):
        delta_t = float("inf")
        
        # x + delta_t * vx = min_x + radius
        a = (min_x + self.radius - self.x)/(1.0*self.vx)
        if a >= 0 and a < delta_t:
            delta_t = a

        # x + delta_t * vx = max_x - radius
        b = (max_x - self.radius - self.x)/(1.0*self.vx)
        if b >= 0 and b < delta_t:
            delta_t = b

        # y + delta_t * vy = min_y + radius
        c = (min_y + self.radius - self.y)/(1.0*self.vy)
        if c >= 0 and c < delta_t:
            delta_t = c
        
        # y + delta_t * vy = max_y - radius
        d = (max_y - self.radius - self.y)/(1.0*self.vy)
        if d >= 0 and d < delta_t:
            delta_t = d
        
        return delta_t
        
    def show_stats(self):
        print ("radius: ", self.radius)
        print ("position: ", self.x, self.y)
        print ("velocity: ", self.vx, self.vy)
        print ("mass: ", self.mass)
        return

    
# # if __name__ == "__main__":
    
height = 600
width = 800
offset = 5
max_radius = 10
min_radius = 10
num_balls = 5
refresh_speed = 1
rand.seed(12394)
root = Tk()
p = Painter(root, width, height, offset, min_radius, max_radius, num_balls, refresh_speed)
root.mainloop()

