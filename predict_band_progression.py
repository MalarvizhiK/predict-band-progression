from pandas import read_excel, merge
from numpy import arange
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# Plotly requires pip install plotly
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
#Import the DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
init_notebook_mode()

class algorithm:
    
    # k-means cluster algorithm 
    def cluster_dataset(excel_filename):
        # Importing an Excel spreadsheet with two sheets as two DataFrames
        df_assessment = read_excel(excel_filename, sheet_name = 0)
        df_response = read_excel(excel_filename, sheet_name = 1)
        # Adding a column of value 1 to act as a count for that instance
        df_response["n"] = 1
        # Merge on the CampaignID columns
        df = merge(df_assessment, df_response, on = "AssessmentID")
        # Create a pivot table to count each of the 22 assessments
        table = df.pivot_table(index = ["EmployeeID"], columns = ["AssessmentID"], values = "n")
        # Fill NA values with 0 and reset the index to AssessmentID
        table = table.fillna(0).reset_index()
        # Extracting the columns (22 assessments)
        cols = table.columns[1:]
        cluster = KMeans(n_clusters = 5) # At least 7-times times cluster = employee
        # Predict the cluster from first employee down all the rows
        table["cluster"] = cluster.fit_predict(table[table.columns[2:]])
        # Principal component separation to create a 2-dimensional picture
        pca = PCA(n_components = 2)
        table['x'] = pca.fit_transform(table[cols])[:,0]
        table['y'] = pca.fit_transform(table[cols])[:,1]
        table = table.reset_index()
        business_clusters = table[["EmployeeID", "cluster", "x", "y"]]
        final = merge(df_response, business_clusters)
        final = merge(df_assessment, final);
        trace0 = go.Scatter(x = business_clusters[business_clusters.cluster == 0]["x"],
                    y = business_clusters[business_clusters.cluster == 0]["y"],
                    name = "Cluster 1",
                    mode = "markers",
                    marker = dict(size = 10,
                                 color = "rgba(15, 152, 152, 0.5)",
                                 line = dict(width = 1, color = "rgb(0,0,0)")))
        trace1 = go.Scatter(x = business_clusters[business_clusters.cluster == 1]["x"],
                    y = business_clusters[business_clusters.cluster == 1]["y"],
                    name = "Cluster 2",
                    mode = "markers",
                    marker = dict(size = 10,
                                 color = "rgba(180, 18, 180, 0.5)",
                                 line = dict(width = 1, color = "rgb(0,0,0)")))
        trace2 = go.Scatter(x = business_clusters[business_clusters.cluster == 2]["x"],
                    y = business_clusters[business_clusters.cluster == 2]["y"],
                    name = "Cluster 3",
                    mode = "markers",
                    marker = dict(size = 10,
                                 color = "rgba(132, 132, 132, 0.8)",
                                 line = dict(width = 1, color = "rgb(0,0,0)")))
        trace3 = go.Scatter(x = business_clusters[business_clusters.cluster == 3]["x"],
                    y = business_clusters[business_clusters.cluster == 3]["y"],
                    name = "Cluster 4",
                    mode = "markers",
                    marker = dict(size = 10,
                                 color = "rgba(122, 122, 12, 0.8)",
                                 line = dict(width = 1, color = "rgb(0,0,0)")))
        trace4 = go.Scatter(x = business_clusters[business_clusters.cluster == 4]["x"],
                    y = business_clusters[business_clusters.cluster == 4]["y"],
                    name = "Cluster 5",
                    mode = "markers",
                    marker = dict(size = 10,
                                 color = "rgba(230, 20, 30, 0.5)",
                                 line = dict(width = 1, color = "rgb(0,0,0)")))

        # data = [trace0, trace1, trace2, trace3, trace4]
        # iplot(data)
        # assessment types
        final["0"] = final.cluster == 0
        final.groupby("0").Type.value_counts()
        return final


    # decision tree algorithm 
    def predict_progression(final):
        """
        Import the Sample Progression Dataset
        """
        #Import the dataset for prediction
        dataset = read_excel('SampleProgressionData.xlsx', sheet_name=0)
        """
        Split the data into a training and a testing set
        """
        train_features = dataset.iloc[0:197,:-1]
        train_targets = dataset.iloc[0:197,-1]
        i=0
        df_cluster_data_col = {}
        Dict_progression = {} 
        Dict_rec_progression = {} 
        while i < 5:
            # Number of employees in this cluster
            array_n = final[final.cluster == i]["EmployeeID"].unique()
            len(array_n)
            print("cluster ", i )
            print("Employees: ", array_n)
            # List of employees
            final[final.cluster == i]
            cluster_data_n=final[final.cluster == i]
            cluster_data_n=cluster_data_n[0:len(array_n)]
            # cluster_data_n
            df_cluster_data_n=pd.DataFrame(cluster_data_n, columns = ['EmployeeID', 'MajorityBand','CurrentBand','NumberYears','Progression']) 
            df_cluster_data_n['MajorityBand']=df_cluster_data_n['CurrentBand'].max()
            df_cluster_data_n.fillna(0, inplace=True)
            dataset_cluster_n = pd.DataFrame(df_cluster_data_n,columns = ['EmployeeID','MajorityBand', 'CurrentBand','NumberYears','Progression'])
            test_features = dataset_cluster_n.iloc[:,1:4]
            test_targets = dataset_cluster_n.iloc[:,-1]
            """
            Train the model
            """
            tree = DecisionTreeClassifier(criterion = 'entropy').fit(train_features,train_targets)
            """
            Predict the classes of new, unseen data
            """
            prediction = tree.predict(test_features)
            """
            Check the accuracy
            """
            print("The prediction accuracy is: ",tree.score(test_features,test_targets)*100,"%")
            df_cluster_data_n['Progression']=list(prediction)
            strmax = df_cluster_data_n['CurrentBand'].max()
            print("strmax ", strmax)
            print("prediction ", prediction)
            print('---------------------------------------------------------------------')
            print("PREDICTION FOR BAND ", strmax)
            print('---------------------------------------------------------------------')
            df_cluster_data_n = df_cluster_data_n.loc[df_cluster_data_n["Progression"]==1]
            df_cluster_data_empid=pd.DataFrame(df_cluster_data_n, columns = ['EmployeeID'])
            df_cluster_data_col[i]=df_cluster_data_empid
            Dict_progression[strmax]=list(df_cluster_data_empid['EmployeeID'].unique())
            print("Dict_progression ", Dict_progression)
            i=i+1
            # Show the next promotion band and not the cluster highest band for recommendation to employees
            list_promotion = Dict_progression[strmax]
            for emp_band_promo in list_promotion:
                array = df_cluster_data_n.loc[df_cluster_data_n['EmployeeID'] == emp_band_promo]['CurrentBand'].unique()
                promotion_band = array[0]+1 
                list_emp_band = []
                if promotion_band in Dict_rec_progression:
                    list_emp_band = Dict_rec_progression[promotion_band]
                list_emp_band.append(emp_band_promo)     
                list_emp_band.sort()
                Dict_rec_progression[promotion_band] = list_emp_band
        print("Dict_progression", Dict_progression)
        print("Dict_rec_progression", Dict_rec_progression)             
        return Dict_rec_progression    
    
    
