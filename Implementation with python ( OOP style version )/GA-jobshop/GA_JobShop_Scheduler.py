"""
===== Original Version Code: https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-jobshop/GA_jobshop_makespan.py
===== Original Author's Information =====
Original Author: cheng-man wu
LinkedIn: www.linkedin.com/in/chengmanwu
Github: https://github.com/wurmen
=====
===== Adaptor: James, NTUST-IM
"""

import numpy as np
import pandas as pd

class Scheduler:
    def __init__(self):
        # Initial基本參數
        self.__parameters = {
            # Table
            "processTimeTable": None,
            "machinesSequenceTable": None,
            # basic parameters
            "populationSize": 30,
            "crossoverRate": 0.2,
            "mutationRate": 0.8,
            "mutationSelectionRate": 0.8,
            "maxGeneration": 2000,
        }
        
    # Initial Constructor
    def Scheduler(self):
        print("Construct Initial Scheduler")
        
    # Constructor with tablename arguments
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
    
    # 印出所有參數
    def PrintAllParameters(self):
        print("Current Parameters List\n------")
        print(pd.Series(self.__parameters))
    
    # 啟動函式，部分原碼暫時沿用原版本，待後續視情況修改
    def Run(self):
        print("Calculating...")
        
        dfshape=self.__parameters["processTimeTable"].shape
        num_mc=dfshape[1] # number of machines
        num_job=dfshape[0] # number of jobs
        num_gene=num_mc*num_job # number of genes in a chromosome

        pt=[list(map(int, pt_tmp.iloc[i])) for i in range(num_job)]
        ms=[list(map(int,ms_tmp.iloc[i])) for i in range(num_job)]
        
        Tbest=999999999999999
        best_list,best_obj=[],[]
        population_list=[]
        makespan_record=[]
        for t in range(self.__parameters["populationSize"]):
            print("=== Generation:" + str(t) + "===")
            nxm_random_num=list(np.random.permutation(num_gene)) # generate a random permutation of 0 to num_job*num_mc-1
            population_list.append(nxm_random_num) # add to the population_list
            for j in range(num_gene):
                population_list[i][j]=population_list[i][j]%num_job # convert to job number format, every job appears m times
    '''
    def NewPupulation(self):
        # 產生初始群體

    def ReProduction(self):
        # 產生新群體

    def Selection(self):
        # 選擇

    def Crossover(self):
        # 交配

    def Mutation(self):
        # 突變

    def Repair(self):
        # 修復

    def CalcFitness(self, c):
        # 計算適應值

    def PrintResult(self):
        # 印出計算結果

    def PrintFitnessPlot(self):
        # 繪製適應度趨勢圖

    def GenerateGanttChart(self):
        # 繪製甘特圖
    '''
    
