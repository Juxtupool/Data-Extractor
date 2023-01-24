from sys import argv
from os.path import exists
from datetime import datetime

script, file, new = argv

#user info
prompt=">"
print("Enter Your name: ")
user=input(prompt)

#date and time 
timestamp = 1674556568.0382988 
date_time = datetime.fromtimestamp(timestamp)
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")

#file open and read
data=open(file)
in_data=data.read()

print(f'{user} your file info is begin exported...\n')
#file write
export=open(new,'w')
export.write(in_data)

print(f'{file} file data will be deleted in a moment')
print('Type yes or no')
x=input('>').lower()

if x=='yes':
 	target=open(file,'w')
 	target.truncate()
 	target.write(f'All of data has been deleted by User {user} at {str_date_time}')
 	print(f'\nData of your file {file} has been deleted')
 	print('\nGood luck!')
 	export.close()
 	data.close()
 	exit()
else:
 	print('\nGood Bye!')
exit()
