#!/bin/python3
# By Jonathan Schleucher @Imathnathan
# Solves 2x2 Linear equations, both with and without pivoting


from decimal import *


# Setze Dezimalstellen auf vier
getcontext().prec = 4

# Setze A
A = [[0, 0], [0, 0]]
A[0][0] = Decimal(input())
A[0][1] = Decimal(input())
A[1][0] = Decimal(input())
A[1][1] = Decimal(input())
# Setze b
b = [0, 0]
b[0] = Decimal(input())
b[1] = Decimal(input())

# shallow copy in gespeicherten input und Pivotvariante
APivot = [val for val in A]
Ain = [val for val in A]
bPivot = [val for val in b]
Bin = [val for val in b]

# Führe spalten pivotisierung für APivot aus.
if APivot[0][0] < APivot[1][0]:
    # Tausche Zeilen von APivot und bPivot
    APivot[0], APivot[1], bPivot[0], bPivot[1] = ((APivot[1], APivot[0],
                                                   bPivot[1], bPivot[0]))
print("Pivotisierung")
print(A, b)
print(APivot, bPivot)

# Gauss Stufenform herstellen
for vec, mat in ((b, A), (bPivot, APivot)):
    print(f"A21/A11 = {mat[1][0] / mat[0][0]}")
    vec[1] = vec[1] - vec[0] * mat[1][0] / mat[0][0]
for mat in (A, APivot):
    mat[1] = [mat[1][0] - mat[0][0] * mat[1][0] / mat[0][0],
              mat[1][1] - mat[0][1] * mat[1][0] / mat[0][0]]
print("Stufenform")
print(A, b)
print(APivot, bPivot)

# Gauss zweite Zeile normalisieren
for vec, mat in ((b, A), (bPivot, APivot)):
    vec[1] = vec[1] / mat[1][1]
for mat in (A, APivot):
    mat[1] = [mat[1][0] / mat[1][1], mat[1][1] / mat[1][1]]
print("Normalisierte 2. Zeile")
print(A, b)
print(APivot, bPivot)

# Gauss rücksubstitution
for vec, mat in ((b, A), (bPivot, APivot)):
    vec[0] = vec[0] - vec[1] * mat[0][1] / mat[1][1]
for mat in (A, APivot):
    mat[0] = [mat[0][0] - mat[1][0] * mat[0][1] / mat[1][1],
              mat[0][1] - mat[1][1] * mat[0][1] / mat[1][1]]
print("Rücksubstitution")
print(A, b)
print(APivot, bPivot)


# Gauss erste Zeile normalisieren
for vec, mat in ((b, A), (bPivot, APivot)):
    vec[0] = vec[0] / mat[0][0]
for mat in (A, APivot):
    mat[0] = [mat[0][0] / mat[0][0], mat[0][1] / mat[0][0]]
print("Erste Zeile normalisiert.")
print(A, b)
print(APivot, bPivot)


print(f"A input = {Ain}")
print(f"b input = {Bin}")
print(f"x_1 = {b[0]}")
print(f"x_2 = {b[1]}")
print(f"x_1 Pivot = {bPivot[0]}")
print(f"x_2 Pivot = {bPivot[1]}")
