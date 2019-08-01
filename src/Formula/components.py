from Formula import Component, StaticComponent


class Text(StaticComponent):
    def __init__(self, device, **kwargs):
        super().__init__(**kwargs)
        self.device = device
        self.params.update({
            'value': kwargs.get("value", ''),
            'font': kwargs.get("font", 'auto'),
            'font_size': kwargs.get("fontsize"),
            'colour': kwargs.get("colour", 'black'),
        })

    def render(self):
        return self.device.engine.text(**self.params)


class Box(StaticComponent):
    def __init__(self, device, **kwargs):
        super().__init__(**kwargs)
        self.device = device
        self.params.update({
            'line_size': kwargs.get('line_size', 1),
            'colour': kwargs.get('colour', 'grey'),
            'fill': kwargs.get('fill', False),
        })

    def render(self):
        return self.device.engine.rect(**self.size, **self.params)


class Button(Component):
    def __init__(self, device, **kwargs):
        super().__init__(**kwargs)
        self.device = device
        self.contents.extend([
            Box(
                contents=[
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

    @self.device.engine.change
    def toggle_pressed(self):
        if self.state = 'pressed':
            self.state = 'init'
            self.contents[0].params.update({
                'colour': 'grey',
            })
        else:
            self.state = 'pressed'
            self.contents[0].params.update({
                'colour': 'black',
            })
