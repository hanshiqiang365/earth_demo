#author: hanshiqiang365 （微信公众号：韩思工作室）

import pygame
import math
import sys

def sign(a):
   return (a > 0) - (a < 0)

black = 0, 0, 0
white = 255, 255, 255

k = 1e7            # 距离缩放参数
m = 5.9742e24      # 地球质量
M = 1898.7e27      # 木星质量
G = 6.67259e-17    # 万有引力常量
t = 1e5            # 时间缩放参数

pos_x= 0           # 地球坐标
pos_y= 400
earth = pos_x, pos_y
vel_x= 80          # 地球速度
vel_y= 60
jupiter = 700, 300 # 木星坐标
v_j = 3            # 木星速度

pygame.init()

demoIcon = pygame.image.load("demo_icon.png")
pygame.display.set_icon(demoIcon)

pygame.mixer.init()
pygame.mixer.music.load("demo_bgm.wav")
pygame.mixer.music.play(-1)

screen= pygame.display.set_mode((1130, 600))
font = pygame.font.Font('zhaozi.ttf', 30)
text = font.render("《流浪地球》电影——木星引力弹弓模拟示意图 - 韩思工作室", 1, white)
pygame.display.set_caption("Wanderring Earth - Slingshot Demo - developed by hanshiqiang365")

e = pygame.image.load("earth.png").convert_alpha()
j = pygame.image.load("jupiter.png").convert_alpha()

clock = pygame.time.Clock()

enablemovement = False

while True:
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         enablemovement = bool(1-enablemovement)
      if event.type == pygame.QUIT:
         sys.exit()

   if enablemovement:
      screen.fill(black)

      jupiter = jupiter[0] - v_j, jupiter[1]
      screen.blit(j, jupiter)

      delta_x = (jupiter[0] - earth[0]) * k
      delta_y = (jupiter[1] - earth[1]) * k

      r2 = delta_x ** 2 + delta_y ** 2
      F = G * m * M / r2
      theta = math.acos(delta_x / r2 ** 0.5)

      fx = abs(F * math.cos(theta)) * sign(delta_x)
      fy = abs(F * math.sin(theta)) * sign(delta_y)

      ax = fx / m
      ay = fy / m

      vel_x += ax * t
      vel_y += ay * t

      pos_x += vel_x * t / k
      pos_y += vel_y * t / k
      earth = int(pos_x), int(pos_y)
      screen.blit(e, earth)
      
      v = '地球速度 %.2f km/s' % ((vel_x ** 2 + vel_y ** 2) ** 0.5)
      speed = font.render(v, 1, white)
      screen.blit(text, (150, 100))
      screen.blit(speed, (200, 50))
      pygame.display.update()

   clock.tick(20)
