2.) (5 points): Download this dataset and assess it using ISLP 3.3 and 3.4 (like how you did for homework 3).
frame = pd.read_csv('FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv')


3.) (5 points): Describe each of the 12 variables in your own words, then mention the datatype of each.
Facility Name: Name of the hospital. Int. 

Facility ID: Unique ID tag for each hospital. String.

State: State the hospital resides in. String.

Measure Name: Looks like the naming code for each what type of discharge method/action. String.

Number of Discharges: Number of discharges for the Measure type. Int.

Footnote: From what it looks like. This column is used when there isn't any data for the row. So I'm assuming they're using this as a way
to explain why this data is empty. It may be due to not having the data or the data might be so little that it's insignificant for the set. String.

Excess Readmission Ratio: Our rate for how many readmissions we see against how many readmissions we expected to see. I'm assuming that we want to see less admissions then we predicted. So anything > 1.0 is above what we wanted. Float.

Predicted Readmission Rate: This looks like a percentage that represents the prediction for readmissions of the population. I'm assuming this is for the hosptial board's current data prediction model. float.

Expected Readmission Rate: This is a percentage that looks at past data as our benchmark for what our prediction model should be aiming for. float.

Number of Readmissions: So according to the data dictionary on the Hospital Readmission website. These are 30 day intervals of readmissions. 

Start Date: Start of the reporting period for this data set. datetime

End Date: End of the reporting period for this data set. datetime


4.) 5 points): Form your research question that can be answered by this dataset.

Can we predict which hospitals will get penalties because of high readmission rates. Focusing on Expected Readmission Rates > 1 for the HF tag by using the discharge valume and historical Expected Readmission Rates.

5.) (5 points): Explain why your research question would be interesting to the board-- do not tailor your research question to me just because I'm your machine learning instructor. I'm interested in your model, but the board cares about money/patients. 

This question would help the board find high-risk patients for follow-up care. If they have a ERR > 1
they'll face Medicare penalties. This will indicate that care at these hospitals aren't up to par for heart failure pateints.

6.) (40 points): Choose any algorithm from chapter 5, 6, 7, or 8 to answer your research question. Explain your choice. For example, if you choose Lasso then be sure you apply lasso to your logistic or linear regression model. If you choose a decision tree, make sure your choice is informative for the board. Not too easy or insulting. 

Algorithm that uses a linear regression model and lasso method.
Used R-code regression model with lasso to get the initial runthrough. Then used generative AI to transfer it to
 python. Found out the implementation was incorrect, so it needed to be frankestein'd into functionality. 

7.) Attached to this repository is a Jupyter Notebook. The notebook should give more examples and data of the exam as a whole. 

In terms of ethical practice, this algorithm could easily false flag some relatively safe hospitals as "bad" for
 patients with heart failure. It also doesn't account for complex cases with where multiple flags would need to 
be checked. This would definitely succeed in ways of reducing cost, but would make patient living possibly worse.
This also isn't a fair model for smaller hospitals.

This model should only need a python interpreter with all files in the same directory. 


9.) To the board. It would be wise to target ERR's that close in on 1.0. We should also consider reviewing this model every quarter to inspect how much patient care and cost correlate. This may allow us to potentially, increase patient care results alongside make more profits by avoiding fines.
