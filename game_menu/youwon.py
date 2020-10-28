from asciimatics.effects import Cycle
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("You won !", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(screen,
              FigletText("Press 'q' to quit game.", font='small'),
              int(screen.height / 1 - 8)
              ),
    ]
    screen.play([Scene(effects, 500)])
Screen.wrapper(demo)

#import replaceme replace, replaceme with the .py file.
#replaceme
