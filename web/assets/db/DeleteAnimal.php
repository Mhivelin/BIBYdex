<?php

// recuperation de l'identifiant de l'animal à supprimer
$IdAnimal = $_GET['IdAnimal'];

// connexion à la base de données
require("connexion_dbd.php");

// creation de la requete
$sql = "DELETE FROM ANIMAL WHERE IdAnimal = :IdAnimal";

// preparation de la requete
$sth = $dbh->prepare($sql);

// passage des parametres
$sth->bindParam(':IdAnimal', $IdAnimal, PDO::PARAM_INT);

// execution de la requete
$sth->execute();

// redirection vers la page d'affichage de tous les animaux
header("Location: ShowAllEspeces.php");
