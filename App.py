import streamlit as st
from streamlit import image

from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image

st.set_page_config(initial_sidebar_state="collapsed", page_title="My App", page_icon=image)
image = Image.open('img/sparkling-line.png')
logo_path = os.path.join(os.path.dirname(__file__), "img", "sparkling-line.svg")

pages = [" ",'Home', 'Project1', 'Project2', 'Project3']
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


options = {
    "show_menu": False,
    "show_sidebar": True,
}

page = st_navbar(pages, styles=styles, logo_path=logo_path, options=options)

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




