from pyparsing import Opt
import streamlit as st
from presentacionif import presentacion_if
from convbases.conversorbasesif import conversor_bases_if
from derivadas.derviadasif import derivadas_if
from integrales.falsaposicionif import falsa_posicion_if
from derivadas.derivadadeunpolinomioif import derivada_de_un_polinomio_if
from derivadas.biseccionif import biseccion_if
from integrales.trapeciosif import trapecios_if
from integrales.simpson1by3if import simpson1by3_if
from integrales.solidoderevolucionif import solidoderevolucion_if

st.set_page_config(
    layout="wide",
    page_icon='馃洜',
    initial_sidebar_state='expanded',
    menu_items={'About': "### Github:\n www.github.com/etensor/baseconvpy"}
    )

st.title('Conversor de bases')


opt_menu = st.sidebar.selectbox(
    "Navegador del proyecto",
    ("Presentaci贸n","Conversor de bases", "Derivadas", "Falsa posici贸n", "Derivada de un polinomio", "Bisecci贸n", "Trapecios", "Rectangulo", "Simpson 1/3", "Solidos de revolci贸n")
)

if opt_menu == 'Presentaci贸n':
    st.subheader('Presentaci贸n')
    presentacion_if()

if opt_menu == 'Conversor de bases':
    st.subheader('Conversor de bases')
    conversor_bases_if()

if opt_menu == 'Derivadas':
    st.subheader('Calculadora de Derivadas')
    derivadas_if()

if opt_menu == 'Falsa posici贸n':
    st.subheader('Falsa posici贸n')
    falsa_posicion_if()

if opt_menu == 'Derivada de un polinomio':
    st.subheader('Derivada de un polinomio')
    derivada_de_un_polinomio_if()

if opt_menu == 'Bisecci贸n':
    st.subheader('Bisecci贸n')
    biseccion_if()

if opt_menu == 'Trapecios':
    st.subheader('Trapecios')
    trapecios_if()

if opt_menu == 'Rectangulo':
    st.subheader('Rectangulo')
    trapecios_if()

if opt_menu == 'Simpson 1/3':
    st.subheader('Simpson 1/3')
    simpson1by3_if()

if opt_menu == 'Solidos de revolci贸n':
    st.subheader('Solidos de revolci贸n')
    solidoderevolucion_if()

#with open('../css/presentacion.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)