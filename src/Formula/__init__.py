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

    def update(self):
        bitmap = Bitmap(self.engine.size)
        for component in components:
            bitmap.add(component.bitmap())
        self.engine.show_bitmap(bitmap)

    def interact(self, **kwargs):
        pos = kwargs['pos']
        for c in components:
            if c.pos[0] <= pos[0] and pos[0] <= c.pos[0] + c.pos[2]:
                c.interact(
                    Interaction(**kwargs)
                )
        

class StaticComponent:
    def __init__(self, **kwargs):
        self.contents = kwargs.get(contents, {})
        self.params = kwargs.get(params, {})
        self.name = kwargs.get(name, "")
        self.size = kwargs.get(size, None)
    
    def bitmap(self):
        bitmap = Bitmap(self.size)
        for component in self.components[self.state]:
            bitmap.add(component.bitmap())
        bitmap.add(self.render())
        return bitmap

    def render(self):
        pass


class Component:
    def __init__(self, **kwargs):
        self.contents = kwargs.get(contents, {})
        self.name = kwargs.get(name, "")
        self.hooks = kwargs.get(hooks, {})
        self.state = "init"
        self.params = kwargs.get(params, {})
        self.size = kwargs.get(size, None)

    def bitmap(self):
        bitmap = Bitmap(self.x, self.y)
        for component in self.components[self.state]:
            bitmap.add(component.bitmap())
        bitmap.add(self.render())
        return bitmap

    def render(self):
        pass

    def interact(self, interaction):
        if self.hooks[interaction.type] is not None:
            self.hooks[interaction.type]()
        else:
            comp = self.get_sub_comp(interaction)
            if comp:
                comp.interact(interaction)
