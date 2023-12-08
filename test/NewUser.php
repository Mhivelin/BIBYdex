<?php
//connexion à la base de donnée
require("connexion.php");

try{

    // récupération des infos envoyé par le formulaire
    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        // Pseudo
        $pseudo = $_POST['pseudo'];
        if (empty($pseudo)) {
            echo "Pseudo est vide";
        } else {
            echo $pseudo;
        }

        //mail
        $mail = $_POST['mail'];
        if (empty($mail)) {
            echo "Mail est vide";
        } else {
            echo $mail;
        }

        // password
        $passwordHash = $_POST['password'];
        if (empty($passwordHash)) {
            echo "Mdp est vide";
        } else {
            echo $passwordHash;
        }
    }

    //$idUtilisateur = 1; //auto increment
    $pseudo = "nomUtilisateur";
    $mail = "email@example.com";
    $passwordHash = "hashDuMotDePasse";

    // Création de la requête en utilisant les valeurs récupérées à partir du formulaire
    $sth = $dbh -> prepare("INSERT INTO UTILISATEUR(Pseudo,Mail,PasswordHash) 
                            VALUES (:pseudo, :mail, :passwordHash)");

    // Insertion des valeurs dans la requête sql
    $sth->bindValue(':pseudo', $pseudo);
    $sth->bindValue(':mail', $mail);
    $sth->bindValue(':passwordHash', $passwordHash);
    
    // Exécution de la requête
    $sth->execute();
    
}
catch(PDOException $e){
    //$dbh->rollBack();
    echo "Requête exécutée: " . $sql;
    echo "Erreur : " . $e->getMessage();
}


?>