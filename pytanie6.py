from traffic_simulator import *

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
PEDESTRIAN_CROSSING_NR1_CORD = (50.0693760, 19.9086055)

l1 = round(abs(UP_LEFT[1] - TRAFFIC_SIGNALS_AWITEKS[1]) * SCALE)
l2 = round(abs(TRAFFIC_SIGNALS_AWITEKS[1] - NAWOJKI_FIRST_TURN[1]) * SCALE)
l3 = round(abs(NAWOJKI_FIRST_TURN[1] - TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[1]) * SCALE)
l4 = round(abs(ALEJA_KIJOWSKA[1] - TRAFFIC_SIGNALS_CZARNOWIEJSKA[1]) * SCALE) - 80
l5 = round(abs(TRAFFIC_SIGNALS_CZARNOWIEJSKA[1] - CZARNOWIEJSKA_CROSSING[1]) * SCALE) - 100
pedestrian_crossing_position_len = round(abs(CZARNOWIEJSKA_CROSSING[1] - PEDESTRIAN_CROSSING_NR1_CORD[1]) * SCALE) - 540
# print(l1)
# print(l2)
d1 = round(abs(ALEJA_KIJOWSKA[0] - TRAFFIC_SIGNALS_ALEJA_KIJOWSKA[0]) * SCALE)
# print(d1)
# print(pedestrian_crossing_position_len)

NAWOJKI_RIGHT_START = (-50 - l1 - 15, 4)
NAWOJKI_LEFT_START = (-50 - l1 - 15, -4)
WEST_RIGHT = (-65, 4)
WEST_LEFT = (-65, -4)
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
RIGHT_NAWOJKI_FIRST_AND_SECOND_PART = (WEST_RIGHT, (-45, 2))
RIGHT_CROSSING = ((-45, 2), (-30, 2))
PEDESTRIAN_CROSSING_NR1 = ((-45 + pedestrian_crossing_position_len, 2), (-45 + pedestrian_crossing_position_len + 3, 2))
LEFT_NAWOJKI_FIRST_AND_SECOND_PART = ((-45, -2), WEST_LEFT)
LEFT_CROSSING = ((-30, -2), (-45, -2))
NAWOJKI_SECOND_PART_INBOUND = ((-30, 2), (125, 2))
NAWOJKI_SECOND_AND_HALF_PART_INBOUND = ((125, 2), RIGHT_FIRST_TURN_NAWOJKI)
NAWOJKI_SECOND_PART_OUTBOUND = ((132, -2), (-30, -2))
NAWOJKI_SECOND_AND_HALF_PART_OUTBOUND = (LEFT_FIRST_TURN_NAWOJKI, (132, -2))
NAWOJKI_THIRD_PART_INBOUND_I = ((RIGHT_FIRST_TURN_NAWOJKI[0], RIGHT_FIRST_TURN_NAWOJKI[1]), (288, 22))
NAWOJKI_THIRD_PART_INBOUND_II = ((288, 22), RIGHT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA)
NAWOJKI_THIRD_PART_OUTBOUND_I = (LEFT_TRAFFIC_SIGNALS_ALEJA_KIJOWSKA, (288, 18))
NAWOJKI_THIRD_PART_OUTBOUND_II = ((288, 18), LEFT_FIRST_TURN_NAWOJKI)
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
RIGHT_THIRD_PART_CZARNOWIEJSKA = ((-50 + l2 + l3 + l4 + l5, 68), (750, 80))
RIGHT_FOURTH_PART_CZARNOWIEJSKA = ((750, 80), (780, 82))
RIGHT_FIFTH_PART_CZARNOWIEJSKA = ((780, 82), (870, 84))
LEFT_SECOND_PART_CZARNOWIEJSKA = (LEFT_CZARNOWIEJSKA_SECOND_PART, LEFT_CZARNOWIEJSKA_FIRST_PART)
LEFT_THIRD_PART_CZARNOWIEJSKA = ((750, 76), (-50 + l2 + l3 + l4 + l5, 64))
LEFT_FOURTH_PART_CZARNOWIEJSKA = ((800, 78), (750, 76))
LEFT_FIFTH_PART_CZARNOWIEJSKA = ((870, 80), (800, 78))

CZARNOWIEJSKA_FIRST_TURN_RIGHT = turn_road(RIGHT_CZARNOWIEJSKA_FIRST_PART, (RIGHT_CZARNOWIEJSKA_FIRST_PART[0] + 1, RIGHT_CZARNOWIEJSKA_FIRST_PART[1] + 1), TURN_RIGHT, 15)
CZARNOWIEJSKA_FIRST_TURN_LEFT = turn_road((LEFT_CZARNOWIEJSKA_FIRST_PART[0] - 1, LEFT_CZARNOWIEJSKA_FIRST_PART[1] - 1), LEFT_CZARNOWIEJSKA_FIRST_PART, TURN_LEFT, 15)

BUS_LINE_NAWOJKI_FIRST_PART_I = ((-10, 6), (85, 6))
BUS_LINE_NAWOJKI_FIRST_PART_II = ((85, 6), (100, 6))
BUS_FIRST_JOIN = ((-29, 2.5), (-8, 6.5))
BUS_FIRST_MERGE = ((100, 6), (125, 2))

BUS_SECOND_JOIN = ((130, 2.5), (158, 6.5))
BUS_LINE_CZARNOWIEJSKA = ((155, 6), (185, 6))
BUS_LINE_CZARNOWIEJSKA_II = ((185, 6), (260, 20))
BUS_SECOND_MERGE = ((260, 20), (288, 22))

BUS_THIRD_JOIN = ((l2 + l3, 50), (400, 53))
BUS_LINE_CZARNOWIEJSKA_III = ((400, 53), (468, 49))
BUS_LINE_CZARNOWIEJSKA_IV = ((467.5, 49), (565, 67.5))
BUS_THIRD_MERGE = ((565, 67.5), (585, 67))

BUS_FOURTH_JOIN = ((585, 67), (610, 74))
BUS_LINE_CZARNOWIEJSKA_V = ((610, 74), (755, 84.5))
BUS_FOURTH_MERGE = ((755, 84.5), (779, 82.5))

MIECHOWSKA_TURN_RIGHT = turn_road(RIGHT_NAWOJKI_END, (l2 + l3 - 4, 50), TURN_RIGHT, 15)

sim.create_roads([
    # index-0
    NAWOJKI_FIRST_PART_INBOUND,
    RIGHT_NAWOJKI_FIRST_AND_SECOND_PART,
    RIGHT_CROSSING,
    NAWOJKI_SECOND_PART_INBOUND,
    NAWOJKI_SECOND_AND_HALF_PART_INBOUND,
    NAWOJKI_THIRD_PART_INBOUND_I,
    NAWOJKI_THIRD_PART_INBOUND_II,
    RIGHT_KIJOWSKA_CROSSING_STRAIGHT,
    NAWOJKI_LAST_PART_INBOUND,

    NAWOJKI_FIRST_PART_OUTBOUND,
    LEFT_NAWOJKI_FIRST_AND_SECOND_PART,
    LEFT_CROSSING,
    NAWOJKI_SECOND_PART_OUTBOUND,
    NAWOJKI_SECOND_AND_HALF_PART_OUTBOUND,
    #index-14
    NAWOJKI_THIRD_PART_OUTBOUND_II,
    NAWOJKI_THIRD_PART_OUTBOUND_I,
    LEFT_KIJOWSKA_CROSSING_STRAIGHT,
    NAWOJKI_LAST_PART_OUTBOUND,

    # index-18
    LEFT_ALEJA_KIJOWSKA_ROAD,
    RIGHT_ALEJA_KIJOWSKA_ROAD,


    RIGHT_MIECHOWSKA_ROAD,
    LEFT_MIECHOWSKA_ROAD,

    RIGHT_FIRST_PART_CZARNOWIEJSKA,
    LEFT_FIRST_PART_CZARNOWIEJSKA,

    URZEDNICZA_ROAD,

    #index-25
    LEFT_SECOND_PART_CZARNOWIEJSKA,
    LEFT_THIRD_PART_CZARNOWIEJSKA,
    LEFT_FOURTH_PART_CZARNOWIEJSKA,
    LEFT_FIFTH_PART_CZARNOWIEJSKA,
    RIGHT_SECOND_PART_CZARNOWIEJSKA,
    RIGHT_THIRD_PART_CZARNOWIEJSKA,
    RIGHT_FOURTH_PART_CZARNOWIEJSKA,
    RIGHT_FIFTH_PART_CZARNOWIEJSKA,

    #index-33
    BUS_LINE_NAWOJKI_FIRST_PART_I,
    BUS_LINE_NAWOJKI_FIRST_PART_II,
    BUS_FIRST_JOIN,
    BUS_FIRST_MERGE,

    BUS_SECOND_JOIN,
    BUS_LINE_CZARNOWIEJSKA,
    BUS_LINE_CZARNOWIEJSKA_II,
    BUS_SECOND_MERGE,

    BUS_THIRD_JOIN,
    BUS_LINE_CZARNOWIEJSKA_III,
    BUS_LINE_CZARNOWIEJSKA_IV,
    BUS_THIRD_MERGE,

    BUS_FOURTH_JOIN,
    BUS_LINE_CZARNOWIEJSKA_V,
    BUS_FOURTH_MERGE,

    # index-48
    *KIJOWSKA_NAWOJKI_TURN_RIGHT,
    *KIJOWSKA_NAWOJKI_TURN_LEFT,

    *NAWOJKI_KIJOWSKA_TURN_RIGHT,
    *NAWOJKI_KIJOWSKA_TURN_LEFT,

    *NAWOJKI_SECOND_TURN_RIGHT,
    *NAWOJKI_SECOND_TURN_LEFT,

    *CZARNOWIEJSKA_FIRST_TURN_RIGHT,
    *CZARNOWIEJSKA_FIRST_TURN_LEFT
    # *MIECHOWSKA_TURN_RIGHT

])

sim.create_signal([[6, 17], [18]])
sim.create_signal([[1, 12]])
sim.create_signal([[28, 31, 47]])

sim.create_pedestrian_crossing((-30 + pedestrian_crossing_position_len, 0), (NAWOJKI_SECOND_PART_INBOUND, NAWOJKI_SECOND_AND_HALF_PART_OUTBOUND))
print(-30 + pedestrian_crossing_position_len)
print(-50 + l2)
sim.create_pedestrian_crossing((288, 22), (NAWOJKI_THIRD_PART_INBOUND_I, NAWOJKI_THIRD_PART_OUTBOUND_I))
sim.create_pedestrian_crossing((288, 22), (NAWOJKI_THIRD_PART_INBOUND_I, NAWOJKI_THIRD_PART_OUTBOUND_I))
sim.create_pedestrian_crossing((-50 + l2 + l3 + l4 + l5, 68), (RIGHT_SECOND_PART_CZARNOWIEJSKA, LEFT_THIRD_PART_CZARNOWIEJSKA))
def road(a): return range(a, a+15)



sim.create_gen({
    'vehicle_rate': 30,
    'vehicles': [
        [2, {'path': [0, 1, 2, 3, 4, 5, 6, 7, 8, 22, 29 ,30, 31, 32]}],
        [1, {'path': [18, *road(48 + 15), 15, 14, 13, 12, 11, 10, 9]}],
        [3, {'path': [18, *road(48), 8, 21]}],
        [4, {'path': [28, 27, 26, 25, 23, 17, 16, 15, 14, 13, 12, 11, 10, 9]}],
        [2, {'path': [0, 1, 2, 35, 33, 34, 36, 37, 38, 39, 40, 6, 7, 8, 41, 42, 43, 44, 45, 46, 47, 32]}]
    ]}
)

sim.create_gen({
    'vehicle_rate': 2,
    'vehicles': [
        [4, {'path': [0, 1, 2, 35, 33, 34, 36, 37, 38, 39, 40,6, 7, 8, 41, 42, 43, 44, 45, 46, 47, 32], 'l': 8, 'v_max': 6}]
    ]}
)

sim.create_pedestrian_gen()

win = Window(sim)
win.zoom = 1.5
asyncio.run(win.run(steps_per_update=5))
