# Abinfo_Barro
Nel repository sono presenti gli script bash(installazione.sh e esecuzione.sh) e lo script python(analisi.py) necessari all'installazione e all'esecuzione dell'applicazione. Di seguito riporto una breve descrizione dei file e le istruzioni per installazione e esecuzione dell'applicazione.

DESCRIZIONE DEI FILE
- installazione.sh: si occupa dell'installazione dell'applicazione. Esso crea una directory chiamata App_Barro sulla home e copia all'interno esecuzione.sh e analisi.py. Attribuisce il permesso di esecuzione a esecuzione.sh, aggiunge la nuova directory al path di sistema e al pythonpath e, infine, stampa su terminale un messaggio di completamento dell'installazione.

- esecuzione.sh: si occupa dell'esecuzione dell'applicazione. Esso scarica da Github il file Nemo_6670.dat, stampa sul terminale un messaggio per controllare se il download ha avuto successo e infine esegue analisi.py dando Nemo_6670.dat come input.

- analisi.py: si occupa dell'analisi dei dati di Nemo_6670.dat. Prende come input il Nemo_6670.dat dato da esecuzione.sh, apre il file e immagazzina i dati di Magnitudine assoluta, codice colore, età, magnetizzazione e massa delle stelle creando un array per ognuna di queste grandezze fisiche. Riordina gli array di dati in sottogruppi divisi in base all'età delle stelle e produce quattro grafici che vengono proiettati sullo schermo e contemporaneamente salvati nella cartella App_Barro all'esecuzione dell'applicazione.

I grafici creati sono:

Diagramma Magnitudine assoluta-indice a colore (in leggenda si leggono gli intervalli di età in cui sono stati divisi i dati con il colore con cui vengono rappresentati. Ogni sottogruppo ha un colore diverso); 

Istogramma della metallicità delle stelle(Le stelle sono state divise in tre popolazioni in base a tre diverse fasce d'età e in figura sono rappresentati gli istogrammi relativi ai sottogruppi con diverso colore. In figura ci sono anche i valori di media e mediana relativi a ogni sottogruppo);

Plot della metallicità in funzione della massa(Le stelle sono state divise nelle stesse tre popolazioni del grafico precedente e il colore dei sottogruppi è lo stesso del grafico precedente);

Istogramma 2D per la relazione tra metallicità e massa.

ISTRUZIONI SU COME UTILIZZARE L'APPLICAZIONE:
- scarica installazione.sh, esecuzione.sh e analisi.py dal repository
- apri la cartella dei download dove sono stati scaricati i tre script e apri un terminale bash che ha la stessa directory della cartella dei download(dentro la cartella dei download tasto dx>Open in terminal)
- digita "chmod +x" installazione.sh da terminale per dare il permesso di esecuzione a esecuzione.sh
- digita "./installazione.sh" da terminale: si è creata una cartella App_Barro sulla Home e appare un messaggio di installazione andata a buon fine sul terminale. L'app è installata.
- apri la cartella App_Barro sulla home e apri un terminale con questa directory (dentro la cartella tasto dx>Open in terminal)
- digita sul nuovo terminale "./esecuzione.sh": l'applicazione ora viene eseguita. Appare un messaggio sul terminale di download del file di dati avvenuto con successo e appare sullo schermo il primo grafico.
- cliccare la x in alto a destra per chiudere il primo grafico e in automatico appare il secondo. Iterare il procedimento fino all'esaurimento dei grafici.
Quando l'app crea un grafico lo salva nella cartella dunque una volta chiusi tutti i grafici potremo trovarli salvati nella cartella App_Barro con i nomi "fig_1.png", "fig_2.png", "fig_3.png", "fig_4.png".

Ho aggiunto anche il Jupyter notebook analisi.ipynb corrispondente allo script analisi.py in caso si volesse leggere il codice direttamente dal notebook. 
