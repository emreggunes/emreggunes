# MoodTracker-DSA210Project

## Project Overview
Over the next three months, I’ll be analyzing how my daily habits influence my mood. This project focuses on understanding the role of factors like sleep hours, work hours, exercise time, screen time, and social interactions in shaping my daily emotional well-being.

By visualizing patterns and conducting statistical analyses, I aim to pinpoint which habits have the most significant impact on improving or deteriorating my mood. The ultimate goal is to identify actionable changes that lead to consistent improvements in emotional well-being.

## Objectives
The primary objectives of this project are:
1. **Mood Analysis**: To measure how daily habits such as sleep, exercise, work, and social interactions correlate with mood variations.
2. **Key Habit Identification**: To identify the habits with the strongest influence on improving mood and create strategies to enhance emotional well-being.
3. **Data-Driven Improvement**: To develop a data-driven approach for maintaining a balanced and positive emotional state.
4. **Applied Data Science**: To apply data analysis, visualization, and statistical techniques to a personal dataset, enhancing my understanding and skills in data science.

## Motivation
The key motivations for selecting this project are:
1. **Emotional Health**: Understanding how my habits affect my mood is essential for improving my mental health and overall well-being.
2. **Actionable Insights**: Analyzing my daily data will provide a scientific foundation for optimizing my habits to foster a positive emotional state.
3. **DSA 210 Course Application**: This project allows me to apply theoretical knowledge from the course to a real-world problem and gain hands-on experience in data science.
4. **Long-Term Benefits**: The insights gained will serve as a practical guide for maintaining emotional stability and happiness over time.

## Dataset
The dataset for this project consists of daily records I have maintained over three months. The data includes the following attributes:
- **Date**: The specific day of the record
- **Sleep Hours**: Total hours slept
- **Work Hours**: Time spent on professional tasks
- **Reading Hours**: Time spent reading books, articles, or other materials
- **Writing Hours**: Time spent journaling, creative writing, or work-related writing
- **Exercise Hours**: Hours of physical activity or workout
- **Social Time (Hours)**: Hours spent interacting with family or friends
- **Screen Time (Hours)**: Hours spent on electronic devices
- **Steps**: Total steps taken during the day
- **Mood (1-10)**: Self-reported mood score (1 being poor and 10 excellent)

The data is recorded daily in a structured format and will be cleaned to address any missing or inconsistent entries before analysis.

## Data Considerations
- **External Influences**: Variations due to external events (e.g., stressful workdays, illness) will be flagged as potential outliers.
- **Consistency**: Efforts will be made to ensure accurate and consistent logging of daily activities and mood scores.
- **Trends and Patterns**: Specific focus will be placed on identifying consistent patterns in habits and mood over time.

## Tools and Technologies
- **Python**: For data cleaning, analysis, and visualization
- **Pandas**: For data manipulation and preprocessing
- **Matplotlib and Seaborn**: For visualizations (e.g., scatter plots, heatmaps, time series)
- **SciPy/Statsmodels**: For hypothesis testing and statistical analyses

## Analysis Plan
1. **Data Collection**:
   - Import the daily records into a Pandas DataFrame.
   - Clean the data by handling missing values and ensuring consistent formatting.
2. **Visualization**:
   - Create scatter plots, heatmaps, and time series plots to explore relationships and trends. Examples include:
     - Scatter plot of sleep hours vs. mood.
     - Heatmap showing correlations between habits and mood.
     - Time series plot comparing daily habits and mood over three months.
3. **Hypothesis Testing**:
   - Test hypotheses such as:
     - H₀: Changes in daily habits have no effect on mood.
     - Hₐ: Changes in one or more habits significantly impact mood.
   - Use regression analysis to identify the strongest predictors of mood.
4. **Trend Analysis**:
   - Explore trends in mood over time to identify patterns of improvement or decline.
   - Determine whether specific habits (e.g., more sleep or exercise) align consistently with positive mood scores.

## Example Analysis
An example visualization will include a scatter plot showing the relationship between sleep hours and mood. The x-axis will represent sleep hours, while the y-axis will represent mood scores. This plot will help determine if more sleep consistently correlates with a higher mood score.

## Conclusion
By the end of this project, I aim to identify which daily habits have the greatest influence on my mood. The insights gained will help me optimize my routine to maintain a consistently positive emotional state. Beyond personal improvement, this project demonstrates how data science can be applied to track and enhance emotional well-being in a practical, real-world setting.
