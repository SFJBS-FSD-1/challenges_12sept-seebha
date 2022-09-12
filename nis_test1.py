"""Challenge 1:  Write a function that takes a natural number
                 as input and outputs the number of digit in it.
                 Conversion of number to string is not allowed"""


def number_of_digits(num):
    count=0
    while num != 0:
        num=num//10
        count += 1
    return count


num=int(input("Enter a natural number:"))
print(f'The number of digits in {num} is {number_of_digits(num)}')

"""Challenge 2:  Write a function that takes a natural number as 
                 input and outputs the reverse of that number. 
                 Conversion of number to string is not allowed"""


def reverse_num(num):
    rev_num=0
    while num != 0:
        n = num % 10
        rev_num = rev_num * 10 + n
        num = num // 10
    return rev_num


num=int(input("Enter a natural number:"))
print("The reversed number is:",reverse_num(num))

"""Challenge 3 : Write a function where user will enter a natural number as 
                 input and output returns the number of zeroes in the end of
                 the factorial of that number.
                 Conversion of number to string is not allowed"""


def fact_of_num(num):
    if num ==1 or num ==0:
        return 1
    else:
        return num*fact_of_num(num-1)


def num_of_zeroes(num):
    factorial=fact_of_num(num)
    count=0
    while factorial!=0:
        n=factorial%10
        if n==0:
            count += 1
        else:
            break
        factorial=factorial//10
    return count


num=int(input("Enter a natural number:"))
print("Number of zeroes at end=",num_of_zeroes(num))

"""Challenge 4 : list1 = ["India" , "England", "Spain"]
list2 = ["Delhi","London","Madrid"]
Write your own function that takes list1 and list2 as inputs and returns a dictionary like
  dict1 = {“India” : “Delhi” , “England”:”London”, “Spain”:”Madrid”}"""


def convert_to_dic(l1,l2):
    dic1={}
    for i in range(len(l1)):
        dic1[l1[i]]=l2[i]
    return dic1


list1 = ["India" , "England", "Spain"]
list2 = ["Delhi","London","Madrid"]
print("dic1 =",convert_to_dic(list1,list2))

"""Challenge 5 :
Given
places = {(“19.07'53.2”, “72.54'51.0”): "Mumbai",
                 (“28.33'34.1”, “77.06'16.6”): "Delhi"}
Write code to create a new dictionary using given dictionary
city = {"Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”},
             “Delhi” : {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”} }
 """

places = {("19.07'53.2", "72.54'51.0"): "Mumbai",
                 ("28.33'34.1", "77.06'16.6"): "Delhi"}
city={}
for k,v in places.items():
    city[v]={"Latitude":k[0],"Longitude":k[1]}
print("city = ",city)



"""Challnege 6 : Given mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
Using for loop find the sum of all even numbers in mylist"""

mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
sum=0
for i in mylist:
    if i%2==0:
        sum=sum+i
print("sum of even numbers in list=",sum)







