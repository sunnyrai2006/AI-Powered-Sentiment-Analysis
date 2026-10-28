
import streamlit as st
import joblib
from pathlib import Path

# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="Sentiment AI",
    page_icon= r"C:\Users\sunny rai\OneDrive\Desktop\sentiment analysis\Neon AI Sentiment Insight Icon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# 2. MODEL PATH
# ==================================================
MODEL_PATH = Path(
    r"C:\Users\sunny rai\OneDrive\Desktop\sentiment analysis\sentiment_analysis.pkl"
)

# ==================================================
# 3. CUSTOM CSS
# ==================================================
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #f5f7ff 0%,
        #eef5ff 55%,
        #f8f4ff 100%
    );
}

/* Main content width and spacing */
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header */
.hero {
    background: linear-gradient(
        120deg,
        #1d4ed8,
        #6366f1,
        #7c3aed
    );
    padding: 35px;
    border-radius: 22px;
    color: #ffffff;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(79, 70, 229, 0.18);
}

.hero h1 {
    color: #ffffff !important;
    font-size: 2.4rem;
    margin-bottom: 8px;
}

.hero p {
    color: #eef2ff !important;
    font-size: 1.05rem;
}

.hero span {
    color: #ffffff !important;
}

/* General text contrast */
.stApp p,
.stApp h2,
.stApp h3,
.stApp label,
.stMarkdown {
    color: #1e293b;
}

/* Input area */
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
    font-size: 1rem !important;
}

.stTextArea textarea:focus {
    border: 1px solid #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.15) !important;
}

/* Button */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 11px;
    padding: 0.7rem 1rem;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: #ffffff !important;
    font-weight: 600;
    min-height: 48px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    filter: brightness(1.08);
    border: none;
    color: #ffffff !important;
}

/* Result card */
.sentiment-card {
    padding: 24px;
    border-radius: 16px;
    text-align: center;
    margin: 12px 0 22px 0;
    border: 1px solid transparent;
}

.positive {
    background: #dcfce7;
    border-color: #86efac;
    color: #166534 !important;
}

.negative {
    background: #ffe4e6;
    border-color: #fda4af;
    color: #9f1239 !important;
}

.neutral {
    background: #fef3c7;
    border-color: #fcd34d;
    color: #92400e !important;
}

.result-label {
    font-size: 26px;
    font-weight: 700;
}

.result-description {
    font-size: 14px;
    margin-top: 6px;
}

/* Probability section */
.probability-panel {
    background: #ffffff;
    padding: 22px;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    margin-top: 18px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b !important;
    font-size: 0.85rem;
    padding: 28px 0 5px;
    border-top: 1px solid #e2e8f0;
    margin-top: 35px;
}

/* Small-screen adjustments */
@media (max-width: 640px) {
    .hero {
        padding: 24px;
    }

    .hero h1 {
        font-size: 1.8rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# 4. LOAD TRAINED MODEL
# ==================================================
@st.cache_resource
def load_model(path):
    return joblib.load(path)

# ==================================================
# 5. HEADER
# ==================================================
st.markdown("""
<div class="hero">
    <h1>💬 Sentiment AI</h1>
    <p>Understand customer opinions with machine learning.</p>
    <span>
        ✦ AI-powered analysis &nbsp; • &nbsp;
        Three sentiment classes
    </span>
</div>
""", unsafe_allow_html=True)

# ==================================================
# 6. CHECK AND LOAD MODEL
# ==================================================
if not MODEL_PATH.exists():
    st.error(
        f"Trained model not found at:\n\n{MODEL_PATH}\n\n"
        "Please check the file path and filename."
    )
    st.stop()

try:
    model = load_model(str(MODEL_PATH))
except Exception as e:
    st.error(f"Could not load the trained model: {e}")
    st.stop()

# ==================================================
# 7. REVIEW INPUT
# ==================================================
with st.container(border=True):
    st.subheader("✍️ Analyze a customer review")

    st.write(
        "Enter a customer review below to predict its sentiment."
    )

    review = st.text_area(
        "Customer review",
        placeholder=(
            "Example: The product quality is excellent "
            "and delivery was very fast..."
        ),
        height=150,
        label_visibility="collapsed"
    )

    analyze = st.button(
        "✦  Analyze Sentiment",
        type="primary"
    )

# ==================================================
# 8. PREDICTION AND RESULTS
# ==================================================
if analyze:
    if not review.strip():
        st.warning("Please enter a review before analyzing.")

    else:
        try:
            clean_review = review.strip()

            prediction = str(
                model.predict([clean_review])[0]
            )

            normalized = prediction.strip().lower()

            sentiment_styles = {
                "positive": (
                    "positive",
                    "😊",
                    "Positive",
                    "The review expresses a positive sentiment."
                ),
                "negative": (
                    "negative",
                    "😞",
                    "Negative",
                    "The review expresses a negative sentiment."
                ),
                "neutral": (
                    "neutral",
                    "😐",
                    "Neutral",
                    "The review expresses a neutral sentiment."
                )
            }

            style, emoji, label, description = (
                sentiment_styles.get(
                    normalized,
                    (
                        "neutral",
                        "💬",
                        prediction,
                        "Predicted sentiment from the model."
                    )
                )
            )

            st.markdown("### 📊 Analysis Result")

            st.markdown(
                f"""
                <div class="sentiment-card {style}">
                    <div style="font-size:46px">{emoji}</div>
                    <div class="result-label">{label}</div>
                    <div class="result-description">
                        {description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # ------------------------------------------
            # CLASS PROBABILITIES
            # ------------------------------------------
            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(
                    [clean_review]
                )[0]

                st.markdown("### 📈 Class Probabilities")

                st.caption(
                    "Model-estimated probabilities; these are "
                    "not guarantees of prediction correctness."
                )

                for class_name, probability in zip(
                    model.classes_,
                    probabilities
                ):
                    st.write(
                        f"**{class_name}** — {probability:.1%}"
                    )
                    st.progress(float(probability))

        except Exception as e:
            st.error(f"Prediction failed: {e}")

# ==================================================
# 9. FOOTER
# ==================================================
st.markdown("""
<div class="footer">
    <strong>Sentiment AI</strong><br>
    Built with Python, Scikit-learn and Streamlit<br>
    For educational purposes. Predictions may be incorrect.
</div>
""", unsafe_allow_html=True)
