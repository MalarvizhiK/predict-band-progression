# predict-band-progression

IBM assessment tool evaluates an employee across 5 dimensions like Business, Skills, Innvovation, Customer, and Responsibility to others. Here, we have evaluated an employee across Business, Innovation and Skills dimension and recommend band progression for employees based on evaluation. The tool looks at a higher band employee as a role model and it starts clustering the results. When the Machine Learning(ML) K-means clustering algorithm clusters the dataset, we will end up with 5 clusters for 5 bands like Band 10, Band 9, Band 8, Band 7, Band 6. When a lower level employee falls in to each of the higher bands that is above than his current band, then we recommend band progression for him. It is purely based on the work he has performed for the whole year.      

This application is a recommendation engine that helps a manager to find where their employees are placed across various dimensions. If an employee is eligible for progression then the flask based python web application can indicate where the employee stand for the checkpoint dimension.     


In this hypothetical example, we have a dataset of 70 employees. The data is collected from github, JIRA, and other IBM internal tools to capture the work that he has performed. The collected data is normalised to plot and predict the results according to the requirements of machine learning algorithm. We have categorized data for different levels of employees based on their work load. In every dataset, you can find the various types of assessment in Sheet 1. Sheet 2 contains the employees and the various assessment types, they have worked.     

Machine learning model is using K-means clustering algorithm to cluster the work done by all employees. We have created 5 clusters for 5 bands like Band 10, Band 9, Band 8, Band 7, Band 6. The decision tree algorithm gets employees from each of the cluster, and predicts whether an employee is eligible for band progression or not. In each of the cluster, we fetch the highest band and check whether other employees in the cluster have the experience to get promoted to the next band. Say, if an employee id 110 whose current band is 9 and he is clustered along with other employees whose band is 10, then it means that he is performing the job of band 10. The decision tree algorithm is trained with dataset SampleProgressionData.xlsx where we fed all the combinations where an employee is eligible for progression. Based on the training data, Decision Tree Algorithm predicts whether an employee is eligible for band progression or not.      


#### Steps to run the application:
1. Git clone the application.  
2. Install python3.   
3. Run the application as below:  
    > python3 flask_main.py  

 You will get the ouput as below:  
 * Serving Flask app "flask_main" (lazy loading)  
 * Environment: production  
   WARNING: This is a development server. Do not use it in a production deployment.  
   Use a production WSGI server instead.  
 * Debug mode: off  
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
  
4. Enter http://127.0.0.1:5000/  in browser:    

   Following are the endpoints of this application:

   a) Finding band progression for a particular employee:    
      http://127.0.0.1:5000/find_progression/110    
      ![Find Progression of an employee](images/find_progression.png)

    
   b) Finding band progression results of all employees:      
      http://127.0.0.1:5000/   
      ![Results of all employees](images/results_endpoint.png)
      
   c) Finding band progression results for Business dimension of all employees:   
      http://127.0.0.1:5000/business    
     ![Business Dimension of all employees](images/business_endpoint.png)
     
   d) Finding band progression results for Skills dimension of all employees:   
      http://127.0.0.1:5000/skills  
      ![Skills Dimension of all employees](images/skills_endpoint.png)
    
   e) Finding band progression results for Innovation dimension of all employees:   
      http://127.0.0.1:5000/innovation  
      ![Innovation Dimension of all employees](images/innovation_endpoint.png)
      
#### Steps to python notebook:  

The application can be run as a Jupyter notebook as well. Enter below command in your command prompt or in Watson Studio, open this notebook.  

    > jupyter notebook Employee clustering.ipynb    
    
 ![jupyter notebook](images/jupyter_notebook.png)


 Here, you can find the k-means clustering plot for 5 clusters as below:   
![k-means plot](images/k-means-plot.png)
