
def actions(data_set):
    """
    this function allow us to open the list of actions and provide them to the 
    algorithme. 
    """
    
    dataSet1 = ".\\dataset1_Python+P7 .csv"
    dataSet2 = ".\\dataset2_Python+P7 .csv"
    lineCount = 0
    tableName =[]
    tablePrice =[]
    tableProfit =[]
   
    with open(dataSet1, encoding="utf-8") as data1:
        for line in data1:
            if (lineCount >=1):
                X = line.replace("\n", "").split(",")
                
                if float(X[1]) <= 0 or float(X[2]) <=0:
                    continue                   
                    
                tableName.append(X[0])
                tablePrice.append(float(X[1])*100)
                tableProfit.append((float(X[2])/100)*float(X[1]))
            
            lineCount +=1
   
    return tableName, tablePrice, tableProfit

if __name__ == "__main__":
    print(actions('data_set'))