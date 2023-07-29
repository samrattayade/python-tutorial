f=open("samrat.txt","w")
f.write(input("Enter in txt file: "))
f.close()

f=open("samrat.txt","r")
print(f.read())
