from shell_exe import execute

xres = {}
for i in range(0, 16):
    xres[str(i)] = execute([["xgetres", f"color{i}"]])
xres["bg"] = execute([["xgetres", "background"]])
xres["fg"] = execute([["xgetres", "foreground"]])


class Status2d():

    @staticmethod
    def draw(x: int, y: int, w: int, h: int) -> str:
        return f"^r{x},{y},{w},{h}^"

    @staticmethod
    def color(color: str, txt: str) -> str:
        return f"^c{color}^{txt}^d^"

    @staticmethod
    def offset(amount: int) -> str:
        return f"^f{amount}^"


class VerticalBar():
    def __init__(self, w, height, c, o):
        self.max_height = 27
        self.h = int(height*(self.max_height-2)/100)
        self.w = w
        self.x = 0
        self.y = self.max_height-self.h
        self.c = c
        self.o = o

    def draw(self):
        rect = Status2d.draw(self.x, self.y, self.w, self.h)
        offset = Status2d.offset(self.o)
        return f"{Status2d.color(self.c, rect)}{Status2d.offset(self.o)}"
