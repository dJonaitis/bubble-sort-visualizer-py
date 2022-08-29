import pygame
import sys
import random

pygame.init()

width, height = 1500, 700
padding = 25
useableArea = width - padding * 2

window = pygame.display.set_mode((width, height))


originalArray = []
mainArr = []
arrLength = 75 # the amount of items in array
maxVal = 100 # the maximum value an item in the array can be
gap = 3 # gap between columns
colWidth = 10


heightMultiplier = 5 # the factor by which to multiply array valus to get the pixel value

def initArr():
    global mainArr
    for i in range(1, arrLength):
        originalArray.append(random.randrange(1, maxVal, 1))
    mainArr = originalArray
    print(originalArray)

def init():
    initArr()

    main()

def draw(index):
    window.fill((255, 255, 255))
    for i, value in enumerate(originalArray):
        left = 50 + i*colWidth + i*gap
        top = 10
        rect = pygame.Rect(left, top, colWidth, value*heightMultiplier)
        if i == index:
            pygame.draw.rect(window, (255, 0, 0), rect)
        else:
            pygame.draw.rect(window, (0, 0, 0), rect)

    

def main():
    run = True
    start = False

    while run:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                start = True

        # sorting
        if start:
            for i in range(len(mainArr) - 1):
                swapped = False
                for j in range(len(mainArr) - i - 1):
                    if mainArr[j] > mainArr[j + 1]:
                        swapped = True
                        temp = mainArr[j]
                        mainArr[j] = mainArr[j + 1]
                        mainArr[j + 1] = temp
                    pygame.time.delay(60)
                    draw(j)
                    pygame.display.update()

                if  not swapped: 
                    break
        
        pygame.display.update()
        draw(None)
            

init()