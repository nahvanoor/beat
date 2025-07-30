import numpy as np
import pandas as pd
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

pd.Series(data=my_list)

pd.Series(data=my_list,index=labels)

pd.Series(my_list,labels)

pd.Series(arr)

pd.Series(arr,labels)

pd.Series(d)

pd.Series(data=labels)


ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan']) 
ser1
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan']) 
ser2
ser1 + ser2


from numpy.random import randint
np.random.seed(24)
x=randint(1,100,9).reshape(3,3)
x
df=pd.DataFrame(data=x,index="A B C".split(),columns="X Y Z".split())
df.index.name="index"
df.x
df['X']
df.loc['A']
df.iloc[1]


details={'First Name':['Nahva','Ranjinee','Kamaru'],'Age':[22,21,21],'Gender':['Female','Female','Female']}
pd.DataFrame(details,[1,2,3])

detail=[['Nahva',22,'Female'],['Ranjinee',21,'FEmale'],['nafeesathul',21,'Female']]
pd.DataFrame(detail,[1,2,3],['Name','Age','Gender'])




details1={"First_Name":['Nahva','shijas','Ranjinee','nafeesathul'],"Last_Name":['C','u','R','Kamaru'] ,"Age":[22,22,21,21],"Gender":['Female','NA','Female','Female']}
df=pd.DataFrame(details1,[1,2,3,4])
df["Name"]=df["First_Name"]+" "+df["Last_Name"]
df[["First_Name","Last_Name","Name","Age","Gender"]]


df.drop("Gender",axis=1,inplace=True)
df.drop(2,inplace=True)
df
df.reset_index()
df
df.reset_index(inplace=True)
ind=[1,2,3]
df["Index"]=ind
df.set_index("Index")
df
df.set_index("Index",inplace=True)
df



outer=["CSE","CSE","CSE","CSE","CSE","CE","CE","IT","IT","IT"]
inner=[1,2,3,4,5,1,2,3,1,2,3]
multi_index=pd.MultiIndex.from_tuples(zip(outer,inner))
multi_index
d={"Names":["Nahva","Mittu","Ranjinee","Nadiya","Nishal","Kamaru","Harsha","Shahma","Shafinaz","Shahana"],"Maths":[71,66,75,69,72,70,85,81,73,83],"Science":[83,73,81,85,70,72,69,75,66,71]}
marklist=pd.DataFrame(d,index=multi_index)

marklist.loc["CE"].loc[2]
marklist.loc["CSE"].loc[[1,2]]
marklist.index.names=["Department","RollNo"]

marklist.loc[[("CSE",2),("CE",2),("IT",2)]]
marklist.loc["CSE"].loc[[2,3],["Names","Maths"]]
marklist.loc["CSE"].loc[[2,3]]
marklist.loc["CSE"].loc[[4,5]]
marklist[(marklist["Maths"]>50) & (marklist["Science"]>70)]
marklist[(marklist["Maths"]>50) & (marklist["Science"]>70)]["Names"]
marklist.loc["CSE"].loc[[2,3],["Maths","Science"]]
marklist

marklist.xs("CSE")
marklist.xs(("CSE",2))
marklist.xs(1,level="RollNo")

new_df=pd.DataFrame(randint(1,100,30).reshape(6,5),index="R1 R2 R3 R4 R5 R6".split(),columns="C1 C2 C3 C4 C5".split())
new_df
result=new_df[new_df>40]
result
result.dropna(thresh=3)
result.dropna(inplace=True)
result.fillna(value=0,inplace=True,axis=1)
result
result[["C4"]].fillna(value=result[["C4"]].mean())
result[["C1","C2","C3","C4","C5"]].fillna(value=result[["C1","C2","C3","C4","C5"]].mean())



d={"Department":["CSE","CSE","IT","CE","CSE","IT","IT","ME","CE","ME"],"Names":["Nahva","Mittu","Kamaru","Harsha","Ranjinee","Nadiya","Nishal","Shafinaz","Shahma","Shahana"],"Total_Marks":[220,230,201,211,246,190,190,200,180,176]}
dep_details=pd.DataFrame(d)
dep_details
dep=dep_details.groupby("Department")
dep.mean(numeric_only=True)
dep.sum(numeric_only=True)
dep.median(numeric_only=True)
dep.count()
dep.max(numeric_only=True)
dep.min(numeric_only=True)
dep.describe()
dep.describe().loc["CSE"]
dep.describe().transpose()
dep.describe().transpose()["IT"]


table1={"A":["A0","A1","A2"],"B":["B0","B1","B2"]}
table2={"C":["C0","C1","C2"],"D":["D0","D1","D2"]}
table3={"E":["E0","E1","E2"],"F":["F0","F1","F2"]}
df1=pd.DataFrame(table1)
df2=pd.DataFrame(table2)
df3=pd.DataFrame(table3)
df1
df2
df3
pd.concat([df1,df2,df3])
pd.concat([df1,df2,df3],axis=1)


left=pd.DataFrame({"key1":["k0","k1","k1","k2"],"key2":["k0","k0","k2","k3"],"A":["A0","A1","A2","A3"],"B":["B0","B1","B2","B3"]})
right=pd.DataFrame({"key1":["k0","k0","k1","k2"],"key2":["k0","k2","k2","k3"],"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"]})
left
right
pd.merge(left,right,how="inner",on=["key1","key2"])
pd.merge(left,right,how="outer",on=["key1","key2"])
pd.merge(left,right,how="left",on=["key1","key2"])
pd.merge(left,right,how="right",on=["key1","key2"])
right.join(left,on=["key1","key2"])



d={"Department":["CSE","CSE","IT","CE","CSE","IT","IT","ME","CE","ME"],"Names":["Nahva","Mittu","Kamaru","Harsha","Ranjinee","Nadiya","Nishal","Shafinaz","Shahma","Shahana"],"Total_Marks":[220,230,201,211,246,190,190,200,180,176]}
dep_details=pd.DataFrame(d)
dep_details.head()
dep_details.tail()
dep_details.info()
dep_details["Department"].unique()
dep_details["Department"].nunique()
dep_details["Department"].value_counts()


def up(name):
    name=name.upper()
    return name
dep_details["Names"].apply(up)
dep_details["Total_Marks"].sum()
dep_details["Total_Marks"].max()
dep_details["Total_Marks"].min()
dep_details["Names"].apply(len)
dep_details.columns
dep_details.index
dep_details.sort_values(by="Total_Marks")



new_df=pd.DataFrame(randint(1,100,30).reshape(6,5),index="R1 R2 R3 R4 R5 R6".split(),columns="C1 C2 C3 C4 C5".split())
new_df
result=new_df[new_df>40]
result.isnull()
result.isnull().sum()


df1=pd.read_csv("C:\\Users\\USER\\Downloads\\example1.csv")
df2=pd.read_csv(r"C:\Users\USER\Downloads\example1.csv")
df3=pd.read_csv("C:/Users/USER/Downloads/example1.csv")
df1
df2
df3


d={"Department":["CSE","CSE","IT","CE","CSE","IT","IT","ME","CE","ME"],"Names":["Nahva","Mittu","Kamaru","Harsha","Ranjinee","Nadiya","Nishal","Shafinaz","Shahma","Shahana"],"Total_Marks":[220,230,201,211,246,190,190,200,180,176]}
dep_details=pd.DataFrame(d)
dep_details.to_csv("department.csv",index=False)
import os
os.getcwd()
pd.read_csv("Department.csv")

df4=pd.read_excel(r"C:\Users\USER\Downloads\Excel_Sample.xlsx",sheet_name="Sheet1")
df4
dep_details.to_excel("sample.xlsx",sheet_name="Sheet1",index=False)


df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
df



#Salaries Exercise

#Import pandas as pd.
import pandas as pd
#Read Salaries.csv as a dataframe called sal.
sal=pd.read_csv(r"C:\Users\USER\Downloads\Salaries.csv")
#Check the head of the DataFrame. 
sal.head()
#Use the .info() method to find out how many entries there are.
sal.info()
#What is the average BasePay ?
sal["BasePay"].mean()
#What is the highest amount of OvertimePay in the dataset ? 
sal["OvertimePay"].max()
#What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
'''employee=sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]
employee["JobTitle"]'''
sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"]
#How much does JOSEPH DRISCOLL make (including benefits)? 
'''employee["TotalPayBenefits"]'''
sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["TotalPayBenefits"]
#What is the name of highest paid person (including benefits)?
sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()]
#What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()]
#What was the average (mean) BasePay of all employees per year? (2011-2014) ?
year=sal.groupby("Year")
year["BasePay"].mean()
#How many unique job titles are there? 
sal["JobTitle"].nunique()
#What are the top 5 most common jobs? 
sal["JobTitle"].value_counts().head()
#How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) 
sal1=sal[sal["Year"]==2013]["JobTitle"].value_counts().to_frame()
sal1[sal1["count"]==1].count()
#How many people have the word Chief in their job title? (This is pretty tricky) 
def chief(a):
    if "Chief" in a:
        return a
sal["JobTitle"].apply(chief).count()
#Bonus: Is there a correlation between length of the Job Title string and Salary? 
sal["Length"]=sal["JobTitle"].apply(len)
sal[["Length","TotalPayBenefits"]].corr()




# Ecommerce Purchases Exercise

#Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. 
import pandas as pd
ecom=pd.read_csv(r"C:\Users\USER\Downloads\Ecommerce Purchases.csv")
#Check the head of the DataFrame.
ecom.head()
#How many rows and columns are there? 
ecom.info()
#What is the average Purchase Price? 
ecom["Purchase Price"].mean()
#What were the highest and lowest purchase prices? 
ecom["Purchase Price"].max()
ecom["Purchase Price"].min()
#How many people have English 'en' as their Language of choice on the website? 
ecom[ecom["Language"]=="en"].count()
#How many people have the job title of "Lawyer" ?
ecom[ecom["Job"]=="Lawyer"].info()
#How many people made the purchase during the AM and how many people made the purchase during PM ? 
ecom["AM or PM"].value_counts()
#What are the 5 most common Job Titles? 
ecom["Job"].value_counts().head()
#Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? 
ecom[ecom["Lot"]=="90 WT"]["Purchase Price"]
#What is the email of the person with the following Credit Card Number: 4926535242672853 
ecom[ecom["Credit Card"]==4926535242672853]["Email"]
#How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?
ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)].count()
#Hard: How many people have a credit card that expires in 2025? 
def credit_card(a):
    if "25" in a:
        return a
ecom["CC Exp Date"].apply(credit_card).count()

sum(ecom["CC Exp Date"].apply(lambda a:a[3:])=="25")

#Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
def providers(a):
    b=a.split("@")
    return b[1]
ecom["Email"].apply(providers).value_counts().head()
