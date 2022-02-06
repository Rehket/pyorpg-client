import pygame
import os

import global_vars as g

class ResourceManagerClass():
    def __init__(self):
        self.backgrounds = []
        self.plrSprites = []
        self.tileSprites = []
        self.itemSprites = []
        self.spellSprites = []

    def getAmountOfFiles(self, folder, fileExtension):
        return sum(
            bool(file.endswith(fileExtension))
            for file in os.listdir(f'{g.dataPath}/{folder}')
        )

    def loadImage(self, image):
        if image.endswith('.bmp'):
            tempImage = pygame.image.load(image).convert()
            tempImage.set_colorkey((0, 0, 0)) # set black color to transparent
            return tempImage

        elif image.endswith('.png'):
            return pygame.image.load(image).convert_alpha()

    def loadEverything(self):
        self.loadPlrSprites()
        self.loadItems()
        self.loadSpells()

    def loadPlrSprites(self):
        amount = self.getAmountOfFiles('sprites', '.png')

        for i in range(amount):
            try:
                self.plrSprites.append(
                    self.loadImage(f'{g.dataPath}/sprites/' + str(i) + '.png')
                )

            except:
                break

    def loadItems(self):
        amount = self.getAmountOfFiles('items', '.png')

        for i in range(amount):
            try:
                self.itemSprites.append(
                    self.loadImage(f'{g.dataPath}/items/' + str(i) + '.png')
                )

            except:
                break

    def loadSpells(self):
        amount = self.getAmountOfFiles('spells', '.bmp')

        for i in range(amount):
            try:
                self.spellSprites.append(
                    self.loadImage(f'{g.dataPath}/spells/' + str(i) + '.bmp')
                )


            except:
                break


ResourceManager = ResourceManagerClass()