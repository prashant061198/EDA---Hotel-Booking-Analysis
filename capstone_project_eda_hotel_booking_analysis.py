# -*- coding: utf-8 -*-
"""Capstone Project EDA - Hotel Booking Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16qbi7nJoaoccXubz9AevAqUsapoAe49Z

```
# This is formatted as code
```

# **Project Name**    - **HOTEL BOOKING ANALYSIS**

##### **Project Type**    - EDA - Hotel Booking Analysis
##### **Contribution**    - Individual
##### **Team Member 1 -**  Prashant Saini

# **Project Summary -**

This project is related to hotel booking and has two hotel descriptions, i.e., city hotel and resort hotel. There are 119390 rows and 32 columns in this dataset. In this section, we divide the data manipulation workflow into three sections, i.e., data collection, data cleaning and manipulation, and exploratory data analysis. First import important libaries such as numpy, pandas, matplotlib for data cleaning and maniuplations. As we get the data collection's first step to find different columns, which is done by coding Head(), Tail(), info(), describe(), columns(), and some other data collection methods, some of the column names are updated here, i.e., hotel, is_canceled, lead_time, arrival_date_year, arrival_date-month, arrival-date-weeknumber, arrival-date-day-of-month, stays_in_weekend_nights, As we progressed, we found the unique value of each column and generated a list in tabular form, as well as checked the dataset type of each column; we discovered that some columns were not accurate data types, which were corrected later in the data cleaning section, and duplicate data items must be removed, as we discovered duplicates equal to 87396, which were later dropped from the dataset. 

Before we can visualise any data from the data set, we have to do some data wrangling. For that, we checked the null value of all the columns.
Also, drop the duplicate values in the dataset, and we can replace missing values with zeros.

Different charts are used for data visualization so that better insights and Business objective is attained.

# **GitHub Link -**

Provide your GitHub Link here.

# **Problem Statement**

**Write Problem Statement Here.**
####1. For this project we will analysing Hotel Booking data. This data set contains booking iformation for a city hotel and a resort hotel, and includes information such as when the booking was made , length of stay , the number of adults , children , or babies, and the number of available parking spaces.

####2.The main objective behind this project is to explore and analyse data to discover important factor that govern the bookings and give insights to hotel management , which can perform _ various campaigns to boost the business and performance.

#### **Define Your Business Objective?**

Answer Here. 
####1. Generate Maximum Hotel Revenue.
####2. High Customer Satisfaction.

# **General Guidelines** : -

1.   Well-structured, formatted, and commented code is required. 
2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits. 
     
     The additional credits will have advantages over other students during Star Student selection.
       
             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
                       without a single error logged. ]

3.   Each and every logic should have proper comments.
4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
        

```
# Chart visualization code
```
            

*   Why did you pick the specific chart?
*   What is/are the insight(s) found from the chart?
* Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

5. You have to create at least 20 logical & meaningful charts having important insights.


[ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule. 

U - Univariate Analysis,

B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)

M - Multivariate Analysis
 ]

# ***Let's Begin !***

## ***1. Know Your Data***

### Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""### Dataset Loading"""

# Load Dataset
from google.colab import drive
drive.mount('/content/drive')

dataset_path = '/content/drive/MyDrive/csv_files/Hotel Bookings.csv'
df = pd.read_csv(dataset_path)

"""### Dataset First View"""

# Dataset First Look
df

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
df.shape # In dataset, there are 32 Columns and 119390 Rows

"""### Dataset Information"""

# Dataset Info
df.info()

"""#### Duplicate Values"""

# Dataset Duplicate Value Count
df.duplicated().value_counts() 

#True means Duplicate data and In our Dataset there are 31994 duplicate values

"""#### Missing Values/Null Values"""

# Missing Values/Null Values Count
df.isnull().sum().sort_values(ascending=False)

# Visualizing the missing values
#Import missingno library to isualizing the missing values
import missingno as msnm 
msnm.bar(df)

"""### What did you know about your dataset?

Answer Here: In this Dataset, ther are following points to be noted as :
####1. There are 32 Columns and 119390 Rows in hotel booking dataset.
####2. In 32 Columns 4 are float dtype, 16 are int64 dtype and 12 are object dtype and memory usage: 29.1+ MB
####3. There are 31994 duplicate values which we can drop in our analysis.
####4. Total Counts of missing and nan values in columns are as follow
####4(a) Children - 4
####4(b) Country - 488
####4(c) Agent - 16340
####4(d) Company - 112593
####5. In datawrangling, we can replace our missing or nan values with zeros(0).
####6. The dataset have 32 variables (Continuous and Categorical) with one identified dependent variable (categorical), which is 'is_cancelled.

## ***2. Understanding Your Variables***
"""

# Dataset Columns
df.columns

"""##### 1. Hotel: Type of hotel i.e., City hotel or Resort Hotel
##### 2. Is_canceled: Canceled (1) or not (0)
##### 3. Lead_time: no. of days before actual arrival in the hotel
##### 4. Arrival_date_year: year of booking (2015, 2016 and 2017)
#####5. Arrival_date_month: month of booking
#####6. Arrival_date_week_number: week number of the year in which booking
#####7.Arrival_date_day_of_month: arrival month date             
#####8. Stays_in_weekend_nights: no. of weekends guest stayed                
#####9. Stays_in_week_nights: no. of week days guest stayed                   
#####10. Adults: Number of adults                                 
#####11. Children: Number of Childrens                               
#####12. Babies: Number of babies                                 
#####13. Meal:   Types of meal bookedi.e., 
            BB – Bed & Breakfast
            HB – only two meals including breakfast meal
            FB – breakfast, lunch, and dinner
#####14. Country: Country of origin                             
#####15. Market_segment: Market Segment Destination
                     TA: Travel agents
                     TO: Tour operators                       
#####16. Distribution_channel:TA/TO                
#####17. Is_repeated_guest: Repeated guest (1) or not (0)                
#####18. Previous_cancellations: Number of previous bookings that were cancelled by the customer prior to the current booking.                 
#####19. Previous_bookings_not_canceled: Number of previous bookings not cancelled by the customer prior to the current booking.        
#####20. Reserved_room_type: Code of room type reserved (A,B,C,D,E,F,G,H,L,P)                     
#####21. Assigned_room_type: Code for the type of room assigned to the booking.                     
#####22. Booking_changes: Count of changes made to booking.                      
#####23. Deposit_type: No Deposit, Non-refund, Refundable.                           
#####24. Agent: ID of the travel agency that made the booking                           
#####25. Company: ID of the travel company that made the booking                            
#####26. Days_in_waiting_list: Number of days in waiting list                   
#####27. Customer_type: Type of customer (Contract, Group, Transient, Transient Party)                          
#####28. adr(Average daily rate): Average daily rates defined by dividing the sum of all lodging transactions by the total number of staying nights.                                    
#####29. Required_car_parking_spaces: If Car parking is required           
#####30. Total_of_special_requests: Number of additional special requests(ex: twin bed or high floor)             
#####31. Reservation_status: Reservation last status(checkout, Canceled)                     
#####32. Reservation_status_date: Date of the specific status

"""

# Dataset Describe
df.describe()

"""### Variables Description

Answer Here: In description, we get the count, mean, standard deviation, minimum, 25%, 50%, 75% and maximum values of each variables

### Check Unique Values for each variable.
"""

# Check Unique Values for each variable.
print(df.apply(lambda col: col.unique()))

"""## 3. ***Data Wrangling***

### Data Wrangling Code
"""

# Creating a copy so as not to disturb original dataset.
df1 = df.copy()

# Drop the duplicates values from dataset
df1.drop_duplicates()

#Replace missing or nan values with zeros
df1['agent'].fillna(0, inplace = True)
df1['company'].fillna(0, inplace = True)
df1['country'].fillna(0, inplace = True)
df1['children'].fillna(0, inplace = True)

#Done with missing values
df1.isna().sum().sort_values(ascending=False)[:6]

#Create two new columns/Variables/Features
df1['Total_Guests'] = df1['adults'] + df1['babies'] + df1['children']
df1['Total_stay'] = df1['stays_in_week_nights'] + df1['stays_in_weekend_nights']

"""### What all manipulations have you done and insights you found?

Answer Here. In this dataset  
####1. following Insights found.

*   Duplicate Values
*   NAN or Missing Values

####2. Following Manipulation and data cleaning done on dataset are



*  Creating a copy so as not to disturb original dataset. 
*  Drop the duplicate values to get the better analysis. 

*   Replace missing or nan values with zeros
*   Create two new columns i.e., Total_Guests, Total_stay


*   Removing rows which contain total guests as Zero

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

#### Chart - 1
"""

# Chart - 1 visualization code
# Enlarging the pie chart
plt.rcParams['figure.figsize'] = 5,5

# Indexing labels. tolist() will convert the index to list for easy manipulation
labels = df1['hotel'].value_counts().index.tolist()

# Value count of sizes
sizes = df1['hotel'].value_counts()

# As the name suggest, explode will determine how much each section is separated from each other 
explode = (0, 0.1)

# Determine colour of pie chart
colors = ['Orange', 'Green']

plt.pie(sizes, explode=explode,labels = labels, colors=colors, autopct='%1.1f%%',startangle=90, textprops={'fontsize': 14})
# autopct allows us to display the percent value using string formatting.
plt.show()

"""##### 1. Why did you pick the specific chart?

Answer Here - To determine which type of hotels are booking the most

##### 2. What is/are the insight(s) found from the chart?

Answer Here. City Hotels are booking the most almost 66% out of 100%.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here - 1. Resort Hotel tend to be on the expensive side and most people will just stick with city hotel.

#### Chart - 2
"""

# Chart - 2 visualization code
sns.countplot (x= 'arrival_date_year', data= df1, hue= 'hotel').set_title ('yearly bookings')

"""##### 1. Why did you pick the specific chart?

Answer Here. To check in which year most booking has done.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. In 2016, City hotel has the highest number of booking

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Bookings across years is higher for city hotel compared to resort hotel and do not increase proportionately over the years.

#### Chart - 3
"""

# Chart - 3 visualization code
# Enlarging the pie chart
plt.rcParams['figure.figsize'] = 5,5

# Indexing labels. tolist() will convert the index to list for easy manipulation
labels = df1['is_repeated_guest'].value_counts().index.tolist()

# Value count of sizes
sizes = df1['is_repeated_guest'].value_counts()

# As the name suggest, explode will determine how much each section is separated from each other 
explode = (0, 0.1)

# Determine colour of pie chart
colors = ['Orange', 'Green']

plt.pie(sizes, explode=explode,labels = labels, colors=colors, autopct='%1.1f%%',startangle=360, textprops={'fontsize': 14})
# autopct allows us to display the percent value using string formatting.
plt.show()

#Repeated Guests(1)
#Non-repeated Guests (0)

"""##### 1. Why did you pick the specific chart?

Answer Here. To check the repeated guests in hotel.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. Only 3.2% guests revisited the hotels. Rest 96.8% guests were new.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Thus retention rate is low. To increase the retention rate hotels focus on providing personalized service, Listen to guest feedback (and ask for it!), Post-Stay: Nurture your guest relationships to bring them back for more.

#### Chart - 4
"""

# Chart - 4 visualization code
plt.rcParams['figure.figsize'] = 7,7

labels = df1['customer_type'].value_counts().index.tolist()

sizes = df1['customer_type'].value_counts()

explode = (0,0.1,0.2,0.2)
colors = ['Blue','Red','cyan','green',]
plt.pie(sizes,explode=explode, labels = labels, colors=colors, autopct='%1.1f%%',startangle=360, textprops={'fontsize': 14} )
plt.show()

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine what types of customer book the hotel most frequently

##### 2. What is/are the insight(s) found from the chart?

Answer Here. Most of the guests were transient type(75.1%) and transient party were 21% and3.4% belongs to group. Remaining guests belong to contract type.


*   Contract — when the booking has an allotment or other type of contract associated to it.


*   Group — when the booking is associated to a group;

*   Transient — when the booking is not part of a group or contract, and is not associated to other transient booking;


*   Transient-party — when the booking is transient, but is associated to at least other transient booking

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Hotels has to focused and provide good services to the transient guests as Transient guests usually are the most profitable ones since the hotel doesn’t have to pay OTA fees.

#### Chart - 5
"""

# Chart - 5 visualization code
y = list(df1.agent.value_counts().head(10))
x = list(df1.agent.value_counts().head(10).index)
sns.barplot(x,y).set_title('Agent ID that made the hotel booking')

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine which Agent ID of the travel agency made the booking

##### 2. What is/are the insight(s) found from the chart?

Answer Here. Agent ID 9 travel agency made the highest booking.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Hotels must maintain a positive relationship with Agent ID 9, as this agency brings them the most profitable business.

#### Chart - 6
"""

# Chart - 6 visualization code
plt.title("Segments wise booking")
sns.countplot(x = "market_segment", data = df1)
plt.xticks(rotation = 90)
plt.show()

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine by which market segment the hotels booked the most.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. Online Travel Agency(TA) has been most frequently to book hotel by the customer.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Yes, it has a positive impact on business because customers book hotels online and hotels use digital advertising through apps such as OYO and Make My Trip to provide special discounts and attract guests.

#### Chart - 7
"""

# Chart - 7 visualization code
plt.title("Most Frequently Meal")
sns.countplot(x = "meal", data = df1)
plt.xticks(rotation = 90)
plt.show()

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine which meal is most preferred by the guests.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. BB (Bed & Breakfast) meal is mostly preferred by the guests

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Hotels should provide complimentary breakfast to guests in order to increase revenue or have a positive impact on business.

#### Chart - 8
"""

# Chart - 8 visualization code
total_guests_country_wise = pd.DataFrame(df1[['country','Total_Guests']])
total_guests_country_wise_df = total_guests_country_wise.groupby(['country'])['Total_Guests'].sum()
total_guests_country_wise_df.sort_values(ascending=False,inplace=True)
top_10 = total_guests_country_wise_df.head(10)

plt.figure(figsize=(12,6))
sns.barplot(top_10.index,top_10).set_title('People from top 10 travelling countries')

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine which country guests booked the hotels most

##### 2. What is/are the insight(s) found from the chart?

Answer Here. Maximum Guests coming from portugal.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. We can do more advertising and can provide attractive offers to portugal guests to enhance the customer volume.

#### Chart - 9
"""

# Chart - 9 visualization code

plt.figure(figsize=(12,8))
sns.barplot(x='arrival_date_month', y = 'adr', hue = 'hotel', data = df1,)
plt.xticks(rotation = 50)
plt.show()

"""##### 1. Why did you pick the specific chart?

Answer Here. In which month the average daily rate is higher

##### 2. What is/are the insight(s) found from the chart?

Answer Here. For resort hotels, the adr is more expensive during june, july and august.
For city Hotels, the adr is more expensive in august, july, june and may.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. In both hotels, the adr is higher in the summer months (June, July, and August), which means guests go on summer vacation and enjoy their holidays with family and friends.

#### Chart - 10
"""

# Chart - 10 visualization code
plt.figure(figsize=(14,7))
sns.countplot(df1['assigned_room_type'], palette='husl')
plt.show()

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine which room reserved the most

##### 2. What is/are the insight(s) found from the chart?

Answer Here. The “A” room type is the most popular among the clients, with 72% of the reservations.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. If "A" rooms are the most popular, hotels must increase the number of "A" rooms while decreasing the number of other types of rooms. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g., overbooking) in this case, the customer may be asked to cancel their booking if he does not get the room he wants.

#### Chart - 11
"""

# Chart - 11 visualization code

df_not_canceled = df1[df1['is_canceled'] == 0]
total_nights = df_not_canceled['stays_in_weekend_nights']+ df_not_canceled['stays_in_week_nights']

plt.figure(figsize=(12,6))
top_5 = total_nights.value_counts().head(8)
plt.xlabel("Number of Nights", size=10)
plt.ylabel("Number of Guests", size=10)
sns.barplot(top_5.index, top_5).set_title("How long Guests stay in hotels")

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine how long guests stay in hotels.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. Most people stay for one, two, or three. More than 60% of guests come under these three options.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. To create positive business impact, hotels provide additional services and special discounts on next bookings to generate more revenues.

#### Chart - 12
"""

# Chart - 12 visualization code
f, ax = plt.subplots(figsize=(8,8))
sns.scatterplot(x='Total_stay',y='adr',hue='hotel', data=df1, ax=ax,)

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine the relation between total stay vs adr (average daily rate).

##### 2. What is/are the insight(s) found from the chart?

Answer Here. As guests stay in the hotel for a longer period of time, they must pay a lower average daily rate.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. As the hotel offers a special discount on booking for customers who stay in the hotel for more than 2-3 days, they must pay a lower ADR.

#### Chart - 13
"""

# Chart - 13 visualization code
average_adr = df1.groupby('hotel')['adr'].mean()
plt.subplots(figsize=(5,5))
average_adr.plot(kind='bar', color = ('g','r')).set_title("Average ADR of Hotel")
plt.ylabel("Average ADR")
plt.xlabel("Hotal Name")

"""##### 1. Why did you pick the specific chart?

Answer Here. To specify the average ADR for both hotels.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. The average ADR of a city hotel is higher than that of resort hotels. so the profit and revenue will be higher for the city hotel.

##### 3. Will the gained insights help creating a positive business impact? 
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here. Here we can do more advertising and offer special services for resort hotels to get more customers, which results in higher profits.

#### Chart - 14 - Correlation Heatmap
"""

# Correlation Heatmap visualization code
plt.subplots(figsize=(21,15))
corr_df1 = df1.corr()
sns.heatmap(data=corr_df1, annot=True)

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine the correlation of following variables in our dataset.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. 
####1. Is_canceled and same_same alloted are negatively correlated. Not getting the same room as per reversed room is not the reason for booking cancellations.
#####2. Lead-time and total stay is positively correlated means more is the stay of guests more will be the lead time.
####3. ADR and total people are highly correlated. That means more the people more will be the average daily rate.
####4. Higher the adr higher the revenue.
####5. is_repeated_guests and previous booking not canceled has stong correlation. May be repeated guests are not more likely to cancel their bookings.

#### Chart - 15 - Pair Plot
"""

# Chart - 15 visualization code

sns.pairplot(data=df1, vars=["lead_time","is_canceled"])

"""##### 1. Why did you pick the specific chart?

Answer Here. To determine the relation between lead time and canceled bokings.

##### 2. What is/are the insight(s) found from the chart?

Answer Here. The number of booking cancellations (1) increases as the lead time increases

## **5. Solution to Business Objective**

#### What do you suggest the client to achieve Business Objective ? 
Explain Briefly.

Answer Here. 
####1. The client has to be more focused on city hotels as a large number of guests book city hotels, which generate more revenue and are more profitable.

####2. Hotels asked their guests to provide feedback on room service, food, and other things that could be useful for hotels to improve upon and provide better customer satisfaction so that the number of repeat guests increases.

# **Conclusion**

Write the conclusion here.
####1. City Hotel seems to be more preferred among travellers and it also generates more revenue & profit.
####2. Most number of bookings are made in July and August as compared rest of the months.
####3. Room Type A is the most preferred room type among travellers.
####4. Most number of bookings are made from Portugal & Great Britain
####5.  Most of the guest stays for 1-4 days in the hotels.
####6. Online Travel Agency(TA) has been most frequently to book hotel by the customer.
####7. Agent ID 9 travel agency made the highest booking.
####8. BB (Bed & Breakfast) meal is mostly preferred by the guests.
####9. Most of the guests were transient type(75.1%) and transient party were 21% and3.4% belongs to group. Remaining guests belong to contract type.
####10. Only 3.2% guests revisited the hotels. Rest 96.8% guests were new

### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
"""