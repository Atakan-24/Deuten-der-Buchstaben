def deuten(buchstaben, woerterbuch):
    for wort in woerterbuch:
        if set(buchstaben) == set(wort):
            return wort
    return "Kein passendes Wort gefunden."

if __name__ == "__main__":
    # Beispiel-Wörterbuch
    woerterbuch = ["hallo", "welt", "python", "programmieren", "beispiel"]

    # Benutzereingabe entgegennehmen
    eingabe = input("Geben Sie Buchstaben ein: ").lower()

    # Deuten der Buchstaben
    ergebnis = deuten(eingabe, woerterbuch)

    # Ausgabe des Ergebnisses
    print("Deutung:", ergebnis)
