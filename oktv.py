# --------------------------------------------megoldas----------------------------------------------
def count_parachutes(n, m, heights):
    MOD = 10**9 + 7

    # dp1[i][j] - Hányféle módon repülhet el i, j-ról pontosan 1 átrepüléssel
    dp1 = [[0] * m for _ in range(n)]

    # dp2[i][j] - Hányféle módon repülhet el i, j-ról pontosan 2 átrepüléssel
    dp2 = [[0] * m for _ in range(n)]

    # dp_all[i][j] - Hányféle módon repülhet el i, j-ról bármilyen számú átrepüléssel
    dp_all = [[0] * m for _ in range(n)]

    # Számítsuk ki az egyes csúcsokból induló lehetséges repüléseket
    # Először azokat, ahol pontosan egy átrepülés van.
    for i in range(n):
        for j in range(m):
            # Repülés egy másik csúcsra azonos sorban vagy oszlopban
            for k in range(n):
                if heights[k][j] < heights[i][j]:
                    dp1[i][j] += 1
                if heights[i][k] < heights[i][j]:
                    dp1[i][j] += 1

    # Két repüléses utak
    for i in range(n):
        for j in range(m):
            if dp1[i][j] > 0:
                dp2[i][j] += dp1[i][j]

    # Maximum párosítás és összes valid utak
    for i in range(n):
        for j in range(m):
            dp_all[i][j] += dp1[i][j] + dp2[i][j]

    # Eredmények kiírása
    print("Pontos 1 átrepüléssel elérhető utak száma:", dp1)
    print("Pontos 2 átrepüléssel elérhető utak száma:", dp2)
    print("Összes lehetséges repülési mód:", dp_all)


# Bemenet:
height = [[1, 1, 3, 5], [1, 1, 1, 4], [9, 2, 7, 6]]

# Függvény meghívása a bemenettel
count_parachutes(3, 4, height)


# ----------------------------------------------teszt------------------------------------------


def is_valid_move(current, next_point):
    """Ellenőrzi, hogy az átugrott csúcs magasabb-e, mint a célpont."""
    return next_point < current


def count_possible_moves(n, m, height):
    """Számolja, hány lehetséges repülési mód van 1 és 2 átrepüléssel."""
    # Kezdjük a repülés számolását minden csúcsról
    moves_1 = 0
    moves_2 = 0
    total_moves = 0

    for i in range(n):
        for j in range(m):
            # Minden csúcsra megnézzük az összes lehetséges célt
            current_height = height[i][j]
            # Átvizsgáljuk a sorokat és oszlopokat is
            # 1. átrepülés
            for k in range(i + 1, n):  # sorok alatt
                if is_valid_move(current_height, height[k][j]):
                    moves_1 += 1
            for k in range(j + 1, m):  # oszlopok alatt
                if is_valid_move(current_height, height[i][k]):
                    moves_1 += 1

            # 2. átrepülés: Keresünk még egy további lehetséges csúcsot
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    if is_valid_move(current_height, height[k][l]):
                        moves_2 += 1

    # Összesen a lehetséges repülési mód
    total_moves = moves_1 + moves_2

    return moves_1, moves_2, total_moves


# Tesztelés a fenti 10 esetre
test_cases = [
    {"height": [[1, 1, 3, 5], [1, 1, 1, 4], [9, 2, 7, 6]]},
    {"height": [[4, 1, 2], [6, 7, 3], [5, 8, 6], [9, 4, 2]]},
    {"height": [[1, 2], [2, 1]]},
    {"height": [[5, 3, 8], [6, 4, 2], [1, 9, 7]]},
    {"height": [[3, 3, 3], [3, 3, 3], [3, 3, 3]]},
    {
        "height": [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
    },
    {"height": [[2, 3, 4], [5, 6, 7], [8, 9, 10]]},
    {"height": [[3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]},
    {"height": [[1, 2, 3], [4, 5, 6]]},
    {"height": [[1, 3], [2, 4], [5, 6]]},
]

# Tesztelés minden bemeneti esetre
for i, test_case in enumerate(test_cases):
    height = test_case["height"]
    n = len(height)
    m = len(height[0]) if n > 0 else 0
    moves_1, moves_2, total_moves = count_possible_moves(n, m, height)

    print(f"\nTeszt {i+1}:")
    print("Bemeneti magasság mátrix:")
    for row in height:
        print(row)

    print(f"Pontos 1 átrepüléssel elérhető utak száma: {moves_1}")
    print(f"Pontos 2 átrepüléssel elérhető utak száma: {moves_2}")
    print(f"Összes lehetséges repülési mód: {total_moves}")
