import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DiaSense AI",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("models/diabetes_rf_pipeline.joblib")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F8F5F2;
    color: #30272E;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"] {
    background: #4B3044;
}

section[data-testid="stSidebar"] * {
    color: #F8F5F2 !important;
}

.sidebar-logo {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 600;
    margin-bottom: 6px;
}

.sidebar-sub {
    font-size: 12px;
    opacity: 0.7;
    margin-bottom: 35px;
}

.sidebar-section {
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    opacity: 0.55;
    margin: 25px 0 12px 0;
}

/* ================= HERO ================= */

.hero {
    padding: 55px 0 25px 0;
}

.hero-kicker {
    color: #687044;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 68px;
    line-height: 1.02;
    color: #4B3044;
    margin: 12px 0 20px 0;
}

.hero-description {
    font-size: 18px;
    line-height: 1.75;
    color: #746B70;
    max-width: 700px;
}

/* ================= HEADINGS ================= */

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 43px;
    line-height: 1.15;
    color: #4B3044;
    margin-top: 30px;
}

.section-subtitle {
    color: #746B70;
    font-size: 16px;
    margin-bottom: 25px;
}

.question-title {
    font-weight: 700;
    font-size: 17px;
    color: #4B3044;
    margin-top: 25px;
    margin-bottom: 8px;
}

/* ================= CARDS ================= */

.card {
    background: #EEE7E3;
    border-radius: 22px;
    padding: 30px;
    margin: 12px 0;
}

.olive-card {
    background: #DCE0C8;
    border-radius: 22px;
    padding: 30px;
    margin: 12px 0;
}

.white-card {
    background: #FFFFFF;
    border: 1px solid #E8E0DC;
    border-radius: 22px;
    padding: 30px;
    margin: 12px 0;
}

.card-number {
    font-family: 'Playfair Display', serif;
    font-size: 35px;
    color: #687044;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #4B3044;
    margin: 8px 0;
}

.card-text {
    color: #71686D;
    line-height: 1.65;
}

/* ================= BUTTONS ================= */

.stButton > button {
    border-radius: 30px;
    border: none;
    background: #4B3044;
    color: white;
    padding: 14px 28px;
    font-size: 15px;
    font-weight: 600;
}

.stButton > button:hover {
    background: #64435B;
    color: white;
}

/* ================= INPUTS ================= */

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 12px;
}

div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label {
    color: #4B3044;
}

/* ================= RESULT ================= */

.result-wrapper {
    background: #EEE7E3;
    border-radius: 28px;
    padding: 45px;
    text-align: center;
    margin: 25px 0;
}

.result-label {
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #687044;
    font-weight: 700;
}

.result-number {
    font-family: 'Playfair Display', serif;
    font-size: 78px;
    color: #4B3044;
    font-weight: 700;
    margin: 5px 0;
}

.result-status {
    font-size: 23px;
    font-weight: 700;
    color: #4B3044;
}

/* ================= DISCLAIMER ================= */

.disclaimer {
    background: #E8E7D7;
    border-left: 5px solid #687044;
    border-radius: 12px;
    padding: 22px;
    margin: 25px 0;
    color: #514D45;
    line-height: 1.6;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #8A8085;
    font-size: 12px;
    padding: 50px 0 25px 0;
}

hr {
    border: none;
    border-top: 1px solid #E1D9D5;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">DiaSense AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-sub">Diabetes risk awareness powered by machine learning</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">Explore</div>',
        unsafe_allow_html=True
    )

    if st.button("⌂   Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

    if st.button("◉   Take the Test", use_container_width=True):
        st.session_state.page = "Test"
        st.rerun()

    if st.button("▣   Result", use_container_width=True):
        st.session_state.page = "Result"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption(
        "DiaSense AI is an educational project and does not replace professional medical advice."
    )

# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    st.markdown('<div class="hero">', unsafe_allow_html=True)

    st.markdown(
        '<div class="hero-kicker">AI · HEALTH · AWARENESS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-title">Understand your risk.<br>Take charge of your health.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-description">'
        'DiaSense AI uses a trained machine-learning model to estimate '
        'diabetes risk from simple health and lifestyle information.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Take the Test  →"):
        st.session_state.page = "Test"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ---------- HOW IT WORKS ----------

    st.markdown(
        '<div class="section-title">How it works</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Three simple steps to understand your estimated risk.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="white-card">
        <div class="card-number">01</div>
        <div class="card-title">Tell us about you</div>
        <div class="card-text">
        Answer a few questions about age, BMI, blood pressure,
        cholesterol and lifestyle.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="white-card">
        <div class="card-number">02</div>
        <div class="card-title">AI analyses patterns</div>
        <div class="card-text">
        A Random Forest machine-learning model analyses the
        information and identifies patterns associated with diabetes.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="white-card">
        <div class="card-number">03</div>
        <div class="card-title">Understand your result</div>
        <div class="card-text">
        Receive an estimated risk score along with practical areas
        you can pay attention to.
        </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------- ABOUT DIABETES ----------

    st.markdown(
        '<div class="section-title">Why diabetes awareness matters</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="olive-card">
    <div class="card-title">What is diabetes?</div>
    <div class="card-text">
    Diabetes is a chronic condition in which blood glucose levels become
    too high. Risk can be influenced by several factors including body
    weight, physical activity, blood pressure, cholesterol and other
    health characteristics.
    <br><br>
    Understanding potential risk factors can encourage people to pay
    attention to their health and seek appropriate professional advice.
    </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- WHAT WE ASSESS ----------

    st.markdown(
        '<div class="section-title">What does DiaSense look at?</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
        <div class="card-title">Personal factors</div>
        <div class="card-text">
        • Age<br>
        • BMI<br>
        • Sex
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <div class="card-title">Health & lifestyle factors</div>
        <div class="card-text">
        • Blood pressure<br>
        • Cholesterol<br>
        • Physical activity<br>
        • Smoking<br>
        • Relevant health history
        </div>
        </div>
        """, unsafe_allow_html=True)

    # ---------- LIMITATION ----------

    st.markdown(
        '<div class="section-title">A quick note</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="disclaimer">
    <b>Important:</b> DiaSense AI is an academic machine-learning project
    designed for educational risk awareness. Its result is an estimate
    based on patterns in the training dataset. It is not a diagnosis,
    medical test, or substitute for a healthcare professional.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="footer">DiaSense AI · Academic Project · Machine Learning for Health Awareness</div>',
        unsafe_allow_html=True
    )

# =========================================================
# TEST PAGE
# =========================================================

elif st.session_state.page == "Test":

    st.markdown(
        '<div class="section-title">Take the Test</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Answer honestly. The test takes about a minute.'
        '</div>',
        unsafe_allow_html=True
    )

    # ---------- AGE ----------

    st.markdown(
        '<div class="question-title">1. What is your age?</div>',
        unsafe_allow_html=True
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25,
        step=1,
        label_visibility="collapsed"
    )

    # ---------- BMI ----------

    st.markdown(
        '<div class="question-title">2. What is your BMI?</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "BMI = weight (kg) ÷ height² (m²). "
        "Example: 70 kg ÷ (1.65 × 1.65) = 25.7."
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0,
        step=0.1,
        label_visibility="collapsed"
    )

    # ---------- BLOOD PRESSURE ----------

    st.markdown(
        '<div class="question-title">3. What is your blood pressure?</div>',
        unsafe_allow_html=True
    )

    bp_option = st.selectbox(
        "Blood pressure",
        [
            "Normal — below 120/80 mmHg",
            "Elevated — 120–129 / below 80 mmHg",
            "High — 130/80 mmHg or higher",
            "I don't know"
        ],
        label_visibility="collapsed"
    )

    st.caption(
        "If you have a recent BP reading, choose the category that matches it."
    )

    # ---------- CHOLESTEROL ----------

    st.markdown(
        '<div class="question-title">4. Do you have high cholesterol?</div>',
        unsafe_allow_html=True
    )

    cholesterol = st.selectbox(
        "Cholesterol",
        ["Yes", "No", "Don't know"],
        label_visibility="collapsed"
    )

    # ---------- PHYSICAL ACTIVITY ----------

    st.markdown(
        '<div class="question-title">5. How would you describe your regular physical activity?</div>',
        unsafe_allow_html=True
    )

    activity = st.selectbox(
        "Physical activity",
        ["High", "Moderate", "Low"],
        label_visibility="collapsed"
    )

    # ---------- SMOKING ----------

    st.markdown(
        '<div class="question-title">6. Do you currently smoke?</div>',
        unsafe_allow_html=True
    )

    smoker = st.selectbox(
        "Smoking",
        ["No", "Yes"],
        label_visibility="collapsed"
    )

    # ---------- STROKE ----------

    st.markdown(
        '<div class="question-title">7. Have you ever had a stroke?</div>',
        unsafe_allow_html=True
    )

    stroke = st.selectbox(
        "Stroke",
        ["No", "Yes", "Don't know"],
        label_visibility="collapsed"
    )

    # ---------- HEART DISEASE ----------

    st.markdown(
        '<div class="question-title">8. Have you had heart disease or a heart attack?</div>',
        unsafe_allow_html=True
    )

    heart = st.selectbox(
        "Heart disease",
        ["No", "Yes", "Don't know"],
        label_visibility="collapsed"
    )

    # ---------- SEX ----------

    st.markdown(
        '<div class="question-title">9. What is your sex?</div>',
        unsafe_allow_html=True
    )

    sex = st.selectbox(
        "Sex",
        ["Female", "Male", "Prefer not to say"],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- SUBMIT ----------

    if st.button("Submit & See My Result  →", use_container_width=True):

        # Blood pressure
        if bp_option.startswith("High"):
            high_bp = 1
        else:
            high_bp = 0

        # Cholesterol
        if cholesterol == "Yes":
            high_chol = 1
            chol_check = 1
        elif cholesterol == "No":
            high_chol = 0
            chol_check = 1
        else:
            high_chol = 0
            chol_check = 0

        # Activity
        if activity in ["High", "Moderate"]:
            phys_activity = 1
        else:
            phys_activity = 0

        # Other features
        smoker_value = 1 if smoker == "Yes" else 0

        stroke_value = 1 if stroke == "Yes" else 0

        heart_value = 1 if heart == "Yes" else 0

        sex_value = 1 if sex == "Male" else 0

        # Create model input
        data = pd.DataFrame([{
            "HighBP": high_bp,
            "HighChol": high_chol,
            "CholCheck": chol_check,
            "BMI": bmi,
            "Smoker": smoker_value,
            "Stroke": stroke_value,
            "HeartDiseaseorAttack": heart_value,
            "PhysActivity": phys_activity,
            "Fruits": 1,
            "Veggies": 1,
            "HvyAlcoholConsump": 0,
            "AnyHealthcare": 1,
            "NoDocbcCost": 0,
            "GenHlth": 3,
            "MentHlth": 0,
            "PhysHlth": 0,
            "DiffWalk": 0,
            "Sex": sex_value,
            "Age": age,
            "Education": 4,
            "Income": 5
        }])

        probability = model.predict_proba(data)[0][1]

        risk = probability * 100

        # Store results
        st.session_state.risk = risk
        st.session_state.age = age
        st.session_state.bmi = bmi
        st.session_state.activity = activity
        st.session_state.bp = bp_option
        st.session_state.cholesterol = cholesterol

        st.session_state.page = "Result"

        st.rerun()

# =========================================================
# RESULT PAGE
# =========================================================

elif st.session_state.page == "Result":

    if "risk" not in st.session_state:

        st.markdown(
            '<div class="section-title">Your Result</div>',
            unsafe_allow_html=True
        )

        st.info("Take the test first to generate your result.")

        if st.button("Take the Test →"):
            st.session_state.page = "Test"
            st.rerun()

    else:

        risk = st.session_state.risk
        bmi = st.session_state.bmi
        activity = st.session_state.activity
        bp = st.session_state.bp
        cholesterol = st.session_state.cholesterol

        st.markdown(
            '<div class="section-title">Your Result</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Your estimated risk is based on the information you provided.'
            '</div>',
            unsafe_allow_html=True
        )

        # ---------- RESULT CARD ----------

        if risk >= 50:
            status = "Higher estimated risk"
        elif risk >= 30:
            status = "Moderate estimated risk"
        else:
            status = "Lower estimated risk"

        st.markdown(f"""
        <div class="result-wrapper">
            <div class="result-label">Estimated diabetes risk</div>
            <div class="result-number">{risk:.1f}%</div>
            <div class="result-status">{status}</div>
        </div>
        """, unsafe_allow_html=True)

        st.progress(min(risk / 100, 1.0))

        # ---------- RISK OUTLOOK ----------

        st.markdown(
            '<div class="section-title">Risk Outlook</div>',
            unsafe_allow_html=True
        )

        if risk >= 50:
            outlook = (
                "Your current profile contains several factors associated "
                "with higher diabetes risk. This does not mean that you "
                "will develop diabetes, but it may be a good reason to "
                "pay closer attention to your health and discuss concerns "
                "with a healthcare professional."
            )

        elif risk >= 30:
            outlook = (
                "Your current profile shows some factors associated with "
                "diabetes risk. Maintaining healthy habits and monitoring "
                "important health measures may help support your long-term "
                "health."
            )

        else:
            outlook = (
                "Your current profile shows a lower estimated risk. "
                "Continue maintaining healthy lifestyle habits and regular "
                "health check-ups."
            )

        st.markdown(
            f'<div class="olive-card">{outlook}</div>',
            unsafe_allow_html=True
        )

        # ---------- IMPROVEMENT PRIORITIES ----------

        st.markdown(
            '<div class="section-title">Your Improvement Priorities</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "These percentages represent suggested priority levels based "
            "on your answers. They are not guaranteed reductions in medical risk."
        )

        # BMI priority
        if bmi >= 30:
            bmi_priority = 90
            bmi_text = "Weight management may be an important area to discuss with a professional."
        elif bmi >= 25:
            bmi_priority = 65
            bmi_text = "Gradual, sustainable weight management may be beneficial."
        else:
            bmi_priority = 25
            bmi_text = "Continue maintaining a healthy weight."

        # Activity priority
        if activity == "Low":
            activity_priority = 85
            activity_text = "Consider gradually increasing regular movement."
        elif activity == "Moderate":
            activity_priority = 55
            activity_text = "Try to make physical activity more consistent."
        else:
            activity_priority = 25
            activity_text = "Keep your current activity routine consistent."

        # BP priority
        if bp.startswith("High"):
            bp_priority = 90
            bp_text = "Monitor your blood pressure and discuss it with a healthcare professional."
        elif bp.startswith("Elevated"):
            bp_priority = 65
            bp_text = "Keep an eye on your blood pressure and maintain healthy habits."
        else:
            bp_priority = 25
            bp_text = "Continue monitoring your blood pressure when appropriate."

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="white-card">
                <div class="card-title">Body Weight</div>
                <h2>{bmi_priority}%</h2>
                <div class="card-text">{bmi_text}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="white-card">
                <div class="card-title">Physical Activity</div>
                <h2>{activity_priority}%</h2>
                <div class="card-text">{activity_text}</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="white-card">
                <div class="card-title">Blood Pressure</div>
                <h2>{bp_priority}%</h2>
                <div class="card-text">{bp_text}</div>
            </div>
            """, unsafe_allow_html=True)

        # ---------- ACTION PLAN ----------

        st.markdown(
            '<div class="section-title">Your Simple Action Plan</div>',
            unsafe_allow_html=True
        )

        actions = [
            ("Move more", "Build regular physical activity into your week."),
            ("Eat balanced", "Choose balanced meals and limit excessive added sugar."),
            ("Watch your weight", "If appropriate, work toward a healthy and sustainable weight."),
            ("Monitor health", "Keep track of blood pressure and cholesterol when recommended."),
            ("Talk to a professional", "Discuss concerning results or health changes with a qualified doctor.")
        ]

        for title, description in actions:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">✓ &nbsp; {title}</div>
                <div class="card-text">{description}</div>
            </div>
            """, unsafe_allow_html=True)

        # ---------- DISCLAIMER ----------

        st.markdown("""
        <div class="disclaimer">
        <b>Important medical disclaimer</b><br><br>
        This result is generated by a machine-learning model for educational
        and awareness purposes only. It is not a medical diagnosis and should
        not be used to make medical decisions. If you are concerned about your
        health or diabetes risk, please speak with a qualified healthcare
        professional.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("← Take the Test Again", use_container_width=True):
            st.session_state.page = "Test"
            st.rerun()

        st.markdown(
            '<div class="footer">DiaSense AI · Academic Machine Learning Project</div>',
            unsafe_allow_html=True
        )