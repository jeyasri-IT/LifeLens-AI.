import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px


# ===============================
# PAGE CONFIG
# ===============================

st.set_page_config(
    page_title="LifeLens AI",
    page_icon="🧠",
    layout="wide"
)


# ===============================
# CUSTOM CSS
# ===============================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #050816,
        #1e293b
    );
}

h1,h2,h3{
    color:white;
}

.card{
    background:rgba(255,255,255,0.1);
    padding:20px;
    border-radius:20px;
}

</style>

""",unsafe_allow_html=True)



# ===============================
# LOAD DATA AND MODEL
# ===============================

df = pd.read_csv("life_data.csv")

model = joblib.load(
    "lifelens_model.pkl"
)



# ===============================
# SIDEBAR
# ===============================

st.sidebar.title("🧠 LifeLens AI")


page = st.sidebar.radio(
    "Menu",
    [
        "🏠 Dashboard",
        "📊 Analytics",
        "🤖 Prediction",
        "📈 Feature Importance",
        "ℹ️ About"
    ]
)



# ===============================
# DASHBOARD
# ===============================

if page == "🏠 Dashboard":


    st.title("🧠 LifeLens AI Dashboard")

    st.write(
        "AI powered productivity prediction system"
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(
            "Total Records",
            df.shape[0]
        )


    with col2:

        st.metric(
            "Features",
            df.shape[1]
        )


    with col3:

        st.metric(
            "Model",
            "Random Forest"
        )


    st.divider()


    st.subheader(
        "Dataset Preview"
    )


    st.dataframe(
        df.head(10),
        use_container_width=True
    )




# ===============================
# ANALYTICS
# ===============================

elif page == "📊 Analytics":


    st.title(
        "📊 Data Analytics"
    )


    fig1 = px.histogram(
        df,
        x="Productivity_Score",
        title="Productivity Score Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )



    fig2 = px.histogram(
        df,
        x="Stress_Level",
        title="Stress Level Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )



    fig3 = px.scatter(
        df,
        x="Sleep_Hours",
        y="Productivity_Score",
        title="Sleep Hours vs Productivity"
    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )



    fig4 = px.scatter(
        df,
        x="Screen_Time",
        y="Productivity_Score",
        title="Screen Time vs Productivity"
    )


    st.plotly_chart(
        fig4,
        use_container_width=True
    )





# ===============================
# PREDICTION
# ===============================

elif page == "🤖 Prediction":


    st.title(
        "🤖 Productivity Predictor"
    )


    st.write(
        "Enter your lifestyle details"
    )


    age = st.number_input(
        "Age",
        18,
        60,
        21
    )


    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


    sleep = st.slider(
        "Sleep Hours",
        4.0,
        9.0,
        7.0
    )


    screen = st.slider(
        "Screen Time",
        1.0,
        12.0,
        5.0
    )


    exercise = st.slider(
        "Exercise Minutes",
        0,
        120,
        30
    )


    water = st.slider(
        "Water Intake",
        1.0,
        5.0,
        2.5
    )


    study = st.slider(
        "Work / Study Hours",
        2.0,
        12.0,
        6.0
    )


    stress = st.slider(
        "Stress Level",
        1,
        10,
        5
    )


    mood = st.selectbox(
        "Mood",
        [
            "Happy",
            "Neutral",
            "Sad",
            "Stressed"
        ]
    )



    if st.button(
        "🚀 Predict"
    ):


        gender_value = (
            1 if gender=="Male"
            else 0
        )


        mood_value = {
            "Happy":0,
            "Neutral":1,
            "Sad":2,
            "Stressed":3
        }



        input_data = pd.DataFrame({

            "Age":[age],

            "Gender":[gender_value],

            "Sleep_Hours":[sleep],

            "Screen_Time":[screen],

            "Exercise_Minutes":[exercise],

            "Water_Intake":[water],

            "Work_Study_Hours":[study],

            "Stress_Level":[stress],

            "Mood":[mood_value[mood]]

        })



        prediction = model.predict(
            input_data
        )


        score = round(
            prediction[0],
            2
        )



        st.success(
            f"🎯 Productivity Score : {score}%"
        )



        if score >=75:


            st.success(
                "🟢 Excellent Productivity\n\n"
                "Maintain your healthy routine."
            )


        elif score >=50:


            st.warning(
                "🟡 Moderate Productivity\n\n"
                "Improve sleep and reduce stress."
            )


        else:


            st.error(
                "🔴 Low Productivity\n\n"
                "Focus on exercise, sleep and mental health."
            )





# ===============================
# FEATURE IMPORTANCE
# ===============================

elif page == "📈 Feature Importance":


    st.title(
        "📈 Feature Importance"
    )


    importance = pd.DataFrame({

        "Feature":
        model.feature_names_in_,


        "Importance":
        model.feature_importances_

    })


    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )



    fig = px.bar(

        importance,

        x="Importance",

        y="Feature",

        title="Important Factors Affecting Productivity"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )




# ===============================
# ABOUT
# ===============================

else:


    st.title(
        "ℹ️ About LifeLens AI"
    )


    st.write("""

## LifeLens AI

An AI-based lifestyle analytics system
that predicts productivity using Machine Learning.

### Machine Learning:
- Random Forest Regressor

### Technologies:
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Plotly


### ML Workflow:

Dataset → Cleaning → EDA → 
Feature Engineering → Model Training →
Prediction

""")