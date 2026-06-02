from underground import generate_map, print_map


def heuristics(start_location: tuple[int, int], end_location: tuple[int, int]) -> int:
    x1, y1 = start_location
    x2, y2 = end_location
    return abs(x1 - x2) + abs(y1 - y2)


def choice(neighbours: set[tuple[int, int]], knowledge: dict[tuple[int, int], int]) -> tuple[int, int]:
    best = None
    best_score = float("inf")

    for n in neighbours:
        score = heuristics(n, end_position)

        # kara za odwiedzone
        if n in knowledge:
            score += 2

        # kara za ryzykowne pola
        if is_wind(n, underground, range_x, range_y):
            score += 3

        if score < best_score:
            best_score = score
            best = n

    if best is None:
        return neighbours.pop()

    neighbours.remove(best)
    return best


def possible_neighbours(cur_field: tuple[int, int], range_x: int, range_y: int) -> list[tuple[int, int]]:
    temp_neighbours = []
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for offset in offsets:
        x_neigh = cur_field[0] + offset[0]
        y_neigh = cur_field[1] + offset[1]

        if x_neigh < 0 or y_neigh < 0 or x_neigh == range_x or y_neigh == range_y:
            continue

        temp_neighbours.append((x_neigh, y_neigh))

    return temp_neighbours


def is_hole(cur_field: tuple[int, int], holes: set[tuple[int, int]]) -> bool:
    return cur_field in holes


def is_wind(cur_field: tuple[int, int], holes: set[tuple[int, int]], range_x: int, range_y: int) -> bool:
    for neighbour in possible_neighbours(cur_field, range_x, range_y):
        if neighbour in holes:
            return True
    return False


#parametry
runs = 50000

success = 0
fail = 0

range_x, range_y = 7, 7

for _ in range(runs):

    underground = generate_map(range_x, range_y)

    knowledge: dict[tuple[int, int], int] = {}
    start_position = (0, 0)
    end_position = (range_x - 1, range_y - 1)

    neighbours = {start_position}
    visited = set()

    reached = False
    died = False

    while True:
        if len(neighbours) == 0:
            break

        current = choice(neighbours, knowledge)
        visited.add(current)

        if is_hole(current, underground):
            died = True
            break

        if current == end_position:
            reached = True
            break

        if is_wind(current, underground, range_x, range_y):
            knowledge[current] = 1
        else:
            knowledge[current] = 0

        new_possible_neighbours = {
            x for x in possible_neighbours(current, range_x, range_y)
            if x not in visited and x not in neighbours
        }

        for n in new_possible_neighbours:
            neighbours.add(n)

    if reached:
        success += 1
    else:
        fail += 1


print("\n--- STATYSTYKI ---")
print("Próby:", runs)
print("Sukcesy:", success)
print("Porażki:", fail)
print("Success rate:", round(success / runs, 3))
print("\nprzykładowa mapa")

underground = generate_map(range_x, range_y)

knowledge = {}
neighbours = {(0, 0)}
visited = set()

while len(neighbours) > 0:
    current = choice(neighbours, knowledge)
    visited.add(current)

    if is_hole(current, underground):
        break

    if is_wind(current, underground, range_x, range_y):
        knowledge[current] = 1
    else:
        knowledge[current] = 0

    for n in possible_neighbours(current, range_x, range_y):
        if n not in visited:
            neighbours.add(n)

print_map(underground, range_x, range_y, list(visited))