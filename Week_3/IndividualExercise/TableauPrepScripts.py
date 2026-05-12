import pandas as pd

def get_output_schema():
    return pd.DataFrame({
        'Employee_ID': prep_string(),
        'Employee_Name': prep_string(),
        'Department': prep_string(),
        'Age': prep_int(),
        'Salary': prep_int(),
        'Hire_Date': prep_string(),
        'City': prep_string(),
        'Average_Salary_All_Employees': prep_decimal(),
        'Oldest_Employee_Name': prep_string(),
        'Oldest_Employee_Department': prep_string()
    })

def process_it_employees(df):
    
    # Avg salary of all employees
    avg_salary_all = round(df['Salary'].mean(), 2)
    
    # Finds the oldest employee in the dataset and the department he works in
    oldest_idx = df['Age'].idxmax()
    oldest_name = df.loc[oldest_idx, 'Employee_Name']
    oldest_dept = df.loc[oldest_idx, 'Department']
    
    # Contains all employees of the IT deparment
    df_it = df[df['Department'] == 'IT'].copy()
    
    # Creation of the new columns with the calculated values
    df_it['Average_Salary_All_Employees'] = avg_salary_all
    df_it['Oldest_Employee_Name'] = oldest_name
    df_it['Oldest_Employee_Department'] = oldest_dept
    
    return df_it

