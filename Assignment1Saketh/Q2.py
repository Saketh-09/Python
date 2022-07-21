classes=int(input('How many classes did you take?'))
className=[]
classGrade=[]
sum=0
for i in range(classes):
    className.append(input('What was the name of this class? '))
    classGrade.append(int(input('What was your grade? for '+className[i]+' :')))
    sum+=classGrade[i]
mean=sum/classes
print('REPORT CARD')
for i in range(classes):
    print('\t'+className[i]+' - '+str(classGrade[i]))
print('\tOverall GPA - '+str(mean))