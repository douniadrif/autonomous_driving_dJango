# autonomous_driving_dJango


 Conception et réalisation d’une solution automatisée permettant la collection, le traitement et la visualisation en des données




   Présenté par : DRIF Dounia Entreprise : INTELLCAP
   
   
   

Introduction :


D’Après plusieurs études de l’existant, de conception et de modélisation fonctionnelle et organisationnelle nous avons développé les interfaces de notre plateforme pour répondre aux besoins d’entreprise concernant d’une part la mise en situation des avis des future utilisateurs des drones autonomes aux maroc et ailleurs et d’autre part données estimer capter par les drones autonome au moment de vol en vous présent un rapport pour plus des détails sur l’enchainement de travaille et les résultats obtenus .
La compréhension du problème métier

Le but de ce projet est de collectée est analysée des données pour en extraire des indicateurs relatifs aux :
1- besoinsd’usagerspotentielsdesvéhiculesélectriquesautonomes ou de drones autonomes (point de départ, point d’arrivée, distances à parcourir, fréquences, nombre de passagers, taille des personnes, poids des personnes, encombrement des affaires à transporter volume et poids, présence d’objets fragiles, présence d’objets dangereux comme une batterie inflammable par exemple; le prix à pays par rapport à des seuils mini-maxi; possibilité d’adhérer à un contrat de service avec un minimum de trajets à effectuer ...);
-
 Quels sont les besoins d’utilisateurs ? Quels La distance la plus récurrents ?

Quels La moyenne de prix par km ?
 quel es le poids des personnes et baguage final de véhicule ?
 Quel espace a réservé aux objets fragiles ?
 quels sont les facteurs qui influence le choix d’acceptation d’utilisations des drone ?
 quels sont les critères sur lesquels en se basent pour construire un drone autonome ou une véhicule Autonome ?




2- Les capteurs produisent des data auxquels se rajoutent d’autres éléments à analyser:
-
- quels Sont les données capter par les drones autonome ?
-  quels sont les facteurs qu’on peuvent suivre a Distance ?
-  quels le carburant consommé par trajet au km ?
- quel est le temps passé sur la route ou en vol ?
- quel est le temps de charge des batteries




3- concevoir une application pour tablette qui sert d’interface d’accès aux données :
une présentation des données étudier ?
 une partie d’utilisateurs qui éclairent les critères sur lesquels en se basent pour construire un drone autonome ?
une partie qui suit les données capter par les drones ?
 d’offrir un portail interactif contient des Dashboard des utilisateurs et des données des collectés par les capteurs

La compréhension des données
les problèmes métiers relatifs à des données existantes :
externe : sur le site web deloitte , des tableaux de bord d'enquête client automatique des differents payés de monde . interne : pas des données propre au entreprise
identifier la qualité des données disponibles :
ndisponibilité d’autres sources open des données qui traitent le même sujet puisque c’est un projet qui n’est pas encore réalisé opte pour le choix :
- Un formulaire aux utilisateurs .
- Des données générer automatiquement par un système .
- Scraping des données a partie d’un site web .
les données à analyser
- point de départ, point d’arrivée, distances à parcourir, fréquences, nombre de passagers, taille des personnes, poids des personnes, encombrement des affaires à transporter volume et poids, présence d’objets fragiles, présence d’objets dangereux , le prix à pays par rapport à des seuils mini-maxi , possibilité d’adhérer à un contrat de service avec un minimum de trajets à effectuer .
-

- La vitesse , la vitesse de vent , la vitesse d’internet , la température , l’humidité , la position ( longiture , latitude ) , la pression , puissance et tension ?
La construction du Data Hub
Préparation et nettoyage recodage des données
o extraction d’adresse complet à partir de point de départ et et point arrivé
o transformation d’adresse en données longitude départ ,latitude départ
o Longitude arrivé , et latitude arrivé .
o programme qui calcule la distance a partie de longitude
et latitude .
o un programme sur python qui génèrent des données
automatiques
o affectation de temps a chaque ligne
o un programme qui décale le temps chaque minute
Le déploiement
mise en production pour les utilisateurs finaux des modèles obtenus
génération d’un rapport décrivant les connaissances
  
Consultation des Dashboard
mise en production pour les avis des future utilisateurs
 mise en production pour les avis des future utilisateurs françcaise :
 
de méme pour les autres payés (UK , USA , Canada, GERMANY )
mise en production pour les avis des future utilisateurs marocains des véhicules autonome en se basent sur une formulaire replie par une population marocaines :
mettre la connaissance obtenue par la modélisation des dashboard , dans une forme portail contient des Dashboard et l’intégrer au processus de prise de décision.
 
 mise en production pour les avis des future utilisateurs marocains des DRONE autonome en se basent sur une formulaire replie par une population marocaines :

  
Échantillon de nos base de données :
 la mise en place d’une plateforme , permettant Une visualisation graphiques des différents données estimer capter par les drones autonome au moment de vol .
 
  
Conclusion Générale
Dans ce rapport, nous avons étudié caractéristiques des DRONE Autonome et les véhicule Autonome par la conception et le développement d’une plateforme web qui offre des services aux décisionnels de prendre leurs décisions liées aux critères sur lesquels en se basent pour la réalisation de ce Project ainsi une visualisation des champs capter par les capteurs aux moment de vol .
Nous avons essayé à définir les besoins afin de réaliser une conception évolutive du portail qui peut être optimisé et accepte de nouvelles tâches tel la réception des données en temps réel .
 
