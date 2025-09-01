import json
import random
import string
from pathlib import Path
import streamlit as st

class Bank:
    database = 'data.json'
    data = []

    # Load data
    try: 
        if Path(database).exists() and Path(database).stat().st_size > 0:
            with open(database) as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        st.error(f"An exception occurred: {err}")

    @classmethod    
    def __update(cls):
        with open(cls.database,'w') as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def find_user(cls, accnumber, pin):
        return [i for i in cls.data if i['accountNo'] == accnumber and i['pin'] == pin]

    def Createaccount(self, name, age, email, pin):
        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }
        if info["age"] < 18 or len(str(info['pin'])) != 4:
            return None
        else:
            Bank.data.append(info)
            Bank.__update()
            return info

    def depositmoney(self, accnumber, pin, amount):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return None
        if amount > 10000 or amount < 0:
            return False
        userdata[0]['balance'] += amount
        Bank.__update()
        return userdata[0]

    def withdrawmoney(self, accnumber, pin, amount):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return None
        if userdata[0]['balance'] < amount:
            return False
        userdata[0]['balance'] -= amount
        Bank.__update()
        return userdata[0]

    def showdetail(self, accnumber, pin):
        userdata = Bank.find_user(accnumber, pin)
        return userdata[0] if userdata else None

    def updatedetail(self, accnumber, pin, name=None, email=None, newpin=None):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return None
        if name: userdata[0]['name'] = name
        if email: userdata[0]['email'] = email
        if newpin: userdata[0]['pin'] = newpin
        Bank.__update()
        return userdata[0]

    def Delete(self, accnumber, pin):
        userdata = Bank.find_user(accnumber, pin)
        if not userdata:
            return None
        Bank.data.remove(userdata[0])
        Bank.__update()
        return True
