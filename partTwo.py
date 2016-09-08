users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key,data in users.items():
 	print key
 	number = 0

  	for value in data:
  		number += 1
  		full_name = (value["first_name"] + " " + value["last_name"]).upper()
		length = len(value["first_name"]) + len(value["last_name"])
		print str(number) +"-"+ full_name +"-"+ str(length)
		
#Fantastic use of the for key,data in users.items() loop!
