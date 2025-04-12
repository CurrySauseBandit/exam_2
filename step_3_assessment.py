import pandas as pd
import matplotlib.pyplot as plt

"""
3.) (5 points): Describe each of the 12 variables in your own words, then mention the datatype of each.

Facility Name: Name of the hospital. Int.

Facility ID: Unique ID tag for each hospital. String.

State: State the hospital resides in. String.

Measure Name: Looks like the naming code for each what type of discharge method/action. String.

Number of Discharges: Number of discharges for the Measure type. Int.

Footnote: From what it looks like. This column is used when there isn't any data for the row. So I'm assuming they're using this as a way to explain why this data is empty. It may be due to not having the data or the data might be so little that it's insignificant for the set. String.

Excess Readmission Ratio: Our rate for how many readmissions we see against how many readmissions we expected to see. I'm assuming that we want to see less admissions then we predicted. So anything > 1.0 is above what we wanted. Float.

Predicted Readmission Rate: This looks like a percentage that represents the prediction for readmissions of the population. I'm assuming this is for the hosptial board's current data prediction model. float.

Expected Readmission Rate: This is a percentage that looks at past data as our benchmark for what our prediction model should be aiming for. float.

Number of Readmissions: So according to the data dictionary on the Hospital Readmission website. These are 30 day intervals of readmissions.

Start Date: Start of the reporting period for this data set. datetime

End Date: End of the reporting period for this data set. datetime

"""

frame = pd.read_csv('FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv')
print(frame)
print(frame.dtypes)
print(frame.info())
print(frame.describe())
frame.hist(figsize=(12,10))
plt.show()