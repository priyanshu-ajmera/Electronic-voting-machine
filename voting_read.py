from xlrd import *

def vote_calc():
    workbook=open_workbook('voting.xls')
    wosksheet=workbook.sheet_by_index(0)
    x=1
    votes=[1,2,3,4,5]
    for i in range(0,5):
        votes[i]=int(worksheet.cell(x,1).value)
        x=x+i
    x=votes[0]
    for i in range(0,5):
        if(x<votes[i]):
            x=votes[i]
    return(x)
