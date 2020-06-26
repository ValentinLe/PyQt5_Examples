# PyQt5_Examples

Programme permettant de repertorier les différents composants principaux de PyQt5. Le script `example.py`ouvre une fenêtre listant toutes les classes contenant un exemple de Widget par exemple l'utiisation d'un bouton, d'une liste déroulante, etc. et permettra de l'ouvrir dans une autre fenêtre.

<div align="center">
  <figure>
    <img src="https://github.com/ValentinLe/PyQt5_Examples/blob/master/screenshots/mainWindow.PNG" alt="mainWindow" />
    <figcaption> Fenêtre principale du programme listant tous les exemples. </figcaption>
  </figure>
</div>

<div align="center">
  <figure>
    <img src="https://github.com/ValentinLe/PyQt5_Examples/blob/master/screenshots/exemple1.PNG" alt="exemple" />
    <figcaption> Exemple d'une barre de progression (ici contrôlée par une slideBar). </figcaption>
  </figure>
</div>

Le script `CreateSommaray.py` va lister l'ensemble des classes (des exemples) du fichier `example.py` en indiquant la ligne dans le fichier afin de pouvoir accéder au code plus rapidement. Pour l'exemple précédent sur la barre de progression, on a dans `Sommary.txt` :
line 320
class WinProgressBar(QWidget):
        """ control d'une bar de progression avec slider """
