Write a script that performs the following steps:

Collect the following individual pieces of data from the user:
First name
Last name
City where they live
Their hourly wage
The number of hours they work each week

Present the collected information based on the data input in a format like:

Hi, Firstname Lastname! How are you?
I hope the weather is nice in City.
Based on the information you provided, you earn X dollars per week, approximately Y dollars per month, and Z dollars per year.

#Name: Muhammad Ariff
#Date: 08/08/2022
fn=input("Input your first name: ")
ls=input("Input your last name: ")
city=input("Input the city you live in: ")
hw=float(input("Input your hourly wage: "))
hr=int(input("Number of hours worked each week: "))
x=hr*hw
y=x*4
z=y*12

print(f"Hi {fn.capitalize()} {ls.capitalize()}! How are you?\nI hope the weather is nice in {city.capitalize()} \
\nBased on the info you provided, you earn ${x} per week,approximately ${y} per month and ${z} per year")
