import wikipedia
import re


# changer la langue de wikipedia
wikipedia.set_lang("fr")

# Fonction qui permet de recuperer des especes (description, nom, photo) sur wikipedia
def recuperationEspeces(nomEspeces):
    try:
        # On recupere le resume de la page wikipedia
        resume = wikipedia.summary(nomEspeces, sentences=1)
        # On recupere le nom de l'espece
        nomEspeces = wikipedia.page(nomEspeces)
        # On recupere l'URL de la page wikipedia
        url = nomEspeces.url
        # On recupere l'image qui correspond a l'espece
        images = nomEspeces.images
        print(images)

        for image in images:
    # Utilisation d'une expression régulière pour vérifier si l'image correspond aux critères
    # critères : .jpg ou .png pas de logo wikipedia doit contenir le nom de l'espece 
            if image.endswith(".jpg") or image.endswith(".png") and "logo" not in image and nomEspeces.title in image:
                print("image : ", image)
                cheminImage = image
                break



        
        print("nomEspeces : ", nomEspeces)
        print("url : ", url)
        print("image : ", cheminImage)
        print("resume : ", resume)


        # On retourne le resume, le nom de l'espece, l'URL et l'image

        #print(nomEspeces.content)


        return resume, nomEspeces.title, url, image
    except:
        print("Erreur lors de la recuperation des especes")
        return None

liste_animaux = ["Abeille","Abeille charpentière","Abyssin","Accenteur mouchet","Addax","Agame Barbu","Agame des colons","Agouti doré","Agouti ponctué","Aigle royal","Aigrette Garzette","Ailurops","Akhal téké doré","Akita americain","Akita Inu","Albatros hurleur","Alligator d'Amérique","Alouette des champs","Alpaga","American curl","American staff","Anaconda vert","Ane de Provence","Ane grand noir du Berry","Ane sauvage d'Asie","Ane sauvage de Somalie","Angora Turc","Anhinga","Antilope à nez tacheté","Antilope Cervicapre","Antilope du Tibet","Appaloosa","Ara de Spix","Ara hyacinthe","Ara jaune et Bleu","Ara rouge","Araçari d'Azara","Ardennais","Argiope frelon","Argus bleu","Atèle noir de Colombie","Atlas","Aubrac","Autruche","Axolotl","Aye-Aye","Babiroussa","Babouin anubis","Babouin olive","Baleine à bosse","Baleine bleue","Baleine grise","Balinais","Bandicoot lapin","Barbican à tête rouge","Baribal","Barzoï","Basenji","Basilic vert","Basset Hound","Bateleur des savanes","Baudet du Poitou","Beagle","Beauceron","Bec en sabot","Belette","Belle-Dame","Béluga","Bengal","Berger Allemand","Berger Australien","Berger blanc Suisse","Berger d'Anatolie","Berger d'Ecosse","Berger d'Islande","Berger de Beauce","Berger de Brie","Bergeronnette grise","Bernache du Canada","Biche des palétuviers","Bichon Maltais","Bihoreau gris","Bilby","Binturong","Bison d'Amérique du Nord","Blaireau d'Amérique","Blaireau d'Europe","Blesbok","Bleu russe","Bobcat","Bobtail","Boeuf musqué","Bondrée apivore","Bongo","Bonobo","Border-collie","Boto","Bouledogue Anglais","Bouledogue Français","Bouquetin des Alpes","Bourdon terrestre","Bouvier Bernois","Bouvreuil pivoine","Boxer","Braque Allemand","Braque de Weimar","Briard","British shorthair","Brochet","Brumby","Bubale de Coke","Buffle d'Afrique","Buffle d'Asie","Buffle d'eau","Bulldog Anglais","Burmese","Buse à épaulettes","Buse variable","Butor étoilé","Cabiaï","Cacatoès à huppe jaune","Cacatoès funèbre","Cacatoès noir","Cacatoès rosalbin","Cachalot","Caille des blés","Caïman à lunettes","Calao à cimier","Calao bicorne","Calao leucomèle","Calao terrestre","Calliste septicolore","Camargue","Caméléon panthère","Campagnol roussâtre","Canard branchu","Canard mandarin","Cane corso","Caniche","Capucin brun","Capybara","Caracal","Caracara huppé","Carcajou","Cardinal rouge","Cariacou","Caribou","Carlin","Casoar à casque","Castor d'Europe","Cavalier King Charles","Céphalophe zébré","Cercopithèque de Brazza","Cercopithèque de Wolf","Cerf axis","Cerf de Virginie","Cerf elaphe","Cerf-souris","Cétoine dorée","Chacal à dos noir","Chameau de bactriane","Chamois","Chardonneret élégant","Charolaise","Chartreux","Chat de Pallas","Chat de temminck","Chat des sables","Chat marsupial","Chat pêcheur","Chat sauvage","Chat-huant","Chauve souris géante","Chevêche d'Athéna","Chèvre des montagnes rocheuses","Chèvre naine","Chevreuil","Chevrotin de Balabac","Chien chinois à crête","Chien de prairie","Chien des buissons","Chien du Groenland","Chien viverrin","Chien-loup Tchécoslovaque","Chihuahua","Chimpanzé","Chinchilla","Chiru","Chirurgien bleu","Chital","Chouette chevêche","Chouette effraie","Chouette Hulotte","Chouette lapone","Chow-Chow","Cigale commune","Cigogne blanche","Cigogne noire","Cincle plongeur","Circaète Jean Leblanc","Civette de Malaisie","Clydesdale","Coati à nez blanc","Coati à queue annelée","Cob irlandais","Cobe à croissant","Cobra royal","Coccinelle à 7 points","Cocker Anglais","Colibri d'Anna","Colibri porte-épée","Colley à poil long","Colobe d'Angola","Comtois","Condor des Andes","Condylure à nez étoilé","Connemara","Coq de roche","Coracine casquée","Corbeau freux","Cormoran pie","Corneille noire","Cornish rex","Cotinga de Cayenne","Coton de Tuléar","Coucou geai","Couleuvre Rayée","Couleuvre verte et jaune","Couscous des célèbes","Couscous tacheté","Coyote","Crabe des cocotiers","Crabe rouge de rocher","Crapaud d'Amérique","Criocère du lis","Crocodile du Nil","Crotale cascabelle","Cygne à cou noir","Cygne chanteur","Cygne noir","Cygne tuberculé","Daim","Dalmatien","Damalisque","Daman du Cap","Dasyure","Dauphin pilote","Dauphin rose d'Amazonie","Dauphin souffleur","Deerhound","Dendrobate bleue","Dendrobate fraise","Dendrolague","Desman","Dhole","Diable cornu","Diable de tasmanie","Dik dik","Dindon","Dingo","Doberman","Dodo","Dogue Allemand","Dogue de Bordeaux","Dogue du Tibet","Doryphore","Douc","Draco volans","Dragon d'Australie","Dragon de Komodo","Dromadaire","Dugong","Echasse blanche","Echidné à nez court","Ecureuil de Barbarie","Ecureuil de Prévost","Ecureuil du Yucatan","Ecureuil fouisseur du Cap","Ecureuil Géant d'Inde","Ecureuil gris","Ecureuil roux","Eider à lunettes","Elan","Eland du Cap","Elephant d'Afrique","Elephant d'Asie","Elephant de mer","Emeu d'Australie","Entelle d'Hanuman","Epeire fasciée","Etourneau améthyste","Etourneau sansonnet","Eurasier","Eurylaime de Gould","Eyra","Faisan de Colchide","Faucon crécerelle","Faucon pèlerin","Fauvette mélanocéphale","Fell","Fennec","Fjord","Flamant nain","Flamant rose","Fossa","Fou à pieds bleus","Fou de Bassan","Fouine","Frégate superbe","Frelon asiatique","Frelon européen","Frison","Galago du Sénégal","Gallinule poule d'eau","Gavial","Gazelle de Thomson","Geai bleu","Geai des chênes","Géant des Flandres","Gecko du midi","Gecko géant de Madagascar","Gélada","Gendarme","Genette commune","Gerenuk","Gibbon lar","Girafe","Globicéphale noir","Glouton","Gnou bleu","Goéland argenté","Golden retriever","Gorfou sauteur","Gorge bleue à miroir","Gorille","Goujon","Goundi de l'Atlas","Goura couronné","Grand cormoran","Grand Danois","Grand duc bruyant","Grand duc indien","Grand koudou","Grandala bleu","Grande aigrette","Grèbe huppé","Grenouille fraise","Grenouille Taureau","Grenouille verte","Grillon champêtre","Gris du Gabon","Grizzly","Groenendael","Groenlandais","Grue Antigone","Grue Caronculée","Grue Couronnée","Grue du Japon","Guanaco","Guépard d'Afrique","Guépard d'Asie","Guêpe commune","Guêpier d'Europe","Guira cantara","Gypaète barbu","Haflinger","Hamadryas","Hamster d'Europe","Harfang des neiges","Harpie féroce","Hémione","Henson","Hérisson","Hermine","Héron cendré","Héron garde-boeufs","Héron vert","Hibou grand-duc","Hippopotame","Hippotrague noir","Hirondelle bicolore","Hirondelle rustique","Hoazin hupée","Hocco nocturne","Huppe fasciée","Husky","Hydropote","Hyène brune","Hyène rayée","Hyène tachetée","Hylochère","Ibijau gris","Ibis chauve","Ibis rouge","Iguane rhinocéros","Iguane rose","Iguane vert","Ili pika","Impala","Indri","Isatis","Jabiru d'Afrique","Jabiru d'Amérique","Jacamar à queue rousse","Jack Russell Terrier","Jaguar","Jaguarondi","Jaseur boréal","Kakapo","Kangourou arboricole","Kangourou roux","Kiwi austral","Koala","Kodiak","Kokoï de Colombie","Komondor","Konik polski","Kookaburra à ailes bleues","Labrador retriever","Laekenois","Lagopède alpin","Lama","Lamantin","Langur sacré","Lapin de garenne","Léiothrix jaune","Lémur couronné","Leonberg","Léopard d'Afrique","Léopard des mers","Léopard des neiges","Leptophye ponctuée","Lérot","Lévrier Afghan","Lévrier Persan","Lévrier Russe","Lézard à collerette","Lézard Jésus","Libellule dépressive","Lièvre d'Europe","Lièvre de Patagonie","Lièvre sauteur","Linotte mélodieuse","Lion d'Afrique","Lion d'Asie","Lipizzan","Loir gris","Loriquet à tête bleu","Loup à crinière","Loup Arctique","Loup d'Abyssinie","Loup de l'Est","Loup de Mongolie","Loup des Indes","Loup du Mexique","Loup gris","Loup Ibérique","Loup rouge","Loutre","Lucane cerf-volant","Lycaon","Lynx Boréal","Lynx du désert","Lynx roux","Macaque à queue de lion","Macaque berbère","Macareux moine","Machaon","Magot","Main Coon","Maki catta","Maki vari noir et blanc","Maki vari roux","Malamute","Malinois","Mamba noir","Mammouth laineux","Manakin de Bokermann","Manchot empereur","Mandrill","Mangouste ichneumon","Mangouste jaune","Mante orchidée","Mante religieuse","Manul","Mara","Marabout","Margay","Markhor","Marmotte des Alpes","Martin chasseur à ailes bleues","Martin chasseur à collier blanc","Martin pêcheur","Martin pêcheur vert","Martinet à ventre blanc","Martre à gorge jaune","Martre des pins","Mâtin de Naples","Mau egyptien","Merle à plastron","Merle d'Amérique","Merle noir","Merlebleu azuré","Mésange bleue","Mésange boréale","Mésange hupée","Messager sagittaire","Milan royal","Miro incarnat","Moineau domestique","Moloch","Monarque","Montagne des Pyrénées","Moro sphinx","Morse","Motmot à sourcils bleus","Motmot à tête bleue","Mouche à damier","Moucherolle royal","Mouffette rayée","Mouffette tachetée","Mouflon","Moustique tigre","Mouton cheviot","Munchkin","Muntjac de Reeves","Musaraigne éléphant","Muscardin","Mustang","Myrmidon","Nandinie","Nandou de Darwin","Narval","Nasique","Nautile","Nebelung","Nestor kéa","Nette rousse","Nicator à gorge grise","Nicobar à camail","Nilgaut","Niverolle alpine","Noctuelle potagère","Noctule commune","Noddi brun","Norvégien","Nothocrax nocturne","Numbat","Nyala","Nyctale de tengmalm","Ocelot","OKapi","Olinguito","Omble chevalier","Ombrette africaine","Onagre","Opossum","Orang outan","Orignal","Oriole de Baltimore","Ornithorynque","Orque","Oryctérope du Cap","Oryx algazelle","Oryx gazelle","Otarie de Californie","Otarie des Galapagos","Otocyon","Ouakari chauve","Ouandérou","Ouaouaron","Ouistiti à toupets blancs","Ouistiti argenté","Ouistiti pygmée","Ourébi","Ours à collier","Ours à lunettes","Ours brun","Ours esprit","Ours lippu","Ours malais","Ours noir","Ours polaire","Pacarana","Panda géant","Panda roux","Pangolin de Chine","Pangolin Géant","Panthere de Ceylan","Panthère de l'Amour","Panthère longibande","Panthère nébuleuse","Panure à moustaches","Paon bleu","Paon du jour","Paresseux à deux doigts","Paresseux à gorge brune","Paruline jaune","Patas","Pécari à collier","Pélican blanc","Pélican brun","Pélican frisé","Perche","Percheron","Persan","Petrogale","Phacochère","Phasme scorpion","Phoque à capuchon","Phoque veau marin","Pic épeiche","Pic flamboyant","Pic vert","Pie bavarde","Pièride du chou","Pilandok","Pinché à crête blanche","Pingouin","Pinson des arbres","Pintade vulturine","Piranha","Pirolle de TaÏwan","Pirolle verte","Podarge de Ceylan","Pogona","Poisson clown","Polatouche de Sibérie","Poney shetland","Porc Epic d'Amérique","Porc Epic du Cap","Porc pie noir","Potamochère","Potoo","Pottok","Poule Araucana","Poule du Sussex","Poule soie blanche","Poule Wyandotte","Processionnaire du pin","Pronghorn","Propithèque à couronne dorée","Protèle","Pudu des Andes","Pug","Puma","Punaise de feu","Putois à pieds noirs","Putois d'Europe","Pygargue à tête blanche","Python vert","Quarter-Horse","Quéléa à bec rouge","Quetzal","Quinnat","Quiscale bronzé","Quokka","Quoll","Ragondin","Raie léopard","Raie Manta","Raie pastenague","Rainette aux yeux rouges","Rascasse volante","Rat-taupe nu","Ratel","Raton laveur","Renard corsac","Renard crabier","Renard des sables","Renard des savanes","Renard gris","Renard polaire","Renard roux","Renne","Requin à pointes noires","Requin Baleine","Requin blanc","Requin citron","Requin marteau (grand)","Requin pointe blanche","resplendissant","Rhinocéros blanc","Rhinocéros de Sumatra","Rhinocéros indien","Rhinocéros noir","Rhinopithèque de Stryker","Rollier à longs brins","Rollier Indien","Rorqual à bosse","Rorqual bleu","Rossignol du Japon","Rouge gorge","Rouge-queue noir","Sacré de Birmanie","Saïga","Saïmiri à tête noire","Saint-Bernard","Saki à face blanche","Salamandre Tachetée","Salers","Saluki","Sambar","Samoyède","Sanglier commun","Saola","Sapajou apelle","Saumon royal","Sauterelle de Bosc","Sauterelle verte (grande)","Schnauzer","Scinque à flancs rouges","Scolie des jardins","Sconce","Scottish Terrier","Selkirk rex","Selle français","Semnopithèque de Thomas","Serpent à sonnette","Serpentaire bacha","Serval","Setter Irlandais","Shar Peï","Shetland (poney)","Shiba-inu","Shih Tzu","Siamois","Siberian husky","Silure glane","Singe hurleur noir","Sittelle à poitrine blanche","Sittelle torchepot","Sizerin flammé","Smilodon","Somali","Sorraïa","Souimanga écarlate","Souris rayée d'Afrique","Spatule rose","Spermophile rayé","Sphynx","Spilogale","Spitz nain","Spizaète orné","Springbok","Steenbok","Suricate","Takin","Tamandua du Mexique","Tamanoir","Tamarin à mains dorées","Tamarin empereur","Tamarin lion doré","Tamia rayé","Tangara émeraude","Tangara évêque","Tantale ibis","Tapir de Malaisie","Tapir du Brésil","Tarentaise","Tarente du midi","Tarier pâtre","Tarine","Tarsier des Philippines","Tatou à neuf bandes","Tatou géant","Taupe à nez étoilé","Taupe d'Europe","Tchitrec de paradis","Teckel à poils longs","Tenrec zébré","Terre-neuve","Tervueren","Tétras des prairies","Tétras lyre","Thon rouge","Tigre à dents de sabre","Tigre blanc royal","Tigre de Sibérie","Tigre de Sumatra","Tigre de Tasmanie","Tigre doré","Tigre du Bengal","Tisserin gendarme","Topi","Tortue géante","Tortue imbriquée","Tortue luth","Tortue molle","Tortue verte","Toucan à carène","Toucan ariel","Toucan toco","Touraco vert","Travailleur à bec rouge","Triton alpestre","Troglodyte des marais","Troglodyte mignon","Trogon de Cuba","Tropidacris cristata","Truite fario","Tyrannosaure","Unau","Vampire d'Azara","Vanneau soldat","Varan bigarré","Vautour africain","Vautour fauve","Vautour pape","Vautour percnoptère","Verdier d'Europe","Vigogne","Vipère à cornes","Vipère Aspic","Viscache des plaines","Vison","Wallaby de Bennett","Wallaby des rochers","Wapiti","Waterbuck","Welsh corgi","West highland terrier","Wombat commun","Xantusie du désert","Xérus","Xylocope violacé","Yack","Yapock","York Chocolat","Yorkshire terrier","Zèbre de Burchell","Zèbre de Grévy","Zorille du Cap"]

# connexion a la base de donnees
import mysql.connector

DB_HOST="localhost"
DB_DATABASE="BIBYdex"
DB_USERNAME="BIBYdex"
DB_PASSWORD="proutBIBYdex"

mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_DATABASE
    )


# recuperation du curseur
mycursor = mydb.cursor()



# table animal
# 1. Nom = nomEspeces
# 2. Description = resume
# 3. CheminImage = image
# 4. IdAnimal auto increment


for animal in liste_animaux:
    
    try:

        # incrementation dans la base de donnees
        sql = "INSERT INTO ANIMAL (Nom, Description, CheminImage) VALUES (%s, %s, %s)"
        # recuperation des especes
        resume, nomEspeces, url, image = recuperationEspeces(animal)
        # recuperation des valeurs
        val = (nomEspeces, resume, image)
                # execution de la requete
        mycursor.execute(sql, val)
        # validation de la requete
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    except:
        pass

    

    



    
