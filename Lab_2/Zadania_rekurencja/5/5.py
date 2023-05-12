def hanoi(n, aktualny, docelowy, roboczy):
  if n > 0:
      hanoi(n-1, aktualny, roboczy, docelowy)
      print(aktualny, "->", docelowy)
      hanoi(n-1, roboczy, docelowy, aktualny)

n = int(input('Podaj liczbę krążków: '))
hanoi(n, "A", "B", "C")