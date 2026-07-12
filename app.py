import streamlit as st
from datetime import datetime, timedelta, timezone
import google.generativeai as genai

# 1. Sahifa sozlamalari (Tepadagi nom va ikonka)
st.set_page_config(page_title="Sirli syurpriz ✨", page_icon="🎁")

# 2. Sun'iy intellekt (Gemini) ni ulash
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    pass

# 3. Vaqtni O'zbekiston (UTC+5) mintaqasiga moslash
uzb_vaqti = timezone(timedelta(hours=5))
hozir = datetime.now(uzb_vaqti)

# Qulf ochiladigan vaqt (2026-yil, 15-iyul, 00:00:00)
maqsad = datetime(2026, 7, 15, 0, 0, 0, tzinfo=uzb_vaqti)

# 4. Asosiy dizayn va mantiq
st.markdown("<h1 style='text-align: center; color: #ff66b2; font-family: cursive; font-size: 50px;'>RL</h1>", unsafe_allow_html=True)

# Agar hali vaqt kelmagan bo'lsa (Taymer ko'rinadi)
if hozir < maqsad:
    farq = maqsad - hozir
    kun = farq.days
    soat, qoldiq = divmod(farq.seconds, 3600)
    daqiqa, soniya = divmod(qoldiq, 60)

    st.markdown("<h2 style='text-align: center;'>Senga atalgan sirli syurprizning <br> qulfi ochilishiga... ⏳</h2>", unsafe_allow_html=True)
    
    st.write("") # Bo'sh joy
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Kun", f"{kun}")
    with col2:
        st.metric("Soat", f"{soat}")
    with col3:
        st.metric("Daqiqa", f"{daqiqa}")

    st.write("")
    st.warning("🔒 15-iyul 00:00 da senga atalgan mo'jizaviy sovg'a shu yerda namoyon bo'ladi...")

# Agar vaqt yetib kelgan bo'lsa (Syurpriz ochiladi)
else:
    st.balloons() # Ekranda sharlar uchadi
    st.markdown("<h1 style='text-align: center; color: #ff66b2;'>Tug'ilgan kuning bilan, Laylo! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>20 yoshing muborak bo'lsin! 🎂✨</h3>", unsafe_allow_html=True)
    
    # Musiqa qismi
    try:
        st.audio("happy_birthday.mp3", format="audio/mp3", autoplay=True)
    except:
        pass
        
    st.write("---")
    
    # AI tabrik qismi
    st.markdown("<h4 style='text-align: center;'>Senga maxsus tilaklarim bor... 👇</h4>", unsafe_allow_html=True)
    
    if st.button("Menga atalgan tilakni o'qish 💌", use_container_width=True):
        with st.spinner("Senga atalgan eng samimiy so'zlar yozilmoqda..."):
            try:
                # Sun'iy intellekt Laylo uchun chiroyli tabrik yozib beradi
                response = model.generate_content("Laylo ismli qizni 20 yoshga to'lishi bilan tabrikla. Unga baxt, omad, chiroyli va samimiy tilaklar yoz. Matn o'zbek tilida bo'lsin, juda ta'sirli va romantik, mehribon ruhda bo'lsin. She'r qo'shsang ham bo'ladi.")
                st.success(response.text)
            except Exception as e:
                st.error("Hozircha tilaklarni yuklashda xatolik bo'ldi, lekin men baribir seni juda yaxshi ko'raman va senga dunyodagi eng zo'r narsalarni tilayman! 😊")