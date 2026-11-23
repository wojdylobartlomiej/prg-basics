categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
pom=0
max=0
i=0
for i in range(len(expenses)):
    if expenses[i] > pom:
        max=i
        pom=expenses[i]
    else:
        continue
    i=+1
print(categories[max])