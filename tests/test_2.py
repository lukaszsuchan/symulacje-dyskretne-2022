from traffic_simulator import *

# Create simulation
sim = Simulation()

sim.create_roads([
    ((0, 100), (150, 100)),
    ((150, 100), (300, 100))
])

sim.create_pedestrian_crossing((150, 100), (((0, 100), (150, 100)), ((150, 100), (300, 100))))

sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [0, 1]}]
    ]
})

sim.create_pedestrian_gen()

win = Window(sim)
win.offset = (-150, -110)
asyncio.run(win.run(steps_per_update=5))