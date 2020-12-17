# this program is read credit card transaction and calculate resposne time and send alert after specified tereshold
print("let's see what is going on in transactions")
card_list = []
for i in range(100):
    card_list.append(i)
print(card_list)
fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')

import pygal
results = { 1:18, 2:16, 3:18, 4:17, 5:18, 6:13, }
chart = pygal.Bar()
chart.force_uri_protocol = 'http'
chart.x_labels = results.keys()
chart.add('D6', results.values())
chart.render_to_file('rolling_dice.svg')

f_path = 'alice.txt'
f = open("alice.txt", "a")
f.write("list of card")
with open(f_path) as f_obj:
    lines = f_obj.readlines()
    print(f_obj)
