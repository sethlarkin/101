
#file_p = open("test.txt","r")
#print(file_p.nextLine())

new_file = open("new_file.txt","r")

#open file
with open("test.txt","r") as f:
    for line in f:
        print(line)
        new_file.write(line + "__NEW FILE")
#for line in file_p:
#    print(line)
