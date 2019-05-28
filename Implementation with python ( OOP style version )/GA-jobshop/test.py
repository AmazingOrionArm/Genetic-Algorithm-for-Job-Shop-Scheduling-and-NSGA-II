import jobshopscheduling as jss

#---Main Function--
mainScheduler = jss.Scheduler()
mainScheduler["processTimeTable"] = "ProcessingTime.csv"
mainScheduler["machinesSequenceTable"] = "MachinesSequence.csv"

mainScheduler.Run()

mainScheduler.PrintResult()
mainScheduler.PrintFitnessPlot()
mainScheduler.GenerateGanttChart()
#---
