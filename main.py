'''
2D pixelart what-if demake of the Mario Party 6 minigame Memory Lane (https://mario.fandom.com/wiki/Memory_Lane).

Imagine Nintendo's Super Mario IP would have been heavily influenced by the 1993 theatrical movie Super Mario Bros.
(https://en.wikipedia.org/wiki/Super_Mario_Bros._(film)) and the Mario Party games would more be like a kind of
violent battle royal as seen in the 1987 movie The Running Man (https://en.wikipedia.org/wiki/The_Running_Man_(1987_film)).

Code and graphics by Kevin Spathmann (Pfeifenreiniger on GitHub: https://github.com/Pfeifenreiniger)
Fonts used: Masheen from fontsov.com (https://fontsov.com/font/masheen21695.html)
Musics, SFX, and voices used ????
Original Game (included in Mario Party 6) by Hudson Soft™ and Nintendo™
'''

import pygame, sys, random
pygame.init()

##----------------------------DISPLAY SCREEN----------------------------##

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Memory Lane 2D What-If-Demake")
#TODO: Create an icon
# ICON = pygame.image.load("graphics/game_icon.png").convert_alpha()
# pygame.display.set_icon(ICON)
clock = pygame.time.Clock()
FPS = 30


##----------------------------MAIN CLASS----------------------------##

class Main:

    @staticmethod
    def draw_4_way_split_screen_lines():
        pygame.draw.line(SCREEN, (21, 21, 21), (400, 0), (400, 800), 5)
        pygame.draw.line(SCREEN, (21, 21, 21), (0, 300), (800, 300), 5)

    ##---------MAIN METHOD---------##
    @staticmethod
    def run_game():

        from versus_screen import VersusScreen
        from stage import Stage, ShyGuy
        from player import Player
        from camera import Camera

        players = ["mar", "yos", "pea", "lui"]
        vs_screen = VersusScreen(players)
        canvas = pygame.Surface((800, 600))
        stage0 = Stage(0, canvas)
        stage1 = Stage(1, canvas)
        stage2 = Stage(2, canvas)
        stage3 = Stage(3, canvas)
        stage4 = Stage(4, canvas)
        stage_objects = [stage1, stage2, stage3, stage4]

        player1 = Player(players[0], 1, False)
        player2 = Player(players[3], 2, False)
        player3 = Player(players[2], 3, False)
        player4 = Player(players[3], 4, False)
        player_objects = [player1, player2, player3, player4]
        shyguy = ShyGuy()

        camera1 = Camera(stage1, player1)
        camera2 = Camera(stage2, player2)
        camera3 = Camera(stage3, player3)
        camera4 = Camera(stage4, player4)

        correct_tiles_reset = False

        running = True

        # gameloop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            if vs_screen.screen_done != True:
                vs_screen.update()
            else:
                # let shyguy walk across the generated path until he arrives tile 51
                if len(shyguy.my_path) < 1 or shyguy.my_path[-1] != 51:
                    stage0.draw_elements()
                    stage0.get_correct_tiles(shyguy.my_path)
                    shyguy.update()
                else:
                    # resets the display of correct path tiles on the stage and transfers the path to the player
                    if correct_tiles_reset != True:
                        stage0.correct_tiles = []

                        for p in player_objects:
                            p.correct_tile_path = shyguy.my_path

                        correct_tiles_reset = True

                    camera1.draw()
                    camera2.draw()
                    camera3.draw()
                    camera4.draw()

                    counter = 0
                    for s in stage_objects:
                        s.get_correct_tiles(player_objects[counter].my_tile_path)
                        counter += 1

                    Main.draw_4_way_split_screen_lines()
                    # stage0.get_correct_tiles(player1.my_tile_path)

            pygame.display.set_caption("Memory Lane 2D What-If-Demake | " + str(round(clock.get_fps())) + " FPS")
            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    Main.run_game()