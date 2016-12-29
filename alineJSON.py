from sys import argv
import json
script, filename = argv
placate = "Aline's Favorites\n"
favorites = []
exit = False
f = open(filename, 'r')
favorites = json.load(f, encoding="UTF-8")
print placate, favorites
prompt = "Enter another of Aline's favorites, or y to exit.\n" 
exit_response =  raw_input(prompt) 
while (exit == False):
	if exit_response == "y":
		exit = True
		target = open(filename, 'w')
		json.dump(favorites, target, encoding="UTF-8")
		target.close()
		print("Thank You")
	else: 
		exit = False
		favorites.append(exit_response)
		print placate, favorites 
		exit_response = raw_input(prompt)