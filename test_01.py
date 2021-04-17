import requests
from bs4 import BeautifulSoup

#with open("doc.html") as fp:
 # soup = BeautifulSoup(fp, "html.parser")



'''
url = 'https://www.bop.gov/inmates/custody_and_care/female_offenders.jsp'
myobj = {'rollout_tracking': ''}

x = requests.post(url, data = myobj)

print(x.text)
# please ignore the aformentioned.


# my hope here is to create a class that we can mass replicate per user.

#page = soup.find('Women').getText()
#wanted_text = BeautifulSoup(html, 'html.parser')

aforementioned is prior to 04/14/2021

'''
'''
import json
import csv

with open ("02_scvs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"name": []}
    for row in reader:
        data["name"].append({"name":
        row[0], "website": row[1]})
    print(data)

[
  {
    "name": "Ryan Health",
    "wesite": "https://ryanhealth.org/",
    "description": "Ryan Health delivers exceptional primary care to our patients, as well as a range of services from women's health and pediatrics, to behavioral health, HIV care, and chronic disease management.",
    "location": "New York City",
    "phone": "212-749-1820",
    "email": "communityoutreach@ryanhealth.org",
    "subcategory": "health_scvs",
    "param 1": "primary_care",
    "param 2": "insurance",
    "param 3": "",
    "param 4": ""
  },
  {
    "name": "Healthfirst",
    "wesite": "https://hfrepdirectory.healthfirst.org/?",
    "description": "Connecting you and your family to health insurance plans and resources that meet your needs.",
    "location": "All 5 boroughs of New York City",
    "phone": "844-488-1486",
    "email": "N/A",
    "subcategory": "health_scvs",
    "param 1": "primary_care",
    "param 2": "insurance",
    "param 3": "",
    "param 4": ""
  },
  {
    "name": "Workforce1",
    "wesite": "https://dol.ny.gov/location/brooklyn-workforce1-career-center",
    "description": "We help New Yorkers find the careers they will love by connecting them to new job opportunities, referring them to training opportunities that build their skills, and by ensuring they are paid the proper wage and have a safe working environment when they're on the job.",
    "location": "New York State (Brooklyn, NY location)",
    "phone": "718-246-5219",
    "email": "mailto:Workforce1Brooklyn@grantassociatesinc.com",
    "subcategory": "job_scvs",
    "param 1": "full_time",
    "param 2": "part_time",
    "param 3": "temporary",
    "param 4": "permanent"
  },
  {
    "name": "",
    "wesite": "",
    "description": "",
    "location": "",
    "phone": "",
    "email": "",
    "subcategory": "housing_scvs",
    "param 1": "income",
    "param 2": "duration",
    "param 3": "single_occupancy",
    "param 4": "comm_housing"
  }
]

class services:
    def __init__(self, name, website, description, location, phone, email):
        self. name = name
        self.website = website
        self.description = description
        self.location = location
        self.phone = phone
        self.email = email



    def housing_scvs(self, income, duration, single_occupancy, comm_housing):
        self.website = income
        self.duration = duration
        self.single_occpancy = single_occupancy
        self.comm_housing = comm_housing


    def job_scvs(self, full_time, part_time, temporary, permanent):
        self. full_time = full_time
        self.part_time = part_time
        self.temporary = temporary
        self.permanent = permanent



    def health_scvs(self, primary_care, insurance):
        self.primary_care = primary_care
        self.insurance = insurance

'''









'''
class user:
    def __init__(self, name, age, need_1):
        self.name = string(name)
        # I am not sure how to print out the type method here to verify why I am getting the error of user_00.name = Shawn
        #is not defined. 
        
        self.age = float(age)
        self.need_1 = need_1
       # self.need_2 = need_2- Robert/Tanya's area
        #self.need_3 = need_3- Tanya/Robert's area 

#user_00 = user(name, age, need_1, need_2, need_3)



#I have found a sample outline that I am using to create an outline for questions to get a gague of each new user.
#I know from my own story that what I thougt I needed wasn't always what I needed.


need_1 = "This is a task for Shawn."
user_00.name = Shawn
user_00.age = 34
user_00.need_1 = print(f'We want to start with {need_1}')
#user_00.need_2 = "thanks"
u#ser_00.need_3 = 'you are welcome'

user_00 = user()
print(user_00)


'''

### this is the main source that I will be using. 
#https://www.careercenteroffices.com/brooklyn-ny/

url = 'https://www.careercenteroffices.com/brooklyn-ny/' 
myobj = {'rollout_tracking': ''}

x = requests.post(url, data = myobj)

print(x.text)
# please ignore the aformentioned.

import time
import random

greeting_reply = ['thank you for choosing our team.']



hey_there = "Hey There."
print(hey_there.center(40, '-'))
time.sleep(2)
print("WE CAN PLACE TEAM TEXT HERE")
time.sleep(2)
print("We would like for you to take a few moments and complete a survey.")
time.sleep(2)
print('This survey will outline target areas for planned resolution.')
time.sleep(4)
print('intro and obtain vital info here')
time.sleep(2)
print('store values here')

name = input('What is your name? ')

print(f'thanks {name}. We are ready to begin')

time.sleep(5)
print(f'{name}, this is one of the first steps to rebuilding the life you want to live. Here at, TEAM NAME, we\npartner with...')

team_mate =  html/body/footer/div[1]/div[2]/p style='margin-top:2020px:'

print(team_mate)
### Joseph this is where I am having my error. When I am able to resolve this I will be able to complete my 10 questions and post to repo prior to monday. 









"Are you on any form of supervised probation? "

"When was you last medical evaluation? "
"How many days have you secured lodging at for the next week ?"
"Do you curently have any of the following: ...Each one of us can add something"





