#import COVID19 library
import COVID19Py
covid19 = COVID19Py.COVID19(data_source="jhu")
#function for get latest detail all around th world
x = covid19.getLatest()
print("Confirmed Cases: ", x["confirmed"])
print("Deaths: ",x["deaths"])
print("Recovered Cases: ", x["recovered"])