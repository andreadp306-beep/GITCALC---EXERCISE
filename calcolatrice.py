def addizione(x, y):
    """Restituisce la somma di x e y."""
    return x + y

def sottrazione(x, y):
    """Restituisce la differenza tra x e y."""
    return x - y

def moltiplicazione(x, y):
    """Restituisce il prodotto di x e y."""
    return x * y

def divisione(x, y):
    """Restituisce la divisione di x per y, gestendo la divisione per zero."""
    if y == 0:
        return "Errore! Impossibile dividere per zero."
    return x / y

print("--- Seleziona Operazione ---")
print("1. Addizione (+)")
print("2. Sottrazione (-)")
print("3. Moltiplicazione (*)")
print("4. Divisione (/)")
print("5. Esci")
print("----------------------------")

while True:
    # Richiedi l'input dell'utente
    scelta = input("Inserisci la tua scelta (1/2/3/4/5): ")

    # Controlla se la scelta è una delle operazioni valide
    if scelta in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except ValueError:
            print("Input non valido. Per favore, inserisci un numero.")
            continue # Torna all'inizio del ciclo

        if scelta == '1':
            risultato = addizione(num1, num2)
            print(f"{num1} + {num2} = {risultato}\n")

        elif scelta == '2':
            risultato = sottrazione(num1, num2)
            print(f"{num1} - {num2} = {risultato}\n")

        elif scelta == '3':
            risultato = moltiplicazione(num1, num2)
            print(f"{num1} * {num2} = {risultato}\n")

        elif scelta == '4':
            risultato = divisione(num1, num2)
            print(f"{num1} / {num2} = {risultato}\n")
    
    # Controlla se l'utente vuole uscire
    elif scelta == '5':
        print("Calcolatrice chiusa. Arrivederci!")
        break

    else:
        print("Scelta non valida. Riprova.")