<?php
// ----------------------------- page de login -----------------------------

// on démarre la session
session_start();



?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bibydex</title>
    <!-- bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

</head>

<body>
    <div class="container">

        <div class="card" style="width: 80%; ">
            <div class="card-header">

                <h1>Connexion</h1>
            </div>
            <div class=" card-body">

                <!-- formulaire  de connexion -->
                <form action="assets/db/login.php" method="post">


                    <!-- pseudo -->
                    <label for="pseudo" class="form-label">Pseudo</label>
                    <input type="text" class="form-control" name="pseudo" id="pseudo" required>

                    <!-- mot de passe -->
                    <label for="password" class="form-label">Mot de passe</label>
                    <input type="password" class="form-control" name="password" id="password" required>

                    </br>

                    <!-- bouton de connexion -->
                    <input type="submit" class="btn btn-primary" value="Se connecter">



                </form>

                </br>

                <!-- Lien vers la page de création de compte -->
                <h6>Vous n'avez pas de compte ? <a href="CreateAccount-page.php">Créer un compte</a></h3>

            </div>
        </div>
    </div>

</body>

</html>