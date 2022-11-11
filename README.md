Práctica 2 - Restful
Joan Pascual Alcaraz

Programa implementado en Python usando la arquitectura Restful con la librería 
Flask para simular una comunicación asíncrona entre agentes con el objetivo de 
llegar a un consenso en la elección de un número aleatorio. El número aleatorio 
se elige cuando hay una mayoría.

Para simplificar la ejecución, he implemetado los 3 agentes de modo que solo es 
necesario lanzar el programa en una terminal, el código se encarga de repetir su 
ejecución 3 veces. En primer lugar, lanzar el programa app.py con el siguiente 
comando: "python -m flask run". Una vez el servidor está en marcha, se puede lanzar 
el programa agent.py, que generará 3 números aleatorios y los enviará al servidor 
con 1 segundo de diferencia entre ellos. Una vez la aplicación ha recibido los 
3 números, procede a comparar si hay mayoría en la elección o no. En caso 
afirmativo, Muestra por consola el número de intentos que ha llevado. En caso 
contrario, muestra por consola que no hay consenso y se debe volver a lanzar 
el agente manualmente para volver a generar los números.
