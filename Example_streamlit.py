
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")
st.sidebar.button("Button inside SideBar")
st.sidebar.checkbox("Checkbox inside SideBar")

st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)


st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

# Datos de ejemplo para un gráfico de líneas
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['A', 'B', 'C']
)

# Crear un gráfico de líneas en Streamlit
st.line_chart(data)


data = pd.DataFrame({
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': [20, 35, 30, 35]
})

# Crear un gráfico de barras en Streamlit
st.bar_chart(data.set_index('Product'))


# Datos de ejemplo para un mapa de calor
data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [4.1425, -73.629],
    columns=['lat', 'lon']
)

# Crear un mapa de calor en Streamlit
st.map(data)

# Datos de ejemplo
data = pd.DataFrame({
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Sales': [20, 35, 30, 35]
})

st.title("Gráfico de Barras de Ventas por Producto")

# Crear el gráfico de barras

bar = sns.barplot(x='Product', y='Sales', data=data)

# Mostrar el gráfico en Streamlit
st.pyplot(bar.figure)

# Datos de ejemplo

data1 = pd.DataFrame(np.random.randn(100, 2), columns=['X', 'Y'])
data2 = pd.DataFrame(np.random.randn(100, 2) * [10, 5], columns=['X', 'Y'])

st.title("Selector Interactivo para Visualización de Gráficos de Dispersión")

dataset = st.selectbox("Selecciona el conjunto de datos:", ["Dataset 1", "Dataset 2"])

fig, ax = plt.subplots()
if dataset == "Dataset 1":
    ax.scatter(data1['X'], data1['Y'], color='blue')
else:
    ax.scatter(data2['X'], data2['Y'], color='green')

ax.set_title(f"Gráfico de Dispersión - {dataset}")
st.pyplot(fig)


data = pd.DataFrame(np.random.randn(100, 3), columns=['Variable A', 'Variable B', 'Variable C'])

st.title("Exploración de Correlación")

show_heatmap = st.checkbox("Mostrar mapa de calor de correlación")

fig, ax = plt.subplots()  # Asegúrate de asignar fig y ax
if show_heatmap:
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    sns.pairplot(data)
    st.pyplot(None)

x = np.linspace(0, 10, 100)
y = np.sin(x)


np.random.seed(40)  # Para reproducibilidad
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temperaturas = np.random.uniform(low=15, high=40, size=len(dias))

# Crear un DataFrame
data = pd.DataFrame({'Día': dias, 'Temperatura (°C)': temperaturas})

# Título de la aplicación
st.title("Gráfico de Líneas Interactivo de Temperaturas")

# Slider para seleccionar el rango de días
start_day = st.slider("Selecciona el rango de días:", 0, 6, (0, 6), format="Días: %d")
selected_days = data['Día'][start_day[0]:start_day[1] + 1]

# Filtrar los datos según el rango seleccionado
filtered_data = data.iloc[start_day[0]:start_day[1] + 1]

st.line_chart(filtered_data.set_index('Día'))
    
# python -m streamlit run c:/Users/stive/OneDrive/Escritorio/steamlit/Example_streamlit.py
#https://www.canva.com/design/DAGTmvRbU9w/SHbCn1bJ6-4rZF5QgobkOw/edit?utm_content=DAGTmvRbU9w&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

