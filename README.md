# SercqUnpack
Unpacking des fichiers de données de Meurtres en Série

## Qu'est-ce que c'est ?
Un outil pour le jeu vidéo Meurtres en Série (Cobrasoft 1987), un grand succès des jeux d'enquêtes français des années 1980.
Le script Python UnpackData.py parse et traduit les fichiers de données du jeu.
Par rapport à l'endroit où est lancé le script, les fichiers de données doivent être dans ../SERCQ/.
Les fichiers parsés sont :
* DATA.BIN pour la majorité des informations
* TEMxxx.TXT pour le contenu des différentes conversations avec les personnages (touche 'I'nterroger)
Vous devez récupérer les fichiers par ailleurs pour exécuter le script.

## Pour voir le résultat directement
J'ai exporté le résultat (pour la version DOS) dans un fichier output.txt que vous pouvez consulter directement.
ATTENTION: le parsing des fichiers de données contient naturellement beaucoup de SPOILERS.
Il ne vous donnera pas directement la solution, mais vous en approchera fortement.

## Remerciements et liens
Ce script n'a pu être possible qu'en explorant les exécutables décompilés du repository ergonomy-joe/SERCQ.
Si malgré tout ça vous êtes encore perdus, une solution remarquablement rédigée est présente sur la page https://www.oldies-but-goodies.fr/index.php?page=test&id=53 (en bas).

## Questions
Il y a encore des détails qui me chiffonnent et auxquels, sauf erreur de ma part, cet unpacking ne donne pas de réponse :
* Quelle est la réponse à la question finale "Où a été pris l'indice 1 ?", et comment peut-on la trouver ?
* De quelle façon peut-on trouver le code demandé sur Etac ?
* Comment peut-on savoir (sans décompiler le code) que le "prénom" du propriétaire de Bréchou est "J.R." ?
* Où peut-on trouver l'indice 7 ? (il n'est référencé ni dans mon DATA.BIN ni dans le code décompilé de ergonomy-joe)
* La partition (indice 15) sert-elle à quelque chose ?
N'hésitez pas à m'envoyer vos aides à manur@ manur. org (sans les espaces).

