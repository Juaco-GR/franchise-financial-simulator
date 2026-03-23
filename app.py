import streamlit as st

st.title("Simulador de Franquicia")

inversion = st.number_input("Inversión inicial", 10000)
ventas = st.number_input("Ventas mensuales", 5000)

utilidad = ventas * 0.3

st.write("Utilidad estimada:", utilidad)
