# UdacityProjects
Includes projects of Udacity Data Scientists nano program

# Seattle Airbnb Analysis

## Project Motivation

This project aims to analyze Airbnb listings in Seattle to uncover insights about pricing, room types, property types, and amenities. By understanding these factors, we can provide recommendations for potential hosts on how to optimize their listings and for guests on how to find the best accommodations. This analysis also aims to provide a comprehensive understanding of the dynamics of Airbnb listings in Seattle.

## Libraries Used

- `numpy` - For numerical computations
- `pandas` - For data manipulation and analysis
- `matplotlib` - For data visualization
- `seaborn` - For statistical data visualization
- `scikit-learn` - For machine learning and data modeling

## Repository Files

- `SeattleAirbnb.ipynb`: Jupyter Notebook containing the complete analysis and visualizations.
- `SeattleAirbnb.py`: Python script for the analysis.
- `data/`: Directory containing the dataset used for the analysis (`listings.csv`).

## Summary of the Results

### Analysis of Property Type and Room Type

A heatmap was generated to visualize the relationship between property type and room type. Key observations include:

- **Apartments**: Predominantly listed as entire homes/apartments (1080 listings), with fewer private rooms (163) and shared rooms (31).
- **Houses**: A significant number of listings as entire homes/apartments (694) and private rooms (580), with fewer shared rooms (41).
- **Bed & Breakfast**: Mostly listed as private rooms (23), with very few entire homes/apartments (2).

### Analysis of Average Prices

The average price was calculated for different property types and room types:

- **Property Types**: Houses and apartments tend to have higher average prices compared to other property types.
- **Room Types**: Entire homes/apartments generally command higher prices compared to private and shared rooms.

### Analysis of Amenities

A bar plot was created to visualize the top 20 most common amenities in the listings. Key amenities include:

- **Common Amenities**: TV, Wireless Internet, Kitchen, Heating, Washer, Dryer, and Essentials are among the most frequently offered amenities.
- **Specialized Amenities**: Some listings offer unique amenities like Indoor Fireplace and Cable TV.

### Relationship Between Accommodations and Price

A scatter plot was generated to analyze the impact of the number of accommodations on the price. There is a positive correlation, indicating that listings accommodating more guests tend to have higher prices.

## Necessary Acknowledgments

- The dataset used in this project is provided by [kaggle](https://www.kaggle.com/datasets/airbnb/seattle/data).
- Special thanks to the Udacity Data Science program for providing the framework and guidance for this project.



