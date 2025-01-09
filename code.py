import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Application Streamlit Déployable")

# Entrées utilisateur
st.sidebar.header("Paramètres utilisateur")
nombre_points = st.sidebar.slider("Nombre de points", 10, 100, 50)
amplitude = st.sidebar.slider("Amplitude", 1, 10, 5)

# Génération des données
x = np.linspace(0, 2 * np.pi, nombre_points)
y = amplitude * np.sin(x)

# Affichage des données sous forme de tableau
data = pd.DataFrame({'x': x, 'y': y})
st.write("Voici les données générées :", data)

# Affichage du graphique
fig, ax = plt.subplots()
ax.plot(x, y, label="y = Amplitude × sin(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)
