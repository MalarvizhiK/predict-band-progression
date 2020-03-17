# predict-band-progression

IBM assessment tool evaluates an employee across 5 dimensions like Business, Skills, Innvovation, Customer, and Responsibility to others. Here, we have evaluated an employee across Business, Innovation and Skills dimension and recommend band progression for employees based on evaluation. The tool looks at a higher band employee as a role model and it starts clustering the results. When the Machine Learning(ML) K-means clustering algorithm clusters the dataset, we will end up with 5 clusters for 5 bands like Band 10, Band 9, Band 8, Band 7, Band 6. When a lower level employee falls in to each of the higher bands that is above than his current band, then we recommend band progression for him. It is purely based on the work he has performed for the whole year.    
<br/>
This application is a recommendation engine that helps a manager to find where their employees are placed across various dimensions. If an employee is eligible for progression then the flask based python web application can indicate where the employee stand for the checkpoint dimension. 
<br/>
In this hypothetical example, we have a dataset of 70 employees. The data is collected from github, JIRA, and other IBM internal tools to capture the work that he has performed. The collected data is normalised to plot and predict the results according to the requirements of machine learning algorithm. We have categorized data for different levels of employees based on their work load. In every dataset, you can find the various types of assessment in Sheet 1. Sheet 2 contains the employees and the various assessment types, they have worked. 
<br/>

#### Steps to run the application:
1. Git clone the application.  
2. Install python3.   
3. Run the application as below:  
    >> python3 flask_main.py  

 You will get the ouput as below:  
 * Serving Flask app "flask_main" (lazy loading)  
 * Environment: production  
   WARNING: This is a development server. Do not use it in a production deployment.  
   Use a production WSGI server instead.  
 * Debug mode: off  
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
  
4. Enter http://127.0.0.1:5000/  in browser:  


