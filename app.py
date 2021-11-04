import pandas as pd
from flask import request, render_template, Flask
from flask_cors import cross_origin
import pickle
import sklearn
#import scikit-learn
import pandas
#from gevent.pywsgi import  WSGIServer

app = Flask(__name__)
model = open('final_model_flight.pickle' , 'rb')
rf = pickle.load(model)

@app.route("/", methods=["GET", "POST"])
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    try:
        if request.method == "POST":

            # Departure
            date_dep = request.form['Dep_Time']

            # Deperature Day and Month
            Journey_Day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
            Journey_Month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

            # Deperature Time
            Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
            Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

            # Arrival
            date_arr = request.form['Arrival_Time']

            # Arrival Time
            Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
            Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

            # Duration of Flight
            dur_hour = abs(Arrival_hour - Dep_hour)
            dur_min = abs(Arrival_min - Dep_min)

            # Total Stops
            Total_stops = int(request.form['stops'])

            # Airline Selection
            #Air Asia = 0
            airline = request.form['airline']
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

        return render_template("home.html", prediction_text="Your Flight Price is Rs. {}".format(output))

        return render_template("home.html")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    app.run(debug=True)
    #http_server = WSGIServer(('' , 5000) , app)
    #http_server.serve_forever()