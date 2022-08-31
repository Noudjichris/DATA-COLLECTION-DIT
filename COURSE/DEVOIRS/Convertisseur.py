import json
import requests
import csv

class Convertisseur_Devise:
    
    taux = {}
    def __init__(self, url):
        response = requests.get(url)
        data = response.text
        taux = json.loads(data)
 
    def convertir(self, devise_initiale, devise_finale, montant):
        initial_montant = montant
      
        montant = montant * int(self.taux[devise_initiale])
 
        montant = round(montant * self.taux[devise_finale], 2)
        return montant

    def convertToCsv(self, devise_initiale, devise_finale, montant_initial,montant_final):
        with open('devise.csv','w') as f:
            write=csv.writer(f)
            list = [
                str.__add__(montant_initial.Text,devise_initiale),
                str.__add__(montant_final.Text,devise_finale),
            ]
            write.writerows(list) 

if __name__ == "__main__":
 
    url = "https://v6.exchangerate-api.com/v6/d5fd5dbec721882963498a48/latest/USD"#str.__add__('http://data.fixer.io/api/latest?access_key=', key) 
    c = Convertisseur_Devise(url)
    devise_initiale = "USD"
    devise_finale = "EUR"
    montant_initial = 10
 
    montant_final=c.convertir(devise_initiale, devise_finale, montant_initial)
    print('{} {} = {} {}'.format(montant_initial, devise_initiale, montant_final, devise_finale))
        
    c.convertToCsv(devise_initiale, devise_finale, montant_initial, montant_final)