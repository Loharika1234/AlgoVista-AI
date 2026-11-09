# 🚀 AlgoVista AI – Explore. Execute. Understand.

### Your Interactive Journey into Algorithms, Performance Analysis & Data Science

> Don't just learn how an algorithm works. Execute it, observe its behaviour, measure its performance, and understand the logic behind it.

**Live Application:** https://algovista-ai.streamlit.app/  
**Source Code:** https://github.com/Loharika1234/AlgoVista-AI

| Project Information | Details |
|---|---|
| Project | AlgoVista AI |
| Current Version | 0.1.0 |
| Release Stage | Early Public Prototype |
| Platform | Streamlit Web Application |
| Development Status | Actively Under Development |

---

# 1. Welcome to AlgoVista AI!
Have you ever wondered why one algorithm performs faster than another? Why does an algorithm that works perfectly with 10 numbers sometimes become inefficient with 10,000 numbers? What happens inside an algorithm when it sorts an array, searches for an element, or processes a dataset? These questions are at the heart of computer science.
**AlgoVista AI is designed to help you explore these questions through practical experimentation.**
Instead of limiting algorithm learning to definitions, formulas, and textbook examples, AlgoVista AI brings together algorithm execution, performance measurements, complexity analysis, and data exploration.
Whether you are a student learning Data Structures and Algorithms, a developer exploring computational performance, or someone interested in data science, this platform provides an environment to experiment and learn.
-------
# 2. Your Learning Journey
Think of AlgoVista AI as a small computational laboratory. You provide the input. The platform executes the available functionality. You observe the results and investigate what happened.
The platform currently offers four main areas of exploration:
- **Algorithm Lab** – Execute implemented algorithms.
- **Performance Analyzer** – Measure algorithm performance.
- **Complexity Analyzer** – Explore empirical complexity predictions.
- **Data Science Lab** – Investigate datasets and discover patterns.
Let's explore each one!
-------
# 3. Explore the Platform
## 3.1 Algorithm Lab – Watch Logic in Action
**What happens when you give an algorithm an unsorted array?** Let's find out.
The Algorithm Lab currently provides an interactive interface for executing Merge Sort.
**Your first experiment**
Suppose you have this array: `45, 12, 89, 3, 25, 7, 61`. Your task is to arrange these numbers in ascending order.
**How to use it**
1. Open the AlgoVista AI application.
2. Select **Algorithm Lab** from the sidebar.
3. Enter the numbers separated by commas.
4. Execute the algorithm using the available control.
5. Examine the sorted output and performance measurements.
**What will you observe?**
- **Sorted Array** – The final arrangement of your input.
- **Comparisons** – The number of comparisons recorded by the implementation.
- **Execution Time** – The measured time taken by the algorithm.
- **Peak Memory** – The peak Python-traced memory allocation during execution.
**What will you learn?** You can observe how an algorithm transforms an input into an output and begin understanding why algorithm selection matters.
**Currently available:** Merge Sort.
**Coming next:** Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Heap Sort, Counting Sort, and Radix Sort.
## 3.2 Performance Analyzer – How Fast Is Your Algorithm?
An algorithm may work correctly with a small input. But what happens when the input becomes larger? This is where performance analysis becomes interesting.
The Performance Analyzer measures Merge Sort across multiple input sizes.
**How to use it**
1. Open **Performance Analyzer**.
2. Start the benchmark using the available button.
3. Allow the benchmark to finish.
4. Explore the generated performance table and chart.
**What is measured?**
| Measurement | What it tells you |
|---|---|
| Input Size | Number of elements processed |
| Average Time | Mean execution time across benchmark runs |
| Median Time | Middle execution-time measurement |
The current benchmark uses multiple input sizes and repeated executions to provide a more useful performance comparison.
**Experiment with your understanding**
- Does execution time increase as input size increases?
- Does the growth appear linear or faster?
- Why are repeated measurements useful?
- Can a single execution time accurately describe algorithm performance?
**Learning objective:** Understand how input size influences practical execution performance.
## 3.3 Complexity Analyzer – Connect Experiments with Theory
You have measured an algorithm's performance. Now comes the interesting question: **Which theoretical complexity model best describes the observed growth?**
The Complexity Analyzer compares benchmark measurements against selected theoretical growth models.
**How to use it**
1. First, open Performance Analyzer.
2. Run the benchmark.
3. Navigate to Complexity Analyzer.
4. Examine the model comparison scores and predicted best-fitting model.
**Currently supported models**
| Complexity | General interpretation |
|---|---|
| O(log n) | Logarithmic growth |
| O(n) | Linear growth |
| O(n log n) | Linearithmic growth |
| O(n²) | Quadratic growth |
**Understanding the prediction**
The platform calculates an R²-based fit score for each candidate model and identifies the best-fitting candidate among the supported options. A higher R² score indicates a better fit to the measured data under the implemented comparison method.
**Important:** An empirical prediction is not a mathematical proof of an algorithm's Big-O complexity. Actual measurements can be influenced by hardware, Python execution, input characteristics, and benchmarking conditions.
**Learning objective:** Connect theoretical algorithm analysis with experimental observations.
## 3.4 Data Science Lab – Discover What Your Data Is Hiding
Data is more than rows and columns. It can reveal distributions, missing information, relationships, and patterns that are not immediately visible.
The Data Science Lab provides basic dataset exploration and visualization through CSV uploads.
**How to use it**
1. Open **Data Science Lab**.
2. Upload a CSV dataset.
3. Inspect the dataset preview.
4. Examine the dataset dimensions.
5. Explore missing-value information.
6. Review statistical summaries.
7. Explore the available visualizations.
**Available capabilities**
1. **Dataset Preview:** View the first ten rows of your uploaded dataset.
2. **Dataset Overview:** Understand the total number of rows, columns, and missing cells.
3. **Missing Value Analysis:** Identify missing values in individual columns and examine their percentages.
4. **Statistical Summary:** Explore statistical information about your dataset using Pandas.
5. **Histogram:** Understand how values are distributed across a selected numeric column.
6. **Department-wise Student Count:** Explore the number of student records in each department.
7. **Study Hours vs Final Exam Score:** Observe the relationship between study hours and examination scores using a scatter plot.
8. **Correlation Heatmap:** Examine correlations among selected numerical features.
**Try this experiment:** Upload a student-performance dataset and investigate:
- Which columns contain missing values?
- How are study hours distributed?
- How do study hours relate to final examination scores?
- Which numerical features show stronger correlations?
**Learning objective:** Develop practical data exploration skills and learn how visualizations can support data interpretation.
**Compatibility note:** Some current visualizations expect specific columns from the sample student-performance dataset. Support for arbitrary CSV schemas is an area for improvement.
-----------------
# 4. Understanding the Measurements
Before interpreting results, understand what the numbers actually represent.
- **Execution Time:** The measured duration of an algorithm execution. It can vary between runs due to system activity and execution conditions.
- **Comparisons:** The number of comparisons recorded by the algorithm implementation. Different algorithms may count different operations, so comparisons should be interpreted according to each implementation.
- **Peak Memory:** The current implementation uses Python's `tracemalloc` to measure peak traced Python memory allocations. This is not a measurement of total process RAM or a direct proof of theoretical space complexity.
- **Time Complexity:** Describes how the running time of an algorithm grows as the input size increases.
- **Space Complexity:** Describes how the memory requirements of an algorithm grow with input size. Advanced space-analysis capabilities are still under development.
---------------
# 5. What Is Available Today?
AlgoVista AI is an evolving platform. It is important to distinguish implemented features from planned capabilities.
| Module | Current status |
|---|---|
| Dashboard | Available |
| Merge Sort execution | Implemented |
| Merge Sort benchmarking | Implemented |
| Empirical complexity prediction | Implemented |
| CSV dataset upload | Implemented |
| Statistical summaries | Implemented |
| Dataset visualizations | Implemented |
| Additional sorting algorithms | Planned |
| Searching algorithms | Planned |
| Step-by-step algorithm animations | Planned |
| Advanced space analysis | Planned |
| AI-assisted learning | Planned |
------------
# 6. What's Coming Next?
The current release is only the beginning. The development roadmap focuses on expanding the platform into a more comprehensive algorithm and data science learning environment.
**Sorting Algorithms**
- Bubble Sort
- Selection Sort
- Insertion Sort
- Quick Sort
- Heap Sort
- Counting Sort
- Radix Sort
**Searching Algorithms**
- Linear Search
- Binary Search
- Jump Search
- Interpolation Search
- Exponential Search
**Graph Algorithms**
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra's Algorithm
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm
- Prim's Algorithm
- Kruskal's Algorithm
**Advanced Learning & Analysis**
- Step-by-step algorithm visualization.
- Comparisons between multiple algorithms.
- Improved time and space complexity analysis.
- Advanced performance benchmarking.
- Additional dataset exploration features.
- AI-assisted algorithm explanations and learning support.
*These are planned enhancements. They are not all available in the current release.*
---------------
## 7. Version History & Continuous Development
**AlgoVista AI is not a finished destination — it is a continuously evolving learning platform.** Every version represents a new step towards making algorithm analysis, performance measurement, and data science more interactive, understandable, and accessible.
### 🚀 Current Release — Version 0.1.0
**Status: Initial Public Prototype**
The first public release introduces the foundation of AlgoVista AI, allowing users to experiment with algorithms, observe execution behaviour, analyze performance, and explore datasets.
**Available in this release:**
- Merge Sort implementation with sorting results and comparison count.
- Execution-time measurement and memory-allocation tracking.
- Benchmarking across multiple input sizes.
- Empirical time-complexity prediction using mathematical growth models.
- CSV dataset upload and basic dataset exploration.
- Statistical summaries and interactive data visualizations.
- Streamlit-based interactive interface.
### 🛠️ What's Coming Next?
AlgoVista AI will continue to grow through carefully developed and tested updates. Planned improvements include:
- **More Sorting Algorithms:** Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Heap Sort, Counting Sort, and Radix Sort.
- **Searching Algorithms:** Linear Search, Binary Search, Jump Search, Interpolation Search, and Exponential Search.
- **Algorithm Visualization:** Step-by-step execution, comparisons, swaps, and visual explanations of how algorithms work.
- **Advanced Complexity Analysis:** Improved time and space complexity estimation with clearer comparisons between theoretical and observed performance.
- **Expanded Data Science Studio:** More flexible CSV support, data cleaning, feature exploration, and additional visualizations.
- **AI-Assisted Learning:** Interactive explanations, algorithm comparisons, and learning support.
### 📌 Release Roadmap
| Version | Development Focus | Status |
|---|---|---|
| 0.1.0 | Initial platform, Merge Sort, benchmarking, complexity prediction, and dataset exploration | Released |
| 0.2.0 | Additional sorting and searching algorithms | Planned |
| 0.3.0 | Step-by-step algorithm visualization | Planned |
| 0.4.0 | Advanced performance and complexity analysis | Planned |
| 0.5.0 | Expanded Data Science Studio | Planned |
| 0.6.0+ | AI-assisted learning and further enhancements | Future Development |
| 1.0.0 | Integrated, tested, and polished platform release | Target |
*Roadmap versions are development targets, not confirmed release dates. Features will be marked as available only after implementation and testing.*
### 🔄 Our Continuous Development Cycle
Every improvement follows a simple development process:
1. **Explore:** Identify a learning challenge or feature worth improving.
2. **Design:** Plan the functionality and its place in the platform.
3. **Develop:** Implement the feature and integrate it with existing modules.
4. **Test:** Verify correctness, performance, and usability.
5. **Release:** Publish the tested update to the live application.
6. **Improve:** Use feedback and testing results to guide the next iteration.
### 📖 How to Follow Project Updates
AlgoVista AI is actively maintained as a learning and development project. New algorithms, analysis tools, visualizations, bug fixes, and interface improvements will be documented as the project evolves.
- **Source Code & Updates:** [GitHub Repository](https://github.com/Loharika1234/AlgoVista-AI)
- **Live Application:** [Explore AlgoVista AI](https://algovista-ai.streamlit.app/)
- **User Guide:** This document will be updated whenever meaningful features or changes are introduced.
### 💡 Development Philosophy
**Build. Test. Understand. Improve. Repeat.**
The goal is not simply to add more features. It is to make every feature meaningful, reliable, and useful for learning. AlgoVista AI aims to bring algorithms, performance analysis, and data science together in one evolving studio.
*The current release is only the beginning. The next version starts with the next improvement.*
