import csv
import pandas as x
import plotly_express as y
with open('class1.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
total_marks = 0
total_entries = len(file_data)
for i in file_data:
    total_marks = total_marks+float(i[1])
mean = total_marks/total_entries
print("The mean is: "+str(mean))    
v1 = x.read_csv("class1.csv")
v2 = y.scatter(v1, x = 'Student Number', y = 'Marks')
v2.update_layout(shapes = [dict(type = 'line', y0 = mean, y1 = mean, x0 = 0, x1 = total_entries)])
v2.update_yaxes(rangemode = "tozero")
v2.show()