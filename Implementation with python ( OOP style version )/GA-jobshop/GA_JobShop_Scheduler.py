import numpy as np
import pandas as pd

class Scheduler:
    def __init__(self):
        # Initial基本參數
        self.__parameters = {
            # Table
            "processTimeTable": pd.DataFrame(),
            "machinesSequenceTable": pd.DataFrame(),
            # basic parameters
            "populationRate": 30,
            "crossoverRate": 0.8,
            "mutationRate": 0.8,
            "mutationSelectionRate": 0.8,
            "maxGeneration": 0.8,
        }
        
    # 建構子
    def Scheduler(self, processTimeTableName, machinesSequenceTableName):
        # read table
        self.__parameters["processTimeTable"] = pd.read_csv(processTimeTableName)
        self.__parameters["machinesSequenceTable"] = pd.read_csv(machinesSequenceTableName)
        
    # Accessor，Operator [] overloading
    def __getitem__(self, preferParameter):
        return self.__parameters[preferParameter]
    
    # Mutator，Operator [] overloading
    def __setitem__(self, preferParameter, preferValue):
        # 如果要設定的是Table，則利用該TableName讀取Table，再進行assign
        if(preferParameter == "processTimeTable"):
            self.__parameters["processTimeTable"] = pd.read_csv(processTimeTableName)
        elif(preferParameter == "machinesSequenceTable"):
            self.__parameters["machinesSequenceTable"] = pd.read_csv(machinesSequenceTableName)
        # 一般數執行參數則直接assign
        else:
            self.__parameters[preferParameter] = preferValue
        
