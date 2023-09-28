import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Distribución Uniforme')
st.write('La distribución uniforme tiene 2 parámetros a y b')

# Parámetros de la distribución uniforme (inicialmente)
min_value = st.slider('Valor Mínimo', 0.0, 30.0, 10.0)
max_value = st.slider('Valor Máximo', 0.0, 30.0, 20.0)

# Generar datos de la distribución uniforme
datos_uniformes = np.random.uniform(min_value, max_value, 10000)

# Crear un histograma para visualizar la distribución
plt.hist(datos_uniformes, bins=20, density=True, alpha=0.5, color='b', edgecolor='k')

# Agregar título al gráfico
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title(f'Distribución Uniforme entre {min_value} y {max_value}')

# Mostrar el gráfico en Streamlit
st.pyplot(plt)
