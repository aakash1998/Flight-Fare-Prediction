
# Flight Fare Prediction

## Problem Statement

This project is about creating an app using machine learning approch , which predicts the price of the flight using the inputs like the departure date and time , arrival date and time , source city and the destination city , the number of stops and finally the airline in which they would like to travel. Using all these features the price of the flight will be predicted. 

## Approch

- **Data Exploration** : Getting an idea about the data , type of features , number of categorical and numerica variables and creating plots to get a better understanding of the data.
- **Feature Engineering** : Converting the categorical variables into numeric variables using *One hot encoding* and *Label Encoder*.
- **Feature Scaling** : Transforming the data into Gaussian Normal Distribution.
- **Feature Selection** : Selecting the important features and discarding the features which have a high VIF(Variance Inflation Factor) value.
- **Model Training and Testing** : Multiple regression models are being built using different ML algorithms and the one with best accuracy is selected.
- **Hyperparameter Tunning** : Random Forest Regressor was selected for predicting the outcome , and it was tunned using differnt parameters to get a better accuracy.
- **Web App Development** : A web app is made using flask ,python and gunicorn.
- **Deployment** : Finally the app is being deployed on multiple cloud platforms.

## Deployment Link

Flight Fare Prediction Web App : (https://flightfarepredicton.herokuapp.com/)

## Technologies Used 

- python
- sklearn
- flask
- html 
- css
- bootstrap
- pandas
- numpy
- matplotlib
- seaborn
- gunicorn
- heroku
