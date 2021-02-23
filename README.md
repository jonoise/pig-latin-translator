# Pig Latin Translator
En este proyecto desarrollé un traductor para convertir cualquier idioma a [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin).
QUÉ? PIG LATIN? Qué carajos? Pues sí. Resulta que navegando por la red me encontré este artículo de Wikipedia sobre el [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin). Básicamente el Pig Latin consiste en sustraer la primera letra de una palabra y añadirle el sufijo "ay" y colocar ese nuevo string al final de la palabra:

* "pig" = "igpay"
* "latin" = "atinlay"
* "banana" = "ananabay"
* "smile" = "ilesmay"
* "string" = "ingstray"
* "stupid" = "upidstay"

Originalmente el Pig Latin es un idioma inventado por angloparlantes por lo que tiene mejor musicalidad cuando se traduce desde el Inglés, pero usándolo con frases en español también combina muy bien. 

onCay steeay rogramapay ayay uedenpay ablarhay omocay oslay erdoscay ueqay onsay ajajajay    

# Instalación

* Clona el repo:
```
$ git clone https://github.com/soloamilkar/pig-latin-translator
```

* Haz el llamado a la función de_humano_a_pig_latin() con un string de texto dentro y corre el programa.
```python
de_humano_a_pig_latin("Este es mi texto en español, para ser traducido a pig latin")
```

* También hice una función para traducir de pig latin a humano. Voy a convertirlo en un programa que acepte argvs para ejecutarlo desde la terminal.
