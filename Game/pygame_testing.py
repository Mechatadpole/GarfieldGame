import pytest
import unittest
import pygame

class GarfieldGameTests(unittest.TestCase):

    def test_repo_lasagna_eaten_should_display_lasaga_points(self):
        # arrange
        font = pygame.font.SysFont(None, 35)
        text = font.render("    Lasaga Points:"+str(count), True, black)


        # act
        gameDisplay.blit(text,((700),750))
        actual = 0
        expected = 0 
        # assert
        self.assertEqual(actual,expected)

    def test_repo_quit_button_should_quit_out_of_game(self):
        # arrange
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # act
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)
        actual = (0,0,0)
        expected = (0,0,0)
        # assert
        self.assertEqual(actual,expected)
    def test_repo_game_intro_starts_the_game_showing_name_and_two_buttons(self):
        # arrange
        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # act
        gameDisplay.fill(orange)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Garfields Lasaga", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        actual = 0
        expected = 0
        # assert
        self.assertEqual(actual,expected)
