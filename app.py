import streamlit as st
import random

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Per te ❤️", page_icon="💌", layout="wide")

# 2. MEMORIA (SESSION STATE)
if 'si' not in st.session_state:
    st.session_state.si = False
if 'pos_top' not in st.session_state:
    st.session_state.pos_top = None
if 'pos_left' not in st.session_state:
    st.session_state.pos_left = None

# 3. FUNZIONE PER MUOVERE IL PULSANTE "NO"
def mover_boton():
    st.session_state.pos_top = random.randint(10, 80)
    st.session_state.pos_left = random.randint(10, 80)

# 4. CSS DINAMICO
if st.session_state.pos_top is not None:
    stile_movimiento = f"""
        position: fixed !important;
        top: {st.session_state.pos_top}% !important;
        left: {st.session_state.pos_left}% !important;
        z-index: 9999 !important;
        width: 160px !important;
        transition: top 0.15s ease, left 0.15s ease !important; 
    """
else:
    stile_movimiento = "position: relative; width: 160px !important;"

# 5. STILI CSS
st.markdown(f"""
<style>
    /* Importazione del font da Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');
            
    header {{visibility: hidden;}} .stApp > header {{display: none;}} footer {{visibility: hidden;}}
            
    /* Applichiamo il font a tutta l'app */
    .stApp, button, p, h1, h2 {{
        font-family: 'Playfair Display', serif !important;
    }}
            
    .stApp {{
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        background-color: #ffe6f0;
    }}
    
    div.block-container {{
        width: 100%; max-width: 1400px; padding: 2rem 0; margin: auto;
    }}

    div[data-testid="stColumn"]:nth-of-type(3) {{
        background-color: #ffffff !important;
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        border: 2px solid #ff4d94 !important;
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        color: black !important; 
        min-width: 450px !important; 
        max-width: 450px !important;
    }}

    h1, h2 {{ text-align: center !important; color: black !important; }}
    p {{ text-align: center !important; font-size: 1.3rem; color: #333333 !important; }}
    
    div[data-testid="stButton"] button[kind="primary"] {{
        background-color: #ff4d94 !important; border: none !important;
        font-size: 20px !important; border-radius: 15px !important;
        color: white !important; width: 160px !important; height: 55px !important;
    }}
    div[data-testid="stButton"] button[kind="secondary"] {{
        {stile_movimiento}
        background-color: #f0f2f6 !important; border: 1px solid #d6d6d8 !important;
        font-size: 20px !important; border-radius: 15px !important;
        color: black !important; width: 160px !important; height: 55px !important;
    }}
</style>
""", unsafe_allow_html=True)

# 6. STRUTTURA DELLA PAGINA
col_izq, col_hueco1, col_cen, col_hueco2, col_der = st.columns([1.2, 0.5, 2, 0.5, 1.2], vertical_alignment="center")

with col_cen:
    # LOGICA DINAMICA DEL CONTENUTO 
    if st.session_state.si:
        # Se ha detto SI: Gif felice e titolo finale
        img_url = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExenpoNDM3Y3V0ZHh3cTltdHRhM3V0ZzVveTh6Z2xzMjMzcDg3Z2x1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5p8jOW3f00osS705g3/giphy.gif"
        titolo = "Buon San Valentino!❤️"
        messaggio = "Sapevo che avresti detto SI!🥰"
    else:
        # Se non ha ancora cliccato SI: Gif rana e domanda
        img_url = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWZtZGFkMTVvdmh1a204b3F5M2c1OHIwdjgzYzR0ZmZ2NXAyNGF3ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/9Mv6b3qFrjimE5A2EP/giphy.gif"
        titolo = "Vuoi essere il mio Valentino?🌹"
        if st.session_state.pos_top is not None:
            messaggio = "Ops, non credo di aver capito bene... riprova!🤭"
        else:
            messaggio = "Spero che la tua risposta sia sì!🥰"

    # RENDER DEL CONTENUTO 
    st.markdown(f"""<div style="display: flex; justify-content: center; margin-bottom: 10px;">
                <img src="{img_url}" width="250" style="border-radius: 10px;"></div>""", unsafe_allow_html=True)
    
    st.title(titolo)
    st.write(messaggio)
    st.write("") 

    # BOTTONI (compaiono SOLO se non ha ancora detto SI)
    if not st.session_state.si:
        btn_si_col, btn_no_col = st.columns(2)
        with btn_si_col:
            if st.button("SÍ!💖", type="primary", use_container_width=True):
                st.balloons()
                st.session_state.si = True
                st.rerun()
        with btn_no_col:
            if st.button("No...🥀", on_click=mover_boton, use_container_width=True):
                pass