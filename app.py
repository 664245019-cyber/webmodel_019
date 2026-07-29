import streamlit as st

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="ML Web Model Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------- Custom CSS -------------------
st.markdown(
    """
    <style>
        /* ---------- Global ---------- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        * { font-family: 'Inter', sans-serif; }

        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
        }

        /* ---------- Header ---------- */
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 2.5rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
            color: white;
            text-align: center;
        }
        .header-container h1 {
            font-size: 2.4rem;
            font-weight: 800;
            margin: 0 0 0.5rem 0;
            letter-spacing: -0.5px;
        }
        .header-container .subtitle {
            font-size: 1rem;
            opacity: 0.9;
            max-width: 700px;
            margin: 0 auto 1.5rem auto;
            line-height: 1.6;
        }
        .header-divider {
            height: 2px;
            width: 80px;
            background: rgba(255,255,255,0.4);
            margin: 0 auto 1.2rem auto;
            border-radius: 2px;
        }
        .profile-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
        }
        .profile-avatar {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid rgba(255,255,255,0.5);
            background: rgba(255,255,255,0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            flex-shrink: 0;
        }
        .profile-info {
            text-align: left;
            font-size: 0.95rem;
            line-height: 1.8;
        }
        .profile-info strong { font-weight: 600; }

        /* ---------- Card ---------- */
        .card {
            background: white;
            border-radius: 16px;
            padding: 1.8rem 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            border: 1px solid rgba(0,0,0,0.03);
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 40px rgba(102, 126, 234, 0.18);
            border-color: rgba(102, 126, 234, 0.15);
        }
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 0.6rem;
        }
        .card h3 {
            font-size: 1.15rem;
            font-weight: 700;
            color: #1a1a2e;
            margin: 0 0 0.4rem 0;
        }
        .card p {
            font-size: 0.88rem;
            color: #6b7280;
            line-height: 1.5;
            flex: 1;
            margin: 0 0 1rem 0;
        }


        /* ---------- Footer ---------- */
        .footer {
            text-align: center;
            padding: 2rem 0 1rem 0;
            color: #9ca3af;
            font-size: 0.85rem;
            border-top: 1px solid rgba(0,0,0,0.06);
            margin-top: 2.5rem;
        }
        .footer strong { color: #6b7280; }

        /* ---------- Section title ---------- */
        .section-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #1a1a2e;
            text-align: center;
            margin-bottom: 0.2rem;
        }
        .section-sub {
            text-align: center;
            color: #9ca3af;
            font-size: 0.92rem;
            margin-bottom: 1.8rem;
        }

        /* ---------- Sidebar ---------- */
        .sidebar-dev {
            text-align: center;
            padding: 0.5rem 0;
        }
        .sidebar-dev .avatar {
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
        }
        .sidebar-dev h4 {
            font-weight: 700;
            color: #1a1a2e;
            margin: 0;
        }
        .sidebar-dev .detail {
            font-size: 0.85rem;
            color: #6b7280;
            line-height: 1.7;
            margin-top: 0.4rem;
        }
        .sidebar-dev .badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-size: 0.7rem;
            font-weight: 600;
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            margin-top: 0.8rem;
        }
        .sidebar-status {
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 12px;
            padding: 0.8rem;
            text-align: center;
            margin-top: 1.2rem;
        }
        .sidebar-status .check {
            font-size: 1.3rem;
            color: #16a34a;
        }
        .sidebar-status p {
            font-size: 0.8rem;
            color: #16a34a;
            font-weight: 600;
            margin: 0.2rem 0 0 0;
        }

        /* ---------- Card Link Button ---------- */
        .card-btn {
            display: block;
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            border: none;
            border-radius: 10px;
            padding: 0.45rem 1.4rem;
            font-weight: 600;
            font-size: 0.85rem;
            width: 100%;
            transition: all 0.25s ease;
            box-shadow: 0 4px 14px rgba(102, 126, 234, 0.25);
            text-decoration: none !important;
            box-sizing: border-box;
            margin-top: 0.5rem;
        }
        .card-btn:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
            color: white !important;
        }

        /* ---------- Responsive ---------- */
        @media (max-width: 768px) {
            .header-container h1 { font-size: 1.6rem; }
            .profile-row { flex-direction: column; text-align: center; }
            .profile-info { text-align: center; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- Sidebar -------------------
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-dev">
            <div class="avatar">👨‍💻</div>
            <h4>ผู้พัฒนา</h4>
            <div class="detail">
                <strong>ชื่อ:</strong> นายคณิศร จันทรสูตร<br>
                <strong>รหัส:</strong> 664245019<br>
                <strong>หมู่เรียน:</strong> 66/43<br>
            </div>
            <span class="badge">ML Portfolio</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### 📊 Portfolio Progress")
    st.progress(1.0)
    st.markdown(
        """
        <div style="text-align:center; font-size:0.85rem; color:#6b7280;">
            <strong>6</strong> / 6 Models
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-status">
            <div class="check">✅</div>
            <p>All Applications Successfully Deployed</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------- Header -------------------
st.markdown(
    """
    <div class="header-container">
        <h1>Web Model</h1>
        <div class="header-divider"></div>
        <p class="subtitle">
            รวบรวมเว็บแอปพลิเคชันด้าน Machine Learning จำนวน 6 ผลงาน
        </p>
        <div class="profile-row">
            <div class="profile-avatar">👨‍💻</div>
            <div class="profile-info">
                <strong>ชื่อผู้พัฒนา</strong><br>
                รหัสนักศึกษา: 664245019 &nbsp;|&nbsp; หมู่เรียน: 66/43<br>
                รายวิชา: Machine Learning
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------- Section Title -------------------
st.markdown('<p class="section-title">📦 Machine Learning Models</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-sub">Explore all six deployed applications below</p>',
    unsafe_allow_html=True,
)

# ------------------- Card Data -------------------
models = [
    {
        "icon": "🧮",
        "name": "K-Nearest Neighbor (KNN)",
        "desc": "Classification using KNN algorithm.",
        "link": "https://knnml2-019-69.streamlit.app/",
    },
    {
        "icon": "🌳",
        "name": "Decision Tree",
        "desc": "Classification using Decision Tree.",
        "link": "https://dtreeheartdeseat-6jh923zdgap4rvgzmd9mxd.streamlit.app/",
    },
    {
        "icon": "⚡",
        "name": "Support Vector Machine (SVM)",
        "desc": "Classification using SVM.",
        "link": "https://m2kpub5tweaxue8xzxzfxh.streamlit.app/",
    },
    {
        "icon": "🌀",
        "name": "K-Means Clustering",
        "desc": "Unsupervised clustering using K-Means.",
        "link": "https://k-mean-019-3sgxqvfnxlswvdsvwawaai.streamlit.app/",
    },
    {
        "icon": "📈",
        "name": "Regression",
        "desc": "Regression prediction model.",
        "link": "https://regression-usug3mbkxvbhpfrgivsasw.streamlit.app/",
    },
    {
        "icon": "🌲",
        "name": "Ensemble (Random Forest)",
        "desc": "Classification using Random Forest.",
        "link": "https://randomforest019-hkmfm94czhwer4z8dql5kz.streamlit.app/",
    },
]

# ------------------- Render Cards (3 cols x 2 rows) -------------------
for i in range(0, 6, 3):
    cols = st.columns(3, gap="medium")
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(models):
            m = models[idx]
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-icon">{m['icon']}</div>
                        <h3>{m['name']}</h3>
                        <p>{m['desc']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"""
                    <a href="{m['link']}" target="_blank" class="card-btn">
                        🚀 Open Application
                    </a>
                    """,
                    unsafe_allow_html=True,
                )

# ------------------- Footer -------------------
st.markdown(
    """
    <div class="footer">
        <strong>Machine Learning Web Portfolio</strong><br>
        Developed by Khanisorn Chanthasoot 019<br>
        © 2026
    </div>
    """,
    unsafe_allow_html=True,
)
