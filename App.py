import os

import streamlit as st
from streamlit_navigation_bar.example import logo_path, options

from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
from PIL import Image

image = Image.open('img/sparkling-line.png')

logo_path = os.path.join(os.path.dirname(__file__),"img", "sparkling-line.svg")
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)


pages = ['Home', 'Project1', 'Project2', 'Project3']
styles = {
    "nav": {
        "background-color": "linear-gradient(to right, royalblue, rgb(123, 209, 146))",
        "display": "flex",
        "justify-content": "center",
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "span": {
        "display": "block",
        "color": "white",
        "padding": "0.2rem 0.725rem",
        "font-size": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px",
    },
}




page = st_navbar(pages, styles=styles, logo_page=logo_path, options=options)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()




