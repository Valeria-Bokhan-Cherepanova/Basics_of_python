class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start drawing  {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Start drawing with a pen'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Start drawing with a pencil'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Start drawing with a handle'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())