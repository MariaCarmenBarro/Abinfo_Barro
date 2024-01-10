#!/bin/bash

# Scarica il file Nemo_6670.dat da GitHub
wget https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat -O Nemo_6670.dat

# Controlla se il download è avvenuto con successo
if [ $? -eq 0 ]; then
    echo "File Nemo_6670.dat scaricato con successo."
else
    echo "Errore durante il download del file Nemo_6670.dat."
fi

# Esegue lo script Python passando il nome del file come input
python3 analisi.py Nemo_6670.dat

