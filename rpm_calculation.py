import math
import random
import csv
import pandas as pd
import streamlit as st

# Función para calcular RPM
def calculate_rpm(angular_velocity, wheel_radii, transmision_relation):
    return (angular_velocity * 60) / (2 * math.pi * wheel_radii * transmision_relation)

# Generar datos aleatorios
def generate_data(num_measurements, angular_velocity_range, wheel_radii_range, transmision_relation):
    data = []
    for _ in range(num_measurements):
        angular_velocity = random.uniform(*angular_velocity_range)  
        wheel_radii = random.uniform(*wheel_radii_range)           
        rpm = calculate_rpm(angular_velocity, wheel_radii, transmision_relation)
        data.append([angular_velocity, wheel_radii, transmision_relation, rpm])
    return data

# Guardar datos en un archivo CSV
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Velocidad Angular (rad/s)", "Radio de la Rueda (m)", "Relación de Transmisión", "RPM"])
        writer.writerows(data)

# Visualización con Streamlit
def visualize_data(data):
    df = pd.DataFrame(data, columns=["Velocidad Angular (rad/s)", "Radio de la Rueda (m)", "Relación de Transmisión", "RPM"])
    st.write("### Datos Generados:")
    st.dataframe(df)

    st.write("### Gráfica de RPM vs Velocidad Angular:")
    st.line_chart(df[["Velocidad Angular (rad/s)", "RPM"]])

if __name__ == "__main__":
    # Configuración de la página
    st.set_page_config(page_title="Visualización de RPM del Tractor")

    # Controles interactivos
    st.title("Visualización de Datos del Tractor")
    st.sidebar.header("Parámetros de Simulación")
    num_measurements = st.sidebar.slider("Número de Mediciones", min_value=5, max_value=50, value=10, step=1)
    angular_velocity_range = st.sidebar.slider("Rango de Velocidad Angular (rad/s)", min_value=1.0, max_value=20.0, value=(5.0, 15.0), step=0.1)
    wheel_radii_range = st.sidebar.slider("Rango del Radio de la Rueda (m)", min_value=0.1, max_value=1.0, value=(0.4, 0.6), step=0.01)
    transmision_relation = st.sidebar.number_input("Relación de Transmisión", min_value=1, max_value=20, value=10, step=1)

    # Generar datos
    data = generate_data(num_measurements, angular_velocity_range, wheel_radii_range, transmision_relation)

    # Guardar datos en un archivo CSV
    csv_filename = "tractor_data.csv"
    save_to_csv(data, csv_filename)
    st.sidebar.success(f"Datos guardados en {csv_filename}")

    # Visualizar datos
    visualize_data(data)