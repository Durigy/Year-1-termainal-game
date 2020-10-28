from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("You Died !", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(screen,
              FigletText("Press 'q' to quit.", font='small'),
              int(screen.height / 1 - 8)
              ),
        Stars(screen, 300)
    ]
    screen.play([Scene(effects, 5000)])


Screen.wrapper(demo)