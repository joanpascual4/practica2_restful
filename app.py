# Práctica 2 - Restful
# Joan Pascual Alcaraz

from flask import Flask, request, jsonify
import random
#Based on: https://realpython.com/api-integration-in-python/

app = Flask(__name__)

numbers = [] # Lista donde se guardan los números aleatorios recibidos
tries = 1 # Número de intentos

def check():
    global tries
    print(numbers)
    # Si ninguno de los números es igual
    if(numbers[0] != numbers[1] and numbers[0] != numbers[2] and numbers[1] != numbers[2]):
        # No hay mayoría, así que se aumentan los intentos
        print("No majority for any number")
        tries += 1
    else:
        # Tenemos mayoría y se imprime el número de intentos
        print("We have reached an agreement! Number of tries: " + str(tries))
        tries = 1 # Se resetean los intentos
    
    numbers.clear() # Se vacía la lista de números tras cada iteración

@app.get("/random")
def get_random_number():
    return jsonify({"random":random.random()})

@app.get("/numbers")
def get_numbers():
    return jsonify(numbers)

@app.post("/addNumber")
def add_number():
    # Si recibimos un JSON
    if request.is_json:
        # Se guarda en un diccionario
        number = request.get_json()
        # Se accede al valor y se guarda en la lista de números
        numbers.append(number["n"])
        print("Received: %i" %number["n"])
        # Si se han recibido 3 números, mirar si hay algún repetido
        if len(numbers) == 3:
            check()
        return number, 201
    return {"error": "Request must be JSON"}, 415

# Save the file as: app.py  #or: export FLASK_APP=app.py
# Run: python -m flask run
# With curl or browser: http://127.0.0.1:5000/random    
# curl -i http://127.0.0.1:5000/addNumber -X POST -H 'Content-Type: application/json' -d '{"seed":2022}'