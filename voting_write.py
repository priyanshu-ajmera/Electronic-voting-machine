import xlwt
from datetime import datetime

patt1=xlwt.easyxf('font:name Arial, color-index Blue, bold ON', num_format_str='#,##0.00')   # for taking comma values sych as 10,000.00
patt2=xlwt.easyxf(num_format_str='DD-MM-YYYY')

wb=xlwt.Workbook()
                  
ws=wb.add_sheet('Voting')
ws.write(0,0,"PARTIES",patt1)
ws.write(1,0,"Congress",patt1)
ws.write(2,0,"BJP",patt1)
ws.write(3,0,"AAP",patt1)
ws.write(4,0,"SVP",patt1)
ws.write(5,0,"Others",patt1)
                  
ws.write(0,1,"VOTES",patt1)
ws.write(1,1,c1,patt1)
ws.write(1,2,c2,patt1)
ws.write(1,3,c3,patt1)
ws.write(1,4,c4,patt1)
ws.write(1,5,c5,patt1)

c1=0
c2=0
c3=0
c4=0
c5=0
password=123456

while 1:
    print("Welcome To The Voting Day")
    print("Press 1 for Congress")
    print("Press 2 for BJP")
    print("Press 3 for AAP")
    print("Press 4 for SVP")
    print("Press 5 for Others")
    ch=int(input("Press a key: "))
    if(ch==1):
        c1=c1+1
    elif(ch==2):
        c2=c2+1
    elif(ch==3):
        c3=c3+1
    elif(ch==4):
        c4=c4+1
    elif(ch==5):
        c5=c5+1
    elif(ch==6):
        Enter_Password=int(input("Enter password to quit the voting"))
        if(Enter_Password==password):
            break
        else:
            continue
    else:
        print("Invalid Key Pressed")

wb.save('voting.xls')
