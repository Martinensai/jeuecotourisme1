# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 03:42:39 2025

@author: hp
"""

import streamlit as st

# Titre du jeu
st.title("Jeu éducatif : Tri des déchets")

# Instructions
st.write("Placez chaque déchet dans la bonne catégorie : Papier, Plastique, Verre, ou Compost.")

# Déchets et catégories
dechets = ["Bouteille en plastique", "Journal", "Peau de banane", "Bouteille en verre"]
categories = ["Papier", "Plastique", "Verre", "Compost"]

# Initialiser le score
score = 0

# Logique du jeu
for dechet in dechets:
    choix = st.selectbox(f"Dans quelle catégorie mettez-vous : {dechet} ?", categories, key=dechet)
    if dechet == "Bouteille en plastique" and choix == "Plastique":
        score += 1
    elif dechet == "Journal" and choix == "Papier":
        score += 1
    elif dechet == "Peau de banane" and choix == "Compost":
        score += 1
    elif dechet == "Bouteille en verre" and choix == "Verre":
        score += 1

# Afficher le score
st.write(f"Votre score est : {score}/{len(dechets)}")

if score == len(dechets):
    st.success("Félicitations, vous êtes un expert du tri !")
else:
    st.warning("Essayez encore pour améliorer votre score.")
