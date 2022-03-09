from unittest import result
from flask import Flask, render_template, url_for, request
import numpy as np
import joblib


app = Flask(__name__)
    

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == "POST":
        Form = dict(request.form)
   
        Fixed_Acidityta = float(Form['Fixed_Acidityta'])
        Volatile_Acidity = float(Form['Volatile_Acidity'])
        Citric_Acid = float(Form['Citric_Acid'])
        Residual_Sugar = float(Form['Residual_Sugar'])
        Chlorides = float(Form['Chlorides'])
        Free_Sulfur_Dioxide = float(Form['Free_Sulfur_Dioxide'])
        Total_Sulfur_Dioxide = float(Form['Total_Sulfur_Dioxide'])
        Density = float(Form['Density'])
        PH = float(Form['PH'])
        Sulphates = float(Form['Sulphates'])
        Alcohol = float(Form['Alcohol'])

        input_data = (Fixed_Acidityta,Volatile_Acidity,
                Citric_Acid,Residual_Sugar,Chlorides,Free_Sulfur_Dioxide,
                Total_Sulfur_Dioxide,Density,PH,Sulphates,Alcohol)
        data = np.array(input_data)

        data_reshaped = data.reshape(1,-1)
        model = joblib.load('./wine_quality_model.sav')
        result = model.predict(data_reshaped)
        print(f"RESult = {result}")
        if (result[0]==1):
            model_result = "Good Quality Wine !!"
        else :
            model_result = "Bad Quality Wine !!"
        return render_template('/result.html', model_result = model_result )
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False)