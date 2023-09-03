#Swimming Athletes
import pandas as pd
import matplotlib.pyplot as plt
# Main Menu
result=pd.read_excel("./csvfile.xlsx",index_col=0)
while(True):
 print("Main Menu")
 print("1. Display Records")
 print("2. Working on Records")
 print("3. Working on Columns")
 print("4. Search specific row/column")
 print("5. Data Visualization")
 print("6. Exit")
 ch=int(input("Enter your choice"))
 if ch==1:
   while(True):
     print("Display Records Menu")
     print("1. Top 5 Resords")
     print("2. Bottom 5 Records")
     print("3. Specific number of records from the top")
     print("4. Specific number of records from the bottom")
     print("5. Particular Detail")
     print("6. Display Complete details")
     print("7. Exit")
     ch3=int(input("Enter choice"))
     if ch3==1:
       print(result.head())
     elif ch3==2:
       print(result.tail())
     elif ch3==3:
       n=int(input("Enter how many records you want to display from the top"))
       print(result.head(n))
     elif ch3==4:
       n=int(input("Enter how many records you want to display from the bottom"))
       print(result.tail(n))
     elif ch3==5:
       st=input("Enter Athlete name for which you want to see the details")
       print(result.loc[st])
     elif ch3==6:
       print("Complete Details")
       print(result)
     elif ch3==7:
       break
 elif ch==2 :
   while(True):
     print("Working on Records Menu")
     print("1. Insert a record")
     print("2. Delete a specific record")
     print("3. Update a specific record")
     print("4. Exit")
     ch4=int(input("Enter choice"))
     if ch4==1:
       a=input("Enter Athlete name")
       b=int(input("Enter Age:"))
       c=input("Enter Country:")
       d=int(input("Enter Year"))
       e=input("Enter Sport")
       f=int(input("Enter number of Gold Medal"))
       g=int(input("Enter number of Silver medal"))
       h=int(input("Enter number of Bronze medal"))
       result.loc[a]=[b,c,d,e,f,g,h]
       print("Data successfully inserted")
     elif ch4==2:
       a=input("Enter Athlete name whose data needs to be deleted")
       result.drop([a],inplace=True)
       print("Data successfully deleted")
     elif ch4==3:
       a=input("Enter Athlete name")
       b=int(input("Enter Age:"))
       c=input("Enter Country:")
       d=int(input("Enter Year"))
       e=input("Enter Sport")
       f=int(input("Enter number of Gold Medal"))
       g=int(input("Enter number of Silver medal"))
       h=int(input("Enter number of Bronze medal"))
       result.loc[a]=[b,c,d,e,f,g,h]
       print("Data successfully updated")
     elif ch4==4:
       break
 elif ch==3:
    while(True):
      print("Working on Columns Menu")
      print("1. Insert a new column data")
      print("2. Delete a specific column")
      print("3. Exit")
      ch5=int(input("Enter choice"))
      if ch5==1:
        print("Enter details")
        h=input("Enter column/heading name")
        det=eval(input("Enter details corresponding to all items:(enclosed in [ ])"))
        result[h]=pd.Series(data=det,index=result.index)
        print("Column inserted")
      elif ch5==2:
        a=input("Enter column name which needs to be deleted")
        result.drop([a],axis=1,inplace=False)
        print("Column Temporary deleted")
      elif ch5==3:
        break
 elif ch==4:
   while(True):
     print("Search Menu")
     print("1. Search for the details of a specific Athlete")
     print("2. Search details of a specific as per a specific column heading")
     print("3. Exit")
     ch6=int(input("Enter choice"))
     if ch6==1:
       st=input("Enter the Athlete name whose details you want to see")
       print(result.loc[st])
     elif ch6==2:
       col=input("Enter column/heading name whose details you want to see")
       print(result[col])
     elif ch6==3:
       break
 elif ch==5:
   while(True):
     print("Data Visualization Menu")
     print("1. Line Plot")
     print("2. Vertical Bar Plot")
     print("3. Horizontal Bar Plot")
     print("4. Histogram")
     print("5. Exit")
     ch7=int(input("Enter choice"))
     if ch7==1:
       result.plot(kind='line')
       plt.show()
     elif ch7==2:
       result.plot(kind='bar')
       plt.show()
     elif ch7==3:
       result.plot(kind='barh')
       plt.show()
     elif ch7==4:
       result.plot(kind='hist')
       plt.show()
     elif ch==5:
       break
 else:
   break

