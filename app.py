import pandas as pd
import plotly_express as px
import streamlit as st

import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header("Histograma ventas de coches")
hist_button=st.button ("Construir Histograma")

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.histogram(car_data, x="odometer",nbins=20) # crear un histograma
    st.plotly_chart(fig, use_container_width=True)
    fig.show() # crear gráfico de dispersión


scatter_plot_button=st.button("Construir Grafico de Dispersión")
if scatter_plot_button:
   st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
   fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
   st.plotly_chart(fig, use_container_width=True)
   fig.show() # crear gráfico de dispersión
 
        