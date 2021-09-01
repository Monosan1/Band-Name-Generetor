#This is where you started, first of all, say your name
name = input("Whats your name? ")

#Print to the user whats this program do

print("Hello  "+ name +"! Welcome my first python project \n To find whats your band name type the following data:")

#Get the 2 information that we need

city = input("Type the city that you was born: ")
pet = input("And now, type the name of your first pet: ")

#And basead on the length (len()) of the answers, it switches the order

if len(city) > len(pet):
  print ("Your band name is: " + city + " " + pet)
else:
  print("Your band name is: " + pet + " " + city) 

#Thats it, thanks for passing by xD