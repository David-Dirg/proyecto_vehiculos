import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de Venta de Vehículos')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para el kilometraje de los vehículos')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión (Precio vs Kilometraje)')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
