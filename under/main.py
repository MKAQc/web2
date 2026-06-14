from underground import generate_map, print_map #mapa z dziurami+rys

#heur
def heuristics(start_location: tuple[int, int], end_location: tuple[int, int]) -> int:#jak daleko do celu, para, zwraca liczbę
    x1, y1 = start_location
    x2, y2 = end_location
    return abs(x1 - x2) + abs(y1 - y2)#wart bezwzgl, dystans kratkami

#funkcja wyboru ruchu
def choice(neighbours: set[tuple[int, int]], knowledge: dict[tuple[int, int], int]) -> tuple[int, int]:#zbiór bez dupli, słownik (pamięćAI)
    best = None#brak wart
    best_score = float("inf")#najg wynik-niesk

    for n in neighbours:#pętla po all możl ruchach
        score = heuristics(n, end_position)#im bliżej celu tym lepiej (mn score)

        # kara za odwiedzone
        if n in knowledge:
            score += 2

        # kara za ryzykowne pola
        if is_wind(n, underground, range_x, range_y):
            score += 3
        #wybór naj ruchu
        if score < best_score:
            best_score = score
            best = n

    if best is None:#awaryjnie-losowy ruch
        return neighbours.pop()#usuwa i zwraca element ze zbioru
    #usuwa wybrany ruch i go zwraca
    neighbours.remove(best)
    return best

#sąsiedzi
def possible_neighbours(cur_field: tuple[int, int], range_x: int, range_y: int) -> list[tuple[int, int]]:#generuje ruchy (4 możliwe)
    temp_neighbours = []
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]#kierunki

    for offset in offsets:
        x_neigh = cur_field[0] + offset[0]
        y_neigh = cur_field[1] + offset[1]

        if x_neigh < 0 or y_neigh < 0 or x_neigh == range_x or y_neigh == range_y:#spr granice mapy
            continue

        temp_neighbours.append((x_neigh, y_neigh))

    return temp_neighbours

#dziury-czy pole to dziura, in-czy należy do zbioru
def is_hole(cur_field: tuple[int, int], holes: set[tuple[int, int]]) -> bool:
    return cur_field in holes

#wiatr-spr czy obok dziura
def is_wind(cur_field: tuple[int, int], holes: set[tuple[int, int]], range_x: int, range_y: int) -> bool:
    for neighbour in possible_neighbours(cur_field, range_x, range_y):#spr sąsiadów
        if neighbour in holes:#jeśli któryś sąsiad to dziura - wiatr
            return True
    return False


#parametry
runs = 50000
#liczniki
success = 0
fail = 0

range_x, range_y = 5, 5

for _ in range(runs):

    underground = generate_map(range_x, range_y)#losowa mapa

    knowledge: dict[tuple[int, int], int] = {}#pamięć AI: klucz: pole, wartość: 0 = safe, 1 = wind, -9 = hole
    start_position = (0, 0)
    end_position = (range_x - 1, range_y - 1)

    neighbours = {start_position}
    visited = set()

    reached = False
    died = False

    while True:#niesk pętla (/break)
        if len(neighbours) == 0:#brak ruchów-koniec
            break

        current = choice(neighbours, knowledge)#wybór nast ruchu
        visited.add(current)

        if is_hole(current, underground):#wpadła-koniec
            died = True
            break

        if current == end_position:#dotarła-sukces
            reached = True
            break
        #zapis wiedzy
        if is_wind(current, underground, range_x, range_y):
            knowledge[current] = 1
        else:
            knowledge[current] = 0
        #tw nowe ruchy (nodwiedz, n w kolej)
        new_possible_neighbours = {
            x for x in possible_neighbours(current, range_x, range_y)
            if x not in visited and x not in neighbours
        }

        for n in new_possible_neighbours:
            neighbours.add(n)#dod nowe opcje ruchu
    #liczenie wyników
    if reached:
        success += 1
    else:
        fail += 1

print("\n--- STATYSTYKI ---")
print("Próby:", runs)
print("Sukcesy:", success)
print("Porażki:", fail)
print("Success rate:", round(success / runs, 3))#wynik-dzieli sukces przez próby, 3msca po przec
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