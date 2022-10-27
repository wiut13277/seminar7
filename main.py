student = {'name': 'Fazliddin',
           'module': 'CS_fun',
           'mark': 80
          }

eng2uz = dict()
eng2uz['one'] = 'bir'
eng2uz['two'] = 'ikki'

print(student)
print(eng2uz)
print(len(student))



myFinalMarks = { 'CSF': 75,'FunPro': 80, 'WT': 85 }

def calculateAverage(finalMarks):
    total = 0
    for key in finalMarks:
        total +=finalMarks[key]
    average = total/len(finalMarks)
    return average

print(calculateAverage(myFinalMarks))