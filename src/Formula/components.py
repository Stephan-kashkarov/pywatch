from Formula import Component
import Formula.engine as engine


class Text(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contents = {
            'value': kwargs.get("value", ''),
            'font': kwargs.get("font", 'auto'),
            'font_size': kwargs.get("fontsize"),
            'colour': kwargs.get("colour", 'black'),
        }

    def render(self):
        return engine.text(**self.contents)


class Box(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contents = {
            'line_size': kwargs.get('line_size', 1),
            'colour': kwargs.get('colour', 'black'),
            'fill': kwargs.get('fill', False),
        }

    def render(self):
        return engine.rect(**self.size, **self.contents)


class Button(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contents = {

        }
        self.callbacks = {

        }
