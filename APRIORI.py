import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori  


store_data = pd.read_csv('store_data.csv', header=None) 

store_data.shape
store_data.columns
store_data.head()  

 

#dataset to be in the form of a list of lists, 
#where the whole dataset is a big list and
#each transaction in the dataset is an inner list within the outer big list.
 
records = []  
for i in range(0, 7501):  
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])
    
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3,
                            min_length=2)  
association_results = list(association_rules)  
type(association_results)
print(len(association_results))


print(association_results[0])  


for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")