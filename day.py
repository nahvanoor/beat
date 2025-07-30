fav_day=input("enter your fav day")
count=0
today=input("current day")
days_left=int(input("how many days left"))
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
today
days_left
index_of_today=days.index(today)
for i in range(0,days_left):
    x=(index_of_today+i)%7
    if days[x]==fav_day:
        count+=1
count