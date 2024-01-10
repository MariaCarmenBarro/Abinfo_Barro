#!/usr/bin/env python
# coding: utf-8

# ## Programma abilità informatiche_ Maria Carmen Barro

# In[1]:


import sys
import numpy as np
import matplotlib.pyplot as plt

#1): Apertura del file di dati e creazione degli array con i dati delle colonne

#Apro il file di dati
def main(file_path):
    # Usa il nome del file passato come argomento
    dati = file_path
    
    #inizializza le liste per i dati
    M_ass = []
    b_y = []
    age_parent = []
    MsuH = []
    m_ini = []

    #apre il file di dati
    try:
        with open(dati, 'r') as ppf:
            header = ppf.readline()  # salta la prima riga del file (header)
            for line in ppf:
                line = line.strip()
                columns = line.split()
        
                #inserisce i dati del file nelle liste
                M_ass.append(float(columns[4]))
                b_y.append(float(columns[8]))
                age_parent.append(float(columns[12]))
                MsuH.append(float(columns[0]))
                m_ini.append(float(columns[1]))

            # Trasforma le liste in array
            M_ass_array = np.array(M_ass)
            b_y_array = np.array(b_y)
            age_parent_array = np.array(age_parent)
            MsuH_array = np.array(MsuH)
            m_ini_array = np.array(m_ini)
     
            #2): Plot (b-y, M_ass)
         
            # Definisco gli intervalli di età in cui voglio suddividere i dati
            intervalli1 = [0, 0.05, 0.11, 0.18, 0.25, 0.33, 0.41, 0.51, 0.61, 0.73, 0.85, 0.99, 1.14, 1.30, 1.48, 1.68, 1.89, 2.13, 2.39, 2.67, 2.99, 3.33, 3.70, 4.12, 4.57, 5.06, 5.60, 6.20, 6.85, 7.57, 8.35, 9.21, 10.15, 11.19, 12.32, 13.56 ]  # Esempio di intervalli personalizzati
 
            #Riordino i dati in sottogruppi divisi per età:
            #inizializzo due liste 
            M_ass_ordinated = [[] for _ in range(len(intervalli1) - 1)]
            b_y_ordinated = [[] for _ in range(len(intervalli1) - 1)]
    
            for i in range(len(intervalli1) - 1):
                lower_age = intervalli1[i]
                upper_age = intervalli1[i+1]
                indices = np.where((age_parent_array >= lower_age) & (age_parent_array < upper_age))
            
                M_ass_ordinated[i] = M_ass_array[indices]
                b_y_ordinated[i] = b_y_array[indices]
        
            # Plot dei dati con colori diversi per ogni valore di i utilizzando una colormap predefinita
            plt.figure(figsize=(14, 11))
        
            num_subsets = len(M_ass_ordinated) #numero dei sottogruppi che voglio plottare
            colormap = plt.cm.gist_ncar  # Scegliamo la colormap 

            for i in range(num_subsets):
                color = colormap(i / num_subsets)  # Utilizzo la colormap per ottenere un colore diverso per ogni valore di i
                plt.scatter( b_y_ordinated[i], M_ass_ordinated[i], color=color, label=f'{intervalli1[i]} Gyr - {intervalli1[i+1]} Gyr', s=5)

            plt.xlabel('b-y')
            plt.ylabel('M$_{v}$')
            plt.title('Diagramma colore-magnitudine')
            plt.legend()
        
            # Setto il range delle x e delle y e inverto l'asse y come in figura nella consegna
            plt.xlim(-0.1, 1)
            plt.gca().invert_yaxis() #inverte l'asse y
            plt.ylim(9, -4)
        
            plt.savefig('fig_1.png', bbox_inches='tight') # salva il plot come immagine    
            plt.show() #mostra il grafico da terminale
        
        
            #3): Istogrammi MsuH con calcolo di media e mediana
        
            # Definisco gli intervalli di età in cui voglio suddividere i dati
            intervalli2 = [0, 1, 5, 13] #è stato controllato che non ci siano stelle con età superiore a 13
        
            #Riordino i dati in sottogruppi divisi per età:
            #inizializzo due liste
            MsuH_ordinated = [[] for _ in range(len(intervalli2) - 1)]
            m_ini_ordinated = [[] for _ in range(len(intervalli2) - 1)]
            for i in range(len(intervalli2) - 1):
                lower_age = intervalli2[i]
                upper_age = intervalli2[i + 1]
                indices = np.where((age_parent_array >= lower_age) & (age_parent_array < upper_age))
    
                MsuH_ordinated[i] = MsuH_array[indices]
                m_ini_ordinated[i] =m_ini_array[indices]
        
            #calcolo media e mediana:
            #inizializzo liste per media e mediana
            mean = []
            median = []
        
            #calcolo media e mediana per ogni sottogruppo e le inserisco nelle rispettive liste
            for i in range(len(MsuH_ordinated)):
                subgroup_mean = np.mean(MsuH_ordinated[i])
                subgroup_median = np.median(MsuH_ordinated[i])
    
                mean.append(subgroup_mean)
                median.append(subgroup_median)
        
            #plot degli istogrammi:
            colors = ['orange', 'pink', 'yellow'] #definisco i colori per i tre istogrammi:
            plt.figure(figsize=(14, 11))

            for i in range(len(MsuH_ordinated)):
                plt.hist(MsuH_ordinated[i], bins=15, alpha=0.8, label=f'Gruppo {i+1}: {intervalli2[i]} Gyr - {intervalli2[i+1]} Gyr', color=colors[i], edgecolor='black')

            plt.xlabel('MsuH')
            plt.ylabel('Frequenza')
            plt.title('Istogramma della metallicità delle stelle')
        
            # Inserimento delle linee verticali per i valori di media e mediana
            for i in range(len(mean)):
                plt.axvline(x=mean[i], color='red', linestyle='--', label=f'Media gruppo {i+1}: {mean[i]:.2f}')
                plt.axvline(x=median[i], color='blue', linestyle='-.', label=f'Mediana gruppo {i+1}: {median[i]:.2f}')
    
            plt.legend()
        
            plt.savefig('fig_2.png', bbox_inches='tight') # salva il plot come immagine
            plt.show() #mostra il grafico da terminale
        
            #4):Plot (M_ass, m_ini)
        
            plt.figure(figsize=( 14, 11))

            for i in range(len(MsuH_ordinated)):
                plt.scatter( m_ini_ordinated[i], MsuH_ordinated[i], color=colors[i], label=f'Gruppo {i+1}: {intervalli2[i]} Gyr - {intervalli2[i+1]} Gyr', s=5)
    
            plt.xlabel('m')
            plt.ylabel('MsuH')
            plt.title('Metallicità in funzione della massa')

            plt.legend()
            plt.grid(True)
        
            plt.savefig('fig_3.png', bbox_inches='tight') # salva il plot come immagine
            plt.show() #mostra il grafico da terminale
        
        
            #5) Istogramma 2D
        
            plt.figure(figsize=(14, 11))

            hist, xedges, yedges = np.histogram2d(np.concatenate(m_ini_ordinated), np.concatenate(MsuH_ordinated), bins=40)

            plt.imshow(hist.T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='viridis')
            plt.colorbar(label='Frequenza')

            plt.xlabel('m')
            plt.ylabel('MsuH')
            plt.title('Istogramma 2D per la relazione tra Metallicità e Massa')

            plt.grid(True)
        
            plt.savefig('fig_4.png', bbox_inches='tight') # salva il plot come immagine
            plt.show() #mostra il grafico da terminale
            
    except FileNotFoundError:
        print("File non trovato. Assicurati di specificare il percorso corretto del file.")
    
    except Exception as e:
        print("Si è verificato un errore durante la lettura del file:", str(e))

if __name__ == "__main__":
    # Controlla se è stato passato un argomento
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # Ottieni il nome del file dalla riga di comando
    file_path = sys.argv[1]

    # Chiamata alla funzione principale con il nome del file come argomento
    main(file_path)


# In[ ]:




