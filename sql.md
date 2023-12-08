# base de données BIBYDEX

## creation de la base de données

```sql
   CREATE TABLE UTILISATEUR(
      IdUtilisateur SMALLINT NOT NULL AUTO_INCREMENT,
      Pseudo VARCHAR(50),
      Mail VARCHAR(100),
      PasswordHash VARCHAR(50),
      PRIMARY KEY(IdUtilisateur)
   );

   CREATE TABLE ANIMAL(
      IdAnimal SMALLINT NOT NULL AUTO_INCREMENT,
      Nom VARCHAR(50),
      Description VARCHAR(500),
      CheminImage VARCHAR(50),
      PRIMARY KEY(IdAnimal)
   );

   CREATE TABLE PHOTO(
      IdUtilisateur SMALLINT,
      IdAnimal SMALLINT NOT NULL AUTO_INCREMENT,
      CheminPhoto VARCHAR(30),
      DatePhoto DATE,
      PRIMARY KEY(IdUtilisateur, IdAnimal),
      FOREIGN KEY(IdUtilisateur) REFERENCES UTILISATEUR(IdUtilisateur),
      FOREIGN KEY(IdAnimal) REFERENCES ANIMAL(IdAnimal)
   );

```

## requêtes
### ajout d'un utilisateur
```sql
INSERT INTO UTILISATEUR(IdUtilisateur, Pseudo, Mail, PasswordHash) VALUES (1, 'Pseudo', 'Mail', 'PasswordHash');
```

### ajout d'un animal
```sql
INSERT INTO ANIMAL(IdAnimal, Nom, Description, CheminImage) VALUES (1, 'Nom', 'Description', 'CheminImage');
```

### ajout d'une photo
```sql
INSERT INTO PHOTO(IdUtilisateur, IdAnimal, CheminPhoto, DatePhoto) VALUES (1, 1, 'CheminPhoto', '2020-01-01');
```

### suppression d'un utilisateur
```sql
DELETE FROM UTILISATEUR WHERE IdUtilisateur = 1;
```

