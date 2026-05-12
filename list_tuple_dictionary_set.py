# userlist = [1,2,3,4,5]

# userlist.append(10)

# userlist[2] =5

# print(userlist)

# usertuple = (1,2,3,4,5)

# userset = {1,2,3,2,1}


# print(userset)

# userset.add(19)

# print(userset)

# userdictionary = dict["a": 1, "b":2]

# print(userdictionary)


# studentName = ['A','B','C','D','E']

# studentName.append('F')

# studentName.remove('B')

# studentName[2] = 'B'

# print(studentName.__len__())

# studentName.sort()

# studentName.reverse()

# print(studentName)

# studentMarks = [1,2,3,4,5]

# MCount = sum(studentMarks)

# MLength = studentMarks.__len__()

# mAverage = MCount/MLength

# print(mAverage)

# print(MCount)


# City = ('A','B','C','D','E')

# print(City[1])

# print(City.count('B'))

# print(City.index('C'))

# tupleTolist = list(City)

# print(tupleTolist)

# usetSet = {1,2,3,4,3,2}

# usetSet.add(5)

# usetSet.remove(1)

# print(usetSet)

# u1 = {1,3,5,7,1,8}

# u2 = {2,4,6,8,0}

# print(u1.union(u2))

# print(u1.intersection(u2))

# print(u1.difference(u2))

# print(u1)

# studentDictonary = {'A': 10, 'B': 12, 'C': 8}

# studentDictonary['D']= 13

# studentDictonary.pop('B')

# print(studentDictonary)

# print(studentDictonary.keys())

# print(studentDictonary.values())

# print(max(studentDictonary.values()))

# print(studentDictonary)

###################################################################################################################

StudentData = {}


StudentData= {
    "Rahul":{
        "Maths" :3,
        "Science": 15
    },
    "Raj":{
        "Maths" :8,
        "Science": 9
    },
    "Rahim":{
        "Maths": 2,
        "Science": 9
    },
    "Ravi":{
        "Maths" :5,
        "Science": 7
    },
    "Karan":{
        "Maths" :1,
        "Science": 9
    }
}

StudentData["Karan"]["Science"] = 11

StudentData.pop("Karan")

print(StudentData)