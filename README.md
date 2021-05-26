RASA CHATBOT 2020-2021
======================

### Participants :
    *Zineddine TIGHIDET*
    *Lifang SU*

### Présentation Vidéo 

- diponible en ligne : https://youtu.be/NEJgeqrZhUw


### Exécution
- Pour tester la partie vers un serveur : (???)

- Pour tester la partie **personnalisé** : 
    - le premier terminal est pour lancer le programme rasa entrainé avec notre modèle dialogique définissant les reactions : `rasa run actions`
    - le deuxieme terminal est pour lancer un  Shell avec le RASA chatbot : `rasa shell` qui s'effectue l'interractions avec l'utilisateur

### Structure du Projet
- **data** : 
    - fichier **nlu.yml** : fichier définissant  tous les motifs `intent` de phrase a repérer dans les questions de l'utilisateur  , ainsi que les  réactions a y exécuter

    - fichier **rules.yml** : où on définit les contraintes lorque on crée une conversation. 

    - fichier **stories.yml** : où on définir les conversaitons qui sont basé sur l'ordre des `intent` et `action` utilisées. Le chat bot va réagir selon les différents types de histoires

- **domain.yml** : fichier on définit les données du chatbot 

- **models** : Dossier on stock nos models lorque une `rasa train` est effectuée

- **actions** : Dossier on implément les actions personnalisées en utilisant `python`. Il y a plusieur façaons à récupérer les données correspondants, soit via des `api`, soit via une `data base`

- **config.yml** : la configuration pour RASA NLU

- **endpoints.yml** : les endpoints pour RASA CHAT BOT. Pour tester nos actions, il faut utiliser `action_endpoint` qui permettre de lancer un serveur qui accept la demande `HTTP` de rasa.


### Références
- RASA : https://rasa.com/



