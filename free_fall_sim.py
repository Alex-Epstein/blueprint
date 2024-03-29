import pymunk, pygame, sys, random

BLACK = pygame.Color("black")
GREY = pygame.Color("grey")
WHITE = pygame.Color("white")

def init():
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0, 98.1)
    return screen, clock, space

def create_circle(space, mass=10, moment=100, x=400, y=0, radius=40, nudge_x=False):
    body = pymunk.Body(mass, moment, pymunk.Body.DYNAMIC)
    body.position = (x, y)
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    if nudge_x:
        body.apply_force_at_local_point((random.randrange(-100 * mass, 100 * mass), 0))
    return shape

def draw_circles(screen, circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen, GREY, (pos_x, pos_y), circle.radius)

def create_bound(space, a_x, a_y, b_x, b_y, radius):
    body = pymunk.Body(0, 0, pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (a_x, a_y), (b_x, b_y), radius)
    space.add(body, shape)
    return shape

def draw_bounds(screen, bounds):
    for bound in bounds:
        a_x = int(bound.a.x)
        a_y = int(bound.a.y)
        b_x = int(bound.b.x)
        b_y = int(bound.b.y)
        pygame.draw.line(screen, BLACK, (a_x, a_y), (b_x, b_y), int(bound.radius))

def run(screen, clock, space, circles, bounds):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        draw_circles(screen, circles)
        draw_bounds(screen, bounds)
        space.step(1.0/60.0)
        pygame.display.update()
        pygame.display.set_caption("fps: " + str(clock.get_fps()))
        clock.tick(120)

def slope(screen, clock, space):
    circles = []
    circles.append(create_circle(space, x=700, nudge_x=True))
    bounds = []
    bounds.append(create_bound(space, 400, 500, 700, 400, 10))
    run(screen, clock, space, circles, bounds)

def scatter(screen, clock, space, num_circles=100):
    circles = []
    for _ in range(num_circles):
        circles.append(create_circle(space, 1, 10, random.randint(100, 700), random.randint(0, 100), 15, False))
    bounds = []
    bounds.append(create_bound(space, 100, 700, 700, 700, 5))
    bounds.append(create_bound(space, 50, 400, 100, 700, 5))
    bounds.append(create_bound(space, 700, 700, 750, 400, 5))
    run(screen, clock, space, circles, bounds)

def main():
    screen, clock, space = init()
    scatter(screen, clock, space, 300)

if __name__ == "__main__":
    main()