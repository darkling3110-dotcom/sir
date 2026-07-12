# app.py
import streamlit as st
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Sirli syurpriz ✨",
    page_icon="🎁",
    layout="wide"
)

if 'gift_opened' not in st.session_state:
    st.session_state.gift_opened = False

# ==========================================
# 🎨 1. SIRLI, QORONG'U VA PREMIUM FON CSS (DARK NEON)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
    
    /* TO'Q, SIRLI VA HASHAMATLI FON */
    .stApp {
        background: linear-gradient(-45deg, #0d0221, #26001b, #1a0033, #0d0221);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #ffffff !important;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* R L IMZOSI UCHUN YORQIN NEON DIZAYN */
    .rl-signature {
        font-family: 'Alex Brush', cursive;
        font-size: 95px;
        color: #ff4d85;
        text-align: center;
        line-height: 1;
        margin-bottom: 15px;
        text-shadow: 0 0 10px rgba(255, 77, 133, 0.5), 0 0 30px rgba(255, 77, 133, 0.3);
        animation: fadeInGlow 3s ease forwards;
    }
    @keyframes fadeInGlow {
        0% { opacity: 0; transform: scale(0.9); filter: blur(5px); }
        100% { opacity: 1; transform: scale(1); filter: blur(0px); }
    }

    .elegant-title {
        font-family: 'Georgia', serif;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        margin-bottom: 30px;
        text-shadow: 0px 4px 15px rgba(255, 77, 133, 0.6);
    }

    /* TAYMER RAQAMLARI UCHUN DIZAYN */
    [data-testid="stMetricValue"] {
        color: #ff4d85 !important;
        font-size: 60px !important;
        text-shadow: 0 0 15px rgba(255, 77, 133, 0.4);
    }
    [data-testid="stMetricLabel"] {
        color: #e0e0e0 !important;
        font-size: 20px !important;
        font-weight: bold;
    }

    /* OYNASIMON KARTA (QORONG'U SHISHA EFFEKTI) */
    .glass-3d-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 45px;
        border: 1px solid rgba(255, 77, 133, 0.2);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(255, 77, 133, 0.1);
        transform: perspective(1000px) rotateX(0.5deg);
        transition: all 0.4s ease;
    }
    .glass-3d-card:hover {
        transform: perspective(1000px) rotateX(0deg) translateY(-4px);
        box-shadow: 0 20px 45px rgba(255, 77, 133, 0.3);
        border: 1px solid rgba(255, 77, 133, 0.5);
    }
    
    /* SOVG'A TUGMASINI YASHIRISH VA JONLANTIRISH */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
    }
    div[data-testid="stButton"] > button {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        animation: floatAndWobble 3s infinite ease-in-out;
        transition: all 0.2s ease;
    }
    div[data-testid="stButton"] > button p {
        font-size: 160px !important;
        margin: 0 !important;
        line-height: 1.1 !important;
    }
    div[data-testid="stButton"] > button:hover {
        animation: violentShake 0.4s infinite !important;
        transform: scale(1.15) !important;
        filter: drop-shadow(0 0 40px rgba(255, 215, 0, 0.6));
    }

    @keyframes floatAndWobble {
        0%, 100% { transform: translateY(0) rotate(-3deg); filter: drop-shadow(0 10px 15px rgba(0,0,0,0.5)); }
        50% { transform: translateY(-20px) rotate(3deg); filter: drop-shadow(0 25px 25px rgba(255,215,0,0.2)); }
    }
    @keyframes violentShake {
        0% { transform: translate(2px, 2px) rotate(0deg); }
        10% { transform: translate(-2px, -3px) rotate(-6deg); }
        20% { transform: translate(-4px, 0px) rotate(6deg); }
        30% { transform: translate(4px, 3px) rotate(0deg); }
        40% { transform: translate(2px, -2px) rotate(6deg); }
        50% { transform: translate(-2px, 3px) rotate(-6deg); }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# ⚙️ 2. MANTIQ VA AI TIZIMI
# ==========================================
TARGET_DATE = datetime.datetime(2026, 7, 15, 0, 0, 0) # Tekshirish uchun 1-iyul, so'ng 15 qilasiz!

def generate_exclusive_wishes():
    api_key = os.getenv("GEMINI_API_KEY")
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        prompt = (
            "Bugun Laylo ismli juda qadrli qizning 20 yoshga to'lgan tug'ilgan kuni. U juda iste'dodli rassom. "
            "Unga atab juda mayin, samimiy, o'zbek tilida lirik tabrik maktubi yozib ber. "
            "Uning 20 yoshga to'layotgani va san'atiga (rassomligiga) mos chiroyli o'xshatishlar qilingan bo'lsin. "
            "Yozuv 'Sirli Do'sting' nomidan bo'lsin."
        )
        response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
        return response.text
    except Exception:
        return (
            "Qadrli Laylo!\n\n"
            "Bugun hayotingdagi eng go'zal sanalardan biri — umringning 20-bahorini qarshilamoqdasan! "
            "Sen chizgan har bir surat dunyoni qanchalik go'zal qilsa, sening borliging ham hayotga shunday yorqin ranglar ulashadi.\n\n"
            "20 yosh senga dunyodagi eng samimiy baxtni va qalbingdagi barcha pokiza orzularing ushalishini olib kelsin. "
            "Tug'ilgan kuning muborak bo'lsin, hayotimdagi eng ajoyib rassom! 🎨🎂🎈"
        )

# ==========================================
# 🖥️ 3. INTERAKTIV RAQAMLI INTERFEYS
# ==========================================
now = datetime.datetime.now()
diff = TARGET_DATE - now

left_col, main_col, right_col = st.columns([1, 2.8, 1])

if diff.total_seconds() > 0:
    with main_col:
        st.write("")
        st.markdown("<div class='rl-signature'>R L</div>", unsafe_allow_html=True)
        # YANGI INTRIGALI MATN
        st.markdown("<div class='elegant-title'>Senga atalgan sirli syurprizning qulfi ochilishiga... ⏳</div>", unsafe_allow_html=True)
        
        kun, soat, daqiqa = diff.days, diff.seconds // 3600, (diff.seconds % 3600) // 60
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Kun", f"{kun}")
        c2.metric("Soat", f"{soat}")
        c3.metric("Daqiqa", f"{daqiqa}")
        st.write("")
        st.warning("🔒 15-iyul 00:00 da senga atalgan mo'jizaviy sovg'a shu yerda namoyon bo'ladi...")

else:
    if not st.session_state.gift_opened:
        with main_col:
            st.write("")
            st.markdown("<div class='rl-signature'>R L</div>", unsafe_allow_html=True)
            # YANGI JONLI MATN
            st.markdown("<div class='elegant-title'>Sirli syurpriz o'z egasini kutmoqda! 🎉</div>", unsafe_allow_html=True)
            st.info("Senga atalgan maxsus sovg'a qulfdan chiqdi. Uni ochish uchun qutining ustiga bos!")
            
            st.write("")
            c_left, c_mid, c_right = st.columns([1, 1, 1])
            with c_mid:
                if st.button("🎁"):
                    st.session_state.gift_opened = True
                    st.rerun() 
    
    else:
        st.balloons() 
        
        with main_col:
            st.markdown("<div class='rl-signature'>R L</div>", unsafe_allow_html=True)
            st.markdown("<div class='elegant-title'>20 Yoshing Muborak, Eng Go'zal Rassom! 🎨</div>", unsafe_allow_html=True)
            
            audio_file = "happy_birthday.mp3"
            if os.path.exists(audio_file):
                st.audio(audio_file, format="audio/mp3", autoplay=True)
            
            tab1, tab2, tab3 = st.tabs(["🌸 Dil So'zlari", "📸 E'tirof", "✉️ Maxsus Maktub"])
            
            with tab1:
                st.write("")
                st.markdown("""
                    <div class='glass-3d-card'>
                        <h3 style='color: #ff4d85; text-align: center; margin-top:0;'>Yaxshiyamki Dunyoga Kelgansan... ✨</h3>
                        <p style='color: #e0e0e0; font-size: 18px; line-height: 1.7; text-align: center;'>
                        Bugun hayotimdagi juda qadrli inson — <b>Laylo</b>ning 20 yoshga to'lgan kuni! Senga uzoq umr, sog'lik va asarlaring kabi go'zal hayot tilayman. 
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
            with tab2:
                st.write("")
                st.markdown("""
                    <div class='glass-3d-card'>
                        <p style='font-family: Georgia, serif; font-style: italic; font-size: 19px; border-left: 5px solid #ff4d85; padding-left: 20px; color: #e0e0e0;'>
                            "Sening har bir chizgan chizigingda va samimiy tabassumingda o'zgacha bir sehr bor. 20 yoshing eng go'zal mo'jizalarning boshlanishi bo'lsin."
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
            with tab3:
                st.write("")
                if st.checkbox("Maktub muhrini buzish va oʻqish 🔓"):
                    st.snow()
                    with st.spinner("Sirli maktub ochilmoqda..."):
                        wish_text = generate_exclusive_wishes()
                    st.markdown(f"""
                        <div class='glass-3d-card' style='border: 2px dashed #ff4d85;'>
                            <p style='white-space: pre-line; font-size: 18px; line-height: 1.8; color: #e0e0e0;'>{wish_text}</p>
                            <hr style='border: 0.5px solid rgba(255, 77, 133, 0.4); margin: 25px 0;'>
                            <p style='text-align: right; font-size: 18px; font-weight: bold; color: #ff4d85; font-style: italic; margin-bottom:0;'>
                                Chuqur ehtirom bilan, Sening Sirli Do'sting... ✍️
                            </p>
                        </div>
                    """, unsafe_allow_html=True)