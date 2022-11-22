from traffic_simulator import Road


class PedestrianCrossing:

    def create_paths(self, location, sin, cos):
        a = 10*sin
        b = 10*cos
        paths = []
        x1 = location[0]
        y1 = location[1] - 3
        for i in range(-3, 4, 1):
            if i == 0: continue
            start = (x1-a+i, y1-b-i)
            end = (x1+a+i, y1+b-i)
            paths.append(Road(start, end))
        return paths

    def __init__(self, location, roads, config={}):
        self.location = location
        self.roads = roads
        self.paths = self.create_paths(self.location, self.roads[0].angle_sin, self.roads[0].angle_cos)

    def set_default_config(self):
        pass

    def update(self):
        pedestrian_cross_time_len = 10
