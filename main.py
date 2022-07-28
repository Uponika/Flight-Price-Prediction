from model import *

def main():
    file = "data\Data_Train.xlsx"
    data = loadData(file)
    columns = ['Airline','Source','Destination','Total_Stops','Additional_Info']
    unwantedCols = ['Date_of_Journey','Dep_Time', 'Arrival_Time', 'Route']
    data = preProcessing(data, columns, unwantedCols)
    x_train, x_test, y_train, y_test = splitData(data)
    model = modelTrain(data, x_train, y_train)
    #y_pred = modelPredict(model, x_test)
    #modelPerformance(y_test, y_pred)
    print("Training success")

if __name__ == '__main__':
    main()
