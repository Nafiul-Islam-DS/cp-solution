#https://codeforces.com/gym/606173/problem/F
car = {"a": 74,
    "b": 73,
    "c": 72,
    "d": 71,
    "e": 70,
    "f": 69,
    "g": 68,
    "h": 67,
    "i": 66,
    "j": 65,
    "k": 64,
    "l": 63,
    "m": 62,
    "n": 61,
    "o": 60,
    "p": 59,
    "q": 58,
    "r": 57,
    "s": 56,
    "t": 55,
    "u": 54,
    "v": 53,
    "w": 52,
    "x": 51,
    "y": 50,
    "z": 49,

    "A": 100,
    "B": 99,
    "C": 98,
    "D": 97,
    "E": 96,
    "F": 95,
    "G": 94,
    "H": 93,
    "I": 92,
    "J": 91,
    "K": 90,
    "L": 89,
    "M": 88,
    "N": 87,
    "O": 86,
    "P": 85,
    "Q": 84,
    "R": 83,
    "S": 82,
    "T": 81,
    "U": 80,
    "V": 79,
    "W": 78,
    "X": 77,
    "Y": 76,
    "Z": 75
    }

R = int(input())
ron = input()
mes = input()
ronpoint = 0
mespoint = 0
for i in range(R):
    ronpoint +=car[ron[i]]
    mespoint += car[mes[i]]
if ronpoint==mespoint:
    print("Both")
else:
    if ronpoint > mespoint:
        print("Ronaldo")
    else:
        print("Messi")