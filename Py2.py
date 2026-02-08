 # new_file = open('New_File.txt', 'x')
 #new_file.close()

import os
print("Checking if my_file exist or not....")
if os.path.exists("./myFolder/New_File.txt"):
   os.remove("./myFolder/New_File.txt")
else:
   print("The file does not exist")



os.remove('Codingal.txt')

# os.rmdir('myFolder') 