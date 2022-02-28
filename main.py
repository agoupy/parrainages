#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:12:38 2022

@author: j64280
"""

import alluvial
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm



list_2017 = pd.read_csv('parrainagestotal_2017.csv',sep=';')
list_2022 = pd.read_csv('parrainagestotal_2022.csv',sep=';')


list_2017['Candidat 2022']='Pas de parrainage en 2022'
n_2017,_=list_2017.shape
n_2022,_=list_2022.shape
n=0

for i in range(n_2017):
    ind = ((list_2022.Nom == list_2017.Nom.iloc[i]) & (list_2022.Prénom == list_2017.Prénom.iloc[i])
       & (list_2022.Département == list_2017.Département.iloc[i]) & (list_2022.Circonscription == list_2017.Circonscription.iloc[i]))
    if ind.any():
        list_2017['Candidat 2022'].iloc[i] = list_2022[ind].Candidat.values[0]
    list_2017['Candidat-e parrainé-e'].iloc[i] = list_2017['Candidat-e parrainé-e'].iloc[i] + ' '

conserve_2017 = ['FILLON François ','MACRON Emmanuel ', 'HAMON Benoît ','ARTHAUD Nathalie ',
                  'DUPONT-AIGNAN Nicolas ','MELENCHON Jean-Luc ',
                  'LASSALLE Jean ','POUTOU Philippe ','CHEMINADE Jacques ','ASSELINEAU François ',
                  'LE PEN Marine ','YADE Rama ','JUPPE Alain ','JARDIN Alexandre ','MARCHANDISE Charlotte ',
                  'ALLIOT-MARIE Michèle ','TAUZIN Didier ','GORGES Jean-Pierre ','TROADEC Christian ',
                  'LARROUTUROU Pierre ','GUAINO Henri ','BAROIN François ']

conserve_2022 = ['PÉCRESSE Valérie','MACRON Emmanuel','HIDALGO Anne','ARTHAUD Nathalie',
                 'DUPONT-AIGNAN Nicolas','ROUSSEL Fabien','MÉLENCHON Jean-Luc','LASSALLE Jean','POUTOU Philippe',
                 'ZEMMOUR Éric','ASSELINEAU François','LE PEN Marine','JADOT Yannick','KAZIB Anasse',
                 'KUZMANOVIC Georges','THOUY Hélène','TAUBIRA Christiane','KOENIG Gaspard','MIGUET Nicolas']

list_2017_filtered = list_2017[list_2017['Candidat 2022']!='Pas de parrainage en 2022']
n_2017_filtered,_=list_2017_filtered.shape

couple_par = []
for i in range(n_2017_filtered):
    if list_2017_filtered['Candidat-e parrainé-e'].iloc[i] in conserve_2017:
        if list_2017_filtered['Candidat 2022'].iloc[i] in conserve_2022:
            couple_par.append([list_2017_filtered['Candidat-e parrainé-e'].iloc[i], list_2017_filtered['Candidat 2022'].iloc[i]])


#%%

cmap = matplotlib.cm.get_cmap('jet')
ax = alluvial.plot(
    couple_par,  alpha=0.8, color_side=0, rand_seed=4, figsize=(10,15),
    disp_width=True, wdisp_sep=' '*2, fontname='Monospace', 
    colors = cmap(np.linspace(0,8,len(conserve_2017)) % 1),
    a_sort=conserve_2017[::-1],b_sort=conserve_2022[::-1])
ax.set_title('Transferts de parrainage entre 2017 et 2022', fontsize=14, fontname='Monospace')
plt.text(1.1,-150,'@Alexandre_Goupy')
plt.savefig('report_signatures.png',bbox_inches='tight',dpi=200)#,transparent=True)