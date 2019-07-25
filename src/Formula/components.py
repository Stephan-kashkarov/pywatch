from Formula import Component
import Formula.engine as engine


class Text(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params = {
            'value': kwargs.get("value", ''),
            'font': kwargs.get("font", 'auto'),
            'font_size': kwargs.get("fontsize"),
            'colour': kwargs.get("colour", 'black'),
        }

    def render():
        return engine.text(**self.params)


class Box(Component):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.params = {
            'line_size': kwargs.get('line_size', 1),
            'colour': kwargs.get('colour', 'black'),
            ''
        }


    
