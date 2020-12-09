countItem = dict()

subjectList = ['database', 'SRS', 'Information Security', 'SRS', 'Information Security', 'BUS'
                , 'database', 'OS', 'BUS', 'Business Psychology', 'OS', 'SRS', 'Information Security'
                , 'SRS', 'BUS', 'SRS', 'BUS', 'Business Psychology']

for iSubject in subjectList:
    countItem[iSubject]=countItem.get(iSubject, 0)+ 1

print(countItem)