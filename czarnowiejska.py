from middleware.traffic_simulator import *

SCALE = 50000

sim = Simulation()

DOWN_RIGHT = (50.0674134, 19.9031611)
UP_LEFT = (50.0699855, 19.9040286)
UP_RIGHT = (50.0658971, 19.9241282)
DOWN_LEFT = (50.0638776, 19.9236128)
TRAFFIC_SIGNALS_AWITEKS = (50.0697536, 19.9060001)
NAWOJKI_FIRST_TURN = (50.069035, 19.910721)
TRAFFIC_SIGNALS_ALEJA_KIJOWSKA = (50.0679708, 19.9136371)
ALEJA_KIJOWSKA = (50.068681, 19.913845)
TRAFFIC_SIGNALS_CZARNOWIEJSKA = (50.0675762, 19.9181620)
MIECHOWKSA = (50.0658352, 19.9140487)
CZARNOWIEJSKA_CROSSING = (50.0664123, 19.9225809)

l1 = round(abs(UP_LEFT[1] - TRAFFIC_SIGNALS_AWITEKS[1]) * SCALE)
l2 = round(abs(TRAFFIC_SIGNALS_AWITEKS[1] - NAWOJKI_FIRST_TURN[1]) * SCALE)
l3 = round(abs(NAWOJKI_FIRST_TURN[1] - TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1]) * SCALE)
l4 = round(abs(ALEJA_KIJOWSKA[1] - TRAFFIC_SIGNALS_CZARNOWIEJSKA[1]) * SCALE) - 80
l5 = round(abs(TRAFFIC_SIGNALS_CZARNOWIEJSKA[1] - CZARNOWIEJSKA_CROSSING[1]) * SCALE) - 100
print(l1)
print(l2)
d1 = round(abs(ALEJA_KIJOWSKA[0] - TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0]) * SCALE)
print(d1)

NAWOJKI_RIGHT_START = (-50 - l1, 4)
NAWOJKI_LEFT_START = (-50 - l1, -4)
WEST_RIGHT = (-50, 4)
WEST_LEFT = (-50, -4)
RIGHT_TRAFFIC_SIGNALS_NAWOJKI = (-50, 2)
LEFT_TRAFFIC_SIGNALS_NAWOJKI = (-50, -2)
RIGHT_FIRST_TURN_NAWOJKI = (-50 + l2, 2)
LEFT_FIRST_TURN_NAWOJKI = (-50 + l2, -2)
RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA = (-50 + l2 + l3, 30)
LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA = (-50 + l2 + l3, 26)
RIGHT_ALEJA_KIJOWSKA_START = (-50 + l2 + l3 + 12, 30 - d1 - 17)
LEFT_ALEJA_KIJOWSKA_START = (-50 + l2 + l3 + 8, 30 - d1 - 17)
RIGHT_NAWOJKI_END = (l2 + l3, 50)
LEFT_NAWOJKI_END = (l2 + l3, 46)
RIGHT_CZARNOWIEJSKA_FIRST_PART = (-50 + l2 + l3 + l4, 45)
LEFT_CZARNOWIEJSKA_FIRST_PART = (-50 + l2 + l3 + l4, 41)
RIGHT_MIECHOWSKA_END = (l2 + l3 - 5, 100)
LEFT_MIECHOWSKA_END = (-4 + l2 + l3 - 5, 100)
URZEDNICZNA_START = (-50 + l2 + l3 + l4, 0)
RIGHT_CZARNOWIEJSKA_SECOND_PART = (-50 + l2 + l3 + l4 + l5, 68)
LEFT_CZARNOWIEJSKA_SECOND_PART = (-50 + l2 + l3 + l4 + l5, 64)

NAWOJKI_FIRST_PART_INBOUND = (NAWOJKI_RIGHT_START, WEST_RIGHT)
NAWOJKI_FIRST_PART_OUTBOUND = (WEST_LEFT, NAWOJKI_LEFT_START)
RIGHT_NAWOJKI_FIRST_AND_SECOND_PART = (WEST_RIGHT, (-35, 2))
RIGHT_CROSSING = ((-35, 2), (-30, 2))
LEFT_NAWOJKI_FIRST_AND_SECOND_PART = ((-30, -2), WEST_LEFT)
LEFT_CROSSING = ((-30, -2), (-35, -2))
NAWOJKI_SECOND_PART_INBOUND = ((-30, 2), RIGHT_FIRST_TURN_NAWOJKI)
NAWOJKI_SECOND_PART_OUTBOUND = (LEFT_FIRST_TURN_NAWOJKI, (-30, -2))
NAWOJKI_THIRD_PART_INBOUND = ((RIGHT_FIRST_TURN_NAWOJKI[0] + 4, RIGHT_FIRST_TURN_NAWOJKI[1] + 0.5), RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA)
NAWOJKI_THIRD_PART_OUTBOUND = (LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA, LEFT_FIRST_TURN_NAWOJKI)
NAWOJKI_LAST_PART_INBOUND = ((RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2), RIGHT_NAWOJKI_END)
NAWOJKI_LAST_PART_OUTBOUND = (LEFT_NAWOJKI_END, (LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2))

NAWOJKI_FIRST_TURN_RIGHT = turn_road(RIGHT_FIRST_TURN_NAWOJKI, (RIGHT_FIRST_TURN_NAWOJKI[0] + 4, RIGHT_FIRST_TURN_NAWOJKI[1] + 0.5), TURN_RIGHT, 15)
NAWOJKI_FIRST_TURN_LEFT = turn_road((LEFT_FIRST_TURN_NAWOJKI[0] - 1, LEFT_FIRST_TURN_NAWOJKI[1] - 1), LEFT_FIRST_TURN_NAWOJKI, TURN_LEFT, 10)

RIGHT_ALEJA_KIJOWSKA_ROAD = ((RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 8, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] - 7), RIGHT_ALEJA_KIJOWSKA_START)
LEFT_ALEJA_KIJOWSKA_ROAD = (LEFT_ALEJA_KIJOWSKA_START, (LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 4, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] - 3))

KIJOWSKA_NAWOJKI_TURN_RIGHT = turn_road((LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 4, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] - 3), (RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2), TURN_LEFT, 15)
KIJOWSKA_NAWOJKI_TURN_LEFT = turn_road((LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 4, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] - 3), LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA, TURN_RIGHT, 15)

NAWOJKI_KIJOWSKA_TURN_RIGHT = turn_road((LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2), (RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 8, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] - 7), TURN_RIGHT, 15)
NAWOJKI_KIJOWSKA_TURN_LEFT = turn_road(RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA, (RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 8, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] - 7), TURN_LEFT, 15)

RIGHT_KIJOWSKA_CROSSING_STRAIGHT = (RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA, (RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2))
LEFT_KIJOWSKA_CROSSING_STRAIGHT = ((LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2), LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA)

RIGHT_FIRST_PART_CZARNOWIEJSKA = (RIGHT_NAWOJKI_END, RIGHT_CZARNOWIEJSKA_FIRST_PART)
LEFT_FIRST_PART_CZARNOWIEJSKA = (LEFT_CZARNOWIEJSKA_FIRST_PART, LEFT_NAWOJKI_END)

NAWOJKI_SECOND_TURN_RIGHT = turn_road((RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 10, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2), (RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 11, RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1] + 2), TURN_RIGHT, 15)
NAWOJKI_SECOND_TURN_LEFT = turn_road((LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0] + 1, LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1]), LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA, TURN_LEFT, 15)


RIGHT_MIECHOWSKA_ROAD = (RIGHT_MIECHOWSKA_END, (l2 + l3, 50))
LEFT_MIECHOWSKA_ROAD = ((l2 + l3 - 4, 50), LEFT_MIECHOWSKA_END)

URZEDNICZA_ROAD = (URZEDNICZNA_START, LEFT_CZARNOWIEJSKA_FIRST_PART)

RIGHT_SECOND_PART_CZARNOWIEJSKA = (RIGHT_CZARNOWIEJSKA_FIRST_PART, RIGHT_CZARNOWIEJSKA_SECOND_PART)
LEFT_SECOND_PART_CZARNOWIEJSKA = (LEFT_CZARNOWIEJSKA_SECOND_PART, LEFT_CZARNOWIEJSKA_FIRST_PART)

CZARNOWIEJSKA_FIRST_TURN_RIGHT = turn_road(RIGHT_CZARNOWIEJSKA_FIRST_PART, (RIGHT_CZARNOWIEJSKA_FIRST_PART[0] + 1, RIGHT_CZARNOWIEJSKA_FIRST_PART[1] + 1), TURN_RIGHT, 15)
CZARNOWIEJSKA_FIRST_TURN_LEFT = turn_road((LEFT_CZARNOWIEJSKA_FIRST_PART[0] - 1, LEFT_CZARNOWIEJSKA_FIRST_PART[1] - 1), LEFT_CZARNOWIEJSKA_FIRST_PART, TURN_LEFT, 15)

sim.create_roads([
    # index-0
    NAWOJKI_FIRST_PART_INBOUND,
    RIGHT_NAWOJKI_FIRST_AND_SECOND_PART,
    RIGHT_CROSSING,
    NAWOJKI_SECOND_PART_INBOUND,
    NAWOJKI_THIRD_PART_INBOUND,
    RIGHT_KIJOWSKA_CROSSING_STRAIGHT,
    NAWOJKI_LAST_PART_INBOUND,

    NAWOJKI_FIRST_PART_OUTBOUND,
    LEFT_NAWOJKI_FIRST_AND_SECOND_PART,
    LEFT_CROSSING,
    NAWOJKI_SECOND_PART_OUTBOUND,
    NAWOJKI_THIRD_PART_OUTBOUND,
    LEFT_KIJOWSKA_CROSSING_STRAIGHT,
    NAWOJKI_LAST_PART_OUTBOUND,

    # index-14
    LEFT_ALEJA_KIJOWSKA_ROAD,
    RIGHT_ALEJA_KIJOWSKA_ROAD,


    RIGHT_MIECHOWSKA_ROAD,
    LEFT_MIECHOWSKA_ROAD,

    RIGHT_FIRST_PART_CZARNOWIEJSKA,
    LEFT_FIRST_PART_CZARNOWIEJSKA,

    URZEDNICZA_ROAD,

    LEFT_SECOND_PART_CZARNOWIEJSKA,
    RIGHT_SECOND_PART_CZARNOWIEJSKA,

    # index-23
    *KIJOWSKA_NAWOJKI_TURN_RIGHT,
    *KIJOWSKA_NAWOJKI_TURN_LEFT,

    *NAWOJKI_KIJOWSKA_TURN_RIGHT,
    *NAWOJKI_KIJOWSKA_TURN_LEFT,

    *NAWOJKI_SECOND_TURN_RIGHT,
    *NAWOJKI_SECOND_TURN_LEFT,

    *NAWOJKI_FIRST_TURN_RIGHT,
    # *NAWOJKI_FIRST_TURN_LEFT,
    *CZARNOWIEJSKA_FIRST_TURN_RIGHT,
    *CZARNOWIEJSKA_FIRST_TURN_LEFT

])

sim.create_signal([[4, 13] ,[14]])

def road(a): return range(a, a+15)

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [3, {'path': [0, 1, 2, *road(23 + 6*15), 3, 4, 5, 6]}],
        # [1, {'path': [14, *road(23 + 15), 11]}],
        # [3, {'path': [14, *road(23), 6]}],
        # [1, {'path': [4, *road(23 + 45), 15]}]
    ]}
)

win = Window(sim)
win.zoom = 1.5
asyncio.run(win.run(steps_per_update=5))
