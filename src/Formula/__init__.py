'''
    Formula base file

    This file contains the base Component class for Formula

'''
from Formula.engine import Bitmap, Interaction


class Device:
    def __init__(self, engine, **kwargs):
        self.engine = engine
        self.components = kwargs.get('components', [])
        self.name = kwargs.get('name', "")
        self.order_components()

    def update(self):
        bitmap = Bitmap(size=self.engine.size)
        for component in components:
            bitmap.add(component.bitmap(), pos=component.pos)
        self.engine.show_bitmap(bitmap)

    def interact(self, **kwargs):
        pos = kwargs['pos']
        for c in components:
            if c.pos[0] <= pos[0] and pos[0] <= c.pos[0] + c.size[0]:
                c.interact(Interaction(**kwargs))

    def order_components(self):
        y = 0
        x = 0
        height = self.size[0]
        width = self.size[1]
        for component in self.components:
            if component.size[0]:
                height -= component.size[0]

        for component in self.components:
            component.pos = [y, x]
            if not component.size:
                component.size = [int(height/len(self.components)), width]
            y += component.size[0]


class StaticComponent:
    def __init__(self, **kwargs):
        self.components = kwargs.get(components, {})
        self.params = kwargs.get(params, {})
        self.name = kwargs.get(name, "")
        self.size = kwargs.get(size, None)
        self.changes = True
        self.pos = None

    def bitmap(self):
        bitmap = Bitmap(size=self.size)
        if self.changes:
            bitmap.add(self.render())
            self.changes = False
        for component in self.components[self.state]:
            bitmap.add(component.bitmap())
        return bitmap

    def render(self):
        pass

    def interact(self, interaction):
        if self.hooks[interaction.type] is not None:
            self.hooks[interaction.type]()
        pos = interaction.pos
        for c in components:
            if c.pos[0] <= pos[0] and pos[0] <= c.pos[0] + c.size[0]:
                c.interact(interaction)

    def order_components(self):
        y = 0
        x = 0
        height = self.size[0]
        width = self.size[1]
        for component in self.components:
            if component.size[0]:
                height -= component.size[0]

        for component in self.components:
            component.pos = [y, x]
            if not component.size:
                component.size = [int(height/len(self.components)), width]
            y += component.size[0]


class Component:
    def __init__(self, **kwargs):
        self.components = kwargs.get(components, [])
        self.name = kwargs.get(name, "")
        self.hooks = kwargs.get(hooks, {})
        self.state = "init"
        self.params = kwargs.get(params, {})
        self.size = kwargs.get(size, None)
        self.pos = None
        self.changes = True

    def bitmap(self):
        bitmap = Bitmap(size=self.size)
        if self.changes:
            bitmap.add(self.render())
            self.changes = False
        for component in self.components[self.state]:
            bitmap.add(component.bitmap())
        return bitmap

    def render(self):
        pass

    def interact(self, interaction):
        if self.hooks[interaction.type] is not None:
            self.hooks[interaction.type]()
        else:
            pos = interaction.pos
            for c in components:
                if c.pos[0] <= pos[0] and pos[0] <= c.pos[0] + c.size[0]:
                    c.interact(interaction)

    def order_components(self):
        y = 0
        x = 0
        height = self.size[0]
        width = self.size[1]
        for component in self.components:
            if component.size[0]:
                height -= component.size[0]

        for component in self.components:
            component.pos = [y, x]
            if not component.size:
                component.size = [int(height/len(self.components)), width]
            y += component.size[0]
