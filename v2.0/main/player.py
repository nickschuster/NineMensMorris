import pygame

class Player:
    # Phase identifiers
    PLACEMENT_PHASE = 0
    MOVING_PHASE = 1
    ROVING_PHASE = 2

    def __init__(self, number, sprite):
        self.number = number
        self.phase = self.PLACEMENT_PHASE
        self.numPieces = 0
        self.lost = False
        self.sprite = sprite
        self.oldMills = [[]]

    # Updates the phase of the player.
    #
    # Returns nothing.
    def updatePhase(self, phase=-1):
        if self.numPieces <= 3:
            self.phase = self.ROVING_PHASE
        elif phase != -1:
            self.phase = phase

    # Updates the win state of the player.
    #
    # Returns nothing.
    def checkWin(self):
        if self.numPieces <= 2 and self.phase == self.ROVING_PHASE:
            self.lost = True
