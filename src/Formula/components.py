from Formula import Component, StaticComponent
from Formula.engine import Bitmap, color_chart


class Text(StaticComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params.update({
            'value': kwargs.get("value", ''),
            'font': kwargs.get("font", 'auto'),
            'font_size': kwargs.get("fontsize"),
            'color': kwargs.get("color", 'black'),
        })

    def render(self):
        pass


class Box(StaticComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params.update({
            'line_size': kwargs.get('line_size', 1),
            'color': kwargs.get('color', 'black'),
            'fill': kwargs.get('fill', True),
        })

    def render(self):
        if fill:
            self.bitmap = []
            for y in range(self.size[0]):
                self.bitmap.append([])
                for x in range(self.size[1]):
                    self.bitmap[y].append(color_chart[self.params.color])
            self.bitmap = Bitmap(map=self.bitmap)
        else:
            pass


class Button(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.components.extend([
            Box(
                components=[
                    Text(
                        **kwargs.get('Text', {
                            'value': "Button",
                        })
                    )
                ],
                **kwargs.get('Box', {}),
            )
        ])
        self.params.update({
            'init': {
                
            },
            'pressed': {

            }
        })
        self.callbacks.update({
            'press': self.toggle_pressed(),
        })

    def toggle_pressed(self):
        self.changes = True
        if self.state = 'pressed':
            self.state = 'init'
            self.components[0].params.update({
                'color': 'grey',
            })
        else:
            self.state = 'pressed'
            self.components[0].params.update({
                'color': 'black',
            })

    def render():
        return None
    

class Row(StaticComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)