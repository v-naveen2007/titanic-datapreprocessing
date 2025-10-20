1. What are the different types of missing data?

There are three main types:

MCAR (Missing Completely at Random): Missingness is independent of both observed and unobserved data.

MAR (Missing at Random): Missingness depends only on observed data, not the missing values themselves.

MNAR (Missing Not at Random): Missingness depends on the value of the missing data itself.

2. How do you handle categorical variables?

Categorical variables are handled by converting them into numerical form using encoding techniques such as:

Label Encoding: Assigns a unique number to each category (used for ordinal data).

One-Hot Encoding: Creates a binary column for each category (used for nominal data).
These techniques allow machine learning models to interpret categorical data effectively.

3. What is the difference between normalization and standardization?

Normalization: Scales data to a fixed range, typically 0 to 1. Formula:


X' = \frac{X - X_{min}}{X_{max} - X_{min}}

Z = \frac{X - \mu}{\sigma}

4. How do you detect outliers?

Outliers can be detected using:

Boxplots: Visualize data distribution and detect extreme values (1.5×IQR rule).

Z-Score Method: Values with |Z| > 3 are considered outliers.

IQR (Interquartile Range): Outliers lie outside Q1 − 1.5×IQR or Q3 + 1.5×IQR.

5. Why is preprocessing important in ML?

Data preprocessing ensures that data is clean, consistent, and suitable for analysis.
It improves:

Model accuracy and performance

Training speed

Generalization of the model to unseen data
Without preprocessing, models may produce misleading or inaccurate results.

6. What is One-Hot Encoding vs Label Encoding?

Feature	One-Hot Encoding	Label Encoding

Output	Creates new binary columns for each category	Assigns an integer to each category
Suitable For	Nominal data (no order)	Ordinal data (has order)
Example	Male → [1,0], Female → [0,1]	Male → 0, Female → 1

7. How do you handle data imbalance?

To handle imbalance in datasets:

Resampling techniques:

Oversampling (e.g., SMOTE) for minority class

Undersampling for majority class


Use class weights in models

Generate synthetic data for minority class
Balancing helps models learn from all classes equally.

8. Can preprocessing affect model accuracy?

Yes ✅. Preprocessing directly affects model accuracy because:

Clean, scaled, and encoded data improves learning efficiency.

It reduces noise, handles missing data, and normalizes features.

Proper preprocessing helps models detect meaningful patterns instead of no your README file (with emojis, tables, and bold headings)?
