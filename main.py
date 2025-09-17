import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="COE Cat A Explorer", layout="wide")

st.title("📊 COE Category A Price Explorer")
st.write(
    "Upload the cleaned CSV (`coe_catA_clean_full.csv`) to explore history interactively."
)

# File upload
uploaded = st.file_uploader("Upload your CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded, parse_dates=["date"])
    df = df.sort_values("date")

    st.success(
        f"Loaded {len(df)} rows from {df['date'].min().date()} → {df['date'].max().date()}"
    )

    # Filters
    st.sidebar.header("Filters")
    start_date = st.sidebar.date_input("Start date", df["date"].min().date())
    end_date = st.sidebar.date_input("End date", df["date"].max().date())

    mask = (df["date"] >= pd.to_datetime(start_date)) & (
        df["date"] <= pd.to_datetime(end_date)
    )
    df_filtered = df.loc[mask]

    # Plot
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df_filtered["date"], df_filtered["Cat_A"], label="Cat A Price", lw=1.5)

    # Highlight dips
    n_dips = st.sidebar.slider(
        "Highlight lowest N dips", min_value=1, max_value=20, value=5
    )
    dips = df_filtered.nsmallest(n_dips, "Cat_A")
    ax.scatter(
        dips["date"], dips["Cat_A"], color="red", zorder=5, label=f"Lowest {n_dips}"
    )

    ax.set_title("COE Cat A Price Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (SGD)")
    ax.legend()
    st.pyplot(fig)

    # Show raw data
    st.subheader("📋 Data Preview")
    st.dataframe(df_filtered, use_container_width=True)

    # Option: download filtered data
    csv = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download filtered CSV", csv, "coe_filtered.csv", "text/csv")
else:
    st.info("⬆️ Upload the cleaned CSV to get started.")
