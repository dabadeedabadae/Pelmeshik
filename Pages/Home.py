import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

class Home:
    def __init__(self):
        # Заготовка для возможной инициализации данных
        pass

    def app(self, right_column=None, left_column=None):
        # Основная информация
        name = "Yelnur!!!"
        description = "Just chill guy"


        # Загрузка изображений и анимаций
        sparkling_image = Image.open("img/sparkling-line.png")

        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()




        col1, col2 = st.columns(2, gap="small")

        with col1:
            st.title(name)
            st.write(description)

            st.write('\n')
            st.subheader("Experience")
            st.write("""
            - ✔️ 750+ hours in Fortnite
            - ✔️ An ever-growing knowledge of natural languages: C4 arabic
            - ✔️ The Big Bang Theory, by its very name, proves that the Creator is Allah.
            """)

            # Навыки
            st.write('\n')
            st.subheader("Hard Skills")
            st.write("""
            - 🎮 **Gaming skills**:
            - 👑 Valorant: "Master of toxic arrows" title - I can hit even through smoke.
            - 🛠️ Minecraft: Professional diamond miner and builder of unreal mud castles.
            - 🪂 Fortnite: I build skyscrapers faster than my FPS drops.
            - 🏆 **Team achievements**:
            - "Ace" on AFK opponents (no one moved, but who's counting?).
            - Capturing the flag in 5 seconds thanks to a bug - strategy or talent?
            - 🎉 **Signature style**:
            - I always take a fist with me in Minecraft and a sniper rifle in Fortnite.
            - I win in Valorant even when the whole squad forgot to defuse.
            """)






