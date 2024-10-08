# -*- coding: utf-8 -*-
"""SeattleAirbnb.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jqddvPbt6wprqcwaDYfF-hQTa99R7pxo

# **Seattle Airbnb Analysis**

## **Business Context**

The Seattle Airbnb dataset provides an opportunity to understand the dynamics of short-term rental properties in Seattle. By analyzing this data, we aim to uncover insights that can help property owners optimize their listings, improve guest satisfaction, and increase revenue. Additionally, this analysis can provide valuable information to potential investors and policymakers.

## **Questions to Analyze**

1. What are the predictors of price?
2. What are the average prices in different neighborhoods?
3. What is the relationship between property type and room type?

# **Business Understanding**

## **Business Objectives**

The objective of this analysis is to understand the factors influencing Airbnb rental prices in Seattle. Specifically, we aim to:
1. Identify the predictors of price to understand what factors significantly impact the pricing of Airbnb listings.
2. Determine the average prices in different neighborhoods to provide insights into how location affects rental prices.
3. Analyze the relationship between property type and available rooms to understand how different combinations influence pricing and availability.

By addressing these questions, we aim to provide actionable insights for property owners, potential investors, and policymakers to optimize their strategies and improve decision-making in the Airbnb market.

# **Data Understanding**

We will begin by importing necessary packages, loading the dataset and examining its structure and contents.
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install pycodestyle pycodestyle_magic
!pip install flake8
# %load_ext pycodestyle_magic

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import r2_score, mean_squared_error
# from collections import Counter
# import seaborn as sns
# import ast
# import matplotlib.pyplot as plt
# %matplotlib inline

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# from google.colab import drive
# 
# # Mount Google Drive
# drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Read the CSV file from Google Drive
# data = pd.read_csv('/content/listings.csv')
# 
# # Display the first few rows of the dataframe
# print(data.head())

"""# **Data Preperation**

We will select the relevant features and prepare the data for analysis.

"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Features for the project
# proj_features = [
#     'summary', 'space', 'description', 'experiences_offered',
#     'neighborhood_overview', 'notes', 'transit', 'host_response_time',
#     'host_response_rate', 'host_acceptance_rate', 'host_listings_count',
#     'host_total_listings_count', 'host_verifications', 'host_has_profile_pic',
#     'host_identity_verified', 'street', 'neighbourhood', 'zipcode',
#     'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms',
#     'beds', 'bed_type', 'amenities', 'square_feet', 'price',
#     'security_deposit', 'cleaning_fee', 'guests_included', 'extra_people',
#     'minimum_nights', 'maximum_nights', 'has_availability', 'availability_30',
#     'availability_60', 'availability_90', 'availability_365',
#     'number_of_reviews', 'first_review', 'last_review', 'review_scores_rating',
#     'review_scores_accuracy', 'review_scores_cleanliness',
#     'review_scores_checkin', 'review_scores_communication',
#     'review_scores_location', 'review_scores_value', 'instant_bookable',
#     'cancellation_policy', 'calculated_host_listings_count',
#     'reviews_per_month'
# ]
# 
# # Select the relevant features
# df = data[proj_features]
# 
# # Display the shape of the dataframe
# print(df.shape)

"""# **Assessing Data Quality**

To identify the predictors of price, we will create a new dataframe with selected features, clean and encode the data, develop a linear regression model, and evaluate its performance.


"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Remove the columns with more than 50% missing values
# df = df[df.columns[df.isnull().sum() < .5*df.shape[0]]]
# 
# # Remove rows with missing 'neighbourhood'
# df = df.dropna(subset=['neighbourhood'])
# 
# # Display the shape of the dataframe after cleaning
# df.shape
# 
# # Prepare the categorical and numerical columns
# df.info()
# 
# # Identify categorical and numerical columns
# cat_vars = list(df.select_dtypes(include='object'))
# num_vars = list(df.select_dtypes(include=['float64', 'int64']))
# 
# # Print the numerical variables
# print(num_vars)
# 
# # Remove the rows with missing numeric values
# df = df.dropna(subset=num_vars)

"""There are many columns that are considered as objects, yet some of them should be treated as integer or float (especially those price columns). This is a type change problem that I will handle later. For now, I would like to know about the number of missing values and the number of unique inputs in each column.

# **Creating the 'num_amenities' Column**

We will create a new column named num_amenities to show the number of amenities available at each listing. This column will help us quantify the number of amenities, which could be a significant factor in determining the rental price.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# def count_amenities(amenities_str):
#     """
#     Count the number of amenities in the given string.
# 
#     This function takes a string of amenities, removes the curly braces,
#     splits the string by commas, and returns the count of amenities.
# 
#     Parameters:
#     amenities_str (str): A string containing a list of amenities enclosed
#     in curly braces.
# 
#     Returns:
#     int: The number of amenities.
#     """
#     # Remove curly braces and split by comma
#     amenities_list = amenities_str.strip('{}').split(',')
#     # Find the number of amenities
#     return len(amenities_list)
# 
# 
# # Create a column with the number of amenities
# df['num_amenities'] = df['amenities'].apply(count_amenities)

"""# **Data Analysis**



## **Question 1: What are the predictors of price?**
We will identify the predictors of price using a linear regression model.To understand the relationships between different numerical features in the dataset, we will compute the correlation matrix and visualize it using a heatmap. This will help us identify which features are strongly correlated with each other and with the target variable, price.
The correlation matrix provides a numerical summary of relationships between numerical features, with coefficients ranging from -1 to 1. A coefficient close to 1 indicates a strong positive correlation, -1 indicates a strong negative correlation, and 0 indicates no correlation. The heatmap visualizes these correlations using colors: dark colors represent strong positive correlations, light colors represent strong negative correlations, and neutral colors represent weak or no correlations. This visualization helps us quickly identify significant feature relationships and guide feature selection for predictive models.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Clean the 'price' column
# df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
# 
# # Compute the correlation matrix
# corr_matrix = df[num_vars].corr()
# 
# # Plot the heatmap
# plt.figure(figsize=(15, 12))
# heatmap = sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
#                       linewidths=0.5)
# plt.title('Correlation Heatmap of Numerical Features')
# plt.show()

"""# **Model Implementation and Evaluation**

We will develop a Linear Regression model to identify the key features that determine the price. This involves creating a new dataset with selected features, cleaning the data, encoding categorical values, developing and evaluating the model, and selecting the most significant features.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Create a new dataframe including the features to predict the price
# prc_df = df[['accommodates', 'bathrooms', 'bedrooms', 'beds',
#              'guests_included', 'num_amenities', 'zipcode', 'bed_type',
#              'price']]
# 
# # Group zipcodes with fewer than 100 members into 'Other' category
# zipcode_counts = prc_df['zipcode'].value_counts()
# zipcodes_to_replace = zipcode_counts[zipcode_counts < 100].index
# prc_df['zipcode'] = prc_df['zipcode'].apply(
#     lambda x: 'Other' if x in zipcodes_to_replace else x
# )
# 
# # Drop the rows with missing zipcodes
# prc_df.dropna(subset=['zipcode'], inplace=True)
# 
# # Encode the categorical variables
# prc_df_encoded = pd.get_dummies(prc_df, columns=['zipcode', 'bed_type'],
#                                 drop_first=True)
# 
# # Create the response and feature datasets
# X = prc_df_encoded.drop(['price'], axis=1)
# y = prc_df_encoded['price']
# 
# # Bin the target variable
# y_binned = pd.qcut(y, q=10, labels=False)
# 
# # Split the data into training and testing sets with stratified sampling
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
#                                                     random_state=42,
#                                                     stratify=y_binned)
# 
# # Train the linear model
# model = LinearRegression()
# model.fit(X_train, y_train)
# 
# # Predict using the test set
# y_pred = model.predict(X_test)
# 
# # Evaluate the model
# r2 = r2_score(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# 
# print(f'R^2 Score: {r2}')
# print(f'Mean Squared Error: {mse}')
# 
# # Retrieve and display coefficients
# coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
# print(coefficients.sort_values(by='Coefficient', ascending=False))
# 
# # Plot coefficients
# plt.figure(figsize=(10, 8))
# coefficients.sort_values(by='Coefficient', ascending=True).plot(
#     kind='barh', legend=False
# )
# plt.title('Feature Importance by Coefficient')
# plt.xlabel('Coefficient Value')
# plt.ylabel('Feature')
# plt.show()

"""# **Summary of the findings:**
##Coefficient Interpretation

The coefficients obtained from the linear regression model provide valuable insights into how different features impact the price of Airbnb listings. These insights can be categorized into two main groups: positive coefficients and negative coefficients.

### Positive Coefficients

Features with positive coefficients are associated with an increase in the price of Airbnb listings. The magnitude of these coefficients indicates the strength of their impact on the price. Key features with positive coefficients include:

1. **Bedrooms (31.745141)**:
   - Listings with more bedrooms tend to have significantly higher prices. This is logical as properties with more bedrooms can accommodate larger groups and offer more space and privacy.

2. **Bathrooms (21.402561)**:
   - An increase in the number of bathrooms is positively correlated with higher prices. More bathrooms improve convenience and comfort, especially for larger groups or families.

3. **Bed Type - Real Bed (25.249570)**:
   - Listings that offer a real bed are priced higher than those without. Real beds are generally more comfortable and preferred by guests, thus commanding higher prices.

4. **Bed Type - Pull-out Sofa (19.884977) and Futon (16.739441)**:
   - Listings with pull-out sofas and futons also command higher prices. These types of beds provide additional flexibility in accommodating guests.

5. **Zipcodes 98109, 98121, 98119**:
   - Properties located in these zipcodes are associated with higher prices, suggesting that these are desirable locations.

6. **Accommodates (12.323478)**:
   - The number of guests a property can accommodate is positively correlated with price. Larger properties that can host more guests naturally charge higher rates.

7. **Guests Included (5.248445)**:
    - The number of guests included in the base price also positively impacts the price. Listings that include more guests in the base price can justify higher pricing.

8. **Beds (0.505968)**:
    - The number of beds, although having a smaller impact, still positively correlates with the price. More beds can mean more flexibility in guest accommodation.

9. **Number of Amenities (0.339216)**:
    - A higher number of amenities slightly increases the price. This reflects that more amenities add value to the listing, making it more attractive to potential guests.

### Negative Coefficients

Features with negative coefficients are associated with a decrease in the price of Airbnb listings. The magnitude of these coefficients indicates the strength of their impact on reducing the price. Key features with negative coefficients include:

1. **Bed Type - Couch (-16.908636)**:
   - Listings that offer a couch as a bed type are associated with lower prices. Couches are likely seen as less comfortable and desirable compared to other bed types.

2. **Other Zipcodes**:
   - Several other zipcodes (98102, 98122, 98112, 98107, etc.) are associated with lower prices, indicating that properties in these areas are less in demand compared to those in higher-priced zipcodes.

### Overall Insights

- **Desirable Features**: More bedrooms, bathrooms, real beds, and specific zipcodes (98109, 98121, 98119) significantly increase the price of Airbnb listings.
- **Less Desirable Features**: Certain zipcodes (98102, 98122, 98112, etc.) and couch bed types are associated with lower prices.
- **Value-Adding Features**: While the number of beds and amenities positively impact the price, their effect is smaller compared to major factors like bedrooms and location.

These insights can help property owners and managers understand what features to highlight or improve in their listings to optimize pricing. It also aids in market analysis and strategic decisions regarding property investments and enhancements.

# **Question 2: What are the average prices in different neighborhoods?**

We will calculate and visualize the average prices in different neighborhoods.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Calculate average price by neighborhood
# zipcode_price_df = prc_df.groupby('zipcode')['price'].mean().reset_index()
# 
# # Sort by average price
# zipcode_price_df = zipcode_price_df.sort_values(by='price', ascending=False)
# 
# # Plot the results
# plt.figure(figsize=(14, 8))
# sns.barplot(data=zipcode_price_df, x='price', y='zipcode', palette='viridis')
# plt.title('Average Price by Neighborhood')
# plt.xlabel('Average Price')
# plt.ylabel('Neighborhood')
# plt.show()
# 
# # Select the 5 most expensive and 5 cheapest zip codes
# top_5_expensive = zipcode_price_df.head(5)
# top_5_cheapest = zipcode_price_df.tail(5)
# 
# # Combine the two dataframes
# top_bottom_zipcodes = pd.concat([top_5_expensive, top_5_cheapest])
# 
# # Plot the results
# plt.figure(figsize=(12, 6))
# sns.barplot(data=top_bottom_zipcodes, x='price', y='zipcode',
#             palette='coolwarm')
# plt.title('5 Most Expensive and 5 Cheapest Zip Codes')
# plt.xlabel('Average Price')
# plt.ylabel('Zip Code')
# plt.show()

"""# **Question 3: What is the relationship between property type and room type?**

We will analyze the relationship between property type and available rooms.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%pycodestyle
# # Create a cross-tabulation of property type and room type
# property_room_crosstab = pd.crosstab(df['property_type'], df['room_type'])
# 
# # Plot the heatmap
# plt.figure(figsize=(14, 10))
# sns.heatmap(property_room_crosstab, annot=True, fmt='d', cmap='viridis',
#             linewidths=.5)
# plt.title('Relationship between Property Type and Room Type')
# plt.xlabel('Room Type')
# plt.ylabel('Property Type')
# plt.show()
#

"""# **Summary of the Crosstab: Relationship between Property Type and Room Type**

The heatmap visualization illustrates the distribution of room types across different property types in Airbnb listings. Key insights include:

1. **Apartments**:
   - **Entire home/apt**: The most common combination with 1080 listings, indicating a strong preference for renting out entire apartments.
   - **Private room**: Less common with 163 listings.
   - **Shared room**: Rare with only 31 listings.

2. **Houses**:
   - **Entire home/apt**: A significant number of listings (694), showing that many houses are rented out entirely.
   - **Private room**: Also popular with 580 listings, suggesting many hosts offer rooms within their homes.
   - **Shared room**: Less common with 41 listings.

3. **Bed & Breakfast**:
   - **Private room**: Predominantly listed as private rooms (23 listings), which is typical for this property type.
   - **Entire home/apt**: Rare with only 2 listings.

4. **Condos**:
   - **Entire home/apt**: Most common with 48 listings.
   - **Private room**: Less frequent with 14 listings.
   - **Shared room**: Very rare with just 1 listing.

5. **Lofts and Townhouses**:
   - **Lofts**: Primarily listed as entire homes (23 listings) with a few private rooms (5 listings).
   - **Townhouses**: Balanced distribution between entire homes (30 listings) and private rooms (39 listings), with very few shared rooms (2 listings).

6. **Specialty Properties**:
   - **Bungalows, Cabins, Camper/RVs, Chalets, Tents, Treehouses, Yurts**: These have few listings overall but offer unique accommodations mostly as entire homes or private rooms.
   - **Dorms**: Exclusively listed as shared rooms (2 listings).

### Overall Observations:

1. **Dominance of Entire Home/Apt Listings**:
   - Entire homes/apartments are the most prevalent room type across various property types, especially for apartments and houses, indicating a preference among hosts to rent out entire properties.

2. **Significance of Private Rooms**:
   - Private rooms are also a popular choice, particularly in houses and townhouses, showing that many hosts are willing to share their living spaces.

3. **Limited Shared Rooms**:
   - Shared rooms are the least common across almost all property types, suggesting they are less preferred by both hosts and guests.

4. **Niche Market for Specialty Properties**:
   - Properties like Bed & Breakfasts, Boats, Bungalows, and Treehouses have fewer listings but cater to specific guest preferences looking for unique stays.

This analysis provides a clear understanding of how different property types are utilized in Airbnb listings, highlighting host preferences and potential guest demands for various accommodation types.

# **Conclusion**

This analysis provided insights into the factors influencing Airbnb rental prices in Seattle, the average prices in different neighborhoods, and the relationship between property type and room type. These insights can help property owners optimize their listings and make informed decisions regarding their rental properties.
"""