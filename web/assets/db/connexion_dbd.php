<?php
// page de connexion à la base de donnée

function parseConfig($filePath) {
    $config = [];

    if (!file_exists($filePath)) {
        return $config;
    }

    $lines = file($filePath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    if ($lines === false) {
        return $config;
    }

    foreach ($lines as $line) {
        if (strpos(trim($line), '#') === 0) {
            continue; // Ignore les commentaires
        }

        list($key, $value) = explode('=', $line, 2);
        $config[trim($key)] = trim($value);
    }

    return $config;
}

$config = parseConfig('../../../.env');

// Informations de connexion au serveur de base de données
$servname = $config['DB_HOST'];
$dbname = $config['DB_DATABASE'];
$user = $config['DB_USERNAME'];
$pass = $config['DB_PASSWORD'];

// Connexion à la base avec PDO
try {
    $dbh = new PDO("mysql:host=$servname;dbname=$dbname", $user, $pass);
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} 
catch (Exception $e) {
    die('Erreur : ' . $e->getMessage());
}
?>