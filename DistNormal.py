import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Distribución Normal')

# Sidebar para ajustar los parámetros
st.sidebar.header('Parámetros de la Distribución Normal')
media = st.sidebar.number_input('Media', value=0.0)
desviacion_estandar = st.sidebar.number_input('Desviación Estándar', value=1.0)
tamaño_muestra = st.sidebar.number_input('Tamaño de la Muestra', value=1000)

# Genera una muestra de números aleatorios con distribución normal
simulacion = np.random.normal(media, desviacion_estandar, tamaño_muestra)

# Crea un histograma para visualizar la distribución simulada
st.pyplot(plt.hist(simulacion, bins=30, density=True, alpha=0.6, color='b'))

# Agrega una línea para mostrar la función de densidad de probabilidad teórica
x = np.linspace(-4, 4, 100)
pdf = (1 / (desviacion_estandar * np.sqrt(2 * np.pi))) * np.exp(-(x - media)**2 / (2 * desviacion_estandar**2))
plt.plot(x, pdf, 'k--', linewidth=2)

# Etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Densidad de Probabilidad')
plt.title('Simulación de Distribución Normal')

# Muestra la gráfica en Streamlit
st.pyplot()

# Información adicional
st.write('Esta aplicación simula una distribución normal con los parámetros especificados en la barra lateral.')
