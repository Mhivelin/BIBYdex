<?php 

// connexion à la base de données
$servername = 'localhost';
$dbname = 'BIBYdex';
$username = 'BIBYdex';
$password = 'proutBIBYdex';

//On établit la connexion    
try
{
	$db = new PDO('mysql:host=' + $servername + ';dbname=' + $dbname + ';charset=utf8', $username, $password);
}
catch (Exception $e)
{
        die('Erreur : ' . $e->getMessage());
}