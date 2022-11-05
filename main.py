'''
2D pixelart What-If-Demake of the Mario Party 6 minigame Memory Lane (https://mario.fandom.com/wiki/Memory_Lane).

Imagine Nintendo's Super Mario IP would have been heavily influenced by the 1993 theatrical movie Super Mario Bros.
(https://en.wikipedia.org/wiki/Super_Mario_Bros._(film)) and the Mario Party games would more be like a kind of
violent battle royal as seen in the 1987 movie The Running Man (https://en.wikipedia.org/wiki/The_Running_Man_(1987_film)).

Code and graphics by Kevin Spathmann (Pfeifenreiniger at GitHub: https://github.com/Pfeifenreiniger)

Fonts used:
    Masheen from fontsov.com (https://fontsov.com/font/masheen21695.html)
    Dirtchunk from Priotitype (https://www.fontspace.com/dirtchunk-font-f56491)

Musics, SFX, and voices used:
    Music...
        Main Menu:  Cyberpunk 2077 - Chippin' In by SAMURAI (8-bit cover by tonythehero)
        Stage:      Aim To Head - Heroez
                    (alternatively after entering the 'Konami Code' in Press Space screen: Mario Party 6 - Slow and Steady (8-bit cover) (made with GXSCC))
        Ranking:    FainGames - Cyberpunk 8-bit Relaxing Music
    SFX...
        Menus and Stage:    Various sound files from the sfx library provided by SubspaceAudio at OpenGameArt.org (https://opengameart.org/content/512-sound-effects-8-bit-style)

Original Game (included in Mario Party 6) by Hudson Soft™ and Nintendo™
'''

import pygame, sys, random, gc
pygame.init()

##----------------------------DISPLAY SCREEN----------------------------##

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Memory Lane 2D What-If-Demake")
ICON = pygame.image.load("graphics/icon.png").convert_alpha()
pygame.display.set_icon(ICON)
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

        from menu import PressSpace, MenuScreen

        from versus_screen import VersusScreen
        from stage import Stage, ShyGuy
        from player import Player
        from camera import Camera

        #----loading music----#
        menu_music = pygame.mixer.Sound("music/menu/Cyberpunk 2077 - Chippin’ In by SAMURAI (8-bit cover by tonythehero).wav")
        menu_music.set_volume(1)
        menu_music_to_play = True
        menu_music_started = False

        stage_music_1 = pygame.mixer.Sound("music/stage/Aim To Head - Heroez.wav")
        stage_music_1.set_volume(0.8)
        stage_music_2 = pygame.mixer.Sound("music/stage/Mario Party 6 - Slow and Steady (8-bit cover).WAV")
        stage_music_2.set_volume(0.8)
        stage_music_to_play = False
        stage_music_started = False

        ranking_music = pygame.mixer.Sound("music/ranking/FainGames - Cyberpunk 8-bit Relaxing Music.wav")
        ranking_music.set_volume(1)
        ranking_music_to_play = False
        ranking_music_started = False

        #----loading objects----#
        menu_screen = MenuScreen()
        menu_press_space = PressSpace(menu_screen)

        shyguy = ShyGuy()
        canvas = pygame.Surface((800, 600))
        stage0 = Stage(0, canvas)
        stage1 = Stage(1, canvas)
        stage2 = Stage(2, canvas)
        stage3 = Stage(3, canvas)
        stage4 = Stage(4, canvas)
        stage_objects = [stage1, stage2, stage3, stage4]

        ingame_objects_loaded = False

        def load_ingame_objects():
            """Ingame objects which could change after a game restart. Therefore, a function to (re)load them."""
            players = menu_screen.players
            vs_screen = VersusScreen(players)

            player1 = Player(players[0], 1, False)
            player2 = Player(players[1], 2, False) if menu_screen.numb_of_players > 1 else Player(players[1], 2, True)
            player3 = Player(players[2], 3, False) if menu_screen.numb_of_players > 2 else Player(players[2], 3, True)
            player4 = Player(players[3], 4, False) if menu_screen.numb_of_players > 3 else Player(players[3], 4, True)
            player_objects = [player1, player2, player3, player4]

            camera1 = Camera(stage1, player1)
            camera2 = Camera(stage2, player2)
            camera3 = Camera(stage3, player3)
            camera4 = Camera(stage4, player4)

            return vs_screen, player_objects, camera1, camera2, camera3, camera4

        def delete_objects(*objects):
            for obj in objects:
                del obj

        correct_tiles_reset = False

        player_end_position = []

        running = True

        # gameloop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gc.collect()
                    pygame.quit()
                    sys.exit()

            # music control
            if menu_music_to_play and menu_music_started != True:
                menu_music.play(loops=-1)
                menu_music_started = True
            elif stage_music_to_play and stage_music_started != True:
                menu_music.stop()
                if menu_press_space.konami_code:
                    stage_music_2.play(loops=-1)
                else:
                    stage_music_1.play(loops=-1)
                stage_music_started = True
            elif ranking_music_to_play and ranking_music_started != True:
                if menu_press_space.konami_code:
                    stage_music_2.stop()
                else:
                    stage_music_1.stop()
                ranking_music.play(loops=-1)
                ranking_music_started = True

            # first start: press select screen
            if menu_press_space.screen_done != True:
                menu_press_space.update()
            else:
                # menu screens:  numb_of_players > player select > controls
                menu_screen = menu_press_space.menu_screen
                menu_screen.start_menu_pane_animation = True
                if menu_screen.screen_done != True:
                    menu_screen.update()
                    if menu_screen.restart_game:
                        ranking_music_to_play = False
                        ranking_music.stop()
                        running = False
                        delete_objects(vs_screen, player_objects, camera1, camera2, camera3, camera4, menu_screen, menu_press_space, shyguy, canvas, stage0, stage1, stage2, stage3, stage4, stage_objects)
                        gc.collect()
                        Main.run_game()
                else:
                    if ingame_objects_loaded != True:
                        vs_screen, player_objects, camera1, camera2, camera3, camera4 = load_ingame_objects()
                        ingame_objects_loaded = True

                    if vs_screen.screen_done != True:
                        vs_screen.update()
                    else:
                        menu_music_to_play = False
                        stage_music_to_play = True
                        # let shyguy walk across the generated path until he arrives tile 51
                        if len(shyguy.my_path) < 1 or shyguy.my_path[-1] != 51:
                            stage0.draw_elements()
                            stage0.get_correct_tiles(shyguy.my_path)
                            shyguy.update()
                        else:
                            # resets the display of correct path tiles on the stages and transfers the path to the player
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

                            # checking if a player reached the last tile -> if yes, add him to the position list
                            for p in player_objects:
                                if p.my_tile_path[-1] == 51 and p.pnum not in player_end_position:
                                    player_end_position.append(p.pnum)
                            # if all 4 players arrived the goal (tile 51) > game ends
                            if len(player_end_position) >= 4:

                                menu_screen.current_screen = "positions"
                                menu_screen.menu_pane_direct = "on"
                                menu_screen.load_player_positions(player_end_position)
                                menu_screen.screen_done = False
                                stage_music_to_play = False
                                ranking_music_to_play = True

            pygame.display.set_caption("Memory Lane 2D What-If-Demake | " + str(round(clock.get_fps())) + " FPS")
            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    Main.run_game()