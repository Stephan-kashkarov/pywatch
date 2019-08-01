import Formula as f
from Formula.engine import Breadboard
from Formula.components import (
    Button,
    Text,
    Box
)

device = f.Device(Breadboard(), components=[
    [
        Row(
            components=[
                Box(color='red'),
                Box(color='black'),
            ]
        ),
    ],
    [
        Box(
            components=[
                Box(color='red')
            ],
            color='blue'
        ),
    ],
])

while True:
    device.update()
    if device.engine.interaction:
        device.interact(type='press', pos=device.engine.pos)