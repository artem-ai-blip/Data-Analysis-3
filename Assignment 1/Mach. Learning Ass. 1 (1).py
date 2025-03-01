#!/usr/bin/env python
# coding: utf-8

# **Progress**
# 
# Based on the dataset, the choice of "Driver/sales workers and truck drivers" occupation was made due to their relative significant number of observations which is 3189. 
# 
# Created variable Wage = (Weekly Earnings)/(Weekly hours) or earnwke/uhours
# 
# Out of 3189 5 observetion where removed due to the extreme values which seems unrealistic like a single observation which equals to 120 while the closest biggest value is 76 
# 
# Section of Distributions showed the following: 
# 
# The "Driver/sales workers and truck drivers" are 

# In[1]:


import pandas as pd

data_all = pd.read_csv("https://osf.io/download/4ay9x/")

data_all.columns

data_all[data_all['occ2012']==9130].count()


# In[2]:


top_occ = data_all['occ2012'].value_counts().head(36)
print(top_occ)


# In[3]:


data_all["wage"] = data_all["earnwke"] / data_all["uhours"]
print(data_all[["earnwke", "uhours", "wage"]].head())


# In[4]:


# Isolate category 9130 (Driver/sales workers and truck drivers)
data_9130 = data_all[data_all["occ2012"] == 9130].copy()

# Remove extreme wage values: keeping only wages between 1 and 120
data_9130 = data_9130[(data_9130["wage"] > 1) & (data_9130["wage"] < 120)].copy()

# Verify the correctness and number of observations
print(data_9130["occ2012"].head())
print(f"Number of observations in category 9130: {data_9130.shape[0]}")


# **Distributions**

# In[7]:


# Get distribution statistics of 9130 category by wage
wage_distribution = data_9130["wage"].describe().reset_index()
wage_distribution.columns = ["Statistic", "Value"]

# Display the wage distribution
print(wage_distribution)


# In[8]:


# Compute the distribution of  by state
wage_distribution = data_9130["wage"].value_counts().reset_index()
wage_distribution.columns = ["Wage", "Count"]

# Sort the table for better readability
wage_distribution = wage_distribution.sort_values(by="Wage")

# Display the distribution
print(wage_distribution)


# In[23]:


import matplotlib.pyplot as plt

# Plot histogram of wage distribution
plt.figure(figsize=(10,6))
plt.hist(data_9130["wage"], bins=30, edgecolor='black', alpha=0.7)
plt.xlabel("Wage")
plt.ylabel("Frequency")
plt.title("Histogram of Wage Distribution for 9130 Category (Drivers & Sales Workers)")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()


# In[21]:


# Compute the distribution of  by state
state_distribution = data_9130["state"].value_counts().reset_index()
state_distribution.columns = ["State", "Count"]

# Display the distribution
print(state_distribution)


# In[9]:


# Define Education Level Mapping based on grade92 measurement (31 to 46)
education_mapping = {
    31: "Less than 1st grade",
    32: "1st - 4th grade",
    33: "5th - 6th grade",
    34: "7th - 8th grade",
    35: "9th grade",
    36: "10th grade",
    37: "11th grade",
    38: "12th grade, no diploma",
    39: "High school graduate (diploma or GED)",
    40: "Some college, no degree",
    41: "Associate degree (vocational)",
    42: "Associate degree (academic)",
    43: "Bachelor's degree",
    44: "Master's degree",
    45: "Professional degree",
    46: "Doctorate degree"
}

# Filter grade92 values within the range 31 to 46
data_9130_filtered = data_9130[data_9130["grade92"].between(31, 46, inclusive="both")].copy()

# Convert 'grade92' column to numeric type
data_9130_filtered["grade92"] = pd.to_numeric(data_9130_filtered["grade92"], errors='coerce')

# Apply the mapping for better readability
data_9130_filtered["Education Level"] = data_9130_filtered["grade92"].map(education_mapping)

# Get distribution of grade92 (Education Level)
education_distribution = data_9130_filtered["Education Level"].value_counts().reset_index()
education_distribution.columns = ["Education Level", "Count"]

# Display the distribution
print(education_distribution)


# In[10]:


# Get distribution statistics of 9130 category by grade92 (Education Level)
grade92_distribution = data_9130["grade92"].describe().reset_index()
grade92_distribution.columns = ["Statistic", "Value"]

# Display the grade92 distribution
print(grade92_distribution)


#    - Measurement:  
#      - 31 = Less than 1st grade  
#      - 32 = 1st - 4th grade  
#      - 33 = 5th - 6th grade  
#      - 34 = 7th - 8th grade  
#      - 35 = 9th grade  
#      - 36 = 10th grade  
#      - 37 = 11th grade  
#      - 38 = 12th grade, no diploma  
#      - 39 = High school graduate (diploma or GED)  
#      - 40 = Some college, no degree  
#      - 41 = Associate degree (vocational)  
#      - 42 = Associate degree (academic)  
#      - 43 = Bachelor's degree  
#      - 44 = Master's degree  
#      - 45 = Professional degree  
#      - 46 = Doctorate degree  

# In[11]:


# Define Ethnicity Mapping based on the given codes
ethnicity_mapping = {
    1: "Mexican",
    2: "Puerto Rican",
    3: "Cuban",
    4: "Central/South American",
    5: "Other Spanish",
    6: "Not Hispanic"
}

# Ensure 'ethnic' column is numeric
data_9130["ethnic"] = pd.to_numeric(data_9130["ethnic"], errors='coerce')

# Apply the mapping for better readability
data_9130["Ethnicity"] = data_9130["ethnic"].map(ethnicity_mapping)

# Get distribution of ethnicities
ethnicity_distribution = data_9130["Ethnicity"].value_counts().reset_index()
ethnicity_distribution.columns = ["Ethnicity", "Count"]

# Display the distribution
print(ethnicity_distribution)


# In[12]:


# Get distribution of 9130 category by age
age_distribution = data_9130["age"].describe().reset_index()
age_distribution.columns = ["Statistic", "Value"]

# Display the age distribution statistics
print(age_distribution)


# In[13]:


# Define Sex Mapping
sex_mapping = {
    1: "Male",
    2: "Female"
}

# Ensure 'sex' column is numeric
data_9130["sex"] = pd.to_numeric(data_9130["sex"], errors='coerce')

# Apply the mapping for better readability
data_9130["Sex"] = data_9130["sex"].map(sex_mapping)

# Get distribution of sex in the 9130 category
sex_distribution = data_9130["Sex"].value_counts().reset_index()
sex_distribution.columns = ["Sex", "Count"]

# Display the distribution
print(sex_distribution)


# In[14]:


# Define Marital Status Mapping
marital_mapping = {
    1: "Married (civilian spouse present)",
    2: "Married (Armed Forces spouse present)",
    3: "Married (spouse absent)",
    4: "Widowed",
    5: "Divorced",
    6: "Separated",
    7: "Never Married"
}

# Ensure 'marital' column is numeric
data_9130["marital"] = pd.to_numeric(data_9130["marital"], errors='coerce')

# Apply the mapping for better readability
data_9130["Marital Status"] = data_9130["marital"].map(marital_mapping)

# Get distribution of marital status in the 9130 category
marital_distribution = data_9130["Marital Status"].value_counts().reset_index()
marital_distribution.columns = ["Marital Status", "Count"]

# Display the distribution
print(marital_distribution)


# In[15]:


# Get distribution of number of own children (ownchild) in the 9130 category
ownchild_distribution = data_9130["ownchild"].value_counts().reset_index()
ownchild_distribution.columns = ["Number of Own Children", "Count"]

# Sort the table for better readability
ownchild_distribution = ownchild_distribution.sort_values(by="Number of Own Children")

# Display the distribution
print(ownchild_distribution)


# In[16]:


# Get distribution of industry classification (ind02) in the 9130 category
industry_distribution = data_9130["ind02"].value_counts().reset_index()
industry_distribution.columns = ["Industry Code (ind02)", "Count"]

# Sort the table for better readability
industry_distribution = industry_distribution.sort_values(by="Industry Code (ind02)")

# Display the distribution
print(industry_distribution)


# In[17]:


# Get distribution of class classification in the 9130 category
class_distribution = data_9130["class"].value_counts().reset_index()
class_distribution.columns = ["Class Code", "Count"]

# Sort the table for better readability
class_distribution = class_distribution.sort_values(by="Count")

# Display the distribution
print(class_distribution)


# In[18]:


# Get distribution of union membership (unionmme) in the 9130 category
union_membership_distribution = data_9130["unionmme"].value_counts().reset_index()
union_membership_distribution.columns = ["Union Membership Code", "Count"]

# Sort the table for better readability
union_membership_distribution = union_membership_distribution.sort_values(by="Union Membership Code")

# Display the distribution
print(union_membership_distribution)


# In[19]:


# Get distribution of union coverage (unioncov) in the 9130 category
union_coverage_distribution = data_9130["unioncov"].value_counts().reset_index()
union_coverage_distribution.columns = ["Union Coverage Code", "Count"]

# Sort the table for better readability
union_coverage_distribution = union_coverage_distribution.sort_values(by="Union Coverage Code")

# Display the distribution
print(union_coverage_distribution)


# In[20]:


# Get distribution of labor force status (lfsr94) in the 9130 category
labor_force_distribution = data_9130["lfsr94"].value_counts().reset_index()
labor_force_distribution.columns = ["Labor Force Status Code (lfsr94)", "Count"]

# Sort the table for better readability
labor_force_distribution = labor_force_distribution.sort_values(by="Labor Force Status Code (lfsr94)")

# Display the distribution
print(labor_force_distribution)


# **Regressions**

# In[ ]:




