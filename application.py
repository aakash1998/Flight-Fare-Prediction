import pandas as pd
from flask import request, render_template, Flask
from flask_cors import cross_origin
import pickle
import sklearn
from logger_class import getLog
import pandas

logger = getLog("prediction.py")


logger.info("Initializaing the flask app")
application = Flask(__name__) #defining the app
logger.info("Loading the Final Model")
model = open('final_model_flight.pickle' , 'rb') #loading the model
rf = pickle.load(model)

@application.route("/", methods=["GET", "POST"])
@cross_origin()
def home():
    logger.info("Home Page Route")
    return render_template("home.html")



@application.route("/predict", methods=["GET", "POST"])
@cross_origin()

def predict():
    try:

        if request.method == "POST":

            # Departure
            date_dep = request.form['Dep_Time']
            logger.info("Reading the departure time"  + str(date_dep))
            # Deperature Day and Month
            Journey_Day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
            logger.info("Reding the Journey Day" + str(Journey_Day))
            Journey_Month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
            logger.info("Reading the Journey Month" + str(Journey_Month))
            # Deperature Time
            Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
            logger.info("Reading the departure hour" + str(Dep_hour))
            Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
            logger.info("Reading the departure minute" + str(Dep_min))
            # Arrival
            date_arr = request.form['Arrival_Time']
            logger.info("Reading the arrival date" + str(date_arr))
            # Arrival Time
            Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
            logger.info("Reading the arrival hour" + str(Arrival_hour))
            Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
            logger.info("Reading the arrival min" + str(Arrival_min))
            # Duration of Flight
            dur_hour = abs(Arrival_hour - Dep_hour)
            logger.info("Calculating the duration in hours" + str(dur_hour))
            dur_min = abs(Arrival_min - Dep_min)
            logger.info("Calculating the duration in minutes" + str(dur_min))

            # Total Stops
            Total_stops = int(request.form['stops'])
            logger.info("Reading the total stops" + str(Total_stops))
            # Airline Selection
            #Air Asia = 0
            airline = request.form['airline']
            logger.info("Reading the airline name" + str(airline))
            if airline == 'IndiGo':
                IndiGo = 1
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'Air India':
                IndiGo = 0
                Air_India = 1
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'Jet Airways':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 1
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'SpiceJet':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 1
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'Multiple carriers':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 1
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'GoAir':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 1
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'Vistara':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 1
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0


            elif airline == 'Vistara Premium economy':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 1
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'Jet Airways Business':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 1
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            elif airline == 'Multiple carriers Premium economy':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business =0
                Multiple_carriers_Premium_economy = 1
                Trujet = 0

            elif airline == 'Trujet':
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                #Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 1

            else:
                IndiGo = 0
                Air_India = 0
                Jet_Airways = 0
                SpiceJet = 0
                Multiple_carriers = 0
                GoAir = 0
                Vistara = 0
                # Air_Asia = 0
                Vistara_Premium_economy = 0
                Jet_Airways_Business = 0
                Multiple_carriers_Premium_economy = 0
                Trujet = 0

            # Source
            #Banglore = 0
            source = request.form['Source']
            logger.info("Reading the source" + str(source))
            if(source == 'Kolkata'):
                s_Kolkata = 1
                s_Delhi = 0
                s_Chennai = 0
                s_Mumbai = 0

            elif(source == 'Delhi'):
                s_Kolkata = 0
                s_Delhi = 1
                s_Chennai = 0
                s_Mumbai = 0

            elif(source == 'Chennai'):
                s_Kolkata = 0
                s_Delhi = 0
                s_Chennai = 1
                s_Mumbai = 0

            elif(source == 'Mumbai'):
                s_Kolkata = 0
                s_Delhi = 0
                s_Chennai = 0
                s_Mumbai = 1

            else:
                s_Kolkata = 0
                s_Delhi = 0
                s_Chennai = 0
                s_Mumbai = 0

            # Destination
            #Banglore = 0
            destination = request.form['Destination']
            logger.info("Reading the destination" + str(destination))
            if(destination == 'New Delhi'):
                d_New_Delhi = 1
                d_Kolkata = 0
                d_Cochin = 0
                d_Hyderabad = 0
                d_Delhi = 0

            elif(destination == 'Kolkata'):
                d_New_Delhi = 0
                d_Kolkata = 1
                d_Cochin = 0
                d_Hyderabad = 0
                d_Delhi = 0

            elif destination == 'Cochin':
                d_New_Delhi = 0
                d_Kolkata = 0
                d_Cochin = 1
                d_Hyderabad = 0
                d_Delhi = 0

            elif destination == 'Hyderabad':
                d_New_Delhi = 0
                d_Kolkata = 0
                d_Cochin = 0
                d_Hyderabad = 1
                d_Delhi = 0

            elif destination == 'Delhi':
                d_New_Delhi = 0
                d_Kolkata = 0
                d_Cochin = 0
                d_Hyderabad = 0
                d_Delhi = 1

            else:
                d_New_Delhi = 0
                d_Kolkata = 0
                d_Cochin = 0
                d_Hyderabad = 0
                d_Delhi = 0

        prediction = rf.predict([[
                Total_stops,
                Journey_Day,
                Journey_Month,
                Dep_min,
                Dep_hour,
                Arrival_min,
                Arrival_hour,
                dur_min,
                dur_hour,
                s_Delhi,
                s_Mumbai,
                s_Chennai,
                s_Kolkata,
                d_Hyderabad,
                d_Cochin,
                d_Kolkata,
                d_New_Delhi,
                d_Delhi,
                IndiGo,
                Air_India,
                Jet_Airways,
                SpiceJet,
                Multiple_carriers,
                GoAir,
                Vistara,
                Vistara_Premium_economy,
                Jet_Airways_Business,
                Multiple_carriers_Premium_economy,
                Trujet
            ]])

        output = round(prediction[0] , 0)
        logger.info("Reading the output" + str(output))
        return render_template("home.html", prediction_text="Your Flight Price is Rs. {}".format(output))
        logger.info("Printing the output on the home page")
        return render_template("home.html")
        logger.info("Output Printed")
    except Exception as e:
        logger.info("Exception raised :" + str(e))
        print(str(e))


if __name__ == "__main__":
    application.run(debug=True)
    #http_server = WSGIServer(('' , 5000) , app)
    #http_server.serve_forever()