import random

def estraiNumero(n):
    return random.randint(1, n)

def main():
    nMax = 10

    try:
        nMax = int(input(f"Inserisci il numero massimo con cui vuoi giocare (default {nMax}): ") or nMax)
    except ValueError:
        print("Input non valido. Verrà usato il valore di default. Per la prossima volta, inserisci un numero intero.")

    n = estraiNumero(nMax)
    media = (n + nMax) / 2
    tentativi = 0
    tentativiMax = int(media) - (int(media) // 2)
    rigioca = 's'

    while True:
        while rigioca == 's':
            try:
                guess = int(input(f"Prova a vincere, inserisci un numero tra 1 e {nMax} (tentativi Max: {tentativiMax}): "))
            except ValueError:
                print("Devi inserire un numero!")
                continue

            if guess < 1 or guess > nMax:
                print("Numero non valido. Riprova.")
                continue

            tentativi += 1

            if guess == n:
                print("Hai indovinato!")
                print(f"Hai impiegato {tentativi} tentativi.")
                rigioca = input("Vuoi rigiocare? (s/n): ")
                if rigioca == 's':
                    tentativi = 0
                    n = estraiNumero()
                    continue
            else:
                print("Hai sbagliato.")
                if tentativi >= tentativiMax:
                    print(f"Hai esaurito i tentativi. Il numero era {n}.")
                    rigioca = input("Vuoi rigiocare? (s/n): ")
                    if rigioca == 's':
                        tentativi = 0
                        n = estraiNumero()
                        continue
                if guess < n:
                    print("Consiglio: il numero è più grande.")
                else:
                    print("Consiglio: il numero è più piccolo.")

        break

if __name__ == "__main__":
    main()