import random

def generate_map(range_x: int = 5, range_y: int = 5) -> set[tuple[int, int]]:
    holes = set()
    no_holes = {
        (0, 0), (1, 0), (0, 1),
        (range_x-1, range_y-1),
        (range_x-2, range_y-1),
        (range_x-1, range_y-2)
    }

    for _ in range(4):
        while True:
            x_i = random.randint(0, range_x-1)
            y_i = random.randint(0, range_y-1)
            hole = (x_i, y_i)

            if hole in holes or hole in no_holes:
                continue

            holes.add(hole)
            break

    return holes


def representation(location: tuple[int, int], range_x: int, range_y: int,
                   holes: set[tuple[int, int]], crawler_path: list[tuple[int, int]]) -> str:

    is_hole = location in holes
    is_path = location in crawler_path

    neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neigh_is_hole = False

    for n in neigh:
        x_n = location[0] + n[0]
        y_n = location[1] + n[1]

        if 0 <= x_n < range_x and 0 <= y_n < range_y:
            if (x_n, y_n) in holes:
                neigh_is_hole = True

    if is_hole:
        return "X" if is_path else "o"
    elif is_path:
        return "≅" if neigh_is_hole else "~"
    elif neigh_is_hole:
        return "="
    else:
        return " "


def print_map(holes: set[tuple[int, int]], range_x: int = 5,
              range_y: int = 5, crawler_path: list[tuple[int, int]] = []):

    for y in range(range_y):
        s = ""
        for x in range(range_x):
            f = representation((x, y), range_x, range_y, holes, crawler_path)
            s += "[" + f + "]"
        print(s)


if __name__ == "__main__":
    print_map(generate_map())