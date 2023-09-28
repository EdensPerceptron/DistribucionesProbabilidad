import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Distribución Normal')
st.write('La distribución normal tiene 2 parámetros Media y Desviacion_estándar')

# Sidebar para ajustar los parámetros
tamaño_muestra = st.number_input('tamaño_muestra', value=1000)
desviacion_estandar = st.slider('desviacion_estandar', 0.0, 30.0, 10.0)
media = st.slider('Media', 0.0, 30.0, 20.0)

# Genera una muestra de números aleatorios con distribución normal
simulacion = np.random.normal(media, desviacion_estandar, tamaño_muestra)

# Crea un histograma para visualizar la distribución simulada
plt.hist(simulacion, bins=30, density=True, alpha=0.6, color='g',zorder=1)

    # Agrega una línea para mostrar la función de densidad de probabilidad teórica
    #x = np.linspace(-4, 4, 100)
    #pdf = (1 / (desviacion_estandar * np.sqrt(2 * np.pi))) * np.exp(-(x - media)**2 / (2 * desviacion_estandar**2))
    #plt.plot(x, pdf, 'k--', linewidth=2, zorder=2)

# Etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Densidad de Probabilidad')
plt.title('Simulación de Distribución Normal')

# Muestra la gráfica en Streamlit
st.pyplot(plt)


