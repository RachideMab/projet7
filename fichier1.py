def actions(data_set):
    """
    this function allow us to open the list of actions and provide them to the 
    algorithme. 
    """
    dataSet = ".\\liste_actions.csv"
    lineCount = 0
    tableName = []
    tablePrice = []
    tableProfit = []
   
    with open(dataSet, encoding="utf-8") as file:
        
        for line in file : 
            if (lineCount >= 1):
                X = line.replace("\n", "").split(";") 
                X = line.replace("%", "").split(";")
                tableName.append(X[0])
                tablePrice.append(float(X[1]))
                tableProfit.append(float(X[2])*float(X[1])/100)
            
            lineCount +=1
    return tableName, tablePrice, tableProfit

if __name__ == "__main__":
    print(actions('data_set'))