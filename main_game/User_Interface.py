def user_interface(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

#Room
text="ROOM:________"
print (bordered(text))
#Description
text="DESCRIPTION:\nYou are standing in Main Street - which used to be full of life.\nTo your left, a row of houses - now occupied by refugees that pray\nfora vaccine. There is a bin-bag with a peculiar wooden handle \nsticking out. You can go into the shop, the pub next to it or the\nalleyway. You can go west onto Herod Streator north onto Isiah Road."

print(bordered(text))

text="""
***********************************************************************************************************************************
* +----------------------+                                                                         ________+--------------------+ *
* |         x         x  |                                                x             x         |        |     x       x      | *
* |                      |__      ____________        ________________       ____________         |        |                    | *
* |                      /   \   /            \      /   WINDY PATH   \     /            \        |        |                    | *
* |      LIBRARY x     x /    \_/     ______   \____/       _______    \___/    _______   \_______|        |        LAB 2       | *
* |                      |\          /      \           x  /       \           /       \               x   /                    | *
* |                      | \________/        \____________/         \_________/         \__________        /    x               | *
* |                      |                                                                        |        |                    | *
* |  x                   |                   x                                                    |        |                    | *
* +------/\/-------------+______    +------------+         +------------+        +------------+   |        |                  x | *
* |    x                        |   |            |         |            |        |            |   |        +--------------/\/---+ *
* |        HEROD CLOSE          |   |            |         |            |        |            |   |        |                   |  *
* |            x                |   |   GARDEN   |         |   GARDEN   |        |   GARDEN   |   | ISIAH  |                   |  *
* +--------------------+        |   |            |         |            |        |            |   | ROAD   |        PARK       |  *
* |  x              x  |        | +-+------------+-+     +-+------------+-+    +-+------------+-+ |        /                   |  *
* |                    |        | |                |     |                |    |                | |        /   x            x  |  *
* |       LAB 1        /   x    | |     EMPTY      |     |     EMPTY      |    |     EMPTY      | |        |         _____     |  *
* |                 x  /        | |     HOUSE      |     |     HOUSE      |    |     HOUSE      | |    x   |      _/       \   |  *
* |                    | HEROD  | |                |     |                |    |                | |        |     /          \  |  *
* |  x              x  | STREET | +----------------+     +----------------+    +----------------+ |        |    /   POND    /  |  *
* +-/ /----------------+        |_________________________________________________________________|        |    \          /   |  *
* |  x   x             |                 x                                                                 |     \        |    |  *
* |                    |                                 x   MAIN STREET                   x               |     /         \   |  *
* |                    /                   x                             x                                 |     |         /   |  *
* |      CARPARK       /           +-----------/ /--------------+__+-------------/ /-------------+         |  x   \       / x  |  *
* |             x      |           |             x              |  |                           x |         |        \___/      |  *
* |                    |           | x        SHOP  x         x |  |      x      PUB             |         |                   |  *
* |                    |           |                            |  |                             |         |                   |  *
* |    x             x |           +----------------------------+  +-------------/ /-------------+         +-------------------+  *
* +--------------------+           |                               x                                   x   |                      *
*                      |           |  x                        ALLEYWAY                                    |                      *
*                      |           |                                          x                            |                      *
*                      |___________|_______________________________________________________________________|                      *
*                                                                                                                                 *
***********************************************************************************************************************************"""

print (bordered(text))
print (text)




