import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('munis.csv')

st.title("Mi primer app")

munis = data ['entidad'].unique().tolist()

mun =st.selectbox('Seleccione un municipio: ', munis)

filtro = data [data['entidad']==mun]



gen = (filtro.groupby('clas_gen')['total_recaudo'].sum())

total_gen = gen.sum()
gen = (gen / total_gen).round (2)


det = (filtro.groupby('clasificacion_ofpuj')['total_recaudo'].sum())

total_det = det.sum()
det = (det / total_det).round (3)


# clasificacion general 

# clasificacion detallada 



# pie chart

fig_gen = px.pie(values=gen.values, 
                 names=gen.index, 
                 title=f'Distribución por Clasificación General - {mun}',
                 height=600)
st.plotly_chart(fig_gen)

#treemap

fin = (filtro.groupby(['clas_gen','clasificacion_ofpuj'])['total_recaudo'].sum().reset_index())


fig = px.treemap(fin, path=[px.Constant('Total'),
                            'clas_gen',
                            'clasificacion_ofpuj'],
                            values='total_recaudo')

st.plotly_chart(fig) 