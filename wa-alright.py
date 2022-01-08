import pandas as pd
from alright import WhatsApp
messenger = WhatsApp()


# can also index sheet by name or fetch all sheets
df = pd.read_excel('contacts.xlsx')
mylist = df['Number'].tolist()

numbers = mylist
for number in numbers:
    messenger.find_user(number)
    messenger.send_message("Hallo")
