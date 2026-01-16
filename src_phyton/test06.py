import random

def estraiNumero(n):
    return random.randint(1, n)

def chiedi_nMax(default):
    try:
        return int(input(f"Inserisci il numero massimo (default {default}): ") or default)
    except ValueError:
        print("Input non valido, uso il valore di default.")
        return default

def main():
    nMax = 10
    rigioca = 's'

    while rigioca == 's':
        nMax = chiedi_nMax(nMax)
        n = estraiNumero(nMax)

        media = (n + nMax) / 2
        tentativiMax = int(media) - (int(media) // 2)
        tentativi = 0

        while tentativi < tentativiMax:
            try:
                guess = int(input(f"Inserisci un numero tra 1 e {nMax} (tentativi rimasti: {tentativiMax - tentativi}): "))
            except ValueError:
                print("Devi inserire un numero!")
                continue

            if guess < 1 or guess > nMax:
                print("Numero fuori intervallo.")
                continue

            tentativi += 1

            if guess == n:
                print(f"Hai indovinato in {tentativi} tentativi!")
                break
            elif guess < n:
                print("Il numero è più grande.")
            else:
                print("Il numero è più piccolo.")

        else:
            print(f"Hai perso! Il numero era {n}")

        rigioca = input("Vuoi giocare di nuovo? (s/n): ").lower()

    print("Grazie per aver giocato!")

if __name__ == "__main__":
    main()
