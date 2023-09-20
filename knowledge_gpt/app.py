# import streamlit as st

# # Funciones para cada página:
# def show_home():
#     st.title("Página de Inicio")
#     st.write("Bienvenido a la página de inicio!")

# def show_page1():
#     st.title("Página 1")
#     st.write("Estás en la página 1.")

# def show_page2():
#     st.title("Página 2")
#     st.write("Estás en la página 2.")

# # Navegación lateral:
# choice = st.sidebar.radio("Elije una página:", ["Inicio", "Página 1", "Página 2"])

# # Lógica para mostrar la página seleccionada:
# if choice == "Inicio":
#     show_home()
# elif choice == "Página 1":
#     show_page1()
# elif choice == "Página 2":
#     show_page2()





from st_pages import Page, Section, add_page_title, show_pages
import os
import streamlit as st
st.markdown("""
            ## 🤖PoliChatBot: ¡Descubre, Compara y Decide!
            
            #### Con PoliChatBot, lleva la contienda presidencial a la palma de tu mano. Conviértete en un votante informado en minutos, no en horas.
            Pregunta y sorpréndete. 
            
            ¿Qué propone para mejorar el sistema de salud? 
            
            ¿Cuál es su plan para la educación? 

            ¿Cómo combatirá la delincuencia? 


            ¡Descubre esto y más ahora!

            Funciones Destacadas:

            - 🔍 Búsqueda Instantánea: Encuentra propuestas específicas en segundos.
            - 🔄 Comparador: Sitúa lado a lado las ideas de tus candidatos favoritos.
            """)

show_pages(
    [
        Page("app.py", "Inicio", "🏠"),
        Page(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainLG.py"), "Luisa Gonzáles", "👩‍💼"),
        Page(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainDN.py"), "Daniel Noboa", "👨‍💼"),
       
       
    ]
)

#add_page_title()  # Optional method to add title and icon to current page