<?php

// Connexion à la base de données
$servername = 'localhost';
$dbname = 'BIBYdex';
$username = 'BIBYdex';
$password = 'proutBIBYdex';

// On établit la connexion
try {
    $db = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (Exception $e) {
    die('Erreur : ' . $e->getMessage());
}
