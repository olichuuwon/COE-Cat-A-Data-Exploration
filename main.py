import streamlit as st
import pandas as pd
import altair as alt

# --- Page Config ---
st.set_page_config(page_title="COE Cat A Explorer", layout="wide")

# --- Title ---
st.title("📊 COE Category A Price Explorer")
st.write(
    "Upload the cleaned CSV (`coe_catA_clean_full.csv`) to explore Cat A COE history interactively."
)

# --- File Upload ---
uploaded = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded:
    # --- Load Data ---
    df = pd.read_csv(uploaded, parse_dates=["date"])
    df = df.sort_values("date")

    st.success(
        f"✅ Loaded {len(df)} rows from **{df['date'].min().date()} → {df['date'].max().date()}**"
    )

    # --- Sidebar Filters ---
    st.sidebar.header("⚙️ Filters")
    start_date = st.sidebar.date_input("Start date", df["date"].min().date())
    end_date = st.sidebar.date_input("End date", df["date"].max().date())

    mask = (df["date"] >= pd.to_datetime(start_date)) & (
        df["date"] <= pd.to_datetime(end_date)
    )
    df_filtered = df.loc[mask]

    # --- Line chart ---
    line = alt.Chart(df_filtered).mark_line().encode(x="date:T", y="Cat_A:Q")

    # --- Add dots on each data point with tooltip ---
    dots = (
        alt.Chart(df_filtered)
        .mark_circle(size=40, color="steelblue")
        .encode(x="date:T", y="Cat_A:Q", tooltip=["date:T", "Cat_A:Q"])
    )

    chart = (line + dots).properties(
        width=950, height=450, title="COE Cat A Price Over Time"
    )

    st.altair_chart(chart, use_container_width=True)

    # --- Data Preview ---
    st.subheader("📋 Data Preview")
    st.dataframe(df_filtered, use_container_width=True)

else:
    st.info("⬆️ Please upload a cleaned CSV file to begin.")
