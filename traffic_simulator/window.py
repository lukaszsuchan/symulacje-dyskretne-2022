import asyncio
import math
import pygame

class Window:
    def __init__(self, sim, config={}):
        # Simulation to draw
        self.sim = sim

        # Set default configurations
        self.set_default_config()

        # Update configurations
        for attr, val in config.items():
            setattr(self, attr, val)
        
    def set_default_config(self):
        """Set default configuration"""
        self.width = 1000
        self.height = 700
        self.bg_color = (9, 119, 48)

        self.fps = 60
        self.zoom = 5
        self.offset = (-163, 0)

        self.mouse_last = (0, 0)
        self.mouse_down = False
        self.min_zoom = 0


    async def loop(self, loop=None):
        """Shows a window visualizing the simulation and runs the loop function."""
        # Create a pygame window
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.flip()

        # Fixed fps
        clock = pygame.time.Clock()

        # Draw loop
        running = True
        while running:
            # Update simulation
            if loop: loop(self.sim)

            # Draw simulation
            self.draw()

            # Update window
            pygame.display.update()
            clock.tick(self.fps)

            # Handle all events
            for event in pygame.event.get():
                # Quit program if window is closed
                if event.type == pygame.QUIT:
                    running = False
                # Handle mouse events
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # If mouse button down
                    if event.button == 1:
                        # Left click
                        x, y = pygame.mouse.get_pos()
                        x0, y0 = self.offset
                        self.mouse_last = (x-x0*self.zoom, y-y0*self.zoom)
                        self.mouse_down = True
                    if event.button == 4:
                        # Mouse wheel up
                        self.zoom *= (self.zoom**2+self.zoom/4+1) / (self.zoom**2+1)
                    if event.button == 5:
                        # Mouse wheel down
                        if self.zoom > self.min_zoom:
                            self.zoom *= (self.zoom**2+1) / (self.zoom**2+self.zoom/4+1)
                elif event.type == pygame.MOUSEMOTION:
                    # Drag content
                    if self.mouse_down:
                        x1, y1 = self.mouse_last
                        x2, y2 = pygame.mouse.get_pos()
                        self.offset = ((x2-x1)/self.zoom, (y2-y1)/self.zoom)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False
            await asyncio.sleep(0)

    async def run(self, steps_per_update=1):
        """Runs the simulation by updating in every loop."""
        def loop(sim):
            sim.run(steps_per_update)

        await self.loop(loop)

    def convert(self, x, y=None):
        """Converts simulation coordinates to screen coordinates"""
        if isinstance(x, list):
            return [self.convert(e[0], e[1]) for e in x]
        if isinstance(x, tuple):
            return self.convert(*x)
        return (
            int(self.width/2 + (x + self.offset[0])*self.zoom),
            int(self.height/2 + (y + self.offset[1])*self.zoom)
        )

    def inverse_convert(self, x, y=None):
        """Converts screen coordinates to simulation coordinates"""
        if isinstance(x, list):
            return [self.convert(e[0], e[1]) for e in x]
        if isinstance(x, tuple):
            return self.convert(*x)
        return (
            int(-self.offset[0] + (x - self.width/2)/self.zoom),
            int(-self.offset[1] + (y - self.height/2)/self.zoom)
        )

    def own_convert(self, x, y=None):
        """Converts screen coordinates to simulation coordinates"""
        if isinstance(x, list):
            return [self.convert(e[0], e[1]) for e in x]
        if isinstance(x, tuple):
            return self.convert(*x)
        return (
            int(self.offset[0] + (x - self.width/2)/self.zoom),
            int(self.offset[1] + (y - self.height/2)/self.zoom)
        )


    def background(self, r, g, b):
        """Fills screen with one color."""
        self.screen.fill((r, g, b))

    def polygon(self, vertices, color):
        pygame.draw.polygon(self.screen, color, vertices)

    def rotated_box(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255), filled=True):
        """Draws a rectangle center at *pos* with size *size* rotated anti-clockwise by *angle*."""
        x, y = pos
        l, h = size

        if angle:
            cos, sin = math.cos(angle), math.sin(angle)
        
        vertex = lambda e1, e2: (
            x + (e1*l*cos + e2*h*sin)/2,
            y + (e1*l*sin - e2*h*cos)/2
        )

        if centered:
            vertices = self.convert(
                [vertex(*e) for e in [(-1,-1), (-1, 1), (1,1), (1,-1)]]
            )
        else:
            vertices = self.convert(
                [vertex(*e) for e in [(0,-1), (0, 1), (2,1), (2,-1)]]
            )

        self.polygon(vertices, color)

    def rotated_rect(self, pos, size, angle=None, cos=None, sin=None, centered=True, color=(0, 0, 255)):
        self.rotated_box(pos, size, angle=angle, cos=cos, sin=sin, centered=centered, color=color, filled=False)

    def arrow(self, pos, size, angle=None, cos=None, sin=None, color=(255, 255, 255)):
        if angle:
            cos, sin = math.cos(angle), math.sin(angle)
        
        self.rotated_box(
            pos,
            size,
            cos=(cos - sin) / math.sqrt(2),
            sin=(cos + sin) / math.sqrt(2),
            color=color,
            centered=False
        )

        self.rotated_box(
            pos,
            size,
            cos=(cos + sin) / math.sqrt(2),
            sin=(sin - cos) / math.sqrt(2),
            color=color,
            centered=False
        )

    def draw_roads(self):
        for road in self.sim.roads:
            # Draw road background
            self.rotated_box(
                road.start,
                (road.length, 3.7),
                cos=road.angle_cos,
                sin=road.angle_sin,
                color=(130, 130, 130),
                centered=False
            )

            def arange(start, end, step):
                i = start
                result = []
                while i <= end:
                    result.append(i)
                    i += step
                return result

            # Draw road arrow
            if road.length > 5: 
                for i in arange(-0.5*road.length, 0.5*road.length, 10):
                    pos = (
                        road.start[0] + (road.length/2 + i + 3) * road.angle_cos,
                        road.start[1] + (road.length/2 + i + 3) * road.angle_sin
                    )

                    self.arrow(
                        pos,
                        (-1.25, 0.2),
                        cos=road.angle_cos,
                        sin=road.angle_sin
                    )   

    def draw_vehicle(self, vehicle, road):
        l, h = vehicle.l,  2
        sin, cos = road.angle_sin, road.angle_cos

        x = road.start[0] + cos * vehicle.x 
        y = road.start[1] + sin * vehicle.x 

        self.rotated_box((x, y), (l, h), cos=cos, sin=sin, centered=True)

    def draw_bus(self, bus, road):
        l, h = 8, 2
        sin, cos = road.angle_sin, road.angle_cos

        x = road.start[0] + cos * bus.x
        y = road.start[1] + sin * bus.x

        self.rotated_box((x, y), (l, h), cos=cos, sin=sin,color=(255, 140, 0), centered=True)
    def draw_pedestrian(self, pedestrian, crossing):
        l, h = 1, 1
        sin, cos = crossing.paths[0].angle_sin, crossing.paths[0].angle_cos

        x = crossing.paths[0].start[0] + cos * pedestrian.x
        y = crossing.paths[0].start[1] + sin * pedestrian.x

        self.rotated_box((x, y), (l, h), cos=cos, sin=sin, color=(255, 0, 213), centered=True)

    def draw_vehicles(self):
        for road in self.sim.roads:
            # Draw vehicles
            for vehicle in road.vehicles:
                if vehicle.l == 4:
                    self.draw_vehicle(vehicle, road)

    def draw_buses(self):
        for road in self.sim.roads:
            # Draw bus
            for vehicle in road.vehicles:
                if vehicle.l == 8:
                    self.draw_bus(vehicle, road)

    def draw_pedestrians(self):
        for cross in self.sim.pedestrian_crossing:
            #Draw pedestrian
            for path in cross.paths:
                for pedestrian in path.vehicles:
                    self.draw_pedestrian(pedestrian, cross)

    def draw_signals(self):
        for signal in self.sim.traffic_signals:
            for i in range(len(signal.roads)):
                color = (0, 255, 0) if signal.current_cycle[i] else (255, 0, 0)
                for road in signal.roads[i]:
                    a = 0
                    position = (
                        (1-a)*road.end[0] + a*road.start[0],        
                        (1-a)*road.end[1] + a*road.start[1]
                    )
                    self.rotated_box(
                        position,
                        (1, 3),
                        cos=road.angle_cos, sin=road.angle_sin,
                        color=color)

    def draw_pedestrian_crossing(self):
        for cross in self.sim.pedestrian_crossing:
            for i in range(0, 20, 4):
                self.rotated_box(
                    (cross.location[0], cross.location[1] - 8 + i),
                    (6, 2),
                    cos=cross.roads[0].angle_cos, sin=cross.roads[0].angle_sin,
                    color=(255, 255, 255))
            for i in range(-2, 20, 4):
                self.rotated_box(
                    (cross.location[0], cross.location[1] - 8 + i),
                    (6, 2),
                    cos=cross.roads[0].angle_cos, sin=cross.roads[0].angle_sin,
                    color=(128, 128, 128))

    def draw(self):
        # Fill background
        self.background(*self.bg_color)
        img = pygame.image.load('assets/background.jpg')
        img.convert()
        scale_x = int(self.width*self.zoom)
        scale_y = int(self.height*self.zoom)
        x_end, y_end = self.own_convert(self.width, self.height)
        img = pygame.transform.scale(img, (scale_x, scale_y))
        self.screen.blit(img, ((x_end-170)*self.zoom, (y_end-353)*self.zoom))

        self.draw_roads()
        self.draw_pedestrian_crossing()
        self.draw_vehicles()
        self.draw_buses()
        self.draw_pedestrians()
        self.draw_signals()
