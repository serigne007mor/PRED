Ce readme accompagne le fichier de données "support_vectors_toshare.csv". 
Ces données représentent les vecteurs support d'un SVM.
\
Le SVM a été entrainé pour copier un modèle profond étudié, lui même entrainé sur des données labellisées par un système historique.

# Les données

Ces vecteurs support (VS) déterminent les éléments clé de l'apprentissage du SVM. En d'autre termes, les éléments du jeu d'entrainement du SVM qui ont particpé à la détermination des règles de classification apprises lors de la création du SVM. 

Ces VS doivent nous aider à mieux comprendre le comportement du SVM. Comme ce SVM copie un modèle profond, cela nous donne des pistes d'étude pour le modèle profond, qui est celui étudié dans les travaux d'origine. C'est pourquoi la colonne associée est nommée `label_modele_etudie`.  Ce même modèle a été entrainé sur un système de classification à base de RegEx. En effet le projet de classification a été mis en place pour remplacer un système à base de règles devenu trop lourd à maintenir manuellement. La première version du modèle profond par apprentissage automatique a donc eu pour base les données catégorisées par ce système historique. Cela a permis d'obtenir rapidement un grand volume de données; mais le système historique fait des erreurs, notamment beaucoup de faux positifs. Aussi, il est parfois intéressant d'avoir accès à ce `label_historique` afin de comprendre pourquoi une phrase est considérée, à tord, comme devant être rejetée.

## Le SVM et son entrainement
Le SVM classifie des offres d'emploi de Pôle emploi. Ces offres sont légales, ou portent un motif de rejet. Le modèle détecte 26 motifs de rejet ainsi que le motif "legal" signifiant qu'aucun motif de rejet n'a été trouvé. La prédiction est effectuée sur la représentation vectorielle des offres d'emploi. 

Le SVM a été entrainé sur 480 000 offres afin de copier le comportement d'un réseau de neurones à attention. Son jeu d'entrainement comporte Sur un jeu de données de test de 160 000 offres, sa précision moyenne est de 0.997.
La documentation précise du SVM est disponible ici : https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html (kernel rbf).


## Les offres d'emploi
Chaque ligne du jeu de données représente une offre. 
Les colonnes sont :
| Nom                 | Description                                                         |
|---------------------|---------------------------------------------------------------------|
| id_offre            | Identifiant unique de l'offre dans les bases de données Pôle emploi |
| texte               | Une phrase extraite de l'offre                                      |
| texte_pretraite     | Texte après nettoyages (pas de majuscules...)                       |
| vecteur             | Représentation vectorielle du texte (GloVe)                         |
| label_historique    | Motif de rejet selon le système historique                          |
| label_modele_etudie | Motif de rejet selon le modèle profond étudié                       |
| label_svm           | Motif de rejet selon le SVM                                         |


# Récupération des données
Ce csv utilise les `;` comme caractère de séparation. 
Pour le récupérer dans un script python, il suffit d'utiliser le bloc de code suivant:

```py 
import pandas as pd
df = pd.read_csv("path/support_vectors_toshare.csv",sep=";", encoding="utf-8")
```

## Répartition des vecteurs par classe 
 
Le bloc de code suivant permet de récupérer la répartition des vecteurs par classe. Il est adaptable pour observer les répartitions selon le système historique et le modèle profond en appellant les colones adéquates. 

```py
print(df.groupby(by="label_svm")['id_offre'].count())` 
```

| label_svm                                              |  Nb  |
|--------------------------------------------------------|------|
| DISCRIMINATION : ACTIVITE SYNDICALE OU MUTUALISTE      | 8    |
| DISCRIMINATION : AGE                                   | 579  |
| DISCRIMINATION : APPARENCE PHYSIQUE                    | 311  |
| DISCRIMINATION : CONTRAT AIDE                          | 14   |
| DISCRIMINATION : CONTRAT ETUDIANT                      | 151  |
| DISCRIMINATION : ETAT DE SANTE                         | 1006 |
| DISCRIMINATION : GROSSESSE                             | 30   |
| DISCRIMINATION : HANDICAP                              | 296  |
| DISCRIMINATION : MOEURS                                | 62   |
| DISCRIMINATION : NATIONALITE                           | 123  |
| DISCRIMINATION : OPINIONS POLITIQUES                   | 22   |
| DISCRIMINATION : ORIGINE                               | 193  |
| DISCRIMINATION : RESIDENCE                             | 369  |
| DISCRIMINATION : SEXE - Au moins un accord au féminin  | 415  |
| DISCRIMINATION : SEXE - Intitulé exclusivement féminin | 478  |
| DISCRIMINATION : SEXE - Mention genre exclusif         | 84   |
| DISCRIMINATION : SITUATION FAMILIALE                   | 26   |
| DISCRIMINATION : TAILLE                                | 101  |
| DROIT DU TRAVAIL: ACHAT DE MATERIEL                    | 892  |
| DROIT DU TRAVAIL: CDD POSSIBILITE CDI                  | 1154 |
| LIBERTES : CASIER JUDICIAIRE                           | 117  |
| LIBERTES : TENUE VESTIMENTAIRE                         | 18   |
| Legal                                                  | 4688 |
| OFFRE NON CONFORME : STAGE                             | 78   |
| TERME INAPPROPRIE                                      | 650  |
| TEXTE SPECIFIQUE : GRATUITE                            | 212  |
