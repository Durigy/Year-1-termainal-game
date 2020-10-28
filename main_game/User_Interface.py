# def user_interface(text):
#     user_interface_map()
#     lines = text.splitlines()
#     width = max(len(s) for s in lines)
#     res = ['┌' + '─' * width + '┐']
#     for s in lines:
#         res.append('│' + (s + ' ' * width)[:width] + '│')
#     res.append('└' + '─' * width + '┘')
#     return '\n'.join(res)
#
# def user_interface_map():
#
#     text="""
#     ***********************************************************************************************************************************
#     * +----------------------+                                                                         ________+--------------------+ *
#     * |         x         x  |                                                x             x         |        |     x       x      | *
#     * |                      |__      ____________        ________________       ____________         |        |                    | *
#     * |                      /   \   /            \      /   WINDY PATH   \     /            \        |        |                    | *
#     * |      LIBRARY x     x /    \_/     ______   \____/       _______    \___/    _______   \_______|        |        LAB 2       | *
#     * |                      |\          /      \           x  /       \           /       \               x   /                    | *
#     * |                      | \________/        \____________/         \_________/         \__________        /    x               | *
#     * |                      |                                                                        |        |                    | *
#     * |  x                   |                   x                                                    |        |                    | *
#     * +------/\/-------------+______    +------------+         +------------+        +------------+   |        |                  x | *
#     * |    x                        |   |            |         |            |        |            |   |        +--------------/\/---+ *
#     * |        HEROD CLOSE          |   |            |         |            |        |            |   |        |                   |  *
#     * |            x                |   |   GARDEN   |         |   GARDEN   |        |   GARDEN   |   | ISIAH  |                   |  *
#     * +--------------------+        |   |            |         |            |        |            |   | ROAD   |        PARK       |  *
#     * |  x              x  |        | +-+------------+-+     +-+------------+-+    +-+------------+-+ |        /                   |  *
#     * |                    |        | |                |     |                |    |                | |        /   x            x  |  *
#     * |       LAB 1        /   x    | |     EMPTY      |     |     EMPTY      |    |     EMPTY      | |        |         _____     |  *
#     * |                 x  /        | |     HOUSE      |     |     HOUSE      |    |     HOUSE      | |    x   |      _/       \   |  *
#     * |                    | HEROD  | |                |     |                |    |                | |        |     /          \  |  *
#     * |  x              x  | STREET | +----------------+     +----------------+    +----------------+ |        |    /   POND    /  |  *
#     * +-/ /----------------+        |_________________________________________________________________|        |    \          /   |  *
#     * |  x   x             |                 x                                                                 |     \        |    |  *
#     * |                    |                                 x   MAIN STREET                   x               |     /         \   |  *
#     * |                    /                   x                             x                                 |     |         /   |  *
#     * |      CARPARK       /           +-----------/ /--------------+__+-------------/ /-------------+         |  x   \       / x  |  *
#     * |             x      |           |             x              |  |                           x |         |        \___/      |  *
#     * |                    |           | x        SHOP  x         x |  |      x      PUB             |         |                   |  *
#     * |                    |           |                            |  |                             |         |                   |  *
#     * |    x             x |           +----------------------------+  +-------------/ /-------------+         +-------------------+  *
#     * +--------------------+           |                               x                                   x   |                      *
#     *                      |           |  x                        ALLEYWAY                                    |                      *
#     *                      |           |                                          x                            |                      *
#     *                      |___________|_______________________________________________________________________|                      *
#     *                                                                                                                                 *
#     ***********************************************************************************************************************************"""
#     return text
#
# #room = room["name"] + room["spot name"]
# room = "THE ROOM WILL BE HERE " #Variable from main
#
# #energy = inventory["energy"]
# energy = "100" #Var from main
# length_remaining = 62 - len(room)
# left_remaining = 55 - len(energy)
# text= "ROOM: " + room + " " * length_remaining + "ENERGY: " + energy + " " * left_remaining
#
# print (user_interface(text))
#
# pictures = ["""
# ***********************************************************************************************************************************
# * +----------------------+                                                                         ________+--------------------+ *
# * |         x         x  |                                                x             x         |        |     x       x      | *
# * |                      |__      ____________        ________________       ____________         |        |                    | *
# * |                      /   \   /            \      /   WINDY PATH   \     /            \        |        |                    | *
# * |      LIBRARY x     x /    \_/     ______   \____/       _______    \___/    _______   \_______|        |        LAB 2       | *
# * |                      |\          /      \           x  /       \           /       \               x   /                    | *
# * |                      | \________/        \____________/         \_________/         \__________        /    x               | *
# * |                      |                                                                        |        |                    | *
# * |  x                   |                   x                                                    |        |                    | *
# * +------/\/-------------+______    +------------+         +------------+        +------------+   |        |                  x | *
# * |    x                        |   |            |         |            |        |            |   |        +--------------/\/---+ *
# * |        HEROD CLOSE          |   |            |         |            |        |            |   |        |                   |  *
# * |            x                |   |   GARDEN   |         |   GARDEN   |        |   GARDEN   |   | ISIAH  |                   |  *
# * +--------------------+        |   |            |         |            |        |            |   | ROAD   |        PARK       |  *
# * |  x              x  |        | +-+------------+-+     +-+------------+-+    +-+------------+-+ |        /                   |  *
# * |                    |        | |                |     |                |    |                | |        /   x            x  |  *
# * |       LAB 1        /   x    | |     EMPTY      |     |     EMPTY      |    |     EMPTY      | |        |         _____     |  *
# * |                 x  /        | |     HOUSE      |     |     HOUSE      |    |     HOUSE      | |    x   |      _/       \   |  *
# * |                    | HEROD  | |                |     |                |    |                | |        |     /          \  |  *
# * |  x              x  | STREET | +----------------+     +----------------+    +----------------+ |        |    /   POND    /  |  *
# * +-/ /----------------+        |_________________________________________________________________|        |    \          /   |  *
# * |  x   x             |                 x                                                                 |     \        |    |  *
# * |                    |                                 x   MAIN STREET                   x               |     /         \   |  *
# * |                    /                   x                             x                                 |     |         /   |  *
# * |      CARPARK       /           +-----------/ /--------------+__+-------------/ /-------------+         |  x   \       / x  |  *
# * |             x      |           |             x              |  |                           x |         |        \___/      |  *
# * |                    |           | x        SHOP  x         x |  |      x      PUB             |         |                   |  *
# * |                    |           |                            |  |                             |         |                   |  *
# * |    x             x |           +----------------------------+  +-------------/ /-------------+         +-------------------+  *
# * +--------------------+           |                               x                                   x   |                      *
# *                      |           |  x                        ALLEYWAY                                    |                      *
# *                      |           |                                          x                            |                      *
# *                      |___________|_______________________________________________________________________|                      *
# *                                                                                                                                 *
# ***********************************************************************************************************************************""",
# """
# ***********************************************************************************************************************************
# * +----------------------+                                                                         ________+--------------------+ *
# * |         x         x  |                                                x             x         |        |     x       x      | *
# * |                      |__      ____________        ________________       ____________         |        |                    | *
# * |                      /   \   /            \      /   WINDY PATH   \     /            \        |        |                    | *
# * |      LIBRARY x     x /    \_/     ______   \____/       _______    \___/    _______   \_______|        |        LAB 2       | *
# * |                      |\          /      \           x  /       \           /       \               x   /                    | *
# * |                      | \________/        \____________/         \_________/         \__________        /    x               | *
# * |                      |                                                                        |        |    |               | *
# * |  x                   |                   x                                                    |        |  Here              | *
# * +------/\/-------------+______    +------------+         +------------+        +------------+   |        |                  x | *
# * |    x                        |   |            |         |            |        |            |   |        +--------------/\/---+ *
# * |        HEROD CLOSE          |   |            |         |            |        |            |   |        |                   |  *
# * |            x                |   |   GARDEN   |         |   GARDEN   |        |   GARDEN   |   | ISIAH  |                   |  *
# * +--------------------+        |   |            |         |            |        |            |   | ROAD   |        PARK       |  *
# * |  x              x  |        | +-+------------+-+     +-+------------+-+    +-+------------+-+ |        /                   |  *
# * |                    |        | |                |     |                |    |                | |        /   x            x  |  *
# * |       LAB 1        /   x    | |     EMPTY      |     |     EMPTY      |    |     EMPTY      | |        |         _____     |  *
# * |                 x  /        | |     HOUSE      |     |     HOUSE      |    |     HOUSE      | |    x   |      _/       \   |  *
# * |                    | HEROD  | |                |     |                |    |                | |        |     /          \  |  *
# * |  x              x  | STREET | +----------------+     +----------------+    +----------------+ |        |    /   POND    /  |  *
# * +-/ /----------------+        |_________________________________________________________________|        |    \          /   |  *
# * |  x   x             |                 x                                                                 |     \        |    |  *
# * |                    |                                 x   MAIN STREET                   x               |     /         \   |  *
# * |                    /                   x                             x                                 |     |         /   |  *
# * |      CARPARK       /           +-----------/ /--------------+__+-------------/ /-------------+         |  x   \       / x  |  *
# * |             x      |           |             x              |  |                           x |         |        \___/      |  *
# * |                    |           | x        SHOP  x         x |  |      x      PUB             |         |                   |  *
# * |                    |           |                            |  |                             |         |                   |  *
# * |    x             x |           +----------------------------+  +-------------/ /-------------+         +-------------------+  *
# * +--------------------+           |                               x                                   x   |                      *
# *                      |           |  x                        ALLEYWAY                                    |                      *
# *                      |           |                                          x                            |                      *
# *                      |___________|_______________________________________________________________________|                      *
# *                                                                                                                                 *
# ***********************************************************************************************************************************"""]
#
# text = pictures[1]
# print(user_interface(text))
#
#
# #text= room["main location"]
# words ="DESCRIPTION: You are standing in Main Street - which used to be full of life. I To your left, a row of houses - now occupied by refugees that pray for a vaccine. There is a bin-bag with a peculiar wooden handle sticking out. You can go into the shop, the pub next to it or the nalleyway. You can go west onto Herod Streator north onto Isiah Road."
# words = words.split()
# i = 0
# split_sentences = ""
# text = ""
# line = " "
# for word in words:
#
#         text = text + " " + word
#         if len(text) > 60:
#             total_chars = len(text)
#             remaining_spaces = 80 - total_chars - i
#             total = 1 + i + len(text) + remaining_spaces
#
#             sentence = line + text + " " * remaining_spaces + "*"
#             split_sentences = split_sentences + "\n" + text
#             text = ""
#         elif len(text) < 60:
#             left_over = text
# text = (split_sentences + "\n" + left_over)
# print(user_interface(text))
#
#
# #inventory = player_inventory["items"]
# show_inventory = True
# inventory = ["ice cream", "chocolate", "lolly pop", "more random items"]
#
# room_remaining = 60
# display_inv = ""
# split_inv = ""
# remaining = ""
#
# if show_inventory is True:
#
#     for i in inventory:
#         display_inv = display_inv +"\n" + i
#         if len(display_inv) > 50:
#             total_chars = len(display_inv)
#             remaining_spaces = 70 - total_chars - i
#             total = 1 + i + len(display_inv) + remaining_spaces
#
#             sentence = line + display_inv + " " * remaining_spaces + "*"
#             split_inv = split_inv + "\n" + display_inv
#             display_inv = ""
#
#         elif len(i) < 50:
#             remaining_spaces = 81 - len(i)
#             remaining = remaining + "\n" + i
#
#     inventory_output = ("inventory: " + "\n" + remaining + "\n" + split_inv + " " * remaining_spaces)
#     print(user_interface(inventory_output.upper()))
#
# #print(display_inv.upper())
#
# #print (text + "\n" + "INVENTORY: \n" + inventory_output.upper())
# #print (inventory_output.upper(), end=",")
# #print(text)
# #print(user_interface(text)+ user_interface(inventory_output.upper()))
# #output = "".join(text + inventory_output.upper())
# #print(output)
#
