from pyswip.prolog import Prolog

_ = 0
juego1 = [
    [_, 6, _, 1, _, 4, _, 5, _],
    [_, _, 8, 3, _, 5, 6, _, _],
    [2, _, _, _, _, _, _, _, 1],
    [8, _, _, 4, _, 7, _, _, 6],
    [_, _, 6, _, _, _, 3, _, _],
    [7, _, _, 9, _, 1, _, _, 4],
    [5, _, _, _, _, _, _, _, 2],
    [_, _, 7, 2, _, 6, 9, _, _],
    [_, 4, _, 5, _, 8, _, 7, _]
]

juego2 = [
    [_, _, 1, _, 8, _, 6, _, 4],
    [_, 3, 7, 6, _, _, _, _, _],
    [5, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, 5, _, _, _],
    [_, _, 6, _, 1, _, 8, _, _],
    [_, _, _, 4, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, 3],
    [_, _, _, _, _, 7, 5, 2, _],
    [8, _, 2, _, 9, _, 7, _, _]
]


def mostrarSudoku(table):
    print("".join(["/---", "----"*8, "\\"]))
    for row in table:
        print("".join(["|", "|".join(" %s " % (i or " ") for i in row), "|"]))
    print("".join(["\\---", "----"*8, "/"]))


def solucionar(sudoku):
    prolog.consult("sudoku.pl")
    juego = str(sudoku).replace("0", "_")
    solucion = list(prolog.query("JUEGO=%s,sudoku(JUEGO)" % juego, maxresult=1))
    if solucion:
        solucion = solucion[0]
        return solucion["JUEGO"]
    else:
        return False


def main():
    juego = juego2
    print("-- SUDOKU --")
    mostrarSudoku(juego)
    print()
    print(" -- SOLUCION --")
    solucion = solucionar(juego)
    if solucion:
        mostrarSudoku(solucion)
    else:
        print("El sudoku no tiene solución")


if __name__ == "__main__":
    prolog = Prolog()
    main()
