user_String = "My name is Ganesh"

print(user_String[0])

slice_String = user_String[:6]   #till char 6 read 
slice_String = user_String[2:] # start from 2 till last
slice_String = user_String[0:6:2] # start from 0 to 6 and jump by every 2

print(user_String.strip())  # will remove unwated spaces from starting and ending

print(user_String.replace("name", 'Name')) # replace old keyword with new keyword

print(slice_String)

userName = "Raj, Sham, Ravi, Shankar"

print(userName.split())  # by default it will split using space

print(userName.split(", ")) # it will split using comma + space

print(user_String.find('a')) # find first position of character else it will return -1

chaiType = "Masala"

chaiQuantity = 2

## we can assign directly data to previous string using {} and .format
myOrder = "i order {} {} tea"

print(myOrder.format(chaiQuantity, chaiType))

print("-".join(userName))


for letter in userName:  #for loop 
    print(letter)

