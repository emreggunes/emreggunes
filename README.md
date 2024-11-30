# MoodTracker-DSA210Project

## Project Overview
Over the next three months, I’ll be analyzing how my daily habits influence my mood. This project focuses on understanding the role of factors like sleep hours, work hours, exercise time, screen time, and social interactions in shaping my daily emotional well-being.

By visualizing patterns and performing statistical analysis, I seek to determine which of the habits most strongly improves/deteriorates my mood. The ultimate objective is actionable changes that result in steady improvement of emotional well-being.

## Objectives
The primary objectives of the given project are:
1. **Mood Analysis**: How much daily habits such as sleep, exercise, work, and social interaction relate to mood variations.
2. **Identification of Keystone Habits**: To identify those habits that most strongly drive improved mood and develop strategies to promote emotional wellbeing.
3. **Data-Driven Improvement**: Elaboration of a data-driven method for maintaining emotional balance and positivity.
4. **Applied Data Science**: The application of data analysis, visualization, and statistics to a personal dataset contributes to the deepening of knowledge and skills in data science itself.

## Motivation
Main motivations for choosing this project:
1. **Emotional Health**: Understanding how my habits relate to my mood is key to improving my mental health and well-being.
2. **Actionable Insights**: The analysis of my daily data will, in turn, provide scientific evidence on how to best optimize my habits to achieve the desired positive emotional state.
3. **DSA 210 Course Application**: This project allows me to apply theoretical knowledge from the course into a real-world problem and hands-on experience in data science.
4. **Long-Term Benefits**: Gained insights will be applied as practical guidance toward retaining emotional stability and happiness overtime.

## Dataset
The dataset from this project has been drawn from personal records kept every day over three months' period. The data thus includes the following attributes:
- **Date**: The actual date for the record.
- **Sleep Hours:** Total number of hours of sleep
- **Work Hours**: The amount of time applied to professional work
- **Reading Hours**: Total hours of reading books, articles, etc.
- **Writing Hours**: Hours spent doing journal writing, creative writing, or writing work-related items
- **Exercise Hours**: Exercise time/ hours out/in the gym
- **Social Time (Hours)**: Family/ friends interaction hours
- **Screen Time (Hours)**: Hourly use of electronic appliances
- **Steps**: The number of steps taken within the day
- **Mood (1-10)**: Reported mood score rated by self, ranging from 1 to 10 (poor to excellent)

The data is recorded daily in a structured format and will be cleaned to address any missing or inconsistent entries before analysis.

## Data Considerations
- **External Influences**: Variations due to external events, such as stressful workdays or illness, should be flagged for possible outlier consideration.
- **Consistency**: The subject will make every effort to perform the daily activities and log the mood score as accurately and consistently as possible.
- **Trends and Patterns**: Emphasis will be given to the identification of regular habits and mood patterns over a period of time.

## Tools and Technologies
- **Python**: For cleaning, analyzing, and visualizing data
- **Pandas**: For data manipulation and pre-processing
- **Matplotlib and Seaborn**: For visualizations - scatter plots, heatmaps, time series, among others
- **SciPy/Statsmodels**: Hypothesis testing and statistical analyses

## Analysis Plan
1. **Data Collection**:
   - Import daily records into a Pandas DataFrame.
Data cleaning includes dealing with missing values and normalizing data formats.
2. **Visualization**:
   - Scatter plots, heatmaps, time series plotting for exploration of relationships and trends. Examples include:
     - Scatter plot: Sleep hours vs. Mood.
     - Heatmap: Habit and mood correlations.
- Time series plot comparing daily habits and mood over three months.
3. **Hypothesis Testing**:
   - Test hypotheses such as:
     - H₀: Changes in daily habits have no effect on mood.
     - Hₐ: Changes in one or more habits significantly impact mood.
   - Use regression analysis to identify the strongest predictors of mood.
4. **Trend Analysis**:
   - Analyze the trend of mood over time to find out if there is any improvement or decline.
   - Identify if certain habits-for instance, more sleep or exercise-always correspond to high positive mood scores.

## Example Analysis
An example visualization will include a scatter plot showing the relationship between sleep hours and mood. The x-axis will represent sleep hours, while the y-axis will represent mood scores. This plot will help determine if more sleep consistently correlates with a higher mood score.

## Conclusion
By the end of the project, I hope to learn which daily habits bear most influence on my mood. The insights gained will then be helpful in optimizing the routine so as to always stay in a positive state emotionally. Apart from improvement, this project illustrates how data science could be applied to trace and improve one's emotional condition in a realistic setting.
