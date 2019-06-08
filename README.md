# SQL databse for USDA food description data
Are you interested in getting to know more about food we have everyday?

[United States Department of Agriculture](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/nutrient-data-laboratory/docs/usda-national-nutrient-database-for-standard-reference/) provides great resources about nutritions of daily food.

The importdata.py establishs a SQL database (food.db) for USDA data (FOOD_DES.txt)
The food_query.py takes SQL commends to make queries from the database

## SQL query example
An example code to make a query: $python food_query.py "N_Factor > 6.25"
This will return to the food with N_facotr larger than 6.25. Please refer to SR-Legacy_Doc.pdf for more information about the N_facotr and other variables in this database.

## References:
1. US Department of Agriculture, Agricultural Research Service, Nutrient Data Laboratory. USDA National Nutrient Database for Standard Reference, Legacy. Version Current:  April 2018.  Internet:  /nea/bhnrc/ndl
2. Beginning Python from novice to professional. By Magnus Lie Hetland
