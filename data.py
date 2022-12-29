import json
import csv


def add_account(user, passw):
  with open("passwords.csv", "a") as file:
    writer = csv.writer(file)
    if (exists(user, passw) == False):
      writer.writerow([user, passw])
      return("account created")
    else:
      return("username aleady exists")


def check_creds(user, passw):
  with open("passwords.csv", "r") as file:
    reader = csv.reader(file)
    accounts = []
    for i in reader:
      accounts.append(i)
    for i in accounts:
      if i[0] == user:
        if i[1] == passw:
          return("logged in as " + user)
    return("invalid username or password")


def exists(user, pasw):
  with open("passwords.csv", "r") as file:
    reader = csv.reader(file)
    accounts = []
    for i in reader:
      accounts.append(i)
    for i in accounts:
      if i[0] == user:
        return(True)
    return(False)
        
