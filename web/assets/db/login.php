<?php

// recupération des données du formulaire
$pseudo = $_POST['pseudo'];
$password = $_POST['password'];

// hachage du mot de pass
$password = md5($password);

// connexion à la base de donnée
require("connexion_dbd.php");

try{
    // Création de la requête en utilisant les valeurs récupérées à partir du formulaire
    $sth = $dbh -> prepare("SELECT * FROM UTILISATEUR WHERE Pseudo = :pseudo AND PasswordHash = :passwordHash");

    // Insertion des valeurs dans la requête sql
    $sth->bindValue(':pseudo', $pseudo);
    $sth->bindValue(':passwordHash', $password);
    
    // Exécution de la requête créée ci-dessus
    $sth->execute();
    
    // Récupération du résultat de la requête
    $result = $sth->fetchAll(PDO::FETCH_ASSOC);
    
    // Si le résultat est vide, alors l'utilisateur n'existe pas
    if(empty($result)){
        echo "L'utilisateur n'existe pas ou le mot de passe est incorrect";
        ?>
            <br>
            <a href="../../login-page.php">Se connecter</a>
            <br>
            <a href="../../index.html">Retour au menu</a>
        <?php
    }

    // Sinon, l'utilisateur existe
    else{
        $_SESSION['pseudo'] = $pseudo;
        $_SESSION['password'] = $password;
        echo "Vous êtes connecté";

        ?>
            <br>
            <a href="../../index.html">Retour au menu</a>
        <?php
    }
    
}
catch(PDOException $e){
    //$dbh->rollBack();
    echo "Requête exécutée: " . $sql;
    echo "Erreur : " . $e->getMessage();
}
?>