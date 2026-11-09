import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import tracemalloc
from algorithms.sorting import mergesort
from analysis.time_analyzer import benchmark_merge_sort
from analysis.complexity_predictor import predict_complexity
#page configuration
st.title("ALGOVISTA AI")
st.subheader("Algorithm Complexity and Data Science Studio")
st.write("Analyze algorithms, measure performance, and explore data scientifically...")
st.divider()
st.sidebar.title("Navigation")
menu=st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "Algorithm Lab",
        "Complexity Analyzer",
        "Data Science Lab",
        "Performance Analyzer"
    ]
)
#DashBoard
if menu=="Dashboard":
    st.header("Welcome to AlgoVista AI")
    col1,col2,col3=st.columns(3)
    col1.metric("Algorithms","06")
    col2.metric("Analysis Modules","04")
    col3.metric("Programming Language","Python")
    st.divider()
    st.subheader("Project Capabilities")
    st.write("1.Sorting and Searching Algorithms")
    st.write("2.Time Complexity Measurement")
    st.write("3.Space Complexity")
    st.write("4.Dataset Analysis and Visualization")
    st.write("5.Algorithm Performance BenchMarking")
elif menu == "Algorithm Lab":
    st.header("🧪 Algorithm Laboratory")
    st.write("Experiment with sorting algorithms using your own input.")
    algorithm = st.selectbox(
        "Select Algorithm",
        ["Merge Sort"]
    )
    user_input = st.text_input(
        "Enter numbers separated by commas",
        placeholder="45, 12, 89, 3, 25, 7, 61"
    )
    if st.button("Run Algorithm", type="primary"):
        try:
            arr = [int(x.strip()) for x in user_input.split(",")]
            if not arr:
                st.warning("Please enter some numbers.")
            else:
                result = mergesort(arr)
                st.success("Algorithm executed successfully!")
                st.subheader("Results")
                st.write("Original Array:", arr)
                st.write("Sorted Array:", result["sorted_array"])
                col1, col2, col3 = st.columns(3)
                col1.metric(
                    "Comparisons",
                    result["comparisons"]
                )
                col2.metric(
                    "Execution Time",
                    f'{result["execution_time"]:.8f} sec'
                )
                col3.metric(
                    "Peak Memory",
                    f'{result["peak_memory"]} bytes'
                )
        except ValueError:
            st.error("Invalid input! Enter integers separated by commas.")
elif menu == "Complexity Analyzer":
    st.header("Algorithm Complexity Analyzer")
    st.write("Analyze benchmark results and predict algorithm time complexity.")
    if "benchmark_results" in st.session_state:
        results = st.session_state["benchmark_results"]
        best_model, predictions = predict_complexity(results)
        st.subheader("Benchmark Results")
        st.dataframe(results, use_container_width=True)
        st.subheader("Predicted Time Complexity")
        st.success(f"Best Fitting Model: {best_model}")
        st.subheader("Model Comparison")
        score_df = pd.DataFrame.from_dict(predictions, orient="index")
        st.dataframe(score_df, use_container_width=True)
        st.bar_chart(score_df)
        st.info("This is an empirical estimate, not a mathematical proof.")
    else:
        st.warning("No benchmark data available. Go to Performance Analyzer and run the benchmark first.")
elif menu == "Data Science Lab":
    st.header("Data Science Laboratory")
    st.write("Upload and explore datasets using Python.")
    uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Dataset uploaded successfully!")
            st.subheader("Dataset Preview")
            st.dataframe(df.head(10), use_container_width=True)
            st.subheader("Dataset Information")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Rows", df.shape[0])
            col2.metric("Total Columns", df.shape[1])
            col3.metric("Missing Values", int(df.isnull().sum().sum()))
            st.subheader("Column Names")
            st.write(list(df.columns))
            st.subheader("Statistical Summary")
            st.dataframe(df.describe(include="all"), use_container_width=True)
            st.subheader("Missing Values Analysis")
            st.dataframe(df.isnull().sum().to_frame("Missing Values"))
            st.subheader("Missing Values Percentage")
            missing_df = pd.DataFrame({
            "Missing Count": df.isnull().sum(),
            "Missing Percentage": (df.isnull().mean() * 100).round(2)
            })
            st.dataframe(missing_df)
            st.subheader("Data Visualization - Histogram")
            numeric_columns = df.select_dtypes(include=np.number).columns.drop("Student_ID", errors="ignore").tolist()
            selected_column = st.selectbox("Select a column", numeric_columns)
            fig, ax = plt.subplots()
            ax.hist(df[selected_column].dropna(), bins=10, edgecolor="black")
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")
            ax.set_title(f"Distribution of {selected_column}")
            st.pyplot(fig)
            plt.close(fig)
            st.subheader("Department-wise Student Count")
            department_counts = df["Department"].value_counts()
            st.bar_chart(department_counts)
            st.subheader("Study Hours vs Final Exam Score")
            fig, ax = plt.subplots()
            ax.scatter(df["Study_Hours_Per_Week"], df["Final_Exam_Score"])
            ax.set_xlabel("Study Hours Per Week")
            ax.set_ylabel("Final Exam Score")
            ax.set_title("Study Hours vs Exam Performance")
            ax.grid(True)
            st.pyplot(fig)
            plt.close(fig)
            st.subheader("Correlation Heatmap")
            correlation_columns = ["Study_Hours_Per_Week", "Attendance_Percent", "Assignment_Score", "Previous_Exam_Score", "Final_Exam_Score"]
            correlation_matrix = df[correlation_columns].corr()
            fig, ax = plt.subplots(figsize=(10, 6))
            image = ax.imshow(correlation_matrix, cmap="coolwarm", vmin=0.90, vmax=1.0)
            ax.set_xticks(range(len(correlation_columns)))
            ax.set_yticks(range(len(correlation_columns)))
            ax.set_xticklabels(correlation_columns, rotation=45, ha="right")
            ax.set_yticklabels(correlation_columns)
            for i in range(len(correlation_columns)):
                for j in range(len(correlation_columns)):
                    ax.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", ha="center", va="center")
            fig.colorbar(image, ax=ax, label="Correlation")
            ax.set_title("Feature Correlation Analysis")
            fig.tight_layout()
            st.pyplot(fig)
            plt.close(fig)
        except Exception as e:
            st.error(f"Unable to read dataset: {e}")
    else:
        st.info("Please upload a CSV file to begin analysis.")
elif menu=="Performance Analyzer":
    st.header("🚀 Performance Analyzer")
    st.write(
        "Measure algorithm performance "
        "across different input sizes."
    )
    if st.button("Run Benchmark", type="primary"):
        with st.spinner("Running benchmarks..."):
            results = benchmark_merge_sort()
            st.session_state["benchmark_results"] = results
    if "benchmark_results" in st.session_state:
        results = st.session_state["benchmark_results"]
        st.subheader("Benchmark Results")
        st.dataframe(
            results,
            use_container_width=True
        )
        st.subheader("Execution Time Analysis")
        chart_data = results.set_index("Input Size")
        st.line_chart(
            chart_data[
                ["Average Time", "Median Time"]
            ]
        )
        st.success("Benchmark completed successfully!")

        st.info(
            "Merge Sort theoretical time complexity: O(n log n)"
        )
else:
    st.warning("Please select a valid module.")