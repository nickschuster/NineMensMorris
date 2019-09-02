#draws all game assets and handels all pygame logic
import pygame
from board import Board
from piece import Piece

pygame.init();

gameWidth = 750;
gameHeight = 750;

black = (0,0,0);
white = (255,255,255);
red = (255, 0, 0);

win = False;

phase = 1;

display = pygame.display.set_mode((gameHeight, gameWidth));

pygame.display.set_caption('Nine Men\'s Morris');

boardImg = pygame.image.load("../assets/ninemensboard.png");
whitePiece = pygame.image.load("../assets/whitepiece.png");
blackPiece = pygame.image.load("../assets/blackpiece.png");

display.blit(boardImg, (0,0));

clock = pygame.time.Clock();

gameBoard = Board();

def updateBoard(): 

	for piece in gameBoard.Pieces:
		pos = gameBoard.XYPoints[piece.location];
		if(piece.color == "white"):
			display.blit(whitePiece, (pos[0] - 25,pos[1] - 25));
		else:
			display.blit(blackPiece, (pos[0] - 25,pos[1] - 25));

	pygame.display.flip();

def placePiece(turn, placement):
	i = 0
	mouseX, mouseY = placement
	for pos in gameBoard.XYPoints:
		if ((mouseX <= pos[0]+10 and mouseX >= pos[0]-10) and 
			(mouseY <= pos[1]+10 and mouseY >= pos[1]-10)):
			newPiece = Piece(turn, i);
			gameBoard.Pieces.append(newPiece)
			valid = True;
			break;
		else: 
			valid = False;

		i = i + 1;
	return valid;



def main():
	turn = "white"
	while not win:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit();
				quit();
			elif(event.type) == pygame.MOUSEBUTTONDOWN:
				if(event.button == 1):
					if(phase == 1):
						if(placePiece(turn, event.pos)):
							if(turn == "white"):
								turn = "black";
							else:
								turn = "white";

			updateBoard();

			clock.tick(60);

main();
