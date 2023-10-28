import wikipedia

# changer la langue de wikipedia
wikipedia.set_lang("fr")

# Fonction qui permet de recuperer des especes (description, nom, photo) sur wikipedia
def recuperationEspeces(nomEspeces):
    # On recupere le resume de la page wikipedia
    resume = wikipedia.summary(nomEspeces, sentences=1)
    # On recupere le nom de l'espece
    nomEspeces = wikipedia.page(nomEspeces)
    # On recupere l'URL de la page wikipedia
    url = nomEspeces.url
    # On recupere l'image qui correspond a l'espece
    images = nomEspeces.images

    for image in images:
        if nomEspeces.title in image:
            image = image
            break
        

    print(image)

    # On retourne le resume, le nom de l'espece, l'URL et l'image

    #print(nomEspeces.content)


    return resume, nomEspeces, url, image

# affichage des informations
recuperationEspeces("lion animal")