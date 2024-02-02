import time
import os
import math
import threading
import random
from playsound import playsound
import pygame
from pygame.locals import *
import random
import librosa

import wave
import numpy as np
import soundfile
from scipy.io.wavfile import read
import sounddevice as sd
pygame.init()
 

wall = os.path.dirname(__file__) + '\WallBounce.wav'
Ch = os.path.dirname(__file__) + '\Ch.wav'
Dh = os.path.dirname(__file__) + '\Dh.wav'
Eh = os.path.dirname(__file__) + '\Eh.wav'
Fh = os.path.dirname(__file__) + '\Fh.wav'
Gh = os.path.dirname(__file__) + '\Gh.wav'
Ah = os.path.dirname(__file__) + '\Ah.wav'
Bh = os.path.dirname(__file__) + '\Bh.wav'
Ch2 = os.path.dirname(__file__) + '\Ch2.wav'
frame = os.path.dirname(__file__) + '\Frame.wav'
bounces = 0
brg = 0
playsound(Ch)
playsound(Ch)
playsound(Ch)
playsound(Ch)
playsound(Ch)


def wally():
          global brg
          dfgkjdgib = brg -2
          loops = (dfgkjdgib % 8)
          if loops == 0:
               playsound(Ch)
          elif loops == 1:
               playsound(Dh)
          elif loops == 2:
               playsound(Eh)
          elif loops == 3:
               playsound(Fh)
          elif loops == 4:
               playsound(Gh)
          elif loops == 5:
               playsound(Ah)
          elif loops == 6:
               playsound(Bh)
          elif loops == 7:
               playsound(Ch2)
          
          #yeg, sr = librosa.load(wall)
          #steps = float(loops)    
          #new_y = librosa.effects.pitch_shift(yeg, sr=sr, n_steps=steps)
          #soundfile.write("pitchShifted"+str(loops)+".wav", sr,new_y,)
          #wallnew = os.path.dirname(__file__) + "pitchShifted"+str(loops)+".wav"
          
          return
def framy():
            playsound(frame)
            return

g = 9.81

#bounciness
b = 1.015

#x(v1) and y(v2) velocity
v1 = 8
v2 = 1


v0 = math.sqrt(v1 * v1 + v2 * v2)

v0m = 1000
v3 = v1 / v0
v4 = v2 / v0
vx = 1
if v1 == 0.001 and v2 == 0.001:
     v0 = 0
     v3 = 0
     v4 = -1

t = 0
tmax = 100

#fps             vvv
tstep = 1 /    50


bounces = 1000000
maxbounces = bounces + 1
counter = 1

x0 = round((0.5 * v3 * t * t) + (t * v3 * v0))
y0 = round((0.5 * (v4 - g) * t * t) + (t * v4 * v0))

#starting position
x = 10.0001
y = 2

yresolution = 20
xresolution = 20
resmult = 12


sizemult = 1
size = 1


#enable air resistance
ar = False
tail = "  "



select = False
if select == True:
     v1 = float(input("X Velocity: "))
     v2 = float(input("Y Velocity: "))
     b = float(input("Bounciness: "))
     x = int(input("X Start Coord: "))
     y = int(input("Y Start Coord: "))
     tstep = 1 / int(input("Fps: "))
     bounces = int(input("Bounces: "))
     maxbounces = bounces + 1
     if input("Enable Trail (Y/N): ") == "Y":
        tail = " ."
     else:
          tail = "  "
     if input("Enable Air Resistance (Y/N): ") == "Y":
        ar = True
     else:
          ar = False


m = 1
C = 1
r = 1
p = 1
A = 1
k = 1
e = 1




if ar == True:

    #mass
    m = 0.625

    #coefficient
    C = 0.47

    #radius
    r = 0.2426/2

    #fluid density
    p = 1.293


    #cross sectional area
    A = 3.141592653589793238462643383279502884197169399375 * r * r

    k = 0.5 * p * v0 * C * A
    e = 2.71828183

a = 1

tandb = "::::"
A45 = [1,1]

if x >= xresolution:
     x = xresolution - 1
if y >= yresolution:
     y = yresolution - 1

for tb in range(xresolution):
    tandb += "::"
row = 0
column = 0
grid = []
grid2 = []
grid_display = []
grid_display2 = ""
grid_value = ""
gridvaldisplay = []
while row != yresolution:
        globals()["column"+str(row)] = []
        grid.append(globals()["column"+str(row)])
        globals()["column2"+str(row)] = []
        grid2.append(globals()["column2"+str(row)])
        grid_display.append("")
        gridvaldisplay.append("")
        while column != xresolution:
                globals()["column"+str(row)].append(0)
                globals()["column2"+str(row)].append(0)
                column = column + 1
        globals()["column"+str(row)].append(str(row))
        globals()["column2"+str(row)].append(str(row))
        column = 0
        row = row + 1
x1 = round((0.5 * v3 * t * t) + (t * v3 * v0)) + x
y1 = round((0.5 * (v4 - g) * t * t) + (t * v4 * v0)) + y
x2 = round((0.5 * v3 * t * t) + (t * v3 * v0)) + x
y2 = round((0.5 * (v4 - g) * t * t) + (t * v4 * v0)) + y
x3 = round((0.5 * v3 * t * t) + (t * v3 * v0)) + x
y3 = round((0.5 * (v4 - g) * t * t) + (t * v4 * v0)) + y
bounces = 0
for r in range (yresolution):
    for c in range(xresolution):
          rh = (r - (yresolution / 2) + 0.5)
          ch = (c - (xresolution / 2) + 0.5)
          if ((r - (yresolution / 2) + 0.5) * (r - (yresolution / 2) + 0.5)) + ((c - (xresolution / 2) + 0.5) * (c - (xresolution / 2) + 0.5)) >= (yresolution/2)  * (yresolution/2):
               grid[r][c] = -1

engle=0.00000

window = pygame.display.set_mode((1920, 1080))
 
#yresolution * 4 * resmult

window.fill((0, 0, 0))
xdis = (1920 - yresolution * 4 * resmult) / 2
ydis = (1080 - yresolution * 4 * resmult) / 2
pygame.draw.circle(window, (255, 255, 255), 
                 [(yresolution * 2 * resmult) + xdis, (yresolution * 2 * resmult) + ydis], yresolution*2 * resmult, 4)
pygame.display.update()

red = 255
grn = 0
blu = 0
col = 0

yes = True
num = 0

xh = x
yh = y
countoor = 0
pygame.draw.circle(window, (255, 255, 255), 
                 [(yresolution * 2 * resmult) + xdis, (yresolution * 2 * resmult) + ydis], yresolution*2 * resmult, 8)
pygame.display.update()
time.sleep(1)
moolt = 1.0005
t = 0
while bounces != maxbounces and size <= yresolution + 0.5:
    brg+=1
    if brg >= 8:
         brg = 0
    #sizemult = sizemult * moolt
    moolt = (moolt -1) * 0.99 + 1
    #while ((y - (yresolution / 2)) * (y - (yresolution / 2))) + ((x - (xresolution / 2)) * (x - (xresolution / 2))) > (yresolution/2 - (0.5 * size))  * (yresolution/2 - (0.5 * size)):
                  #x += (v3 * v0) * tstep
                  #y += (v4 * v0)  * tstep
    #              x -= (x - yresolution/2) * tstep * 0.1
    #              y -= (y - yresolution/2) * tstep * 0.1
    xy = math.sqrt((x - yresolution/2) * (x - yresolution/2) + (y - yresolution/2) * (y - yresolution/2))
    xengle = ((x - yresolution/2))
    yengle = ((y - yresolution/2))
    hehe = math.tan(math.radians(45))
    #t = 0
    #v1 = -v1
    #v2 = -v2
    mm = 1
    if x > yresolution / 2 and y < yresolution / 2:
         mm = -1
    if x < yresolution / 2 and y > yresolution / 2:
         mm = -1
    #((round(math.pow(2, -(x - yresolution))) + 0.0000001)/math.sqrt((round(math.pow(2, -(x - yresolution))) + 0.0000001) * (round(math.pow(2, -(x - yresolution))) + 0.0000001)) * 180)
    engless =  math.degrees(math.atan(v2/v1))
    if engless < 0:
         engless += 360
    if v1 > 0 and v2 > 0 and engless > 90:
         engless -= 180
    if v1 < 0 and v2 > 0 and engless > 180:
         engless -= 180
    elif v1 < 0 and v2 > 0 and engless <= 90:
         engless -= 180
    if v1 < 0 and v2 < 0 and engless > 270:
         engless -= 180
    elif v1 < 0 and v2 < 0 and engless <= 180:
         engless -= 180
    if v1 > 0 and v2 < 0 and engless > 360:
         engless -= 180
    elif v1 > 0 and v2 < 0 and engless <= 270:
         engless -= 180
    engless -= 180
         
    englseee = math.degrees(math.atan(-xengle / yengle))
    engler = 2 * englseee - engless - 180
    v0 = math.sqrt(v1 * v1 + v2 * v2)
    #v3 = math.cos(math.radians(-math.degrees(math.acos(v1 / math.sqrt(v1 * v1 + v2 * v2))) - 2 * (mm * math.degrees(math.acos(yengle)) - 90) - (x - yresolution/2)))
    #v4 = math.sin(math.radians(-math.degrees(math.asin(v2 / math.sqrt(v1 * v1 + v2 * v2))) - 2 * (mm * math.degrees(math.asin(xengle)) - 90) - (y - yresolution/2)))
    #v3 = math.cos(math.radians(-math.degrees(math.acos(v1 / math.sqrt(v1 * v1 + v2 * v2))) - 2 * (mm * math.degrees(math.acos(yengle)) - 90) - (x - yresolution/2)))
    v4 = math.sin(math.radians(engler))
    v3 = math.cos(math.radians(engler))



    if num % 4 == 0:
         g3 = 0
         g = 9.81
    if num % 4 == 1:
         g3 = 9.81
         g = 0
    if num % 4 == 2:
         g3 = 0
         g = -9.81
    if num % 4 == 3:
         g3 = -9.81
         g = 0
    
    v0 = v0 * vx
    v0m = v0m * vx
    if v0 > v0m:
         v0 = v0m
    
    if v1 == 0.001 and v2 == 0.001:
     v0 = 0
     v3 = 0
     v4 = -1
    while t <= tmax:
        col += 1 / 255
        if (col - (col % 1)) % 6 == 0:
            grn += 1
        elif (col - (col % 1)) % 6 == 1:
            red -= 1
        elif (col - (col % 1)) % 6 == 2:
            blu += 1
        elif (col - (col % 1)) % 6 == 3:
            grn -= 1
        elif (col - (col % 1)) % 6 == 4:
            red += 1
        elif (col - (col % 1)) % 6 == 5:
            blu -= 1
        if red > 255:
            red = 255
        if red < 0:
            red = 0
        if blu > 255:
            blu = 255
        if blu < 0:
            blu = 0
        if grn > 255:
            grn = 255
        if grn < 0:
            grn = 0
        #window.fill((0, 0, 0))
        pygame.draw.circle(window, (0, 0, 0), 
                 [(yresolution * 2 * resmult) + xdis, (yresolution * 2 * resmult) + ydis], yresolution*2 * resmult + yresolution, 4 + yresolution)
        eckes = xh - yresolution/2
        wuiy = yh - yresolution/2
        eckesandwuiy = math.sqrt(eckes * eckes + wuiy * wuiy)
        g = 10 * (wuiy / eckesandwuiy) * (math.sqrt(math.sqrt(wuiy * wuiy)) / eckesandwuiy)
        f = 10 * (eckes / eckesandwuiy) * (math.sqrt(math.sqrt(eckes * eckes)) / eckesandwuiy)
        g=9.81
        f=0
        if ar == True:
            a = (-k / m) * math.pow(e, ((-k*t)/m)) * v0
        te = t - 0.000000001
        x0 = round((0.5 * (v3 - f) * t) + (t * v3 * v0) + x)
        y0 = round((0.5 * (v4 - g) * t * t) + (t * v4 * v0) + y)
        xh = ((0.5 * (v3 - f) * t) + (t * v3 * v0) + x)
        yh = ((0.5 * (v4 - g) * t * t) + (t * v4 * v0) + y)
        
        if x0 >= 0 and x0 <= xresolution - 1 and y0 >= 0 and y0 <= yresolution - 1 and ((yh - (yresolution / 2)) * (yh - (yresolution / 2))) + ((xh - (xresolution / 2)) * (xh - (xresolution / 2))) < (yresolution/2 - (0.5 * (size)))  * (yresolution/2 - (0.5 * (size))):
            if grid[y0][x0] == -1:
                 grid[y0][x0] = -1
            else:
                grid[y0][x0] = counter
            x1 = ((0.5 * (v3 - f) * t) + (t * v3 * v0)) + x
            y1 = ((0.5 * (v4 - g) * t * t) + (t * v4 * v0)) + y
            x2 = ((0.5 * (v3 - f) * te) + (te * v3 * v0)) + x - yresolution/2
            y2 = ((0.5 * (v4 - g) * te * te) + (te * v4 * v0)) + y - yresolution/2
            x3 = ((0.5 * (v3 - f) * t) + (t * v3 * v0)) + x - yresolution/2
            y3 = ((0.5 * (v4 - g) * t * t) + (t * v4 * v0)) + y - yresolution/2


            if size > yresolution - 2 / resmult:
                 size = yresolution - 2 / resmult
            op = 96
            rud = red/255 * op
            jrn = grn/255 * op
            blr = blu/255 * op
            cover = pygame.Surface((1920,1080))
            cover.set_alpha(int(v0))
            cover.fill((0,0,0))
            if countoor % 1 == 0:
               window.blit(cover, (0, 0))
            
            pygame.draw.circle(window, (red, grn, blu), 
                            [round(xh*4 * resmult) + xdis, round((yresolution - yh)*4 * resmult) + ydis], 2 * resmult * size, 0)
            pygame.draw.circle(window, (rud, jrn, blr), 
                            [round(xh*4 * resmult) + xdis, round((yresolution - yh)*4 * resmult) + ydis], 2 * resmult * size, 2)
            pygame.draw.circle(window, (255, 255, 255), 
                 [(yresolution * 2 * resmult) + xdis, (yresolution * 2 * resmult) + ydis], yresolution*2 * resmult, 8)
            pygame.display.update()
            #globals()["fram"+str(t)+str(bounces)] = threading.Thread(target=framy)
            #globals()["fram"+str(t)+str(bounces)].start()
            time.sleep(tstep / 12)
            row = 0
            column = 0
        else:
             
             if t > tstep * 5:
                
                        
                        vx = 1 * (math.pow(b,bounces))
                        vx = b
                        size = size * sizemult
             xhehe = ((0.5 * (v3 - f) * t) + (t * v3 * v0) + x)
             yhehe = ((0.5 * (v4 - g) * t * t) + (t * v4 * v0) + y)
             while ((yhehe - (yresolution / 2)) * (yhehe - (yresolution / 2))) + ((xhehe - (xresolution / 2)) * (xhehe - (xresolution / 2))) > (yresolution/2 - (0.5 * size))  * (yresolution/2 - (0.5 * size)):
                  t -= 0.0001
                  xhehe = ((0.5 * (v3 - f) * t) + (t * v3 * v0) + x)
                  yhehe = ((0.5 * (v4 - g) * t * t) + (t * v4 * v0) + y)
                  x1 = xhehe
                  y1 = yhehe
             bounces += 1
             x = x1
             y = y1
             v1 = ((x3 - x2)  / (0.000000001)) 
             v2 = ((y3 - y2)  / (0.000000001)) 

             if yes == True:
                  v0m = math.sqrt((v1 * v1) + (v2 * v2))
                  yes = False

             #while ((y - (yresolution / 2)) * (y - (yresolution / 2))) + ((x - (xresolution / 2)) * (x - (xresolution / 2))) < (yresolution/2 - (0.5 * size))  * (yresolution/2 - (0.5 * size)):
             #     x += (v1) * tstep * 0.2
             #     y += (v2)  * tstep * 0.2
             #while ((y - (yresolution / 2)) * (y - (yresolution / 2))) + ((x - (xresolution / 2)) * (x - (xresolution / 2))) > (yresolution/2 - (0.5 * size))  * (yresolution/2 - (0.5 * size)):
             #     x -= (v1) * tstep * 0.2
             #     y -= (v2)  * tstep * 0.2

             t = tmax
             
             
        t += tstep
        countoor += 1
        counter += 1
    t = 0
    #g = g * 1.03
    #num = random.randrange(0,5)

    globals()["wal"+str(bounces)] = threading.Thread(target=wally)
    globals()["wal"+str(bounces)].start()
    
counter = 0
while True:
    grid_display2 += (" \n" + tandb)

    for ree in range(yresolution):
        re = yresolution - ree - 1 
        for c in range(xresolution):
            if str(grid[re][c]) == str(counter):
                grid_display[re] = grid_display[re] + "##"
            elif str(grid[re][c]) == "0":
                grid_display[re] = grid_display[re] + "  "
            

            else:
                grid_display[re] = grid_display[re] + " ."
        grid_display[re] += "::"
        grid_display2 +=  " \n" + ("::" + grid_display[re])


    grid_display2 += (" \n" + tandb)

    os.system('cls')
    
    print(grid_display2)
    time.sleep(tstep / 10)
    grid_display2 = ""
    row = 0
    column = 0
    row = 0
    column = 0
    while row != yresolution:
            grid_display[row] = ""
            row = row + 1
    counter += 1