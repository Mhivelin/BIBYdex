<?php

require("connexion.php");

// selection de tous les utilisateurs
try{
    // Création de la requête en utilisant les valeurs récupérées à partir du formulaire
    $sth = $dbh -> prepare("SELECT * FROM UTILISATEUR");

    // Exécution de la requête créée ci-dessus
    $sth->execute();

    // Récupération du résultat de la requête
    $result = $sth->fetchAll(PDO::FETCH_ASSOC);

    // Si le résultat est vide, alors l'utilisateur n'existe pas
    if(empty($result)){
        echo "Aucun utilisateur";
    }
    // Sinon, l'utilisateur existe
    else{
        echo "<table>";
        echo "<tr>";
        echo "<th>Pseudo</th>";
        echo "<th>Mail</th>";
        echo "<th>Role</th>";
        echo "</tr>";
        foreach($result as $row){
            echo "<tr>";
            echo "<td>" . $row['Pseudo'] . "</td>";
            echo "<td>" . $row['Mail'] . "</td>";
            echo "<td>" . $row['Role'] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    }

}
catch(PDOException $e){
    //$dbh->rollBack();
    echo "Requête exécutée: " . $sql;
    echo "Erreur : " . $e->getMessage();
}