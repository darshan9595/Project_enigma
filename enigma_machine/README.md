
### Enigma Machine Simulator

Ce projet est une simulation d'une machine Enigma, un dispositif de chiffrement mécanique largement utilisé pendant la Seconde Guerre mondiale. Ce projet est codé en Python 3.x. Cette application permet aux utilisateurs de configurer et de simuler le fonctionnement de la machine Enigma à l'aide d'une interface graphique créée avec Tkinter.

## Fonctionnalités

- Configuration des rotors : Choisissez parmi plusieurs rotors (I, II, III, IV, V) et configurez leurs positions initiales, ainsi que leurs paramètres de bague (ring settings).
- Réflecteur : Configurez le réflecteur en utilisant une configuration de câblage standard.
- Plugboard : Ajoutez des connexions personnalisées au plugboard pour simuler le fonctionnement réel de la machine Enigma.
- Chiffrement et déchiffrement : Chiffrez ou déchiffrez des messages avec la configuration de la machine actuelle.
- Sauvegarde des configurations : Sauvegardez la configuration actuelle de la machine ainsi que le message chiffré pour consultation ultérieure.
- Réinitialiser la machine : Réinitialisez la machine Enigma pour restaurer les positions initiales des rotors et les paramètres par défaut.

## Prérequis

Pour exécuter ce projet, vous avez besoin de :

- Python 3.x
- Tkinter (généralement inclus avec Python)

## Installation

1. Clonez ce dépôt sur votre machine locale :
  
   git clone https://github.com/darshan9595/Project_enigma.git
  
2. Accédez au répertoire du projet :
  
   cd enigma_machine
  

## Utilisation

Pour lancer l'application, exécutez le fichier `main.py`, avec la commande  'python main.py'



Une interface graphique s'affichera vous permettant de :
![Image Interphase](./ImageInterphase.png)


1. Configurer la machine Enigma : Sélectionnez l'ordre des rotors, configurez leurs positions initiales et les paramètres de bague.
2. Saisir le plugboard : Ajoutez des paires de connexions (par exemple, "AB, CD, EF").
3. Le réflecteur utilisé dans ce projet est UKW-B, correspondant à la configuration standard YRUHQSLDPXNGOKMIEBFZCWVJAT. Son wiring est visible dans l'interface. Un autre réflecteur peut être utilisé en modifiant simplement le wiring (branchement) directement dans l'interface, mais assurez-vous d'entrer exactement 26 caractères sans espaces ! 
4. Saisissez le message à chiffrer dans la section dédiée au "Message", puis cliquez sur le bouton "Chiffrer". Une nouvelle fenêtre apparaîtra avec le message chiffré.
5. Pour déchiffrer, entrez le message chiffré dans la même section "Message", puis cliquez sur le bouton "Déchiffrer". Une nouvelle fenêtre s'ouvrira avec le message original.
6. Sauvegarder la configuration : Après avoir chiffré ou déchiffré un message, cliquez sur le bouton "Save Configuration" pour enregistrer la configuration actuelle ainsi que le message chiffré. Ces informations seront sauvegardées dans un fichier nommé enigma_encrypted_message.json, situé dans le répertoire enigma_machine, afin de pouvoir les consulter ultérieurement.
7. Réinitialiser la Machine : Si vous souhaitez chiffrer un nouveau message, vous devez réinitialiser la machine en cliquant sur le bouton "Reset Machine". Cela restaurera la configuration initiale des rotors, les positions et les paramètres d'origine, garantissant un chiffrement correct sans interférence des positions précédentes.

## Structure du Projet

- `main.py` : Fichier principal pour lancer l'application.
- `gui.py` : Contient la logique de l'interface utilisateur pour configurer la machine Enigma.
- `rotor.py`, `plugboard.py`, `reflector.py`, `enigma_machine.py`, `state.py` : Classes de base pour modéliser le comportement de chaque composant de la machine Enigma.
- `__init__.py` : Indique que le répertoire est un package Python.

## Notes Importantes

- Le double stepping des rotors est pris en charge dans cette implémentation, reflétant le comportement réel de la machine Enigma. Le double stepping se produit lorsque le rotor du milieu est à sa position de "notch", entraînant une rotation simultanée du rotor du milieu et du rotor de gauche.

## Dépannage

- Problèmes d'importation : Assurez-vous que tous les fichiers se trouvent dans le même répertoire et que vous exécutez le script à partir du bon répertoire.
- Erreur "Module Not Found" : Vérifiez que le répertoire est configuré comme un package Python (avec `__init__.py`).


## Auteur

Darshan Mistry

