## 使用說明 - 安裝
將 **GAJobShopScheduling.py** 和 **\_\_init\_\_.py** 與您的程式放在同個資料夾中，並以下敘述將GAJobShopScheduling.py載入到您的程式中
```python
import GAJobShopScheduling
```
## 使用說明 - 使用方法
首先在您的程式中，建構 Scheduler 實體，此時尚未載入資料表格
```python
yourSchedulerName = GAJobShopScheduling.Scheduler()
```
接著因為本程式 Mutator 採用 Operator [] Overloading 實作，因此載入表格的方式如下
```python
yourSchedulerName["processTimeTable"] = yourProcessTimeTableName
yourSchedulerName["machinesSequenceTable"] = yourMachinesSequenceTableName
```
載入表格後，您可以繼續設定必要參數，或是不設定直接採用預設值，如需要設定使用方式如下
```python
yourSchedulerName[preferParaName] = preferParaValue
# preferParaName 為您想設定的參數名稱
# preferParaValue 為您想設定的值
```
您也可以直接取得目前的參數值
```python
yourSchedulerName[preferParaName]
# preferParaName 為您想設定的參數名稱
```
或是一次印出全部參數的值，他會以pandas series格式輸出
```python
yourSchedulerName.PrintAllParameters()
```
當table檔、參數接設定完成後，可使用Run()來開始運行計算
```python
yourSchedulerName.Run()
```
在此期間程式會印出目前的 Generation，您可以查看目前的進度。計算完成後可利用以下敘述分別取得計算結果、適應度值趨勢圖與甘特圖
```python
yourSchedulerName.PrintResult()
yourSchedulerName.PrintFitnessPlot()
yourSchedulerName.GenerateGanttChart()
```

## 使用說明 - 參數清單對應及其預設值
```python
"processTimeTable": None #必需設定，.csv檔 ( 修改原版本方案 )
"machinesSequenceTable": None #必須設定，.csv檔 ( 修改原版本方案 )
"populationSize": 30 #預設30，( 即原版本的 population_size ) 
"crossoverRate": 0.8 #預設0.8，( 即原版本的 crossover_rate ) 
"mutationRate": 0.2 #預設0.2，( 即原版本的 mutation_rate ) 
"mutationSelectionRate": 0.2 #預設0.2，( 即原版本的 mutation_selection_rate ) 
"maxGeneration": 2000 #預設2000，( 即原版本的 num_iteration ) 
```

## 來源說明
此程式為添加物件導向風格的版本，可更有利於專案中使用，其原版本來自[PO-Lab](https://github.com/PO-LAB/Intelligent-Manufacturing-Systems/blob/master/GA_Application_Job_Shop_Problem/JSP.md)成員[wurmen](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-jobshop/GA_For_Jobshop.md)
