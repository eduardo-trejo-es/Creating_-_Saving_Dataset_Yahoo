from Retriving_Dataset import *

dataSet_Gen= DatasetGenerator()

#dataSet_Gen.RetivingDataPrices_Yahoo('2000-08-23', '2000-11-25',"/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/testClass.csv","/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/testClass.csv")

dataSet_Gen.AddColumnWeekDay("/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/CRUDE_OIL_DataCSV.csv", "/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/CRUDE_OIL_WeekDayNum.csv")