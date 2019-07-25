'''
    Formula base file

    This file contains the base Component class for Formula

'''


class Component:
    def __init__(self, **kwargs):
        self.contents = kwargs.get(contents, {})
        self.name = kwargs.get(name, "")
        self.hooks = kwargs.get(hooks, {})
        self.state = "init"

    def render(self):
        for component in self.components[self.state]:
            component.render()
        return self.bitmap()

    def interact(self, interaction):
        if self.hooks[interaction] is not None:
            self.hooks[interaction]()
        else:
            comp = self.get_sub_comp(interaction)
            comp.interact(interaction)

    def self.bitmap()