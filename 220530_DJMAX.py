import random

a = input("name :" )
print("welcome" + " a")

bg = []
point = 0
hl1 = False
hl2 = False
hl3 = False
hl4 = False

box(size = vec(41,182,1))
for i in range(4):
    bg.append(box(pos = vec(-15+10*i,0,2),size = vec(9,180,1),color = vec(0.5,0.5,0.7)))

bx1 = vec(-15,90,2)
bx2 = vec(-5,90,2)
bx3 = vec(5,90,2)
bx4 = vec(15,90,2)
count = 0

while True:
    rate(100)
    count += 1
    if count%20 == 0:
        m = random.randint(1,4)
        if  m == 1:
            ball1 = sphere(pos = bx1,size = vec(9,9,9), color = color.blue)
            for j in range(180):
                ka = keysdown()
                rate(400)
                ball1.pos.y -= 1
                if 'd' in ka:
                    hl1 = True
                    bg[0].color = color.purple
                    rate(50)
                    bg[0].color = vec(0.5,0.5,0.7)
                    ball1.visible = False
            ball1.visible = False
            if hl1 == False:
                point -= 1
            if hl1 == True:
                point += 1
            hl1 = False
            print("point : "+point)
        if  m == 2:
            ball2 = sphere(pos = bx2,size = vec(9,9,9), color = color.blue)
            for j in range(180):
                kb = keysdown()
                rate(400)
                ball2.pos.y -= 1
                if 'f' in kb:
                    hl2 = True
                    bg[1].color = color.purple
                    rate(50)
                    bg[1].color = vec(0.5,0.5,0.7)
                    ball2.visible = False  
            ball2.visible = False
            if hl2 == False:
                point -= 1
            if hl2 == True:
                point += 1
            hl2 = False
            print("point : "+point)
        if  m == 3:
            ball3 = sphere(pos = bx3,size = vec(9,9,9), color = color.blue)
            for j in range(180):
                kc = keysdown()
                rate(400)
                ball3.pos.y -= 1
                if 'k' in kc:
                    hl3 = True
                    bg[2].color = color.purple
                    rate(50)
                    bg[2].color = vec(0.5,0.5,0.7)
                    ball3.visible = False
            ball3.visible = False
            if hl3 == False:
                point -= 1
            if hl3 == True:
                point += 1
            hl3 = False
            print("point : "+point)
        if  m == 4:
            ball4 = sphere(pos = bx4,size = vec(9,9,9), color = color.blue)
            for j in range(180):
                kd = keysdown()
                rate(400)
                ball4.pos.y -= 1
                if 'l' in kd:
                    hl4 = True
                    bg[3].color = color.purple
                    rate(50)
                    bg[3].color = vec(0.5,0.5,0.7)
                    ball4.visible = False
            ball4.visible = False  
            if hl4 == False:
                point -= 1
            if hl4 == True:
                point += 1
            hl4 = False
            print("point : "+point)
