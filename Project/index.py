with open('File.txt', 'w') as file:
    file.write("Hi! I am peter and i'm learning to code")
file.close()

with open('File.txt', 'r') as file:
   data = file.readlines()
   print("Words in this file are....")
   for line in data:
       words = line.split()
       print (words)
file.close()      