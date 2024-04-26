def deuten(buchstaben, woerterbuch):
    for wort in woerterbuch:
        if set(buchstaben) == set(wort):
            return wort
    return "Kein passendes Wort gefunden."

if __name__ == "__main__":
    # Wörterbuch
    woerterbuch = ["hallo", "welt", "python", "programmieren", "beispiel"]

    
    eingabe = input("Geben Sie wort ein vom wörterbuch: ").lower()

    # Deuten
    ergebnis = deuten(eingabe, woerterbuch)

    # Ausgabe 
    print("Deutung:", ergebnis)
