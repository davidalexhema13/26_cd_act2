import streamlit as st

st.set_page_config(page_title="Texto y Visualización", page_icon="📜")

st.subheader("Ejercicio 1")

nombre = st.text_input("Diga su nombre:")


if nombre != "":
    st.write(f"Hola, {nombre}")

st.divider()  

st.subheader("Ejercicio 2")


numero1 = st.number_input("ingrese un numero ",value = 0)


numero2 = st.number_input("ingrese otro numero", value = 0)


resultado = numero1 * numero2 

st.write(f"Resultado: {resultado}")

if numero1 >100  or numero2 > 100:
    st.warning("numero grandes ")


st.divider()  




st.subheader("Ejercicio 3")


opcion = st.radio(
    "Seleccione la conversión:",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius")
)


temperatura = st.number_input("Ingrese la temperatura:", value=0.0)


if opcion == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    st.write(f"Resultado: {resultado:.2f} °F")

else:
    resultado = (temperatura - 32) * 5/9
    st.write(f"Resultado: {resultado:.2f} °C")

st.divider()





st.subheader("Ejercicio 4 ")


tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])


with tab1:
    st.image("https://i.pinimg.com/736x/a0/f6/d8/a0f6d8722e2ca13e433591c68bc5401f.jpg", 
             caption="Gato", use_container_width=True)
    
    if st.button("Me gusta (Gato)"):
        st.toast("Te gusta ese gato")

with tab2:
    st.image("https://i.pinimg.com/564x/59/7f/13/597f13e20e3bde0339ba9767cbf5ca53.jpg", 
             caption="Perro", use_container_width=True)
    
    if st.button("Me gusta (Perro)"):
        st.toast("Te gusta ese perro")


with tab3:
    st.image("https://cdn.prod.website-files.com/64df6dd37ac6a0dbb9d03cb3/6627cb99ca12e3d36b3b2be9_Diego_Rocha_Chlorochrysa-nitidissima.jpg", 
             caption="Ave", use_container_width=True)
    
    if st.button("Me gusta (Ave)"):
        st.toast("Te gusta esa ave")

st.divider()





st.subheader("Ejercicio 5")


with st.form("form_comentarios"):

    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")

    enviar = st.form_submit_button("Enviar")


if enviar:
    if mensaje != "":
        datos = {
            "Asunto": asunto,
            "Mensaje": mensaje
        }
        st.json(datos)   
    else:
        st.warning("El mensaje no puede estar vacío")

st.divider()




st.subheader("Ejercicio 6 ")


if "logueado" not in st.session_state:
    st.session_state.logueado = False


if not st.session_state.logueado:

    usuario = st.text_input("Usuario:")
    contraseña = st.text_input("Contraseña:", type="password")

    if st.button("Ingresar"):
        if usuario == "admin" and contraseña == "1234":
            st.session_state.logueado = True
            st.success("Inicio de sesión exitoso")
            st.rerun()  
        else:
            st.error("Usuario o contraseña incorrectos")


else:
    st.success("Ya estás logueado")

    if st.button("Cerrar Sesión"):
        st.session_state.logueado = False
        st.rerun()

st.divider()




st.subheader("Ejercicio 7")


if "lista_compras" not in st.session_state:
    st.session_state.lista_compras = []


producto = st.text_input("Ingrese un producto:")


col1, col2 = st.columns(2)

with col1:
    if st.button("Agregar"):
        if producto != "":
            st.session_state.lista_compras.append(producto)
        else:
            st.warning("Ingrese un producto válido")

with col2:
    if st.button("Limpiar Lista"):
        st.session_state.lista_compras = []


st.write("producto agregadoo")

if st.session_state.lista_compras:
    for i, item in enumerate(st.session_state.lista_compras, start=1):
        st.write(f"{i}. {item}")
else:
    st.info("La lista está vacía")

st.divider()






st.subheader("Ejercicio 8 ")

import random


N = st.slider("Seleccione la cantidad de datos (N):", 10, 100, 20)


if st.button("Regenerar"):
    st.rerun()


datos = [random.randint(1, 100) for _ in range(N)]


st.line_chart(datos)

st.divider()
