# Práctica 2 - Restful
# Joan Pascual Alcaraz

import random
import requests
import time

for i in range(3): # Simple way to simulate 3 agents
    number = random.randint(0, 9) # Se genera el número aleatorio
    # Se hace un post del número aleatorio en el endpoint correspondiente
    response = requests.post('http://127.0.0.1:5000/addNumber', json = {"n":number})
    time.sleep(1) # Delay para una mejor simulación