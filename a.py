# ==========================================
# LIFELENS AI
# PART 1 - SETUP + NAVIGATION + HOME
# ==========================================


import streamlit as st
import pandas as pd
import plotly.express as px
import time



# ================= PAGE CONFIG =================

st.set_page_config(

    page_title="LifeLens AI",

    page_icon="🧬",

    layout="wide"

)



# ================= GLOBAL CSS =================


st.markdown("""

<style>


.stApp{

background:

radial-gradient(

circle at top,

#0f766e,

#020617 70%

);

}



html,body,[class*="css"]{

font-family:Poppins,sans-serif;

color:white;

}



h1,h2,h3{

color:#5eead4 !important;

font-weight:900;

}

/* SIDEBAR NAVIGATION FONT FIX */

section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label{

    color:white !important;

    font-size:18px !important;

    font-weight:700 !important;

}


/* RADIO OPTION HOVER */

section[data-testid="stSidebar"] label:hover{

    color:#5eead4 !important;

}


/* SIDEBAR TITLE */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h3{

    color:#5eead4 !important;

}



p,label,span{

color:white !important;

}



.stButton button{


width:100%;

height:55px;

border-radius:25px;

background:

linear-gradient(

45deg,

#14b8a6,

#2563eb

);

color:white;

font-size:18px;

font-weight:bold;

}



.card{


background:

linear-gradient(

145deg,

rgba(255,255,255,0.15),

rgba(255,255,255,0.05)

);


padding:30px;

border-radius:30px;

border:1px solid #14b8a6;

box-shadow:15px 15px 40px black;

text-align:center;


}

/* ================= SIDEBAR RADIO FONT FIX ================= */

section[data-testid="stSidebar"] 
[data-testid="stMarkdownContainer"] * {

    color: #ffffff !important;

}


section[data-testid="stSidebar"] 
div[role="radiogroup"] label {

    color: #ffffff !important;

    font-size: 20px !important;

    font-weight: 700 !important;

}


section[data-testid="stSidebar"] 
div[role="radiogroup"] label p {

    color: #ffffff !important;

    font-size: 20px !important;

    font-weight: 700 !important;

}


/* Selected navigation */

section[data-testid="stSidebar"] 
div[role="radiogroup"] label[data-checked="true"] p {

    color:#5eead4 !important;

}


/* Sidebar background */

section[data-testid="stSidebar"] {

    background: #020617 !important;

}

</style>

""",unsafe_allow_html=True)





# ================= SIDEBAR =================


st.sidebar.markdown(

"""

# 🧬 LifeLens AI

### Navigation

"""

)



page = st.sidebar.radio(

"",

[

"🌌 Home",

"🔐 Login",

"🏠 Dashboard",

"🧬 Wellness Prediction",

"📊 Analytics",

"🤖 AI Assistant",

"🆘 Emergency Vault",

"ℹ️ About"

]

)






# ==========================================
# PART 1 - HOME PAGE
# ==========================================


if page=="🌌 Home":


    st.markdown(

    """

    <h1 style='text-align:center;font-size:65px'>

    🧬 LifeLens AI

    </h1>


    """,

    unsafe_allow_html=True

    )



    st.markdown(

    """

    <h3 style='text-align:center'>

    AI Powered Personal Health Intelligence Platform

    <br>

    Monitor Lifestyle • Predict Wellness • Protect Future

    </h3>

    """,

    unsafe_allow_html=True

    )



    st.markdown(

    """

    <div style='text-align:center;font-size:130px'>

    🤖💙

    </div>

    """,

    unsafe_allow_html=True

    )



    if st.button("🚀 Start Your Health Journey"):

        st.success(
        "Welcome to LifeLens AI"
        )

        st.balloons()



    st.write("")



    st.subheader("✨ Smart Health Features")



    c1,c2,c3,c4 = st.columns(4)



    features=[

    ("😴","Sleep AI","Sleep Quality Analysis"),

    ("🧠","Wellness AI","Health Prediction"),

    ("🚨","Emergency Vault","Medical Safety"),

    ("🤖","AI Assistant","Smart Guidance")

    ]



    for col,item in zip(

        [c1,c2,c3,c4],

        features

    ):

        with col:


            st.markdown(

            f"""

            <div class="card">


            <h1>

            {item[0]}

            </h1>


            <h3>

            {item[1]}

            </h3>


            <p>

            {item[2]}

            </p>


            </div>

            """,

            unsafe_allow_html=True

            )





    st.write("")



    st.subheader("🌎 LifeLens AI Impact")



    a,b,c = st.columns(3)



    with a:

        st.metric(

        "🤖 AI Predictions",

        "50K+"

        )



    with b:

        st.metric(

        "🚨 Emergency Support",

        "24/7"

        )



    with c:

        st.metric(

        "🔐 Security",

        "100%"

        )




    st.success(

    "🧬 LifeLens AI combines AI, Machine Learning and Data Analytics for smarter healthcare."
    )

# ==========================================
# PART 2 - LIFELENS AI LOGIN PAGE
# ==========================================


elif page=="🔐 Login":


    st.markdown("""
    <style>


    .login-box{

        background:

        linear-gradient(

        145deg,

        rgba(255,255,255,0.18),

        rgba(255,255,255,0.05)

        );


        backdrop-filter:blur(25px);


        padding:45px;


        border-radius:40px;


        border:1px solid #14b8a6;


        box-shadow:20px 20px 50px black;


        text-align:center;

    }



    .login-title{

        font-size:55px;

        font-weight:900;

        color:#5eead4;

        text-shadow:

        0px 10px 30px #14b8a6;

    }



    .robot{

        font-size:120px;

        animation:float 3s infinite;

    }



    @keyframes float{


        0%{

        transform:translateY(0px);

        }


        50%{

        transform:translateY(-25px);

        }


        100%{

        transform:translateY(0px);

        }

    }



    .security-card{


        background:

        linear-gradient(

        45deg,

        #0f766e,

        #020617

        );


        padding:25px;

        border-radius:25px;

        text-align:center;

        border:1px solid #5eead4;

    }



    </style>

    """,

    unsafe_allow_html=True

    )




    # HEADER


    st.markdown(

    """

    <div class="login-box">


    <div class="robot">

    🧬🤖

    </div>


    <div class="login-title">

    Welcome Back

    </div>


    <h3>

    Enter Into LifeLens AI

    </h3>


    </div>

    """,

    unsafe_allow_html=True

    )



    st.write("")



    # LOGIN FORM


    col1,col2 = st.columns(2)



    with col1:


        name = st.text_input(

            "👤 Full Name",

            placeholder="Enter your name"

        )



        email = st.text_input(

            "📧 Email Address",

            placeholder="example@gmail.com"

        )




    with col2:


        password = st.text_input(

            "🔒 Password",

            type="password",

            placeholder="Enter password"

        )



        user_type = st.selectbox(

            "👥 User Type",

            [

            "Student",

            "Professional",

            "Family"

            ]

        )




    st.write("")



    # LOGIN BUTTON


    if st.button("🚀 Enter LifeLens AI"):


        if name and email and password:


            st.success(

            f"Welcome {name}! LifeLens AI Activated 🧬"

            )


            st.balloons()



            # move dashboard

            st.session_state.page="🏠 Dashboard"


            time.sleep(1)


            st.rerun()



        else:


            st.warning(

            "⚠️ Please fill all details"

            )




    st.write("")



    # SECURITY FEATURES


    st.markdown(

    """

    <div class="security-card">


    🔐 Secure Health Data Storage


    <br><br>


    🤖 AI Powered Wellness Prediction


    <br><br>


    🚨 Emergency Protection System


    </div>


    """,

    unsafe_allow_html=True

    )# ==========================================
# PART 3 - LIFELENS AI DASHBOARD
# ==========================================


elif page=="🏠 Dashboard":


    st.markdown("""
    <style>


    .dash-title{

        text-align:center;

        font-size:55px;

        font-weight:900;

        color:#5eead4;

        text-shadow:

        0px 10px 30px #14b8a6;

    }



    .dash-ai{

        text-align:center;

        font-size:120px;

        animation:floatDash 3s infinite;

    }



    @keyframes floatDash{


        0%{

        transform:translateY(0px);

        }


        50%{

        transform:translateY(-25px);

        }


        100%{

        transform:translateY(0px);

        }

    }



    .health-card{


        background:

        linear-gradient(

        145deg,

        rgba(255,255,255,0.18),

        rgba(255,255,255,0.05)

        );


        backdrop-filter:blur(20px);


        padding:30px;


        border-radius:35px;


        border:1px solid #14b8a6;


        box-shadow:15px 15px 40px black;


        text-align:center;

    }



    .icon{

        font-size:60px;

    }



    .value{

        font-size:35px;

        font-weight:900;

        color:#5eead4;

    }



    </style>

    """,

    unsafe_allow_html=True

    )




    # TITLE


    st.markdown(

    """

    <div class="dash-title">

    🏠 LifeLens AI Health Dashboard

    </div>

    """,

    unsafe_allow_html=True

    )



    st.markdown(

    """

    <div class="dash-ai">

    🧬🤖

    </div>

    """,

    unsafe_allow_html=True

    )




    st.write("")



    # HEALTH CARDS


    c1,c2,c3,c4 = st.columns(4)



    dashboard_data=[


    ("❤️","Health Score","92%"),


    ("😴","Sleep","7.5 Hrs"),


    ("💧","Water","2.5 L"),


    ("🏃","Activity","HIGH")

    ]




    for col,data in zip(

        [c1,c2,c3,c4],

        dashboard_data

    ):


        with col:


            st.markdown(

            f"""

            <div class="health-card">


            <div class="icon">

            {data[0]}

            </div>



            <h3>

            {data[1]}

            </h3>



            <div class="value">

            {data[2]}

            </div>



            </div>

            """,

            unsafe_allow_html=True

            )




    st.write("")



    # AI INSIGHT


    st.subheader("🤖 AI Health Insight")



    st.markdown(

    """

    <div class="health-card">


    🧠 LifeLens Recommendation


    <br><br>


    Your lifestyle balance is good.

    Maintain proper sleep,

    increase exercise and drink enough water.


    </div>


    """,

    unsafe_allow_html=True

    )




    st.write("")



    # WELLNESS CHART


    st.subheader("📊 Daily Wellness Activity")



    wellness = pd.DataFrame(

    {

    "Activity":

    [

    "Sleep",

    "Water",

    "Exercise",

    "Meditation"

    ],


    "Score":

    [

    85,

    90,

    75,

    80

    ]

    }

    )




    fig = px.bar(

        wellness,

        x="Activity",

        y="Score",

        text="Score",

        template="plotly_dark"

    )



    fig.update_traces(

        textposition="outside"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )




    # HEALTH SCAN BUTTON


    if st.button("🧬 Run AI Health Scan"):


        with st.spinner(

            "AI Scanning Your Lifestyle..."

        ):

            time.sleep(2)



        st.success(

        "✅ LifeLens AI Health Scan Completed"

        )


        st.balloons()# ==========================================
# PART 4 - LIFELENS AI WELLNESS PREDICTION
# ==========================================


elif page=="🧬 Wellness Prediction":


    st.markdown("""
    <style>


    .predict-title{

        text-align:center;

        font-size:55px;

        font-weight:900;

        color:#f0abfc;

        text-shadow:

        0px 10px 30px #c026d3;

    }



    .predict-ai{

        text-align:center;

        font-size:120px;

        animation:floatPredict 3s infinite;

    }



    @keyframes floatPredict{


        0%{

        transform:translateY(0px);

        }


        50%{

        transform:translateY(-25px);

        }


        100%{

        transform:translateY(0px);

        }

    }




    .predict-card{


        background:

        linear-gradient(

        145deg,

        rgba(255,255,255,0.15),

        rgba(255,255,255,0.05)

        );


        backdrop-filter:blur(20px);


        padding:35px;


        border-radius:35px;


        border:1px solid #c026d3;


        box-shadow:15px 15px 40px black;


    }




    .result-card{


        background:

        linear-gradient(

        145deg,

        #312e81,

        #020617

        );


        padding:30px;


        border-radius:30px;


        text-align:center;


        box-shadow:10px 10px 30px black;


    }



    .result-value{


        font-size:30px;

        font-weight:900;

        color:white;

    }



    </style>

    """,

    unsafe_allow_html=True

    )





    # TITLE


    st.markdown(

    """

    <div class="predict-title">

    🧬 AI Wellness Prediction Lab

    </div>

    """,

    unsafe_allow_html=True

    )





    st.markdown(

    """

    <div class="predict-ai">

    🤖🧠

    </div>

    """,

    unsafe_allow_html=True

    )





    st.markdown(

    """

    <div class="predict-card">

    Enter your lifestyle details and get AI wellness analysis 🚀

    </div>

    """,

    unsafe_allow_html=True

    )



    st.write("")





    # INPUT SECTION


    col1,col2 = st.columns(2)



    with col1:


        age = st.number_input(

            "🎂 Age",

            min_value=10,

            max_value=100,

            value=20

        )



        sleep = st.slider(

            "😴 Sleep Hours",

            0.0,

            12.0,

            7.0

        )



        water = st.slider(

            "💧 Water Intake (Litres)",

            0.0,

            5.0,

            2.0

        )



        exercise = st.slider(

            "🏃 Exercise Minutes",

            0,

            180,

            30

        )




    with col2:


        screen = st.slider(

            "📱 Screen Time Hours",

            0.0,

            15.0,

            4.0

        )



        stress = st.slider(

            "😰 Stress Level",

            1,

            10,

            5

        )



        mood = st.slider(

            "😊 Mood Level",

            1,

            10,

            7

        )



        heart = st.slider(

            "❤️ Heart Rate",

            50,

            150,

            75

        )





    st.write("")





    # PREDICTION BUTTON


    if st.button("🚀 Analyze My Wellness"):


        with st.spinner(

            "LifeLens AI Analyzing Health..."

        ):


            time.sleep(2)





        # HEALTH SCORE CALCULATION


        health_score = int(

            (sleep/8)*25

            +

            (water/3)*20

            +

            (exercise/60)*20

            +

            (mood/10)*15

            +

            ((10-stress)/10)*20

        )



        if health_score >= 80:


            health_status="Excellent 🌟"



        elif health_score >=50:


            health_status="Good 👍"



        else:


            health_status="Needs Improvement ⚠️"





        if stress >=7:


            stress_status="High 🔥"


        else:


            stress_status="Low 🌱"





        if sleep>=7 and exercise>=30:


            energy="High ⚡"


        else:


            energy="Medium 🔋"





        st.success(

        "✅ AI Wellness Prediction Completed"

        )





        st.write("")




        # RESULT CARDS


        c1,c2,c3 = st.columns(3)




        results=[


        ("❤️","Health Status",health_status),


        ("🔥","Stress Risk",stress_status),


        ("⚡","Energy Level",energy)

        ]




        for col,data in zip(

            [c1,c2,c3],

            results

        ):


            with col:


                st.markdown(

                f"""

                <div class="result-card">


                <h1>

                {data[0]}

                </h1>



                <h3>

                {data[1]}

                </h3>



                <div class="result-value">

                {data[2]}

                </div>


                </div>


                """,

                unsafe_allow_html=True

                )



        st.write("")


        st.info(

        f"🧠 AI Health Score: {health_score}%"

        )


        st.balloons()# ==========================================
# PART 5 - LIFELENS AI ANALYTICS DASHBOARD
# ==========================================


elif page=="📊 Analytics":


    st.markdown("""
    <style>


    .analytics-title{

        text-align:center;
        font-size:50px;
        font-weight:900;
        color:#34d399;
        text-shadow:0px 10px 30px #10b981;

    }


    .analytics-card{

        background:
        linear-gradient(
        145deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.05)
        );

        backdrop-filter:blur(20px);

        padding:30px;

        border-radius:30px;

        border:1px solid #10b981;

        box-shadow:15px 15px 40px black;

        text-align:center;

    }


    .analytics-icon{

        font-size:60px;

    }


    .analytics-name{

        color:#6ee7b7;

        font-size:22px;

        font-weight:900;

    }


    .analytics-value{

        color:white;

        font-size:35px;

        font-weight:900;

    }


    </style>

    """,
    unsafe_allow_html=True)



    # TITLE

    st.markdown(
    """
    <div class="analytics-title">

    📊 LifeLens AI Health Analytics

    </div>
    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div style="text-align:center;font-size:120px">

    🌎🧬🤖

    </div>
    """,
    unsafe_allow_html=True
    )


    st.write("")



    # KPI CARDS


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.markdown(
        """
        <div class="analytics-card">

        <div class="analytics-icon">
        ❤️
        </div>

        <div class="analytics-name">
        Health Score
        </div>

        <div class="analytics-value">
        92%
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



    with c2:

        st.markdown(
        """
        <div class="analytics-card">

        <div class="analytics-icon">
        😴
        </div>

        <div class="analytics-name">
        Sleep Quality
        </div>

        <div class="analytics-value">
        85%
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



    with c3:

        st.markdown(
        """
        <div class="analytics-card">

        <div class="analytics-icon">
        🧠
        </div>

        <div class="analytics-name">
        Mental Wellness
        </div>

        <div class="analytics-value">
        88%
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



    with c4:

        st.markdown(
        """
        <div class="analytics-card">

        <div class="analytics-icon">
        🏃
        </div>

        <div class="analytics-name">
        Fitness Level
        </div>

        <div class="analytics-value">
        HIGH
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )



    st.write("")



    # CHART 1

    st.subheader("🧬 Lifestyle Performance Analysis")


    lifestyle = pd.DataFrame({

        "Category":[
            "Sleep",
            "Water",
            "Exercise",
            "Mood",
            "Meditation"
        ],

        "Score":[
            85,
            90,
            75,
            88,
            70
        ]

    })



    fig1 = px.bar(

        lifestyle,

        x="Category",

        y="Score",

        text="Score",

        template="plotly_dark"

    )


    fig1.update_traces(
        textposition="outside"
    )


    st.plotly_chart(
        fig1,
        use_container_width=True
    )



    # CHART 2


    st.subheader("🔥 Stress Risk Distribution")


    stress_data = pd.DataFrame({

        "Risk":[
            "Low",
            "Medium",
            "High"
        ],

        "Users":[
            700,
            220,
            80
        ]

    })



    fig2 = px.pie(

        stress_data,

        names="Risk",

        values="Users",

        hole=0.5,

        template="plotly_dark"

    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



    # CHART 3


    st.subheader("🎯 AI Health Feature Importance")


    feature = pd.DataFrame({

        "Feature":[
            "Sleep",
            "Exercise",
            "Water",
            "Stress",
            "Mood"
        ],

        "Importance":[
            95,
            80,
            75,
            90,
            85
        ]

    })



    fig3 = px.line(

        feature,

        x="Feature",

        y="Importance",

        markers=True,

        template="plotly_dark"

    )



    st.plotly_chart(
        fig3,
        use_container_width=True
    )



    st.success(
        "📊 LifeLens AI Analytics Completed Successfully 🤖"
    )# ==========================================
# PART 6 - LIFELENS AI ASSISTANT
# ==========================================


elif page=="🤖 AI Assistant":


    st.markdown("""
    <style>


    .assistant-title{

        text-align:center;

        font-size:50px;

        font-weight:900;

        color:#5eead4;

        text-shadow:
        0px 10px 30px #14b8a6;

    }



    .assistant-card{

        background:

        linear-gradient(
        145deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.05)
        );


        backdrop-filter:blur(20px);


        padding:35px;


        border-radius:35px;


        border:1px solid #14b8a6;


        box-shadow:15px 15px 40px black;


    }



    .assistant-ai{

        text-align:center;

        font-size:120px;

        animation:floatAI 3s infinite;

    }



    @keyframes floatAI{

        0%{
        transform:translateY(0px);
        }


        50%{
        transform:translateY(-20px);
        }


        100%{
        transform:translateY(0px);
        }

    }



    .ai-msg{

        background:#0f766e;

        padding:20px;

        border-radius:25px;

        font-size:18px;

        margin:10px;

    }



    .user-msg{

        background:#2563eb;

        padding:20px;

        border-radius:25px;

        font-size:18px;

        margin:10px;

    }


    </style>

    """,
    unsafe_allow_html=True
    )



    # TITLE


    st.markdown(
    """
    <div class="assistant-title">

    🤖 LifeLens AI Health Assistant

    </div>
    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="assistant-ai">

    🤖💙

    </div>
    """,
    unsafe_allow_html=True
    )



    # INTRO


    st.markdown(
    """
    <div class="assistant-card">

    <div class="ai-msg">

    🤖 Hello! I am LifeLens AI Assistant.

    <br><br>

    I can help you with:

    <br><br>

    😴 Sleep Improvement

    <br>

    💧 Water & Healthy Lifestyle

    <br>

    🏃 Fitness Guidance

    <br>

    🧠 Stress Management

    <br>

    🆘 Emergency Guidance

    </div>


    </div>

    """,
    unsafe_allow_html=True
    )



    st.write("")



    # USER QUESTION


    question = st.text_input(

        "💬 Ask LifeLens AI",

        placeholder="Example: How can I improve my sleep?"

    )



    if st.button("🚀 Ask AI"):


        with st.spinner("AI Thinking..."):

            time.sleep(2)



        q = question.lower()



        if "sleep" in q:


            answer = """

😴 Sleep Tips:

✅ Sleep 7-8 hours daily

✅ Avoid mobile before sleeping

✅ Maintain fixed sleep timing

"""



        elif "water" in q or "hydration" in q:


            answer = """

💧 Hydration Tips:

✅ Drink 2-3 litres water daily

✅ Drink water after waking up

✅ Avoid excess sugary drinks

"""



        elif "stress" in q or "mental" in q:


            answer = """

🧠 Stress Management:

✅ Practice meditation

✅ Take small breaks

✅ Exercise regularly

"""



        elif "exercise" in q or "fitness" in q:


            answer = """

🏃 Fitness Plan:

✅ Walk daily

✅ Exercise 30 minutes

✅ Maintain active lifestyle

"""



        elif "emergency" in q or "help" in q:


            answer = """

🆘 Emergency Guidance:

✅ Stay calm

✅ Contact emergency person

✅ Share medical information

"""



        else:


            answer = """

🌱 General Health Advice:

✅ Sleep properly

✅ Eat balanced food

✅ Stay active

✅ Track your health regularly

"""



        st.markdown(
f"""
<div class="assistant-card">

<div class="user-msg">

👤 You:

<br><br>

{question}

</div>


<div class="ai-msg">

🤖 LifeLens AI:

<br><br>

{answer.replace(chr(10), "<br>")}

</div>


</div>
""",
unsafe_allow_html=True
)



    st.write("")



    # QUICK ACTIONS


    st.subheader("⚡ Quick Health Actions")



    c1,c2,c3 = st.columns(3)



    with c1:

        st.info(
            "😴 Sleep Check"
        )


    with c2:

        st.success(
            "🧠 Stress Check"
        )


    with c3:

        st.warning(
            "🏃 Fitness Plan"
        )# ==========================================
# PART 7 - LIFELENS AI EMERGENCY VAULT
# ==========================================


elif page=="🆘 Emergency Vault":


    st.markdown("""
    <style>


    .vault-title{

        text-align:center;

        font-size:50px;

        font-weight:900;

        color:#ef4444;

        text-shadow:
        0px 10px 30px #dc2626;

    }



    .vault-card{

        background:

        linear-gradient(
        145deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.05)
        );


        backdrop-filter:blur(20px);


        padding:35px;


        border-radius:35px;


        border:2px solid #ef4444;


        box-shadow:15px 15px 40px black;


    }



    </style>

    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="vault-title">

    🚨 LifeLens Emergency Vault

    </div>
    """,
    unsafe_allow_html=True
    )



    st.write("")



    st.markdown(
    """
    <div class="vault-card">

    Securely store your emergency medical information.

    </div>

    """,
    unsafe_allow_html=True
    )



    st.write("")



    # STORAGE


    if "vault_data" not in st.session_state:

        st.session_state.vault_data = {}



    name = st.text_input(
        "👤 Full Name"
    )


    age = st.number_input(
        "🎂 Age",
        1,
        120,
        20
    )


    blood = st.selectbox(

        "🩸 Blood Group",

        [
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]

    )


    phone = st.text_input(
        "📞 Emergency Contact"
    )


    allergy = st.text_area(
        "⚠️ Allergy Details"
    )


    medical = st.text_area(
        "🏥 Medical History"
    )


    medicine = st.text_area(
        "💊 Current Medicines"
    )



    if st.button("💾 Save Emergency Data"):


        st.session_state.vault_data = {


            "Name":name,

            "Age":age,

            "Blood Group":blood,

            "Emergency Contact":phone,

            "Allergy":allergy,

            "Medical History":medical,

            "Medicines":medicine

        }



        st.success(
            "✅ Emergency Vault Saved Successfully"
        )


        st.balloons()



    st.divider()



    st.subheader(
        "📋 Saved Emergency Details"
    )



    if st.session_state.vault_data:


        for key,value in st.session_state.vault_data.items():

            st.info(
                f"{key} : {value}"
            )


    else:


        st.warning(
            "⚠️ Emergency Vault Empty"
        )





# ==========================================
# PART 8 - LIFELENS AI ABOUT PAGE
# ==========================================


elif page=="ℹ️ About":


    st.markdown("""
    <style>


    .about-title{

        text-align:center;

        font-size:50px;

        font-weight:900;

        color:#38bdf8;

    }



    .about-card{

        background:

        linear-gradient(
        145deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.05)
        );


        padding:35px;

        border-radius:35px;

        border:1px solid #38bdf8;

        box-shadow:15px 15px 40px black;

        text-align:center;

    }


    </style>

    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="about-title">

    🛡️ About LifeLens AI

    </div>

    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div style="text-align:center;font-size:120px">

    🤖💙

    </div>

    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="about-card">


    <h2>
    🏥 Project Overview
    </h2>


    <p>

    LifeLens AI is an AI-powered digital health
    safety platform.


    <br><br>


    It helps users monitor wellness,
    store emergency medical information,
    and get AI based health guidance.

    </p>


    </div>

    """,
    unsafe_allow_html=True
    )



    st.write("")



    c1,c2,c3 = st.columns(3)



    with c1:

        st.markdown(
        """
        <div class="about-card">

        🚨

        <h3>
        Emergency SOS
        </h3>

        Instant emergency support.

        </div>
        """,
        unsafe_allow_html=True
        )



    with c2:

        st.markdown(
        """
        <div class="about-card">

        🧬

        <h3>
        Medical Vault
        </h3>

        Secure health storage.

        </div>
        """,
        unsafe_allow_html=True
        )



    with c3:

        st.markdown(
        """
        <div class="about-card">

        🤖

        <h3>
        AI Assistant
        </h3>

        Smart health guidance.

        </div>
        """,
        unsafe_allow_html=True
        )



    st.success(
        "🎉 LifeLens AI Completed Successfully 🚀"
    )# ==========================================
# PART 8 - LIFELENS AI ABOUT PAGE
# ==========================================


elif page=="ℹ️ About":


    st.markdown("""
    <style>


    .about-title{

        text-align:center;

        font-size:50px;

        font-weight:900;

        color:#38bdf8;

        text-shadow:
        0px 10px 30px #2563eb;

    }



    .about-ai{

        text-align:center;

        font-size:120px;

        animation:aboutFloat 3s infinite;

    }



    @keyframes aboutFloat{


        0%{

            transform:translateY(0px);

        }


        50%{

            transform:translateY(-20px);

        }


        100%{

            transform:translateY(0px);

        }


    }




    .about-card{


        background:

        linear-gradient(

        145deg,

        rgba(255,255,255,0.15),

        rgba(255,255,255,0.05)

        );


        backdrop-filter:blur(20px);


        padding:35px;


        border-radius:35px;


        border:1px solid #38bdf8;


        box-shadow:

        15px 15px 40px black;


        text-align:center;


        margin-bottom:20px;


    }




    .about-icon{

        font-size:70px;

    }



    .about-heading{

        color:#38bdf8;

        font-size:28px;

        font-weight:900;

    }



    .about-text{

        color:white;

        font-size:18px;

        line-height:1.8;

    }


    </style>

    """,
    unsafe_allow_html=True
    )




    # TITLE


    st.markdown(
    """
    <div class="about-title">

    🛡️ About LifeLens AI

    </div>
    """,
    unsafe_allow_html=True
    )



    st.markdown(
    """
    <div class="about-ai">

    🤖💙

    </div>
    """,
    unsafe_allow_html=True
    )




    # PROJECT OVERVIEW


    st.markdown(
    """
    <div class="about-card">


    <div class="about-icon">

    🏥

    </div>


    <div class="about-heading">

    Project Overview

    </div>


    <div class="about-text">


    LifeLens AI is an AI-powered personal wellness
    and emergency safety platform.


    <br><br>


    It helps users monitor lifestyle,
    predict wellness status,
    store medical information,
    and receive intelligent AI health guidance.


    </div>


    </div>

    """,
    unsafe_allow_html=True
    )




    # FEATURES


    st.subheader("✨ Key Features")



    c1,c2,c3 = st.columns(3)



    with c1:


        st.markdown(
        """
        <div class="about-card">


        <div class="about-icon">

        🧬

        </div>


        <div class="about-heading">

        Wellness Prediction

        </div>


        <div class="about-text">

        AI analyzes lifestyle data
        and predicts health status.

        </div>


        </div>
        """,
        unsafe_allow_html=True
        )




    with c2:


        st.markdown(
        """
        <div class="about-card">


        <div class="about-icon">

        🚨

        </div>


        <div class="about-heading">

        Emergency Vault

        </div>


        <div class="about-text">

        Securely store emergency
        medical information.

        </div>


        </div>
        """,
        unsafe_allow_html=True
        )





    with c3:


        st.markdown(
        """
        <div class="about-card">


        <div class="about-icon">

        🤖

        </div>


        <div class="about-heading">

        AI Assistant

        </div>


        <div class="about-text">

        Provides smart health
        recommendations.

        </div>


        </div>
        """,
        unsafe_allow_html=True
        )





    # TECHNOLOGY STACK


    st.subheader("⚙️ Technology Stack")



    st.markdown(
    """
    <div class="about-card">


    <div class="about-text">


    🐍 Python

    <br>

    🎨 Streamlit

    <br>

    📊 Data Analytics

    <br>

    🧠 Machine Learning

    <br>

    🤖 Artificial Intelligence

    <br>

    🔐 Secure Digital Storage


    </div>


    </div>

    """,
    unsafe_allow_html=True
    )



    st.success(
        "🎉 LifeLens AI Platform Completed Successfully 🚀"
    )
