<?php

// connexion à la base de données
$servername = 'azdazdaz';
$dbname = 'BIBYdex';
$username = 'BIBYdex';
$password = 'proutBIBYdex';

//On établit la connexion    
try {
    $db = new PDO('mysql:host=' + $servername + ';dbname=' + $dbname + ';charset=utf8', $username, $password);
} catch (Exception $e) {
    die('Erreur : ' . $e->getMessage());
}

$sqlQuery = 'SELECT * FROM UTILISATEUR';
$connect = $mysqlClient->prepare($sqlQuery);
$connect->execute();
$connectVerif = $connect->fetchAll();

echo $connectVerif;