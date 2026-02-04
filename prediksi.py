import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize


def lakukan_prediksi():
    # =========================
    # DATA ACTOR BOHONGAN
    # =========================
    data_actor = pd.DataFrame({
        "actor": [
            "tom hanks",
            "leonardo dicaprio",
            "scarlett johansson",
            "brad pitt",
            "angelina jolie"
        ],
        "rank": [1, 2, 3, 4, 5]
    })

    with st.form("Prediction Form"):
        st.subheader("Worldwide Gross Prediction")
        st.write("Please specify the variables:")

        actor_name = st.text_input("Actor Name")
        imdb_score = st.number_input(
            "IMDB Score", min_value=0.0, max_value=10.0, step=0.1
        )
        budget = st.number_input(
            "Movie Budget (USD)", min_value=0
        )

        submitted = st.form_submit_button("Predict")

        if submitted:
            actor_name = actor_name.lower()
            actor_rank = data_actor[data_actor["actor"] == actor_name]

            if actor_rank.empty:
                st.error("Actor not found (data masih bohongan 😅)")
            else:
                rank = actor_rank["rank"].values[0]

                # =========================
                # DUMMY MODEL (RUMUS PALSU)
                # =========================
                prediction = (
                    budget * 1.8 +
                    imdb_score * 50_000_000 -
                    rank * 20_000_000
                )

                st.success(
                    f"Estimated Worldwide Gross: ${numerize.numerize(prediction)}"
                )