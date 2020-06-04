#! python3
#Determine's Vinny's schedule for the day based on his wake time and emails the schedule to mom and dad

import datetime, smtplib, ssl
from prettytable import PrettyTable

def formatTime(dt):
    return dt.strftime('%I:%M')

def formatDay(dt):
    return dt.strftime('%m/%d')

def sendEmail(content):
    port = 587  # For starttls
    smtp_server = 'smtp.gmail.com'
    sender_email = 'pythonjoed@gmail.com'
    receiver_email = [open('C:\\Users\\User\\Desktop\\distribution_list.txt').read()]
    password = open('C:\\Users\\User\\Desktop\\pw.txt').read()
    message = 'Subject: {}\n\n{}'.format(content.title, content.get_string())

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

currentTime = datetime.datetime.now()

tbl = PrettyTable()
tbl.title = 'Vinny\'s Schedule - ' + formatDay(currentTime)
tbl.field_names = ['Activity', 'Time']

curYear = currentTime.year
curMonth = currentTime.month
curDay = currentTime.day
wakeTime = datetime.datetime(curYear, curMonth, curDay, 7, 45, 0)

formula_1 = wakeTime + datetime.timedelta(minutes= 15)
nap_1_start = formula_1 + datetime.timedelta(hours = 2)
nap_1_end = nap_1_start + datetime.timedelta(hours = 1, minutes= 30)
formula_2 = nap_1_end + datetime.timedelta(minutes= 15)
solid_food_1 = formula_2 + + datetime.timedelta(hours=1, minutes= 15)
nap_2_start = solid_food_1 + datetime.timedelta(minutes= 45)
nap_2_end = nap_2_start + datetime.timedelta(hours= 1, minutes= 30)
formula_3 = nap_2_end + datetime.timedelta(minutes= 15)
solid_food_2 = formula_3 + datetime.timedelta(hours=1, minutes= 15)
nap_3_start = solid_food_2 + datetime.timedelta(hours= 1)
nap_3_end = nap_3_start + datetime.timedelta(minutes= 45)
formula_4 = nap_3_end + datetime.timedelta(minutes= 15)
solid_food_3 = formula_4 + datetime.timedelta(hours=1)

#The following should never change, regardless of what time Vinny starts his day
bath = datetime.datetime(curYear, curMonth, curDay, 8, 0, 0)
formula_5 = datetime.datetime(curYear, curMonth, curDay, 8, 30, 0)
book = datetime.datetime(curYear, curMonth, curDay, 8, 45, 0)
bedtime = datetime.datetime(curYear, curMonth, curDay, 9, 0, 0)

tbl.add_row(['Wake', formatTime(wakeTime)])
tbl.add_row(['Formula', formatTime(formula_1)])
tbl.add_row(['Nap', formatTime(nap_1_start) + ' - ' + formatTime(nap_1_end)])
tbl.add_row(['Formula', formatTime(formula_2)])
tbl.add_row(['Solid Food', formatTime(solid_food_1)])
tbl.add_row(['Nap', formatTime(nap_2_start) + ' - ' + formatTime(nap_2_end)])
tbl.add_row(['Formula', formatTime(formula_3)])
tbl.add_row(['Solid Food', formatTime(solid_food_2)])
tbl.add_row(['Nap', formatTime(nap_3_start) + ' - ' + formatTime(nap_3_end)])
tbl.add_row(['Formula', formatTime(formula_4)])
tbl.add_row(['Solid Food', formatTime(solid_food_3)])
tbl.add_row(['Bath', formatTime(bath)])
tbl.add_row(['Formula', formatTime(formula_5)])
tbl.add_row(['Book', formatTime(book)])
tbl.add_row(['Bedtime', formatTime(bedtime)])



print(tbl)
sendEmail(tbl)