#!/bin/bash

# Specifica il nome della directory di destinazione
app_dir="$HOME/App_Barro"

# Crea una nuova directory (se non esiste già)
mkdir -p "$app_dir"

# Copia i file esecuzione.sh e analisibase.py nella nuova directory
cp esecuzione.sh analisi.py "$app_dir"

# Assegna i permessi di esecuzione al file esecuzione.sh
chmod +x "$app_dir/esecuzione.sh"

# Aggiungi la nuova directory al PYTHONPATH solo se non è già presente
if [[ ":$PYTHONPATH:" != *":$app_dir:"* ]]; then
    echo "export PYTHONPATH=\"$app_dir:\$PYTHONPATH\"" >> "$HOME/.bashrc"
    source "$HOME/.bashrc"
fi

# Aggiungi la nuova directory al PATH di sistema solo se non è già presente
if [[ ":$PATH:" != *":$app_dir:"* ]]; then
    echo "export PATH=\"$app_dir:\$PATH\"" >> "$HOME/.bashrc"
    source "$HOME/.bashrc"
fi

# Fornisci un messaggio di completamento
echo "Installazione completata. Ora troverai su home la cartella 'App_Barro'. Esegui l'applicazione entrando nella cartella, aprendo un terminale e digitando il comando per l'esecuzione './esecuzione.sh' "

