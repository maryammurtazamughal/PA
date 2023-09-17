import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .main {
        background-color: #ADD8E6 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Sensor Data Task")

# File Upload widget
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

def preprocess_data(data):
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    data["Timecategory"] = pd.cut(
        pd.to_datetime(data.Timestamp).dt.hour,
        bins=[0, 12, 17, 20, 22],
        labels=["Morning", "Afternoon", "Evening", "Night"]
    )
    return data

def calculate_summary_statistics(data):
    md = data.median(numeric_only=True)
    cal = data.describe()
    return md, cal

def create_scatter_chart(data):
    Data1 = go.Scatter(
        x=data.Timecategory,
        y=data.Humidity,
        text="humidity",
        mode="lines+markers",
        line=dict(color="green"),
    )
    Data2 = go.Scatter(
        x=data.Timecategory,
        y=data.Temperature,
        text="Temperature",
        mode="lines+markers",
        line=dict(color="purple"),
    )
    layout = go.Layout(
        title="Scatter Humidity and Temperature Over Time of Day in Lines",
        xaxis=dict(title="Timecategory"),
        yaxis=dict(title="Temperature and Humidity")
    )
    return go.Figure(data=[Data1, Data2], layout=layout)

def create_heatmap(data):
    visualize = px.density_heatmap(
        data,
        title="Relationship Between Humidity, Temperature, and Timezone",
        x="Temperature",
        y="Humidity",
    )
    return visualize

def create_bar_chart(data):
    bar_chart = px.bar(
        data,
        x="Timecategory",
        y=["Humidity", "Temperature"],
        barmode="stack",
        orientation="v"
    )
    bar_chart.update_traces(width=5)
    bar_chart.update_layout(title='Bar Chart', height=300, width=600)
    return bar_chart

if uploaded_file is not None:
    csv_data = pd.read_csv(uploaded_file)
    processed_data = preprocess_data(csv_data)
    median_values, summary_stats = calculate_summary_statistics(processed_data)

    original_frame, updated_frame, time_category_frame = st.columns(3)
    original_frame.write("Original Values")
    original_frame.dataframe(csv_data, width=200, height=150)
    updated_frame.write("Updated Values")
    updated_frame.dataframe(processed_data, width=200, height=150)
    st.subheader("Calculation")
    st.json({"Median": median_values, "Summary Statistics": summary_stats})

    time_category_frame.write("Time Category Added")
    time_category_frame.dataframe(processed_data, width=200, height=150)

    visualization_choice = st.sidebar.radio(label="Select Visualization", options=["Scatter", "Time category", "Heatmap"])
    if visualization_choice == "Scatter":
        scatter_chart = create_scatter_chart(csv_data)
        st.subheader("Scatter Chart")
        st.plotly_chart(scatter_chart)
    elif visualization_choice == "Time category":
        time_category_chart = create_scatter_chart(processed_data)
        st.subheader("Data Visualize Over Time Category")
        st.plotly_chart(time_category_chart)
    elif visualization_choice == "Heatmap":
        heatmap = create_heatmap(csv_data)
        st.subheader("Heatmap")
        st.plotly_chart(heatmap)
    else:
        st.write("Please select a visualization option")

    bar_chart = create_bar_chart(processed_data)
    st.subheader("Bar Chart")
    st.plotly_chart(bar_chart)








