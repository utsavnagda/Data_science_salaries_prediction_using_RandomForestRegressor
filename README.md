# Data_science_salaries_prediction_using_RandomForestRegressor
Made a model using Random Forest Regressor to find the salaries based on the provided information. Made a basic HTML to input the data and used Render to deploy the application.

# [Link to the deployed model](https://salary-prediction-using.onrender.com)

# Input
Please go through the data set and pass inputs in the same format.  
Job Title: Your job title e.g Machine Learning Manager or BI Data Analyst,  
Employment Type: Weather you have a full-time role or a contactor role or a part-time role e.g Full-Time, Contract,  
Experience Level: Which level of role do you play in the company e.g Senior or Mid,  
Expertise Level: How experienced you are in the data science industry e.g Intermediate or Expert,  
Salary Currency: The currency in which the salary is paid. e.g United States Dollar or Euro,  
Company Location: The country where the company is based in. e.g United States Dollar,  
Employee Residence: The county of residence of the employee e.g United States or Germany,  
Company Size: The size of the company e.g Large or Mid,  
Year: The current year

# Data set
The [dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/data-science-salaries-2023) was taken from Kaggle. You can go through the link to analyze the data set.

# Ramdom Forest Regressor and Grid Search CV
Used the Random forest regressor model to find the salaries for the given details. The output is in the relevant salary currency i.e. in the same currency as the input.

Also used grid search cross-validation to perform hyper-parameter tuning to the regressor model.

# Conclusion
The input fields are a little stringent but if you input the data correctly the output will be displayed below the input form. 

For future improvement, we can change the text fields in the input form to radio buttons with a quick search option.
