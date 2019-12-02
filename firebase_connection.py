from firebase import firebase

firebase = firebase.FirebaseApplication("https://nupokushaembot.firebaseio.com/", None)

# Add new items

"""data1 = {
	'Name': 'Happy Fox Coffee',
	'Number of reviews': 11,
	'Rating': 3.9,
	'Type': 'Coffee shop',
	'Location': 'Block 38',
	'Working time': '09:00-20:00',
	'Manager phone number': 87758581629
}

data2 = {
	'Name': 'Kunde Social Cafe',
	'Number of reviews': 114,
	'Rating': 4.5,
	'Type': 'Restaurant',
	'Location': 'Block C3',
	'Working time': '09:00-19:00',
	'Manager phone number': 87079525082
}

data3 = {
	'Name': 'Midpoint Cafe & Catering',
	'Number of reviews': 64,
	'Rating': 4.0,
	'Type': 'Restaurant',
	'Location': 'Block C2',
	'Working time': '08:00-19:00',
	'Manager phone number': 87053340905
}

data4 = {
	'Name': 'La Tartine',
	'Number of reviews': 19,
	'Rating': 3.9,
	'Type': 'Cafe',
	'Location': 'Block 3',
	'Working time': '08:00-18:00',
	'Manager phone number': 87172706683
}

data5 = {
	'Name': 'Health Project',
	'Number of reviews': 3,
	'Rating': 4.7,
	'Type': 'Canteen',
	'Location': 'Block 20',
	'Working time': '00:00-24:00',
	'Manager phone number': 87074625563
}

data6 = {
	'Name': '6\'\'Inch',
	'Number of reviews': 0,
	'Rating': 0.0,
	'Type': 'Coffee shop',
	'Location': 'Block C3',
	'Working time': '09:00-19:00',
	'Manager phone number': 87079525082
}

data7 = {
	'Name': 'Бодрый День',
	'Number of reviews': 4,
	'Rating': 5.0,
	'Type': 'Coffee shop',
	'Location': 'New Upper Atrium',
	'Working time': '08:00-19:00',
	'Manager phone number': 87014046742
}

data8 = {
	'Name': 'Health Project Cafe',
	'Number of reviews': 0,
	'Rating': 0.0,
	'Type': 'Coffee shop',
	'Location': 'New Upper Atrium',
	'Working time': '08:00-22:00'
}

data9 = {
	'Name': 'Free Flow',
	'Number of reviews': 0,
	'Rating': 0.0,
	'Type': 'Canteen',
	'Location': 'Block 22',
	'Working time': '08:00-22:00'
}

data10 = {
	'Name': 'Marketplace',
	'Number of reviews': 0,
	'Rating': 0.0,
	'Type': 'Canteen',
	'Location': 'Block 4',
	'Working time': '08:00-20:00'
}

data = {
	'Name': 'Daily Cup',
	'Number of reviews': 0,
	'Rating': 0.0,
	'Type': 'Coffee shop',
	'Location': 'New Atrium',
	'Working time': '08:00-22:00',
	'Food': ['Coffee', 'Dessert']
}"""

# Update items

"""firebase.put('/nupokushaembot/FoodPlace/-Lv4MAUC-rD-gR79GRtV', 'Food', ['Coffee', 'Fast Food', 'Dessert', 'Sushi'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MAfWT5DpD1xeAIhI', 'Food', ['Coffee', 'Dessert', 'Breakfast', 'Lunch', 'Fast Food'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MAruWL6cBDWQvIIP', 'Food', ['Coffee', 'Dessert', 'Breakfast', 'Lunch'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MB60U9bzcUzhXwWt', 'Food', ['Coffee', 'Dessert', 'Fast Food'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MBIgL6k2f5ujAM6X', 'Food', ['Coffee', 'Dessert', 'Breakfast', 'Lunch', 'Fast Food'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MBWxe7BhDT9PpGKA', 'Food', ['Coffee', 'Dessert', 'Fast Food'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MBjwQds5vxVfweI8', 'Food', ['Coffee', 'Dessert', 'Fast Food'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MBw9-gGgsX3NEb2h', 'Food', ['Coffee', 'Dessert', 'Lunch', 'Fast Food'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MC7hyXL9TQm27ekU', 'Food', ['Breakfast', 'Lunch'])
firebase.put('/nupokushaembot/FoodPlace/-Lv4MCK8znVcd8VI9njz', 'Food', ['Fast Food', 'Dessert', 'Breakfast', 'Lunch'])"""

# Get item

print(firebase.get('/nupokushaembot/FoodPlace', '-Lv4MAUC-rD-gR79GRtV'))
