# ==========================================
# LIFELENS AI
# PART 1 - SETUP + NAVIGATION + LANDING
# ==========================================


import streamlit as st
import pandas as pd
import numpy as np
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


/* MAIN BACKGROUND */

.stApp{

background:

radial-gradient(
circle at top,
#0f766e,
#020617 70%
);

}



/* ALL TEXT */

html,body,[class*="css"]{

font-family:"Poppins",sans-serif;

color:white;

}



h1,h2,h3,h4{

color:#5eead4 !important;

font-weight:900;

}



p,label,span{

color:white !important;

}




/* INPUT TEXT FIX */


.stTextInput input{


background:#020617 !important;

color:white !important;

-webkit-text-fill-color:white !important;

font-size:18px !important;

border:

2px solid #14b8a6 !important;


border-radius:15px !important;


}




/* NUMBER INPUT */


.stNumberInput input{


background:#020617 !important;

color:white !important;

-webkit-text-fill-color:white !important;

}




/* SELECT BOX */


div[data-baseweb="select"] > div{


background:#020617 !important;

color:white !important;

border:

2px solid #8b5cf6 !important;


border-radius:15px !important;


}



/* BUTTON */


.stButton button{


width:100%;


background:

linear-gradient(
45deg,
#14b8a6,
#2563eb
);


color:white;


font-size:18px;


font-weight:bold;


border-radius:25px;


height:55px;


box-shadow:

0px 10px 30px #14b8a6;


}




/* GLASS CARD */


.life-card{


background:

linear-gradient(

145deg,

rgba(255,255,255,0.15),

rgba(255,255,255,0.05)

);


backdrop-filter:blur(20px);


padding:35px;


border-radius:35px;


border:

1px solid #14b8a6;


box-shadow:

15px 15px 40px black;


}



/* TITLE */


.main-title{


text-align:center;


font-size:55px;


font-weight:900;


color:#5eead4;


text-shadow:

0px 10px 30px #14b8a6;


}



/* BIG ICON */


.big-icon{


font-size:120px;


text-align:center;


}



</style>


""",

unsafe_allow_html=True

)



# ================= SIDEBAR CSS =================


st.markdown("""

<style>


section[data-testid="stSidebar"]{


background:

linear-gradient(
180deg,
#111827,
#020617
);


}



section[data-testid="stSidebar"] *{


color:white !important;


}



section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{


color:#5eead4 !important;

font-weight:900 !important;

}


</style>


""",

unsafe_allow_html=True

)





# ================= SIDEBAR =================


st.sidebar.markdown(

"""

# 🧬 LifeLens AI

## Navigation

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





# ================= HOME PAGE =================



# ================= HOME PAGE =================

if page=="🌌 Home":


    st.markdown("""
    <style>

    .hero-title{

        text-align:center;
        font-size:65px;
        font-weight:900;
        color:#5eead4;
        text-shadow:0px 10px 40px #14b8a6;

    }


    .hero-sub{

        text-align:center;
        font-size:22px;
        color:white;
        line-height:1.8;

    }


    .feature-card{

        background:
        linear-gradient(
        145deg,
        rgba(255,255,255,0.18),
        rgba(255,255,255,0.05)
        );

        backdrop-filter:blur(20px);

        padding:30px;

        border-radius:30px;

        border:1px solid #14b8a6;

        box-shadow:15px 15px 40px black;

        text-align:center;

        height:230px;

    }


    .feature-icon{

        font-size:60px;

    }


    .feature-title{

        color:#5eead4;

        font-size:25px;

        font-weight:900;

    }


    .stats-card{

        background:#020617;

        padding:25px;

        border-radius:25px;

        border:1px solid #2563eb;

        text-align:center;

    }


    .stats-number{

        font-size:40px;

        font-weight:900;

        color:#5eead4;

    }


    </style>
    """,unsafe_allow_html=True)



    # HERO SECTION

    st.markdown(
    """
    <div class="hero-title">

    🧬 LifeLens AI

    </div>
    """,
    unsafe_allow_html=True
    )


    st.markdown(
    """
    <div class="hero-sub">

    AI Powered Personal Health Intelligence Platform

    <br>

    Monitor Lifestyle • Predict Wellness • Protect Your Future

    </div>
    """,
    unsafe_allow_html=True
    )


    st.markdown(
    """
    <div style="text-align:center;font-size:130px">

    🤖💙

    </div>
    """,
    unsafe_allow_html=True
    )


    st.write("")



    if st.button("🚀 Start Your Health Journey"):

        st.success(
        "Welcome to LifeLens AI - Your Digital Health Companion 🤖"
        )

        st.balloons()



    st.write("")



    # FEATURES


    st.subheader("✨ Smart Health Features")


    c1,c2,c3,c4 = st.columns(4)


    with c1:

        st.markdown(
        """
        <div class="feature-card">

        <div class="feature-icon">
        😴
        </div>

        <div class="feature-title">
        Sleep AI
        </div>

        <p>
        Analyze sleep quality
        and improve rest.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )



    with c2:

        st.markdown(
        """
        <div class="feature-card">

        <div class="feature-icon">
        🧠
        </div>

        <div class="feature-title">
        Wellness AI
        </div>

        <p>
        Predict your health
        condition.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )



    with c3:

        st.markdown(
        """
        <div class="feature-card">

        <div class="feature-icon">
        🚨
        </div>

        <div class="feature-title">
        Emergency Vault
        </div>

        <p>
        Store medical details
        securely.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )



    with c4:

        st.markdown(
        """
        <div class="feature-card">

        <div class="feature-icon">
        🤖
        </div>

        <div class="feature-title">
        AI Assistant
        </div>

        <p>
        Get smart health
        guidance.
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )



    st.write("")



    # PROJECT IMPACT


    st.subheader("🌎 LifeLens AI Impact")


    a,b,c = st.columns(3)


    with a:

        st.markdown(
        """
        <div class="stats-card">

        <div class="stats-number">
        24/7
        </div>

        AI Health Support

        </div>
        """,
        unsafe_allow_html=True
        )


    with b:

        st.markdown(
        """
        <div class="stats-card">

        <div class="stats-number">
        100%
        </div>

        Digital Safety

        </div>
        """,
        unsafe_allow_html=True
        )



    with c:

        st.markdown(
        """
        <div class="stats-card">

        <div class="stats-number">
        AI
        </div>

        Smart Prediction

        </div>
        """,
        unsafe_allow_html=True
        )



    st.write("")


    st.info(
    "🧬 LifeLens AI combines Artificial Intelligence, Data Analytics and Health Monitoring to create a smarter lifestyle companion."
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


        border:

        1px solid #14b8a6;


        box-shadow:

        20px 20px 50px black;


    }



    .login-robot{


        font-size:130px;

        text-align:center;


        animation:

        floatAI 3s infinite;


    }



    @keyframes floatAI{


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




    .login-title{


        text-align:center;


        font-size:50px;


        font-weight:900;


        color:#5eead4;


        text-shadow:

        0px 10px 30px #14b8a6;


    }




    .login-sub{


        text-align:center;


        color:white;


        font-size:20px;


    }


    </style>

    """,

    unsafe_allow_html=True

    )




    # LOGIN HEADER


    st.markdown(

    """

    <div class="login-box">


    <div class="login-robot">

    🧬🤖

    </div>



    <div class="login-title">

    Welcome Back

    </div>



    <div class="login-sub">

    Enter Into Your LifeLens AI World

    </div>



    </div>


    """,

    unsafe_allow_html=True

    )



    st.write("")




    # USER DETAILS


    name = st.text_input(

        "👤 Full Name",

        placeholder="Enter your name"

    )




    email = st.text_input(

        "📧 Email Address",

        placeholder="example@gmail.com"

    )




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


        # Move to Wellness Prediction Page

        st.session_state.page = "🧬 Wellness Prediction"

        time.sleep(1)

        st.rerun()



      else:


        st.warning(
            "⚠️ Please fill all details"
        )

# ==========================================
# PART 3 - LIFELENS AI DASHBOARD
# ==========================================

elif page=="🏠 Dashboard":


 st.markdown("""
    <style>


    .dash-title{


        text-align:center;


        font-size:50px;


        font-weight:900;


        color:#5eead4;


        text-shadow:

        0px 10px 30px #14b8a6;


    }



    .health-ai{


        text-align:center;


        font-size:120px;


        animation:healthFloat 3s infinite;


    }



    @keyframes healthFloat{


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


        border:

        1px solid #14b8a6;


        box-shadow:

        15px 15px 40px black;


        text-align:center;


    }





    .health-icon{


        font-size:70px;


    }




    .health-name{


        color:#5eead4;


        font-size:24px;


        font-weight:900;


    }




    .health-value{


        color:white;


        font-size:38px;


        font-weight:900;


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

    <div class="health-ai">

    🧬🤖

    </div>


    """,

    unsafe_allow_html=True

    )




    st.write("")





    # HEALTH CARDS


    col1,col2,col3,col4 = st.columns(4)




    with col1:


        st.markdown(

        """

        <div class="health-card">


        <div class="health-icon">

        ❤️

        </div>


        <div class="health-name">

        Health Score

        </div>


        <div class="health-value">

        92%

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )





    with col2:


        st.markdown(

        """

        <div class="health-card">


        <div class="health-icon">

        😴

        </div>


        <div class="health-name">

        Sleep

        </div>


        <div class="health-value">

        7.5 Hrs

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )





    with col3:


        st.markdown(

        """

        <div class="health-card">


        <div class="health-icon">

        💧

        </div>


        <div class="health-name">

        Water

        </div>


        <div class="health-value">

        2.5 L

        </div>


        </div>


        """,

        unsafe_allow_html=True

        )





    with col4:


        st.markdown(

        """

        <div class="health-card">


        <div class="health-icon">

        🏃

        </div>


        <div class="health-name">

        Activity

        </div>


        <div class="health-value">

        HIGH

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


    <h3>

    🧠 LifeLens Recommendation

    </h3>


    <p>

    Your lifestyle balance is good.

    Maintain proper sleep,

    increase daily exercise,

    and continue healthy habits.

    </p>


    </div>


    """,

    unsafe_allow_html=True

    )





    st.write("")





    # ACTIVITY CHART


    st.subheader("📊 Daily Wellness Activity")



    wellness = pd.DataFrame({

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

    })




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




    if st.button("🧬 Run Health Scan"):


        with st.spinner("AI Scanning Your Lifestyle..."):

            time.sleep(2)


        st.success(

        "LifeLens AI Health Scan Completed Successfully 🤖"

        )


        st.balloons()

# ==========================================
# PART 4 - LIFELENS AI WELLNESS PREDICTION
# ==========================================

    elif page=="🧬 Wellness Prediction":


     st.markdown("""
    <style>


    .predict-title{


        text-align:center;

        font-size:50px;

        font-weight:900;

        color:#f0abfc;


        text-shadow:

        0px 10px 30px #c026d3;


    }




    .predict-ai{


        text-align:center;

        font-size:120px;


        animation:predictFloat 3s infinite;


    }




    @keyframes predictFloat{


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


        border:

        1px solid #c026d3;


        box-shadow:

        15px 15px 40px black;


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


        box-shadow:

        10px 10px 30px black;


    }



    .result-icon{


        font-size:70px;

    }



    .result-title{


        color:#f0abfc;

        font-size:22px;

        font-weight:900;


    }



    .result-value{


        color:white;

        font-size:32px;

        font-weight:900;


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

    Enter Your Lifestyle Details For AI Analysis 🚀

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

            "LifeLens AI Analyzing Your Health..."

        ):


            time.sleep(2)





        # AI LOGIC


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



        elif health_score > 50:


            health_status="Good 👍"



        else:


            health_status="Needs Improvement ⚠️"





        if stress >= 7:


            stress_risk="High 🔥"


        else:


            stress_risk="Low 🌱"





        if sleep >= 7 and exercise >=30:


            energy="High ⚡"


        else:


            energy="Medium 🔋"






        st.success(

            "AI Wellness Prediction Completed Successfully 🤖"

        )



        st.write("")





        # RESULT CARDS


        c1,c2,c3 = st.columns(3)





        with c1:


            st.markdown(

            f"""

            <div class="result-card">


            <div class="result-icon">

            ❤️

            </div>


            <div class="result-title">

            Health Status

            </div>


            <div class="result-value">

            {health_status}

            </div>


            </div>

            """,

            unsafe_allow_html=True

            )






        with c2:


            st.markdown(

            f"""

            <div class="result-card">


            <div class="result-icon">

            🔥

            </div>


            <div class="result-title">

            Stress Risk

            </div>


            <div class="result-value">

            {stress_risk}

            </div>


            </div>

            """,

            unsafe_allow_html=True

            )







        with c3:


            st.markdown(

            f"""

            <div class="result-card">


            <div class="result-icon">

            ⚡

            </div>


            <div class="result-title">

            Energy Level

            </div>


            <div class="result-value">

            {energy}

            </div>


            </div>

            """,

            unsafe_allow_html=True

            )



        st.balloons()
# ==========================================
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


        text-shadow:

        0px 10px 30px #10b981;


    }




    .analytics-ai{


        text-align:center;

        font-size:120px;


        animation:analyticsFloat 3s infinite;


    }




    @keyframes analyticsFloat{


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





    .analytics-card{


        background:

        linear-gradient(

        145deg,

        rgba(255,255,255,0.15),

        rgba(255,255,255,0.05)

        );


        backdrop-filter:blur(20px);


        padding:30px;


        border-radius:35px;


        border:

        1px solid #10b981;


        box-shadow:

        15px 15px 40px black;


        text-align:center;


    }




    .analytics-icon{


        font-size:65px;


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

    unsafe_allow_html=True

    )





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

    <div class="analytics-ai">

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

        "Category":

        [

        "Sleep",

        "Water",

        "Exercise",

        "Mood",

        "Meditation"

        ],


        "Score":

        [

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

        "Risk":

        [

        "Low",

        "Medium",

        "High"

        ],


        "Users":

        [

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

        "Feature":

        [

        "Sleep",

        "Exercise",

        "Water",

        "Stress",

        "Mood"

        ],


        "Importance":

        [

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

    )


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



    .assistant-robot{


        text-align:center;

        font-size:130px;


        animation:robotFloat 3s infinite;


    }




    @keyframes robotFloat{


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





    .chat-card{


        background:

        linear-gradient(

        145deg,

        rgba(255,255,255,0.15),

        rgba(255,255,255,0.05)

        );


        backdrop-filter:blur(20px);


        padding:30px;


        border-radius:35px;


        border:

        1px solid #14b8a6;


        box-shadow:

        15px 15px 40px black;


    }




    .ai-message{


        background:

        linear-gradient(

        45deg,

        #0f766e,

        #115e59

        );


        padding:20px;


        border-radius:25px;


        color:white;


        font-size:18px;


        margin:15px;


    }




    .user-message{


        background:

        linear-gradient(

        45deg,

        #2563eb,

        #7c3aed

        );


        padding:20px;


        border-radius:25px;


        color:white;


        font-size:18px;


        margin:15px;


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

    <div class="assistant-robot">

    🤖💙

    </div>

    """,

    unsafe_allow_html=True

    )






    # INTRO CARD


    st.markdown(

    """

    <div class="chat-card">


    <div class="ai-message">


    🤖 Hello! I am LifeLens AI Assistant.


    <br><br>


    I can help you with:


    <br><br>


    😴 Sleep Improvement

    <br>

    💧 Healthy Lifestyle

    <br>

    🏃 Fitness Guidance

    <br>

    🧠 Stress Management

    <br>

    🆘 Emergency Support


    </div>


    </div>


    """,

    unsafe_allow_html=True

    )





    st.write("")






    # USER QUESTION


    question = st.text_input(

        "💬 Ask LifeLens AI",

        placeholder="Example: How can I reduce stress?"

    )






    if st.button("🚀 Ask LifeLens AI"):



        with st.spinner(

            "AI Thinking..."

        ):

            time.sleep(2)





        q = question.lower()






        if "sleep" in q:



            answer = """

😴 Sleep Improvement Plan:


✅ Sleep 7-8 hours daily

✅ Avoid mobile before sleep

✅ Maintain fixed sleeping time

✅ Keep your room comfortable


"""





        elif "water" in q or "hydration" in q:



            answer = """

💧 Hydration Tips:


✅ Drink 2-3 litres water daily

✅ Start your day with water

✅ Avoid too many sugary drinks


"""






        elif "stress" in q or "mental" in q:



            answer = """

🧠 Stress Management:


✅ Practice meditation

✅ Take small breaks

✅ Exercise regularly

✅ Talk with trusted people


"""






        elif "exercise" in q or "fitness" in q:



            answer = """

🏃 Fitness Advice:


✅ Walk daily

✅ Exercise 30 minutes

✅ Maintain active lifestyle

✅ Eat balanced food


"""







        elif "emergency" in q or "help" in q:



            answer = """

🆘 Emergency Guidance:


✅ Stay calm

✅ Contact emergency person

✅ Share medical information

✅ Seek professional help


"""







        else:



            answer = """

🌱 LifeLens Recommendation:


✅ Maintain healthy habits

✅ Track your lifestyle

✅ Improve sleep quality

✅ Stay physically active


"""






        st.markdown(

        f"""

        <div class="chat-card">


        <div class="user-message">


        👤 You:


        <br><br>


        {question}


        </div>





        <div class="ai-message">


        🤖 LifeLens AI:


        <br><br>


        {answer}


        </div>


        </div>


        """,

        unsafe_allow_html=True

        )






    st.write("")





    st.subheader(

        "⚡ Quick Health Actions"

    )





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

        )
# ==========================================
# PART - EMERGENCY VAULT
# ==========================================

elif page=="🆘 Emergency Vault":


    st.markdown("""
    <style>

    .vault-title{

        text-align:center;
        font-size:45px;
        font-weight:900;
        color:#ef4444;

    }


    .vault-card{

        background:
        linear-gradient(
        145deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.05)
        );

        padding:30px;

        border-radius:30px;

        border:2px solid #ef4444;

        box-shadow:15px 15px 40px black;

    }

    </style>
    """,
    unsafe_allow_html=True)



    # Initialize storage

    if "vault_data" not in st.session_state:

        st.session_state.vault_data = {}



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



    name = st.text_input(
        "👤 Full Name"
    )


    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=120,
        value=20
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


            "Name": name,

            "Age": age,

            "Blood Group": blood,

            "Emergency Contact": phone,

            "Allergy": allergy,

            "Medical History": medical,

            "Medicines": medicine


        }


        st.success(
            "✅ Emergency Vault Saved Successfully"
        )


        st.balloons()



    st.divider()



    st.subheader(
        "📋 Emergency Vault Details"
    )



    if len(st.session_state.vault_data)>0:


        for key,value in st.session_state.vault_data.items():

            st.info(
                f"{key} : {value}"
            )


    else:


        st.warning(
            "⚠️ Emergency Vault Empty"
        )

# ==========================================
# PART 7 - LIFELENS AI ABOUT PAGE
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

        animation:floatLife 3s infinite;

    }



    @keyframes floatLife{


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





    .life-card{


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


        margin-bottom:25px;


    }




    .life-icon{

        font-size:70px;

        text-align:center;

    }



    .life-head{


        text-align:center;

        color:#38bdf8;

        font-size:28px;

        font-weight:900;


    }



    .life-text{


        text-align:center;

        color:white;

        font-size:18px;

        line-height:1.8;


    }


    </style>

    """,
    unsafe_allow_html=True)



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
    <div class="life-card">


    <div class="life-icon">

    🏥

    </div>


    <div class="life-head">

    Project Overview

    </div>


    <div class="life-text">


    LifeLens AI is an AI-powered digital safety
    platform designed to protect people during
    emergency situations.


    <br><br>


    It securely stores medical information,
    emergency contacts, documents and provides
    intelligent health assistance.


    </div>


    </div>

    """,

    unsafe_allow_html=True

    )




    # FEATURES


    col1,col2,col3 = st.columns(3)



    with col1:


        st.markdown(
        """
        <div class="life-card">


        <div class="life-icon">

        🚨

        </div>


        <div class="life-head">

        Emergency SOS

        </div>


        <div class="life-text">

        One click emergency alert
        system with instant contact
        notification.

        </div>


        </div>

        """,

        unsafe_allow_html=True

        )




    with col2:


        st.markdown(
        """
        <div class="life-card">


        <div class="life-icon">

        🧬

        </div>


        <div class="life-head">

        Medical Vault

        </div>


        <div class="life-text">

        Store medical history,
        prescriptions and health
        documents securely.

        </div>


        </div>

        """,

        unsafe_allow_html=True

        )





    with col3:


        st.markdown(
        """
        <div class="life-card">


        <div class="life-icon">

        🤖

        </div>


        <div class="life-head">

        AI Assistant

        </div>


        <div class="life-text">

        AI based emergency guidance
        and smart health suggestions.

        </div>


        </div>

        """,

        unsafe_allow_html=True

        )




    # TECHNOLOGY


    st.markdown(
    """
    <div class="life-card">


    <div class="life-icon">

    ⚙️

    </div>


    <div class="life-head">

    Technology Stack

    </div>


    <div class="life-text">


    🐍 Python

    <br>

    🎨 Streamlit

    <br>

    🧠 Machine Learning

    <br>

    📊 Data Analytics

    <br>

    🔐 Secure Digital Storage

    <br>

    🤖 AI Assistant


    </div>


    </div>

    """,

    unsafe_allow_html=True

    )



    st.success(
        "🎉 LifeLens AI Platform Completed Successfully 🚀"
    )