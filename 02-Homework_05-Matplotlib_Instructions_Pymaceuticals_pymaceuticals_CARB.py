#!/usr/bin/env python
# coding: utf-8

# # Pymaceuticals Inc.
# ---
# 
# ### Analysis
# * Overall, it is clear that Capomulin is a viable drug regimen to reduce tumor growth.
# * Capomulin had the most number of mice complete the study, with the exception of Remicane, all other regimens observed a number of mice deaths across the duration of the study. 
# * There is a strong correlation between mouse weight and tumor volume, indicating that mouse weight may be contributing to the effectiveness of any drug regimen.
# * There was one potential outlier within the Infubinol regimen. While most mice showed tumor volume increase, there was one mouse that had a reduction in tumor growth in the study. 

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset

# Display the data table for preview


# In[2]:


# Checking the number of mice.
print (f'Number of mice:', data['Mouse ID'].nunique())


# In[3]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
data['Timepoint'] = data['Timepoint'].astype(str)
data['Duplicate ID'] = data['Timepoint'].str.cat(data['Mouse ID'],sep = "")
data.head


# In[4]:


# Optional: Get all the data for the duplicate mouse ID. 
data['Duplicate ID'].nunique()


# In[5]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.
data.drop_duplicates(subset = ['Duplicate ID']), keep = False, inplace = True)
data


# In[6]:


# Checking the number of mice in the clean DataFrame.
print (f'Number of mice:', data['Mouse ID'].nunique())


# ## Summary Statistics

# In[7]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.

mean_datamp = data.groupby(['Drug Regimen'])[['Tumor Volume']].mean()
re_mean_data = mean_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Mean'}, axis = 'columns')
med_data = data.groupby(['Drug Regimen'])['Tumor Volume'].median()
re_medium_data = med_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Median'}, axis = 'columns')
var_data = data.groupby(['Drug Regimen'])[['Tumor Volume (mm3)']].var()
re_var_data = var_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Variance'}, axis = 'columns')
std_data = data.groupby(['Drug Regimen'])[['Tumor Volume']].std()
re_std_data = std_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Standard Deviation'}, axis = 'columns')
sem_data = data.groupby(['Drug Regimen'])[['Tumor Volume']].sem()
re_sem_data = sem_data.rename({'Tumor Volume (mm3)':'Tumor Volume - SEM'}, axis = 'columns')


# In[8]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Using the aggregation method, produce the same summary statistics in a single line


# ## Bar and Pie Charts

# In[9]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pandas.


# In[10]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using using pyplot.


# In[11]:


# Generate a pie plot showing the distribution of female versus male mice using pandas


# In[12]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot


# ## Quartiles, Outliers and Boxplots

# In[13]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

data['Timepoint'] = data['Timepoint'].astype(float)

# Start by getting the last (greatest) timepoint for each mouse.

capomulin_data = data.loc[data['Drug Regimen']=='Capomulin']
ramicane_data = data.loc[data['Drug Regimen']=='Ramicane']
infubinol_data = data.loc[data['Drug Regimen']=='Infubinol']
ceftamin_data = data.loc[data['Drug Regimen']=='Ceftamin']
greatest_capomulin_data = capomulin_data.groupby('Mouse ID').max()['Timepoint']
greatest_ramicane_data = ramicane_data.groupby('Mouse ID').max()['Timepoint']
greatest_infubinol_data = infubinol_data.groupby('Mouse ID').max()['Timepoint']
greatest_ceftamin_data = ceftamin_data.groupby('Mouse ID').max()['Timepoint']

# Merge this group df with the original dataframe to get the tumor volume at the last timepoint
capomulin_merge = pd.merge(greatest_capomulin_data, data, on = ("Mouse ID", "Timepoint"), how = "left")
ramicane_merge = pd.merge(greatest_ramicane_data, data, on = ("Mouse ID", "Timepoint"), how = "left")
infubinol_merge = pd.merge(greatest_infubinol_data, data, on = ("Mouse ID", "Timepoint"), how = "left")
ceftamin_merge = pd.merge(greatest_ceftamin_data, data, on = ("Mouse ID", "Timepoint"), how = "left")


# In[14]:


# Put treatments into a list for for loop (and later for plot labels)
treatments = ['Capomulin', 'Ramicane', 'Infubinol', 'Ceftamin']

# Create empty list to fill with tumor vol data (for plotting)
tumor_vol_data = [vol for vol in merge_vol_data['Tumor Volume (mm3)']]

# Calculate the IQR and quantitatively determine if there are any potential outliers. 
capomulin_tumors = capomulin_merge['Tumor Volume (mm3)']
    
    # Locate the rows which contain mice on each drug and get the tumor volumes
    # add subset  
    quartiles = capomulin_tumors.quantile([.25, .5, .75])
    lower_qt = quartiles[0.25]
    upper_qt =quartiles[0.75]
    iqr_ = upper_qt-lower_qt
    
    print(f"Lower quartile of Capomulin tumors = {lower_qt}")
    print(f"Upper quartile of Capomulin tumors = {upper_qt}")
    print(f"Interquartile range of Capomulin tumors = {iqr_}")
    print(f"The median of Capomulin tumors = {quartiles[0.5]}")
    
    
    # Determine outliers using upper and lower bounds
    lower_bound = lower_qt - (1.5*iqr_)
    upper_bound = upper_qt + (1.5*iqr_)
    print(f"Values below {lower_bound} could be outliers.")
    print(f"Values above {upper_bound} could be outliers.")
    
    


# In[15]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest


# ## Line and Scatter Plots

# In[16]:


# Generate a line plot of tumor volume vs. time point for a mouse treated with Capomulin


# In[17]:


# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and linear regression model 
# for mouse weight and average tumor volume for the Capomulin regimen


# In[ ]:




