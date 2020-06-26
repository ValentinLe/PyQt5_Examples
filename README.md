# PyQt5_Examples

Programme permettant de repertorier les différents composants principaux de PyQt5. Le script `examples.py`ouvre une fenêtre listant toutes les classes contenant un exemple de Widget par exemple l'utiisation d'un bouton, d'une liste déroulante, etc. et permettra de l'ouvrir dans une autre fenêtre.

<br/>

Fenêtre principale du programme listant tous les exemples :
<div align="center">
  <img src="https://github.com/ValentinLe/PyQt5_Examples/blob/master/screenshots/mainWindow.PNG" width="300" height="322" alt="mainWindow" />
</div>

<br/>

Exemple d'une barre de progression (ici contrôlée par une slideBar) :
<div align="center">
  <img src="https://github.com/ValentinLe/PyQt5_Examples/blob/master/screenshots/exemple1.PNG" width="300" height="322" alt="exemple" />
</div>

Le script `CreateSommary.py` va lister l'ensemble des classes (des exemples) du fichier `examples.py` en indiquant la ligne dans le fichier afin de pouvoir accéder au code plus rapidement. Pour l'exemple précédent sur la barre de progression, on a dans `Sommary.txt` : <br/>
line 320  <br/>
class WinProgressBar(QWidget): <br/>
        """ control d'une bar de progression avec slider """
