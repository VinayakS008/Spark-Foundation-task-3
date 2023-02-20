#!/usr/bin/env python
# coding: utf-8

# # GRIP - The Sparks Foundation.

# # Data Science and Business Analytics Internship.

# Task 3:Explaratory Data analysis- Sample Superstore Dataset.
# 
# Author : Sapkal Vinayak Dadaso

# # ---------------------------------------------------------------------------------------------------------------

# In[1]:


# Importing the required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("C:/Users/Vinayak/Downloads/SampleSuperstore.csv")
data.head()


# # Data pre-processing

# In[3]:


data.shape


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data.describe()


# In[7]:


data.dtypes


# # Cheaking the duplication in data

# In[8]:


data.duplicated().sum()


# In[9]:


data.drop_duplicates(inplace=True)


# In[10]:


data.head()


# In[11]:


data.nunique()


# In[12]:


data.columns


# # Deleting the Variable

# In[14]:


col=['Postal Code']
data=data.drop(columns=col,axis=1)


# Continuous Variables
# 
# These are numerical columns like Postal Code,Sales,Quantity,Discount,Profit etc
# 
# Categorical Variables
# 
# These are columns categories like Ship Mode,Segment, Country,State etc.

# In[16]:


cont_cols=['Sales','Quantity','Discount','Profit'] # For Continuous Columns
cat_cols=['Ship Mode','Segment','Country','City','State','Region','Category','Sub-Category']# Categorical Columns
len(set(cont_cols))+len(set(cat_cols))


# In[18]:


data.select_dtypes(include='number')


# In[19]:


data.select_dtypes(exclude='number')


# ## 1) Univariate Analysis

# *Analyzing one variable.
# 
# *The displot represents the univariate distribution of data distribution of a variable against the density distribution

# In[20]:


for i in cont_cols:
    plt.figure(figsize=(10,5))
    plt.style.use("tableau-colorblind10")
    sns.distplot(data[i], bins=30, color="r")
    plt.xlabel(i)
    plt.title("Frequency Distribution of"+i)
    plt.xticks(rotation=45)
    plt.show()


# ## 2) Countplot

# It is used to see the Count wise distribution of a categorical entities

# In[21]:


for i in cat_cols:
    plt.figure(figsize=(8,5))
    sns.countplot(data[i])
    plt.xlabel(i)
    plt.title("Count Distribution of"+i)
    plt.xticks(rotation=0)
    plt.grid(True)
    plt.show()


# ## 3)Boxplot

# > It is used to see quartile wise distribution for any continuous variable
# 
# > It is also used to see the whether outliers are present in the data or not
# 
# > It is used to see quartile wise distribution for any continuous variable against a categorical variable
# 
# left line of box : 25th Percentile(Q1)
# 
# Right line of box : 75th Percentile(Q3)
# 
# Middle line of box : 50th Percentile(Q2)
# 
# Inner Quartile Range : IQR : Q3-Q1
# 
# Upper (Emperical Relationship): Q3+1.5(Q3-Q1) : Q3+1.5(IQR)
# 
# Lower (Emperical Relationship): Q1-1.5(Q3-Q1) : Q1-1.5(IQR)

# In[22]:


for i in cont_cols:
    plt.figure(figsize=(10,5))
    sns.boxplot(data[i])
    plt.xlabel(i)
    plt.title("Statistical Distribution of"+i)
    plt.xticks(rotation=0)
    plt.show()


# ## 4) Bivariate Analysis

# Analyzing two variables

# ### Scatterplot

# It is used to see the relationship between two Continuous variables¶

# In[23]:


for x in cont_cols:
    for y in cont_cols:
        plt.figure(figsize=(10,5))
        if x!=y:
           sns.scatterplot(data[x],data[y],color="r")
           plt.xlabel(x)
           plt.title("Relationship of "+x+" Vs +y")
           plt.xticks(rotation=0)
           plt.grid(True)
           plt.show()


# # 5)Line Graph

# In[24]:


plt.figure(figsize=(10,4))
sns.lineplot('Discount','Profit',data=data,color='r',label='Discount')
plt.title('Discount Vs Profit')
plt.legend()
plt.show()


# From the above lineplot it is seen that the discount decreases then profit also fall down.

# # 6)Pair Plot

# A pairplot a pairwise relationships in a dataset.The pairplot function creates a grid of Axes such that each variable in data will by shared in the y-axis across a single row and in the x-axis across a single column.

# In[25]:


g=sns.pairplot(data[cont_cols], height=2.5,diag_kind='kde')
g.fig.suptitle("pair Plot for Continuous variables")


# From above pairplot it is seen that more sale does not get more profit it depends on the discount. and when sale is high with low discount it gives us more profit.

# # 7)Multivariate Analysis

# Analysing multiple variables

# ## Heat Map

# A heatmap is a matrix representation of the variables which is colored based on the intensity of the value.
# 
# It provide us with an easy tool to understand the correlation between two entities.

# In[26]:


#Correlation Between Variables.
data[cont_cols].corr()


# In[27]:


plt.figure(figsize=(10,6))
sns.heatmap(data[cont_cols].corr(),annot=True,cmap='Greens')


# It is seen that there is weak correlation between the variables.i.e.There is no strong relationship between variables.

# ## Pie Diagram

# In[28]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])

ax.pie(data['Category'].value_counts(),
       labels=["Office Supplies","Furniture","Technology"],
       autopct='%1.2f%%',
       frame=True,
       textprops=dict(color="black",size=12))

ax.axis('equal')
plt.title('Category',
          loc='left',
          color='black',
          fontsize='10')
plt.show()


# In[29]:


data["Ship Mode"].value_counts()


# In[30]:


sns.countplot(x=data["Ship Mode"])


# In[31]:


data["Segment"].value_counts()


# In[32]:


sns.countplot(x=data["Segment"])


# In[33]:


sns.countplot(x=data["Category"])


# From above we can say that the office supply category has highest ratio.

# # 8)To check the Statewise profit

# In[34]:


profit=data.groupby(["State"])["Profit"].sum().nlargest(20)
profit


# In[35]:


plt.figure(figsize=(10,5))
profit.plot.bar()


# In[36]:


data1=data.groupby("Region")[["Sales","Profit"]].sum().sort_values(by="Sales",ascending=False)
data1[:].plot.bar(color=["Red","Green"],figsize=(6,5))
plt.title("profit & loss in Region")
plt.show()


# In the West region it get highest profit.
# 
# . There are three cities are important in profit California, Newyork and Washington.
# 
# . In the central and south region profit is minimum.
# 
# > We conclude that the California and Newyork have more work and we need to give attention on the central and South region because they give us highest sale with genetating loss. and office supply category have highest supply.
