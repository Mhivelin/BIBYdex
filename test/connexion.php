<?php
// page de connexion à la base de donnée

// Informations de connexion au serveur de base de données
$servname = 'localhost';
$dbname = 'BIBYdex';
$user = 'BIBYdex';
$pass = 'proutBIBYdex';

// Connexion à la base avec PDO
$dbh = new PDO("mysql:host=$servname;dbname=$dbname", $user, $pass);

?>


