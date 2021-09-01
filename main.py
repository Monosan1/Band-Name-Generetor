name = input("Type your name: ")
print("Hello  "+ name +"! Welcome to heaven \n To find your band name type the following data:")
city = input("Type the city that you was born: ")
pet = input("And now, type the name of your first pet: ")

if len(city) > len(pet):
  print (city + " " + pet)
else:
  print(pet + " " + city) 

