from flask import Flask, render_template, request,jsonify
import pickle
import pandas as pd

processor =pickle.load(open("./model/column_transformer.pkl","rb"))
model = pickle.load(open("./model/random_forest_regressor.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        job_title = request.form.get("Job Title")
        Employment_Type=request.form.get('Employment Type')
        Experience_Level = request.form.get('Experience Level')
        Experise_Level = request.form.get('Expertise Level')
        salary_cur = request.form.get('Salary Currency')
        company_loc = request.form.get('Company Location')
        emp_residence = request.form.get('Employee Residence')
        company_size = request.form.get('Company Size')
        year = float(request.form.get('Year'))

        new_data_scaled=processor.transform(pd.DataFrame({"Job Title": [job_title],
              "Employment Type": [Employment_Type],
              "Experience Level": [Experience_Level],
              "Expertise Level": [Experise_Level],
              "Salary Currency": [salary_cur],
              "Company Location":[company_loc],
              "Employee Residence":[emp_residence],
              "Company Size":[company_size],
              "Year":[year]}) )
        result=model.predict(new_data_scaled)

        return render_template('predict.html',result=result[0])

    else:
        return render_template('predict.html')

# @app.route("/testget/<name>", methods = ['GET',"POST"])
# def test(name):
#     return f"<h1>test: {name}</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
