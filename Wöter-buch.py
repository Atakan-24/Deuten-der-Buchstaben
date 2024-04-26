def deuten(buchstaben, woerterbuch):
    for wort in woerterbuch:
        if set(buchstaben) == set(wort):
            return wort
    return "Kein passendes Wort gefunden."

if __name__ == "__main__":
    # Wörterbuch
    woerterbuch = ["hallo", "welt", "python", "code", "auto" , "lol" , "bad", "win" , "kp", "brot"]

    while True:
        eingabe = input("Geben Sie ein Wort ein vom Wörterbuch oder 'x' zum Beenden: ").lower()

        if eingabe == 'x':
            print("Programm wird beendet.")
            break

        # Deuten
        ergebnis = deuten(eingabe, woerterbuch)

        # Ausgabe 
        print("Gefundenes Wort:", ergebnis)

