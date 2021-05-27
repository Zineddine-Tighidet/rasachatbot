RASA CHATBOT 2020-2021
======================

### Participants :
    *Zineddine TIGHIDET*
    *Lifang SU*

### Présentation Vidéo 

- diponible en ligne : https://youtu.be/NEJgeqrZhUw

### Branch : **main**

### Exécution
- Pour tester la partie vers un serveur : http://35.195.60.43/guest/conversations/production/74f8a347abee477bb679f1b9b7605076

- Pour tester la partie **personnalisé** :
    - actions personnalisées : demande weather, prix de bitcoin, time, info d'université et le pays avec ip
    - le premier terminal est pour lancer le programme rasa entrainé avec notre modèle dialogique définissant les reactions : `rasa run actions`
    - le deuxieme terminal est pour lancer un  Shell avec le RASA chatbot : `rasa shell` qui s'effectue l'interractions avec l'utilisateur en utilisant le model `CustomizedActionsWithPyton.tar.gz`

### Structure du Projet
- **data** : 
    - fichier **nlu.yml** : fichier définissant  tous les motifs `intent` de phrase a repérer dans les questions de l'utilisateur  , ainsi que les  réactions a y exécuter.

    - fichier **rules.yml** : où on définit les contraintes lorque on crée une conversation. 

    - fichier **stories.yml** : où on définit les conversaitons qui sont basée sur l'ordre des `intent` et `action` utilisées. Le chat bot va réagir selon les différents types d'histoires.

- **domain.yml** : fichier où on définit les données du chatbot à savoir les réponses, les `entités nommées` ainsi que les `actions customisées` (traitements avec un programme Python).

- **models** : Dossier où on stock nos modèles lorque un entraînement `rasa train` est effectué (sous format .tar.gz).

- **actions** : Dossier où on implément les actions customisées en utilisant un programme `Python`. Il y a plusieur façaons à récupérer les données correspondantes, soit via des `API`, soit via une `Data Base`, en effet RASA crée une base de données suite à un processus de machine learning basée sur les données qu'on lui a donnés.

- **config.yml** : la configuration pour RASA NLU.

- **endpoints.yml** : les endpoints pour RASA CHAT BOT. Pour tester nos actions, il faut utiliser `action_endpoint` qui permettre de lancer un serveur qui accept la demande `HTTP` de rasa.


### Références
- RASA : https://rasa.com/
- Rasa : https://rasa.com/
- API Country & IP : https://api.ip2country.info/ip?5.6.7.8
- API Weather : http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=paris 
- API BitCoin : https://api.coindesk.com/v1/bpi/currentprice/eur.json
- API University : http://universities.hipolabs.com/search?name=diderot 
- API Joke : https://v2.jokeapi.dev/joke/Any



