import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Proyecto Módulo 1 - Python Fundamentals",
    page_icon="💻",
    layout="wide"
)

st.sidebar.image("logo.jpg", use_container_width=True)
st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox(
    "Ir a:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

#  HOME
if opcion == "Home":
    st.markdown(
    """
    <style>
    .stElementContainer h1 {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    st.title("📊 Proyecto Python Fundamentals")
    st.markdown("---")
    st.write("**Nombre del estudiante:** Gianella Sophia Alarcón Bardales")
    st.write("**Curso:** Especialización en Python for Analytics")
    st.write("**Módulo:** Python Fundamentals")
    st.write("**Año:** 2026")
    st.markdown("---")
    st.subheader("📝 Descripción del objetivo del proyecto")
    st.write("""Desarrollar una aplicación interactiva en Streamlit que integre los conceptos
             fundamentales de programación en Python aprendidos durante el Módulo 1 del curso, 
             incluyendo variables, estructuras de datos, control de flujo, funciones, programación 
             funcional y programación orientada a objetos (POO).""")
    st.markdown("---")
    st.subheader("🛠️ Tecnologías utilizadas")
    st.write("""
        - **Python 3.12** (Lenguaje de programación principal)
        - **Streamlit** (Framework para la creación de la aplicación web interactiva)
        """)
    st.markdown("---")
    st.subheader("📋 Contenido de la Aplicación")
    st.write("""
    - **Ejercicio 1: Variables y Condicionales**
    - **Ejercicio 2: Listas y Diccionarios**
    - **Ejercicio 3: Funciones y Programación Funcional**
    - **Ejercicio 4: Programa Orientado a Objetos**
    """)
    st.info("👈 Utiliza el menú lateral para navegar por los diferentes ejercicios.")
    st.markdown("---")
    st.caption("© Gianella Alarcón - 2026")
    
# EJERCICIO 1 
elif opcion == "Ejercicio 1":
    st.title("Ejercicio 1: Variables y Condicionales")
    st.subheader("💰 Verificador de presupuesto")
    st.write("Ingresa su presupuesto y gasto para verificar si el gasto está dentro del límite.")

    presupuesto = st.number_input("Ingrese su presupuesto", min_value=0.0,step=1.0)
    gasto = st.number_input("ngrese su gasto", min_value=0.0, step=1.0)

    if st.button("Evaluar gasto"):
        diferencia = presupuesto - gasto
        if gasto <= presupuesto:
            st.success("Dentro del presupuesto")
        else:
            st.warning("Presupuesto excedido")
        st.write(f"La diferencia es: {diferencia}")

# EJERCICIO 2 
elif opcion == "Ejercicio 2":
    st.title("Ejercicio 2: Listas y Diccionarios")
    st.subheader("📋 Registro de actividades")
    st.subheader("➕ Agregar nueva actividad")
    if "actividades" not in st.session_state:
        st.session_state.actividades = []
    
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre de la actividad")
        tipo = st.selectbox("Tipo", ["Operativo", "Administrativo", "Comercial", "Tecnología", "Otro"])
    with col2:
        presupuesto = st.number_input("Presupuesto ($)", min_value=0.0, step=10.0, key="p2")
        gasto_real = st.number_input("Gasto real ($)", min_value=0.0, step=10.0, key="g2")
    
    if st.button("➕ Agregar actividad"):
        if nombre.strip() == "":
            st.warning("Ingrese nombre de actividad")
        else:
            actividad = {
                "nombre": nombre,
                "tipo": tipo,
                "presupuesto": presupuesto,
                "gasto_real": gasto_real
            }
            st.session_state.actividades.append(actividad)
            st.success("Actividad agregada")

    st.markdown("---")
    st.subheader("📊 Actividades registradas")
    if st.session_state.actividades:
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df, use_container_width=True)

        st.markdown("### Estado de actividades")

        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                st.success(f"✅ {act['nombre']} cumple presupuesto")
            else:
                st.warning(f"⚠️ {act['nombre']} excede presupuesto")
    else:
        st.info("No hay actividades registradas")

# EJERCICIO 3
elif opcion == "Ejercicio 3":
    st.title("Ejercicio 3: Listas y Diccionarios")
    st.subheader("📈 Cálculo de retorno esperado")
    st.markdown("---")
        
    st.write("Calcule el retorno esperado de su inversión")
    
    col1, col2 = st.columns(2)
    with col1:
        nombre_inv = st.text_input("Nombre de la inversión/actividad:")
    with col2:
        pres_inv = st.number_input("Presupuesto de la inversión:", min_value=0.0, value=1000.0, step=100.0)
    
    tasa = st.slider("Seleccione la tasa de retorno:", 0.0, 1.0, 0.05)
    meses = st.number_input("Cantidad de meses:", min_value=1, value=12)
    
    def calcular_retorno(actividad, t, m):
        return actividad['presupuesto'] * t * m

    if st.button("Ejecutar Cálculo"):
        actividades_temp = [{"nombre": nombre_inv, "presupuesto": pres_inv}]
        
        resultados = list(map(lambda x: calcular_retorno(x, tasa, meses), actividades_temp))

        retorno_final = resultados[0]
        st.markdown("---")
        st.write(f"**Resultado:**")
        st.write(f"El retorno esperado para '{nombre_inv}' es de: ${retorno_final:,.2f}")
        st.write(f"Fórmula aplicada: {pres_inv} (Presupuesto) * {tasa} (Tasa) * {meses} (Meses)")

# EJERCICIO 4     
elif opcion == "Ejercicio 4":
    st.title("Ejercicio 4: Programa Orientado a Objetos")
    st.subheader("Actividad financiera")
    st.markdown("---")

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo 
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real
            
        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto
        def mostrar_info(self):
            diferencia = self.presupuesto - self.gasto_real
            return {"tipo": self.tipo,
                "presupuesto": f"S/{self.presupuesto:,.2f}",
                "gasto": f"S/{self.gasto_real:,.2f}",
                "diferencia": f"S/{diferencia:,.2f}"}
        
    st.write("### Crear Instancia de Actividad")
    col1, col2 = st.columns(2)
    with col1:
        nombre_poo = st.text_input("Nombre de la actividad:")
        tipo_poo = st.selectbox("Tipo de actividad:", ["Operativo", "Marketing", "Recursos Humanos", "Otros"])
    with col2:
        pres_poo = st.number_input("Presupuesto asignado:", min_value=0.0, step=1.0)
        gasto_poo = st.number_input("Gasto real ejecutado:", min_value=0.0, step=1.0)

    if st.button("Calcular"):
        actividad = Actividad(nombre_poo, tipo_poo, pres_poo, gasto_poo)
        info = actividad.mostrar_info()
        st.markdown("---")
        
        st.write("**Información del Objeto:**")
        if actividad.esta_en_presupuesto():
            st.write(f"✅ **Está en el presupuesto**")
        else:
            st.write(f"❌ **Presupuesto excedido**")
            
        st.write(f"**Tipo:** 💰 {info['tipo']}")
        st.write(f"**Presupuesto:** {info['presupuesto']}")
        st.write(f"**Gasto Real:** {info['gasto']}")
        st.write(f"**Diferencia:** {info['diferencia']}")