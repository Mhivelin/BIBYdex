<?php
// connexion à la base de données
require('connexion_dbd.php');

//nettoie un String
function clean($string) {
    $string = str_replace(' ', '', $string); // Replaces all spaces with hyphens.
 
    return preg_replace('/[^a-zA-Z0-9@]/', '', $string); // Removes special chars.
}

try {
    // Récupération des données du formulaire
    $pseudo = $_POST['pseudo'];
    $mail = $_POST['mail'];
    $passwordHash = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $pseudo = clean($pseudo);
    $mail = clean($mail);
    $passwordHash = clean($passwordHash);
      
    // Requête SQL pour insérer les données
    $sql = "INSERT INTO UTILISATEUR (Pseudo, Mail, PasswordHash) VALUES (:pseudo, :mail, :passwordHash)";
    $stmt = $dbh->prepare($sql);
    $stmt->execute(['pseudo' => $pseudo, 'mail' => $mail, 'passwordHash' => $passwordHash]);
   
    echo "Utilisateur ajouté avec succès.";

    ?>
        <br>
        <a href="../../index.html">Retour au menu</a>
    <?php

} catch(PDOException $e) {
    echo "Erreur : " . $e->getMessage();
}
?>