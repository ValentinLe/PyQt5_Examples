
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Hello(QWidget):
    def __init__(self):
        """ hello world avec GridLayout """
        QWidget.__init__(self)
        self.setWindowTitle("Le titre")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Hello World !")
        layout.addWidget(label,0,0)

        self.setGeometry(100,100,600,100)

class Window(QWindow):
    def __init__(self):
        """ autre type de fenetre """
        QWindow.__init__(self)
        self.setTitle("Le titre MDR")
        self.resize(400,300)

class WinBoxLayout(QWidget):
    def __init__(self):
        """ ajout d'elements hori et verti """
        QWidget.__init__(self)

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        label = QLabel("Label 1")
        layout.addWidget(label,0)
        label = QLabel("Label 2")
        layout.addWidget(label,0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)

        label = QLabel("Label 3")
        layout2.addWidget(label,0)
        label = QLabel("Label 4")
        layout2.addWidget(label,0)


class WinGridLayout(QWidget):
    def __init__(self):
        """ GridLayout un peu plus pousse """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Label (0,0)")
        layout.addWidget(label, 0, 0)
        label = QLabel("Label (0,1)")
        layout.addWidget(label, 0, 1)
        label = QLabel("Label (1,0) passer 2 colonnes")
        layout.addWidget(label, 1, 0, 1, 2)
        # int row, int column, int rowSpan, int columnSpan (span = passer)
        label = QLabel("Label (0,2) passer 2 lignes")
        layout.addWidget(label, 0, 2, 2, 1)

class WinTextAdapt(QWidget):
    def __init__(self):
        """ Faire adapter du texte selon la taille de la fenetre """
        QWidget.__init__(self)
        
        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("The story of Dale")
        layout.addWidget(label, 0, 0)

        label = QLabel("Pour faire un sorte qu'un long texte soit compacte en faisant un retour à la ligne")
        label.setWordWrap(True) #faire des \n pour que le texte soit lisible
        layout.addWidget(label, 0, 1)


class WinButton(QWidget):
    def __init__(self):
        """ gestion d'un boutton """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 0, 0)

    def on_button_clicked(self):
        print("The button was pressed !")

class WinRadioButton(QWidget):
    def __init__(self):
        """ radiobutton qui bug sur isChecked """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Brazil")
        radiobutton.setChecked(True)
        radiobutton.country = "Brazil"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Argentina")
        radiobutton.country = "Argentina"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Ecuador")
        radiobutton.country = "Ecuador"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 2)

    def on_radio_button_toggled(self):
        radionbutton = self.sender()
        if radiobutton.isChecked():
            print("Selected country is %s" % (radiobutton.country))

class WinCheckBox(QWidget):
    def __init__(self):
        """ checkbox detection selection """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox1 = QCheckBox("Kestrel")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0, 0)

        self.checkbox2 = QCheckBox("Arrow")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1, 0)

        self.checkbox3 = QCheckBox("Hobby")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2, 0)

    def checkbox_toggled(self):
        selected = []

        if self.checkbox1.isChecked():
            selected.append(self.checkbox1.text())

        if self.checkbox2.isChecked():
            selected.append(self.checkbox2.text())

        if self.checkbox3.isChecked():
            selected.append(self.checkbox3.text())

        print("Selected : %s" % (" ".join(selected)))

class WinToolTip(QWidget):
    def __init__(self):
        """ les tooltip (infos bulles) """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Simple ToolTip")
        button.setToolTip("This ToolTip simply displays text.")
        layout.addWidget(button, 0, 0)

        button = QPushButton("Formatted ToolTip")
        button.setToolTip("<b>Formated text</b> can also be displayed.")
        layout.addWidget(button, 1, 0)

class WinWhatsThis(QWidget):
    def __init__(self):
        """ liste déroulante info bulle qu'est ce que c'est """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Focus comboBox and press SHIFT + F1")
        layout.addWidget(label)

        self.combobox = QComboBox()
        self.combobox.setWhatsThis("This is a 'WhatsThis' object description.")
        layout.addWidget(self.combobox)


class WinEntry(QWidget):
    def __init__(self):
        """ Line Edit / Entry box pour récupérer du texte """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.lineedit = QLineEdit()
        self.lineedit.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineedit, 0, 0)

    def return_pressed(self):
        print(self.lineedit.text())


class WinButtonGroup(QWidget):
    def __init__(self):
        """ gerer un group de boutton un peu comme JS avec buttons[n] """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.buttongroup = QButtonGroup()
        self.buttongroup.setExclusive(False)
        # mise en place d'un listener sur tous les bouttons du group
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton("Button 1")
        # ajout du boutton dans le group avec son ID
        self.buttongroup.addButton(button, 1)
        layout.addWidget(button)

        button = QPushButton("Button 2")
        self.buttongroup.addButton(button, 2)
        layout.addWidget(button)

    def on_button_clicked(self, id):
        # self.buttongroup.buttons() = un get des bouttons
        for button in self.buttongroup.buttons():
            # self.buttongroup.button(id) = buttons[id]
            if button is self.buttongroup.button(id):
                print("%s was clicked !" % (button.text()))


class WinGroupBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("GroupBox")

        layout = QGridLayout()
        self.setLayout(layout)

        # partie checkable pour enable/disable
        groupbox = QGroupBox("GroupBox Exemple")
        groupbox.setCheckable(True)
        layout.addWidget(groupbox)

        # layout du groupe
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        # partie dans la zone du groupe
        radiobutton = QRadioButton("RadioButton 1")
        radiobutton.setChecked(True)
        vbox.addWidget(radiobutton)
        radiobutton = QRadioButton("RadioButton 2")
        vbox.addWidget(radiobutton)


class WinSlider(QWidget):
    def __init__(self):
        """ les sliders """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        slider = QSlider(Qt.Horizontal)
        slider.setValue(4)
        layout.addWidget(slider, 0, 0)

        slider = QSlider(Qt.Vertical)
        slider.setValue(4)
        layout.addWidget(slider, 0, 1)


class WinDial(QWidget):
    def __init__(self):
        """ slider en forme de compteur de voiture """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.slider_changed)
        layout.addWidget(self.dial)

    def slider_changed(self):
        print("Current dial value : %i" % (self.dial.value()))


class WinShowNumber(QWidget):
    def __init__(self):
        """ Afficheur 7 segments d'un nombre """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        lcdnumber = QLCDNumber()
        lcdnumber.display(4.5792)
        layout.addWidget(lcdnumber, 0, 0)


class WinProgressBar(QWidget):
    def __init__(self):
        """ control d'une bar de progression avec slider """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        # slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.slider_changed)
        layout.addWidget(self.slider, 0, 0)

        # progressbar
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setValue(0)
        layout.addWidget(self.progressbar)

    def slider_changed(self):
        self.progressbar.setValue(self.slider.value())

def openWin(w):
    app = QApplication(sys.argv)

    window = w()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    openWin(Win)


