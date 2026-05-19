import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Retail Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ======================================================
# LOAD DATA
# ======================================================

master_df = pd.read_csv("data/cleaned/master_dataset.csv")

segments_df = pd.read_csv("data/cleaned/customer_segments.csv")
# ======================================================
# TITLE
# ======================================================

st.title("📊 Retail & Marketing Analytics Dashboard")

st.markdown(
    "Interactive business intelligence dashboard for customer segmentation and revenue analytics."
)

# ======================================================
# SIDEBAR FILTERS
# ======================================================

st.sidebar.header("Filters")

selected_state = st.sidebar.multiselect(
    "Select State",
    options=master_df["customer_state"].dropna().unique(),
    default=master_df["customer_state"].dropna().unique()
)

selected_payment = st.sidebar.multiselect(
    "Payment Type",
    options=master_df["payment_type"].dropna().unique(),
    default=master_df["payment_type"].dropna().unique()
)

# ======================================================
# FILTER DATA
# ======================================================

filtered_df = master_df[
    (master_df["customer_state"].isin(selected_state)) &
    (master_df["payment_type"].isin(selected_payment))
]

# ======================================================
# KPI SECTION
# ======================================================

total_revenue = filtered_df["payment_value"].sum()

total_orders = filtered_df["order_id"].nunique()

total_customers = filtered_df["customer_unique_id"].nunique()

average_order_value = total_revenue / total_orders

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"${total_revenue:,.0f}"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col4.metric(
    "Avg Order Value",
    f"${average_order_value:,.2f}"
)

# ======================================================
# MONTHLY REVENUE TREND
# ======================================================

st.subheader("📈 Monthly Revenue Trend")

monthly_sales = filtered_df.groupby(
    "order_month"
)["payment_value"].sum().reset_index()

fig1 = px.line(
    monthly_sales,
    x="order_month",
    y="payment_value",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# ======================================================
# TOP CITIES
# ======================================================

col5, col6 = st.columns(2)

with col5:

    st.subheader("🏙️ Top Cities by Revenue")

    city_sales = filtered_df.groupby(
        "customer_city"
    )["payment_value"].sum().reset_index()

    city_sales = city_sales.sort_values(
        by="payment_value",
        ascending=False
    ).head(10)

    fig2 = px.bar(
        city_sales,
        x="payment_value",
        y="customer_city",
        orientation="h"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ======================================================
# PAYMENT DISTRIBUTION
# ======================================================

with col6:

    st.subheader("💳 Payment Distribution")

    payment_dist = filtered_df.groupby(
        "payment_type"
    )["payment_value"].sum().reset_index()

    fig3 = px.pie(
        payment_dist,
        names="payment_type",
        values="payment_value",
        hole=0.5
    )

    st.plotly_chart(fig3, use_container_width=True)

# ======================================================
# CUSTOMER SEGMENTATION
# ======================================================

st.subheader("🧠 Customer Segmentation")

segment_counts = segments_df["Segment"].value_counts().reset_index()

segment_counts.columns = ["Segment", "Count"]

fig4 = px.bar(
    segment_counts,
    x="Segment",
    y="Count",
    color="Segment"
)

st.plotly_chart(fig4, use_container_width=True)

# ======================================================
# SCATTER PLOT
# ======================================================

st.subheader("🎯 Customer Scatter Analysis")

fig5 = px.scatter(
    segments_df,
    x="Frequency",
    y="Monetary",
    color="Segment",
    size="Recency",
    hover_data=["customer_unique_id"]
)

st.plotly_chart(fig5, use_container_width=True)

# ======================================================
# REGIONAL ANALYSIS
# ======================================================

st.subheader("🌍 State-wise Revenue")

state_sales = filtered_df.groupby(
    "customer_state"
)["payment_value"].sum().reset_index()

state_sales = state_sales.sort_values(
    by="payment_value",
    ascending=False
)

fig6 = px.bar(
    state_sales,
    x="customer_state",
    y="payment_value",
    color="payment_value"
)

st.plotly_chart(fig6, use_container_width=True)

# ======================================================
# INSIGHTS SECTION
# ======================================================

st.subheader("📌 Business Insights")

st.markdown("""
- VIP customers contribute significantly to overall revenue.
- Credit card payments dominate transaction volume.
- Revenue concentration is strongest in urban regions.
- At-risk customers require retention strategies.
- Regional demand trends indicate expansion opportunities.
""")