from graph import *


def up():
    sky()
    sun()
    cloud()


def cloud(x=100, y=50):
    brushColor(255, 255, 255)
    penSize(1)
    penColor(0, 0, 0)
    for i in range(7):
        if i % 2 == 0:
            temp = y
        else:
            temp = y-15
        circle(x, temp, 15)
        x += 11


def sky():
    penSize(0)
    brushColor(42, 178, 255)
    rectangle(0, 0, 500, 200)


def sun():
    brushColor("yellow")
    circle(420, 70, 40)


def sea():
    water()
    boat()


def boat():
    penColor("black")
    brushColor("brown")
    rectangle(250, 250, 430, 225)
    polygon(([430, 225], [430, 250], [490, 225], [430, 225]))
    brushColor("black")
    circle(443, 235, 7)
    brushColor("white")
    circle(443, 235, 5)
    brushColor("black")
    penSize(5)
    line(325, 225, 325, 125)
    penSize(1)
    brushColor(239, 222, 205)
    polygon(([325, 225], [400, 175], [350, 175], [325, 225]))
    polygon(([325, 125], [400, 175], [350, 175], [325, 125]))


def water():
    brushColor("blue")
    rectangle(0, 200, 500, 300)


def beach():
    sand()
    umb()


def sand():
    brushColor("yellow")
    rectangle(0, 300, 500, 450)


def umb():
    penColor("orange")
    penSize(5)
    line(100, 420, 100, 250)
    penSize(0)
    brushColor("red")
    penColor("black")
    penSize(1)
    polygon(([97.5, 250], [102.5, 250], [175, 290], [25, 290], [97.5, 250]))
    penSize(1)
    penColor(0, 0, 0)
    x=300/6
    for i in range(5):
        line(100, 250, x, 290)
        x += 150/6

def main():
    up()
    sea()
    beach()


main()

run()
