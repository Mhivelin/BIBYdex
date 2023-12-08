<?php

require("connexion_dbd.php");

// selection de tous les utilisateurs
try{
    // Création de la requête en utilisant les valeurs récupérées à partir du formulaire
    $sth = $dbh -> prepare("SELECT * FROM ANIMAL");

    // Exécution de la requête créée ci-dessus
    $sth->execute();

    // Récupération du résultat de la requête
    $result = $sth->fetchAll(PDO::FETCH_ASSOC);

    //var_dump($result);
    

    echo "<table>";
    echo "<tr>";
    echo "<th>IdAnimal</th>";
    echo "<th>Nom</th>";
    echo "<th>Description</th>";
    echo "<th>CheminImage</th>";
    echo "<th>Supprimer</th>";
    echo "</tr>";

    foreach ($result as $row) {
        echo "<tr>";
        echo "<td>".$row['IdAnimal']."</td>";
        echo "<td>".$row['Nom']."</td>";
        echo "<td>".$row['Description']."</td>";
        echo "<td><img src='".$row['CheminImage']."' width='100' height='100'></td>";
        echo "<td><a href='DeleteAnimal.php?IdAnimal=".$row['IdAnimal']."'>Supprimer</a></td>";
        echo "</tr>";
    }

    echo "</table>";

    


    
}
catch(PDOException $e){
    //$dbh->rollBack();
    echo "Requête exécutée: " . $sql;
    echo "Erreur : " . $e->getMessage();
}