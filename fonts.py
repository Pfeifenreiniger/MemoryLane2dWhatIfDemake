

from main import pygame

# used fonts
# masheen
FONT_MASHEEN_30 = pygame.font.Font("fonts/masheen/masheen.ttf", 30)
FONT_MASHEEN_BOLD_40 = pygame.font.Font("fonts/masheen/masheen_bold.ttf", 40)

# press start
FONT_PRESS_START_20 = pygame.font.Font("fonts/PressStart2P-vaV7.ttf", 20)
FONT_PRESS_START_30 = pygame.font.Font("fonts/PressStart2P-vaV7.ttf", 30)


# font-outline function
# made by sloth (https://stackoverflow.com/questions/54363047/how-to-draw-outline-on-the-fontpygame)

_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(255, 255, 255), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf