from bs4 import BeautifulSoup as BS
import requests

class Repas:
	titre_jour = ""
	msg = ""
	structure_fermee = False
	entrees = []
	plats = []
	desserts = []
	date =  ""

	def __init__(self, titre_jour, structure_fermee, msg, entrees, plats, desserts):
		self.titre_jour = titre_jour
		self.date = titre_jour[len("Menu du "):]
		self.structure_fermee = structure_fermee
		self.entrees = entrees
		self.plats = plats
		self.desserts = desserts
		self.msg = msg

	def display(self):
		print("----------", self.titre_jour, "----------")
		
		if(self.structure_fermee):
			print(" -->", self.msg)
		
		else:
			print("Entrée : ")
			[print(" -", entree) for entree in self.entrees]
			print("\nPlats : ")
			[print(" -", plat) for plat in self.plats]
			print("\nDesserts : ")
			[print(" -", dessert) for dessert in self.desserts]

class Menu:
	repas = []

	def __init__(self):
		self.repas = []

	def addRepas(self, new_repas:Repas):
		self.repas.append(new_repas)

	def getCurrentDay(self):
		return self.repas[0]

	def getCurrentWeek(self):
		return self.repas[:8]


def makeRequest():
	page = requests.get('http://www.crous-lyon.fr/restaurant/restaurant-jussieu/')
	soup = BS(page.text, 'html.parser')
	day_holder = soup.find(class_='slides')
	les_repas = Menu()

	for elem in day_holder:
		h3 = elem.find("h3")
		if(h3 != -1):
			titre_jour = h3.contents[0]
			entree = []
			plats = []
			desserts = []
			structure_fermee = False
			msg = ""

			repasAll = elem.find(class_='content').findAll("div", recursive=False)
			titres = repasAll[1].findAll(class_='name')
			repas = repasAll[1].findAll("ul")

			if len(titres) == 1:
				structure_fermee = True
				msg = titres[0].contents[0]

			elif len(titres) == 3:
				entree = [elem1.contents[0] for elem1 in repas[0].findAll("li")]
				desserts = [elem1.contents[0] for elem1 in repas[1].findAll("li")]
				plats = [elem1.contents[0] for elem1 in repas[2].findAll("li")]

			else :
				print("Error on titre : ", titres)

			un_repas = Repas(titre_jour, structure_fermee, msg, entree, plats, desserts)
			les_repas.addRepas(un_repas)

	return les_repas
	
def getMenuCurrentDay():
	menu = makeRequest()
	return menu.getCurrentDay()	

def getMenuCurrentWeek():
	menu = makeRequest()
	return menu.getCurrentWeek()	


# def main():
# 	for i in getMenuCurrentWeek():
# 		print(i.display())

# main()
