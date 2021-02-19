# SercqUnpack
Unpacking des fichiers de données de Meurtres en Série

## Qu'est-ce que c'est ?
Un outil pour le jeu vidéo Meurtres en Série (Cobrasoft 1987), grand succès des jeux d'enquêtes français des années 1980.

Le script Python **UnpackData.py** parse et traduit en version lisible les fichiers de données du jeu. Il permet d'afficher *presque* tout le texte que l'on peut obtenir durant l'enquête. Les données sont organisées de la même façon que dans les fichiers de données : chaque élément est rattaché à des coordonnées x/y, une heure d'apparition (start) et de disparition (end), un personnage (optionnel dans certains cas) et un type qui correspond à la touche qui permet de rencontrer l'élément à cet endroit et durant l'intervalle temporel spécifié :
* EVT_DESCRIPTION lorsqu'on 'R'egarde
* EVT_CONVERSATION lorsqu'on 'I'nterroge
* EVT_OBJET lorsqu'on 'F'ouille
* EVT_ACTION lorsqu'on 'A'git

Le delta qui n'est pas présent dans le résultat de ce script est constitué des textes qui ne sont pas dans les fichiers de données, mais directement dans l'exécutable. Il s'agit principalement de ce qui s'affiche à l'écran lorsque vous réalisez une action (avec la touche 'A'). Le script précise tout de même succinctement de quoi il s'agit. (Pour un texte exhaustif du résultat de ces actions, rendez-vous sur le repository du code décompilé indiqué plus bas, dans SERCQ.C votre point d'entrée sera Command_A()).

## Mise en place technique
Par rapport à l'endroit où est lancé le script, les fichiers de données doivent être dans ../SERCQ/.

Les fichiers parsés sont :
* DATA.BIN pour la majorité des informations
* TEMxxx.TXT pour le contenu des différentes conversations avec les personnages (touche 'I'nterroger)

Vous devez récupérer ces fichiers par ailleurs afin d'être en mesure d'exécuter le script.

## Pour voir le résultat directement
J'ai exporté le résultat (pour la version DOS) dans un fichier [output.txt](output.txt) que vous pouvez [consulter directement](output.txt).

**ATTENTION**: le parsing des fichiers de données contient naturellement beaucoup de **SPOILERS** !!
Il ne vous donnera pas directement la solution, mais vous en approchera fortement.

## Remerciements et liens
Ce script n'a pu être possible qu'en explorant les exécutables décompilés du repository [ergonomy-joe/SERCQ](https://github.com/ergonomy-joe/SERCQ). Un grand merci à son auteur.

Si malgré tout ça vous êtes encore perdus, une solution remarquablement bien rédigée est présente sur la page https://www.oldies-but-goodies.fr/index.php?page=test&id=53 (en bas).

## Help ! Questions
Il y a encore des détails qui me chiffonnent et auxquels, sauf erreur de ma part, cet unpacking ne donne pas de réponse :
* Quelle est la réponse à la question finale "Où a été pris l'indice 1 ?", et comment peut-on la trouver ?
* De quelle façon peut-on trouver (sans décompiler) le code demandé sur Etac ?
* Comment peut-on savoir (sans décompiler) que le "prénom" du propriétaire de Bréchou est "J.R." ?
* Où peut-on trouver l'indice 7 ? (il n'est référencé ni dans mon DATA.BIN ni dans le code décompilé de ergonomy-joe)
* La partition (indice 15) sert-elle à quelque chose ?

N'hésitez pas à m'envoyer vos tuyaux à manur@ manur. org (sans les espaces).
