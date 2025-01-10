DSA210 FALL 2025



PROJECT FINAL REPORT

MOODTRACKER ANALYSIS









EMRE GUNES 28411









SUPERVISED BY

ÖZGÜR ASAR









SABANCI UNIVERSITY























# 1. Introduction

This study, termed "MoodTracker," sought to investigate how daily behaviours affect emotional well-being, with mood serving as the key variable. Using three months of self-reported personal data, variables such as Sleep Hours, Work Hours, Reading Hours, Writing Hours, Exercise Hours, Social Time, Screen Time, Steps, and Mood (on a 1-10 scale) were studied to find connections and highlight keystone habits that significantly affect mood. The study delivered practical insights to optimise emotional health and improve daily emotional resilience using data science approaches, visualisations, and statistical analysis.



# 2. Data Overview

The dataset consisted of the following attributes:

Date 

Daily log date.

Sleep Hours

Sleep is a critical component of emotional stability. Getting 7-8 hours of sleep per night produced the greatest mood scores (8-9). Sleep deprivation (<6 hours) and excessive sleep (>9 hours) resulted in decreased mood levels. Optimal sleep schedules can improve brain clarity and emotional resilience.

Work Hours

Productivity and emotional wellness are linked. Working 4-5 hours every day was good for maintaining a positive mindset. Overworking (>7 hours) generated tension, while underworking (<2 hours) led to dissatisfaction. Finding a manageable workload is critical for achieving emotional equilibrium.

Reading and Writing Hours

Allocating 1-2 hours every day to intellectual or creative activities improved mood. Absence of such activities was associated with poorer emotional engagement. Reading or writing on a regular basis can boost your mood and give you a sense of accomplishment.

Exercise Hours 

Physical activity made a significant contribution to mood improvement. Exercising for 1-2 hours every day was associated with mood scores of 8-9. Lack of exercise (<1 hour) negatively impacted mental well-being. Integrating frequent physical activity into daily routines is essential for stress management and mood enhancement.

Social Time

Social interactions were among the strongest predictors of mood (R-squared = 0.050114). Spending 2-4 hours per day with others led to the highest mood scores. Social time, whether excessive (>5 hours) or insufficient (<1 hour), had a detrimental impact on mood. Balanced social connections offer emotional support and fulfilment.

Screen Time

Excessive screen usage (more than 5 hours) was linked to poorer mood, most likely due to digital tiredness and isolation. Limited screen time (2-3 hours) was associated with higher mood scores. Limiting screen time is critical for emotional health.

Steps

A higher step count (>5000 steps per day) was linked to a better mood. Sedentary lifestyles (<3000 steps) lower mood scores, emphasising the importance of physical activity. Increasing daily steps boosts vitality and sense of success.

Mood (1-10)

Self-reported mood score.



# 3. Data Collection Process

This dataset was collected daily for three months. Metrics were recorded manually at the end of each day to ensure accuracy and consistency. The self-reported mood score varied from 1 (extremely poor) to 10 (outstanding). Additional considerations were:

Consistency: Data was logged at the same time daily to prevent discrepancies owing to reporting times.

External Influences: Notes were taken to identify days impacted by external variables, such as illnesses or stressful events, for outlier analysis.

Wearable Devices: A smartwatch was used to accurately monitor step counts.

Screen Time Tracking: Data for screen time tracking came from smartphone usage logs.



# 4. Visualization Summaries and Interpretations

## 4.1 Correlation of Metrics with Mood (Bar Chart)


Most habits have poor associations according to this visualisation. Notable findings:

Work hours showed a correlation of +0.15, indicating a slight positive influence on mood.

Social time had a correlation of -0.22, suggesting that excessive social interaction might reduce mood scores.

Screen time exhibited a correlation of -0.09, reinforcing the importance of limiting screen usage.

## 4.2 Work Hours and Mood (Scatter Plot with Regression Line)


The scatter plot indicated a little positive trend. For example, on days with 5 work hours, the average mood score was 8.0, compared to 6.0 on days when no work was done. This shows that productivity may improve emotional well-being.

## 4.3 Sleep Hours and Mood (Scatter Plot with Regression Line)


The plot revealed that days with 8 hours of sleep resulted in an average mood score of 8.5, whereas days with 5 hours averaged 6.5. Despite a small tendency, adequate sleep proved to boost mood considerably.

## 4.4 Social Time and Mood (Scatter Plot with Regression Line)


The scatterplot revealed a small negative connection. For example, on days with 4+ hours of social time, mood scores declined to an average of 6.5, as opposed to 7.5 on days with 1-2 hours of interaction.

## 4.5 Weekly Process for Screen Time Compared with Mood (Time Series Plot)


On days with 6+ hours of screen use, mood scores were sometimes as low as 5.0. In contrast, on days with 2-3 hours of screen time, mood scores averaged approximately 8.0. This pattern emphasised the significance of managing digital habits.

4.6 Steps and Mood (Boxplot)
 The boxplot revealed that days with 10,000+ steps had no significant difference in mood scores from days with 5,000 steps. For example, both groups reported median mood scores of roughly 7.0, indicating that step count alone was not a reliable predictor of mood.

## 4.7 Regression Analysis Coefficients (Bar Chart)


Regression analysis revealed the following key coefficients:

Work hours: +0.38

Writing hours: +0.58

Steps: -0.0002

These coefficients show that, while work and writing hours had a minor positive effect on mood, their impact was not statistically significant.



# 5. Conclusion

The project highlighted the interconnectivity of everyday routines and emotional well-being, offering practical ideas for improving lifestyle choices and achieving long-term enjoyment. Productivity, including work and writing hours, has a weak but positive link with mood, emphasising the need of established routines. While sleep has a minimal effect, continuous sleep (7-8 hours) is essential for emotional stability. Social interaction might affect mood depending on its quality, however reducing screen time consistently improves emotional health. Physical activity and meaningful engagements were also identified as key drivers to mood improvement.

Actionable Recommendations

To improve emotional well-being, prioritise balanced productivity by committing to 4-5 hours of structured but flexible work or study per day. Consistent sleep is vital, with 7-8 hours of quality sleep benefiting mental health. Engage in 2-4 hours of meaningful social contacts, focussing on quality over quantity. Limit screen usage to 2-3 hours each day, especially in the evenings, to encourage greater relaxation and sleep. To improve mood and energy, incorporate 1-2 hours of pleasurable physical activity each day and aim for 5000+ steps. Finally, set aside 1-2 hours for intellectual or creative activities like reading or writing to provide cerebral stimulation and fulfilment.

Future Steps

To gain a deeper understanding and improve outlier detection, external factors such as stress or significant life events must be included. Analysing the interplay of habits, such as how screen time affects social interactions, might reveal more intricate relationships. Furthermore, collecting data over a longer period of time will allow researchers to investigate long-term trends or seasonal patterns, resulting in a more complete understanding of the links between daily behaviours and emotional well-being.



# 6. Reflections

This study emphasises the importance of having balanced and planned daily routines for long-term emotional well-being. Individuals who follow these tips can boost their mood, productivity, and overall quality of life. In addition, this research highlighted how data science can deliver meaningful insights into personal routines and mental well-being. While the connections between habits and mood were typically weak, the findings highlight the complexities of emotional health and provide areas for future research.



# 7. Code Appendix

The following Python code was used to perform the analyses and generate visualizations:

 1. import pandas as pd

 2. import matplotlib.pyplot as plt

 3. import seaborn as sns

 4. import statsmodels.api as sm

 5.  

 6. # Load the dataset

 7. file_path = 'path_to_your_file.xlsx'

 8. df = pd.ExcelFile(file_path).parse('Sheet1')

 9.  

10. # Convert 'Date' column to datetime

11. df['Date'] = pd.to_datetime(df['Date'])

12.  

13. # Handle missing and infinite values

14. df.replace([float('inf'), -float('inf')], float('nan'), inplace=True)

15. df.dropna(inplace=True)

16.  

17. # Correlation of Metrics with Mood

18. correlation_matrix = df.drop(columns=['Date']).corr()

19. mood_correlation = correlation_matrix['Mood (1-10)'].sort_values(ascending=False)

20. plt.figure(figsize=(10, 6))

21. mood_correlation.drop("Mood (1-10)").plot(kind='bar', color='skyblue', edgecolor='black')

22. plt.title('Correlation of Metrics with Mood', fontsize=14)

23. plt.ylabel('Correlation Coefficient', fontsize=12)

24. plt.xlabel('Metrics', fontsize=12)

25. plt.xticks(rotation=45, ha='right')

26. plt.grid(axis='y', linestyle='--', alpha=0.7)

27. plt.tight_layout()

28. plt.show()

29.  

30. # Regression Analysis

31. X = df.drop(columns=['Date', 'Mood (1-10)'])

32. y = df['Mood (1-10)']

33. X = sm.add_constant(X)

34. model = sm.OLS(y, X).fit()

35. print(model.summary()) 

