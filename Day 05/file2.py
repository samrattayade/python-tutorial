file='myfile.txt'
with open(file,'w') as file_object:
    file_object.write("Latest Technology Workshop")
file=open('myfile.txt',"r")
print(file.read())
    
