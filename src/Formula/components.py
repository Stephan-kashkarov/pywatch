from Formula import Component


class Text(Component):
    def __init__(self, value, **kwargs):
        super().__init__()
        self.value = value

    
