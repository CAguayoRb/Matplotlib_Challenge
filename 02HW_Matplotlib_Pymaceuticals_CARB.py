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

# In[15]:


get_ipython().system('pip install pandas')


# In[24]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

# Study data files
mouse_metadata_path = "Mouse_metadata.csv"
study_results_path = "Study_results.csv"

# Read the mouse data and the study results
mouse_metadata_df = pd.read_csv(mouse_metadata_path)
study_results_df = pd.read_csv(study_results_path)

# Combine the data into a single dataset.
#study_results = study_results.dropna(axis=1)
#merge_mouse_study = mouse_methdata.merge(study_results, on = 'Mouse ID')
merge_mouse_study_df = pd.merge(mouse_metadata_df, study_results_df, on="Mouse ID")
merge_mouse_study_df.head()

# Display the data table for preview
#merge_mouse_study_df.to_csv("output.csv", index=False)
#merge_mouse_study_df.to_csv.head()


# In[27]:


# Checking the number of mice.

print (f'Number of mice:', merge_mouse_study_df['Mouse ID'].nunique())


# In[29]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
#data['Timepoint'] = merge_mouse_study_df['Timepoint'].astype(str)
#data['Duplicate ID'] = merge_mouse_study_df['Timepoint'].str.cat(data['Mouse ID'],sep = "")
#data.head


# In[4]:


# Optional: Get all the data for the duplicate mouse ID. 
data['Duplicate ID'].nunique()


# In[5]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.
data.drop_duplicates(subset = ['Duplicate ID']), keep = False, inplace = True)
data


# In[6]:


# Checking the number of mice in the clean DataFrame.
print (f'Number of mice:', merge_mouse_study_df['Mouse ID'].nunique())


# ## Summary Statistics

# In[60]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.
#data_1 = merge_mouse_study_df

mean_data=merge_mouse_study_df.groupby(['Drug Regimen'])[['Tumor Volume']].mean()
re_mean_data=mean_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Mean'}, axis = 'columns')
med_data=merge_mouse_study_df.groupby(['Drug Regimen'])['Tumor Volume'].median()
re_medium_data=med_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Median'}, axis = 'columns')
var_data=merge_mouse_study_df.groupby(['Drug Regimen'])[['Tumor Volume (mm3)']].var()
re_var_data=var_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Variance'}, axis = 'columns')
std_data=merge_mouse_study_df.groupby(['Drug Regimen'])[['Tumor Volume']].std()
re_std_data=std_data.rename({'Tumor Volume (mm3)':'Tumor Volume - Standard Deviation'}, axis = 'columns')
sem_data=merge_mouse_study_df.groupby(['Drug Regimen'])[['Tumor Volume']].sem()
re_sem_data=sem_data1.rename({'Tumor Volume (mm3)':'Tumor Volume - SEM'}, axis = 'columns')

#Create the table:
#drugregimen_tumorvol=


drugregimen_tumorvol.head()


# In[8]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen



# Using the aggregation method, produce the same summary statistics in a single line.



# ## Bar and Pie Charts

# In[50]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pandas.
drug_groups = merge_mouse_study_df.groupby('Drug Regimen')

measurments_ = drug_groups['Mouse ID'].count()
measurments_

#or 

#merge_mouse_study_df['Mouse ID'].value_counts()

measurments_ = measurments_.drop(measurments_.index[3])

measurments_chart = measurments_.plot(kind="bar", title="Measurments of Drug Regimens")
measurments_chart.set_xlabel("Drug Regimen")
measurments_chart.set_ylabel("Total Number of Measurments")

plt.show()
plt.tight_layout()


# In[ ]:





# In[53]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using using pyplot.
drug_groups = merge_mouse_study_df.groupby('Drug Regimen')
measurments_ = drug_groups['Mouse ID'].count()
measurments_

#Data Set
x_axis = np.arrange(0, len(9))
tick_locations = [x for x in x_axis]

#plt.bar=(drug_groups, measurments_)
plt.title = ('Measurments of Drug Regimens')
plt.xlabel = ('Drug Regimen')
plt.ylabel = ('Total Number of Measurments')

plt.xlim(-0.75, len(drug_groups)- 1)
plt.ylim(0, max(measurments_) + 1)

plt.bar(x_axis, measurments_, facecolor="red", alpha = 0.75, align = "center")
plt.xticks(tick_locations, drug_groups)
plt.show()


# In[11]:


# Generate a pie plot showing the distribution of female versus male mice using pandas.

mouse_sex = 
sex_count =
mf_pie = merge_mouse_study.plot(kind="pie", y='Sex', title=("Female and Male Measurments"))
mf_pie.set_ylabel("Sex")


plt.axis("equal")
plt.show()


# In[61]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot

plt.pie(merge_mouse_study_df.plot(['Sex']))
df = merge_mouse_study_df

df.plot.pie(y='Sex')


# ## Quartiles, Outliers and Boxplots

# In[43]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

data['Timepoint'] =  merge_mouse_study_df['Timepoint'].astype(float)
#data =  merge_mouse_study_df['Timepoint'].astype(float)

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


# In[42]:


# Put treatments into a list for for loop (and later for plot labels)
treatments = ['Capomulin', 'Ramicane', 'Infubinol', 'Ceftamin']

# Create empty list to fill with tumor vol data (for plotting)
tumor_vol_data = [vol for vol in merge_mouse_study_df['Tumor Volume (mm3)']]

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


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest.
#means = [s.MEDV.mean() for s in samples]

tumor_vol_data = 



fig, ax1 = plt.subplots()
ax1.set_xlim(0, len(means)+1)
ax1.set_xlabel("Capomulin","Ramicane", "Infubinol", "Ceftamin") #put the names of the meds. 
ax.set_ylabel("Final Tumor Volume (mm3)")

plt.boxplot(tumor_vol_data, showmeans=True)
plt.grid()
plt.show()


# ## Line and Scatter Plots

# In[16]:


# Generate a line plot of tumor volume vs. time point for a mouse treated with Capomulin.
days = [0, 10, 20, 30, 40]

plt.plot(days, capomulin_tumor, color="blue")

plt.legend(loc="best")

plt.title("Capomulin treatment of mouse I509")
plt.xlabel("Years")
plt.xticks(np.arange(min(days), max(days)+1, 1.0))
plt.ylabel("Tumor Volume (mm3)")

plt.show()


# In[17]:


# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen

x_values = merge_mouse_study["Weight (g)"] #Weight
y_values = merge_mpuse_study[""] #Avg tumor volume WHERE IS AVG TUMOR VOLUME?
plt.scatter(merge_mouse_study.iloc[:,5],merge_mouse_study.iloc[:,7]) #Find correct name of merge of datas.
plt.xlabel('Weight (g)')
plt.ylabel('Average Tumor Volume (mm3)')
plt.show()


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and linear regression model.
# for mouse weight and average tumor volume for the Capomulin regimen.

print(f"The correlation between mouse weight and the average tumor volume is: {round()})

x_values = merge_mouse_study["Weight (g)"] #Weight
y_values = merge_mpuse_study[""] #Avg tumor volume WHERE IS AVG TUMOR VOLUME?
      (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
regress_values = x_values * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + "x +" +str(round(incept,2))
plt.scatter(x_values, y_values)
plt.plot(x_values, regress_values, "r-")
plt.annotate(line_eq,(6,10), fontsize = 15, color="red")
plt.xlabel('Weight (g)')
plt.ylabel('Average Tumor Volume (mm3)')
plt.show()


# In[ ]:




