size(1000,1000)
background(0)
stroke(255)
strokeWeight(3)

#Four Blocks

line(400,0,400,400)
line(0,400,400,400)
line(600,0,600,400)
line(1000,400,600,400)
line(0,600,400,600)
line(400,1000,400,600)
line(600,600,1000,600)
line(600,600,600,1000)

#Roads margin
for x in range(0,450,100):
    line(500,x,500,x+50);

for x in range(0,450,100):
    line(x,500,x+50,500);

for x in range(0,450,100):
    line(500,1000-x,500,1000-x-50);

for x in range(0,450,100):
    line(1000-x,500,1000-x-50,500);
    

#Signals
x1=300
y1=350
ellipseMode(CENTER)
rectMode(CENTER)
noFill()
rect(x1,y1,120,20)
rect(x1,y1-20,80,20)
rect(x1,y1-90,30,120)
rect(x1,y1-230,90,160)
fill(255,0,0)
ellipse(x1,y1-270,30,30)
fill(0)
ellipse(x1,y1-230,30,30)
ellipse(x1,y1-190,30,30)

x1=700
y1=350
rectMode(CENTER)
noFill()
rect(x1,y1,120,20)
rect(x1,y1-20,80,20)
rect(x1,y1-90,30,120)
rect(x1,y1-230,90,160)
fill(255,0,0)
ellipse(x1,y1-270,30,30)
fill(0)
ellipse(x1,y1-230,30,30)
ellipse(x1,y1-190,30,30)

x1=300
y1=950
rectMode(CENTER)
noFill()
rect(x1,y1,120,20)
rect(x1,y1-20,80,20)
rect(x1,y1-90,30,120)
rect(x1,y1-230,90,160)
fill(255,0,0)
ellipse(x1,y1-270,30,30)
fill(0)
ellipse(x1,y1-230,30,30)
ellipse(x1,y1-190,30,30)

x1=700
y1=950
rectMode(CENTER)
noFill()
rect(x1,y1,120,20)
rect(x1,y1-20,80,20)
rect(x1,y1-90,30,120)
rect(x1,y1-230,90,160)
fill(0)
ellipse(x1,y1-270,30,30)
ellipse(x1,y1-230,30,30)
fill(0,255,0)
ellipse(x1,y1-190,30,30)


#Cars
x1=300
y1=450
fill(100,20,150)
stroke(100,20,150)
rect(x1,y1,100,50)
stroke(0)
strokeWeight(1.5)
rect(x1,y1,50,25)
fill(0)
rect(x1-25,y1,15,30)
rect(x1+25,y1,15,40)

x1=650
y1=550
fill(100,250,200)
stroke(100,20,150)
rect(x1,y1,100,50)
stroke(0)
strokeWeight(1.5)
rect(x1,y1,50,25)
fill(0)
rect(x1-25,y1,15,30)
rect(x1+25,y1,15,40)

x1=450
y1=650
fill(255,0,0)
stroke(100,20,150)
rect(x1,y1,50,100)
stroke(0)
strokeWeight(1.5)
rect(x1,y1,25,50)
fill(0)
rect(x1,y1-25,40,15)
rect(x1,y1+25,30,15)

x1=550
y1=700
fill(0,255,0)
stroke(100,20,150)
rect(x1,y1,50,100)
stroke(0)
strokeWeight(1.5)
rect(x1,y1,25,50)
fill(0)
rect(x1,y1-25,40,15)
rect(x1,y1+25,30,15)

x1=450
y1=850
fill(0,0,255)
stroke(100,20,150)
rect(x1,y1,50,100)
stroke(0)
strokeWeight(1.5)
rect(x1,y1,25,50)
fill(0)
rect(x1,y1-25,40,15)
rect(x1,y1+25,30,15)

x1=550
y1=830
fill(255,255,0)
stroke(100,20,150)
rect(x1,y1,50,100)
stroke(0)
strokeWeight(1.5)
rect(x1,y1,25,50)
fill(0)
rect(x1,y1-25,40,15)
rect(x1,y1+25,30,15)

f = createFont("Arial", 16, True)
textFont(f,22)
fill(255)
text("Pratik Chaudhary",10,800)
text("18115059",10,830)
textFont(f,18)
text("Computer Graphics Term Project",10,860)
