<?php

// creation d'un utilisateur dans la base de données

// connexion à la base de données
include("connexion_dbd.php");

// on récupère les données du formulaire
$pseudo = $_POST['pseudo'];
$password = $_POST['password'];
$mail = $_POST['mail'];

// hachage du mot de pass
$password = md5($password);

// on vérifie que le pseudo n'est pas déjà utilisé

// requête SQL avec BIND PARAM
//'SELECT * FROM UTILISATEUR WHERE Pseudo = :pseudo';

$sth = $dbco->prepare("SELECT * FROM UTILISATEUR WHERE Pseudo = :pseudo OR Mail = :mail");
$sth->bindParam("", $pseudo, PDO::PARAM_STR);
$sth->bindParam("", $mail, PDO::PARAM_STR);
$sth->execute();

if ($sth->rowCount() == 0) {

    $sth = $dbco->prepare("INSERT INTO UTILISATEUR(IdUtilisateur, Pseudo, Mail, PasswordHash)
                            VALUES ('',:Pseudo, :Mail, :PasswordHash)");
    $sth->execute(array(
        ':Pseudo' => $pseudo,
        ':Mail' => $mail,
        ':PasswordHash' => $password
    ));
    echo "Entrée ajoutée dans la table";

    $data = $sth->fetchAll();

    // Afficher les résultats
    echo $data;
} else {
    echo "<div class= 'alert alert-danger' role=alert>Le pseudo ou le mail est déjà utilisé</div>";
}