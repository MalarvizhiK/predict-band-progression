from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from predict_band_progression import algorithm
import os

app = Flask(__name__)

port = int( os.getenv( 'PORT', 8000 ) )

class Employee:
    band = 0
    empid = 0
    dimension = ""
    
    def __init__(self, band, empid, dimension):
        self.band = band
        self.empid = empid
        self.dimension = dimension
        
# displays the "business" checkpoint dimension for all employees  
@app.route('/business')
def business():
   # Predict Business Dimension in checkpoint
   # k-means cluster for Business Dimension
   final = algorithm.cluster_dataset("AssessmentResponseBusiness.xlsx")
   # predict band progression for Business Dimension
   dict = {}
   dict = algorithm.predict_progression(final)
   list = []  
   for key in sorted(dict):
       if int(key) > 6 :
           for i in dict[key]:
               list.append(Employee(key, i, "Business"))
   return render_template('show_dimension.html', employees = list)
   
   
# displays the "skills" checkpoint dimension for all employees  
@app.route('/skills')
def skills():
   # Predict Business Dimension in checkpoint
   # k-means cluster for Business Dimension
   final = algorithm.cluster_dataset("AssessmentResponseSkill.xlsx")
   # predict band progression for Business Dimension
   dict = {}
   dict = algorithm.predict_progression(final)
   list = []  
   for key in sorted(dict):
       if int(key) > 6 :
           for i in dict[key]:
               list.append(Employee(key, i, "Skills"))
   return render_template('show_dimension.html', employees = list)   
   
   
# displays all the checkpoint dimension for all employees   
@app.route('/')
def result():
   # Predict Business Dimension in checkpoint
   # k-means cluster for Business Dimension
   final_bus = algorithm.cluster_dataset("AssessmentResponseBusiness.xlsx")
   # predict band progression for Business Dimension
   dict = {}
   dict = algorithm.predict_progression(final_bus)
   list = []  
   for key in sorted(dict):
       if int(key) > 6 :
           for i in dict[key]:
               list.append(Employee(key, i, "Business"))
   
   # Predict Skills Dimension in checkpoint
   # k-means cluster for Skills Dimension
   final_skills = algorithm.cluster_dataset("AssessmentResponseSkill.xlsx")
   # predict band progression for Skills Dimension
   dict = {}
   dict = algorithm.predict_progression(final_skills)
   for key in sorted(dict):
       if int(key) > 6 :
           for i in dict[key]:
               list.append(Employee(key, i, "Skills"))
    
   # Predict Innovation Dimension in checkpoint
   # k-means cluster for Skills Dimension
   final_inn = algorithm.cluster_dataset("AssessmentResponseInnovation.xlsx")
   # predict band progression for Innovation Dimension
   dict = {}
   dict = algorithm.predict_progression(final_inn)
   for key in sorted(dict):
       if int(key) > 6 :
           for i in dict[key]:
               list.append(Employee(key, i, "Innovation"))               
   return render_template('show_all.html', employees = list)  
   
   
# displays the "innovation" checkpoint dimension for all employees  
@app.route('/innovation')
def innovation():
   # Predict Innovation Dimension in checkpoint
   # k-means cluster for Innovation Dimension
   final = algorithm.cluster_dataset("AssessmentResponseInnovation.xlsx")
   # predict band progression for Business Dimension
   dict = {}
   dict = algorithm.predict_progression(final)
   list = []  
   for key in sorted(dict):
       if int(key) > 6 :
           for i in dict[key]:
               list.append(Employee(key, i, "Innovation"))
   return render_template('show_dimension.html', employees = list)   
      
   
# displays all the checkpoint dimension for a particular employee 
@app.route('/find_progression/<empid>')
def find_progression(empid):
   # Predict Business Dimension in checkpoint
   # k-means cluster for Business Dimension
   final = algorithm.cluster_dataset("AssessmentResponseBusiness.xlsx")
   # predict band progression for Business Dimension
   dict = {}
   dict = algorithm.predict_progression(final)
   list = []  
   for key in sorted(dict):
       if int(key) > 6:
           for i in dict[key]:
               if (int(i) == int(empid)):
                   list.append(Employee(key, i, "Business"))
   final_skill = algorithm.cluster_dataset("AssessmentResponseSkill.xlsx")
   # predict band progression for skills Dimension
   dict = {}
   dict = algorithm.predict_progression(final_skill)
   for key in sorted(dict):
       if int(key) > 6:
           for i in dict[key]:
               if (int(i) == int(empid)):
                   list.append(Employee(key, i, "Skills"))
   final_inn = algorithm.cluster_dataset("AssessmentResponseInnovation.xlsx")
   # predict band progression for Innovation Dimension
   dict = {}
   dict = algorithm.predict_progression(final_inn)
   for key in sorted(dict):
       if int(key) > 6:
           for i in dict[key]:
               if (int(i) == int(empid)):
                   list.append(Employee(key, i, "Innovation"))                   
   return render_template('show_all.html', employees = list)      


if __name__ == '__main__':
   app.run( host='0.0.0.0', port=port, debug=True)