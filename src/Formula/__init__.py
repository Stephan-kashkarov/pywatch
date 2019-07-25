'''
    Formula base file

    This file contains the base Component class for Formula

'''
from Formula.engine import Bitmap


class StaticComponent:
    def __init__(self, **kwargs):
        self.contents = kwargs.get(contents, {})
        self.params = kwargs.get(params, {})
        self.name = kwargs.get(name, "")
        self.size = kwargs.get(size, None)
    
    def bitmap(self):
        bitmap = Bitmap(self.x, self.y)
        for component in self.components[self.state]:
            bitmap.blit(component.bitmap())
        bitmap.blit(self.render())
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
            bitmap.blit(component.bitmap())
        bitmap.blit(self.render())
        return bitmap

    def render(self):
        pass

    def interact(self, interaction):
        if self.hooks[interaction] is not None:
            self.hooks[interaction]()
        else:
            comp = self.get_sub_comp(interaction)
            comp.interact(interaction)
