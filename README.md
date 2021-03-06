# Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II
本主題主要介紹如何透過基因演算法 (Genetic Algorithm, GA) 與非凌越排序基因演算法 (Nondominated Sorting Genetic Algorithm II, NSGA-II) 來求解 Job Shop 排程問題。一開始會先進行 GA 及 NSGA-II 的概念介紹，最後再透過 Python 來進行實作並說明。
## § Introduction

|更新時間|文章|
|---|---|
|2018|[Genetic Algorithm (GA)](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/introduction/GA/GA.md)|
|2018|[Nondominated Sorting Genetic Algorithm II (NSGA-II)](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/introduction/NSGA-II/NSGA-II.md)|
## § Implementation with Python

|更新時間|文章|連結|
|---|---|---|
|2018|GA For Flow Shop|[Documentation](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/GA%20for%20flow%20shop%20problem.md) / [Example](https://wurmen.github.io/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation%20with%20python/GA-flowshop/Example.html) / [code](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/GA_flowshop_tardyjob.py) / [Folder](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/tree/master/implementation%20with%20python/GA-flowshop)|
|2018|GA For Job Shop|[Documentation](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-jobshop/GA_For_Jobshop.md) / [Example](https://wurmen.github.io/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation%20with%20python/GA-jobshop/Example1.html) / [code](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-jobshop/GA_jobshop_makespan.py) / [Folder](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/tree/master/implementation%20with%20python/GA-jobshop)|
|2018|NSGA-II|[Documentation](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/NSGA-II/NSGA-II.md) / [Example](https://wurmen.github.io/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation%20with%20python/NSGA-II/Example_NSGAII.html) / [code](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/NSGA-II/NSGA-II%20code.py) / [Folder](https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/tree/master/implementation%20with%20python/NSGA-II)|

## 以下為改編者添加內容：
* 預計新增python(OOP版本)([Job-Shop Scheduling](https://github.com/AmazingOrionArm/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/tree/master/Implementation%20with%20python%20(%20OOP%20style%20version%20)/GA-jobshop)完成)、C++版本，優先製作Job-Shop Scheduling
* 改編動機：改編人因為目前大學專題的內容需要使用到Job-Shop Scheduling，因緣際會下看到這篇，因此希望可以以原作者的原始碼與流程為基礎，改寫為OOP的版本以利在專題中使用，因改編人亦有基本C++程式能力，因此如有餘裕，也將會撰寫C++版本已利於在其他環境用途下使用。
* Reference : [PO-Lab](https://github.com/PO-LAB/Intelligent-Manufacturing-Systems/blob/master/GA_Application_Job_Shop_Problem/JSP.md)
