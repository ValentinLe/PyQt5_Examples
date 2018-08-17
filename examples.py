
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

        self.showMaximized()

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


class WinSplitter(QWidget):
    def __init__(self):
        """ faire un splitter de zones (Frame) """
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.setLayout(layout)

        # les zones
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # les splitters
        splitterhori = QSplitter(Qt.Horizontal)
        splitterhori.addWidget(topleft)
        splitterhori.addWidget(topright)

        splitterverti = QSplitter(Qt.Vertical)
        splitterverti.addWidget(splitterhori)
        splitterverti.addWidget(bottom)
        layout.addWidget(splitterverti)


class WinScrollArea(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        frame = QFrame()

        vbox = QVBoxLayout()
        frame.setLayout(vbox)

        for i in range(200):
            label = QLabel("Label " + str(i))
            vbox.addWidget(label)
        
        scrollbarArea = QScrollArea()
        scrollbarArea.setWidgetResizable(True)
        scrollbarArea.setWidget(frame)
        layout.addWidget(scrollbarArea)
        

class WinSpinBox(QWidget):
    def __init__(self):
        """ spinbox = box number avec les fleches pour ++/-- le nombre """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.spinbox = QSpinBox()
        # doubleSpinBox pour les doubles au lieu des int
        #self.spinbox = QDoubleSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(10)
        # setRange(-10,10) = setMini & setMaxi
        self.spinbox.setSuffix(" euro")
        self.spinbox.valueChanged.connect(self.on_changed_value)
        layout.addWidget(self.spinbox)
        
        self.label = QLabel("Valeur : " + str(self.spinbox.value()))
        layout.addWidget(self.label)

    def on_changed_value(self):
        self.label.setText("Value : " + str(self.spinbox.value()))


class WinProgressDialog(QWidget):
    def __init__(self):
        """ progressBar sans avec un boutton cancel et/ou sa disparition quand 100% """
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

        # progressBar de dialogue
        self.progressdialog = QProgressDialog()
        self.progressdialog.setMinimum(0)
        self.progressdialog.setMaximum(100)
        self.progressdialog.setValue(0)
        layout.addWidget(self.progressdialog)

    def slider_changed(self):
        self.progressdialog.setValue(self.slider.value())


class WinToolBar(QWidget):
    def __init__(self):
        """ button classique qui fonctionnent comme selection button radio """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        toolbar = QToolBar()
        layout.addWidget(toolbar)

        toolbutton = QToolButton()
        toolbutton.setText("Button 1")
        toolbutton.setCheckable(True)
        toolbutton.setAutoExclusive(True)
        toolbar.addWidget(toolbutton)

        toolbutton = QToolButton()
        toolbutton.setText("Button 2")
        toolbutton.setCheckable(True)
        toolbutton.setAutoExclusive(True)
        toolbar.addWidget(toolbutton)

        
class WinToolBox(QWidget):
    def __init__(self):
        """ bouttons bisard on dirai une sorte de menu vertical mais plus pour du text ??? """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        toolbox = QToolBox()
        layout.addWidget(toolbox)

        label = QLabel()
        toolbox.addItem(label,"Honda")
        label = QLabel()
        toolbox.addItem(label,"Toyota")
        label = QLabel()
        toolbox.addItem(label,"Renault")


class WinMenuBar(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)

        actionFile = menubar.addMenu("File")
        actionFile.addAction("New")
        actionFile.addSeparator()
        actionFile.addAction("Quit")

        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")


class WinMenu(QWidget):
    def __init__(self):
        """ menu vertical """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        menu = QMenu()
        layout.addWidget(menu)

        actionFile = menu.addMenu("File")
        actionFile.addAction("New")
        actionFile.addSeparator()
        actionFile.addAction("Quit")

        menu.addMenu("Edit")
        menu.addMenu("View")
        menu.addMenu("Help")


class WinTab(QWidget):
    def __init__(self):
        """ onglets dans la fenetre """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel("Example content in a tab")
        
        frame = QFrame()
        framelayout = QGridLayout()
        frame.setLayout(framelayout)
        
        label2 = QLabel("More example text in the second tab")
        framelayout.addWidget(label2)
        button = QPushButton("Quit")
        button.clicked.connect(self.quit_appli)
        framelayout.addWidget(button)
        
        tabwidget = QTabWidget()
        tabwidget.addTab(label1,"Tab 1")
        tabwidget.addTab(frame,"Tab 2")
        layout.addWidget(tabwidget, 0, 0)

    def quit_appli(self):
        self.close()


class WinTabBar(QWidget):
    def __init__(self):
        """ tab qui fait toute la longueur mais pas integrer widget """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("blabla")

        tabbar = QTabBar()
        tabbar.addTab("Tab 1")
        tabbar.addTab("Tab 2")
        tabbar.addTab("Tab 3 ")
        layout.addWidget(tabbar, 0, 0)


class WinStackedWidget(QWidget):
    def __init__(self):
        """ stackedWidget sorte de liste de widget ou on affiche 1 de la liste L[0] ou L[1] ou ... """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.stackedwidget = QStackedWidget()
        layout.addWidget(self.stackedwidget, 0, 0)

        for k in range(1,4):
            label = QLabel("Stack Child %i" %(k))
            self.stackedwidget.addWidget(label)

            button = QPushButton("Stack %i" %(k))
            button.page = k
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button, k, 0)

    def on_button_clicked(self):
        button = self.sender() # get declencheur de la fonction
        self.stackedwidget.setCurrentIndex(button.page - 1)


class WinDockWidget(QWidget):
    def __init__(self):
        """ dockWidget est utile pour separer des widgets de la fenetre principale """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        dockwidget = QDockWidget()
        dockwidget.setFeatures(QDockWidget.DockWidgetClosable |
                               QDockWidget.DockWidgetVerticalTitleBar |
                               QDockWidget.DockWidgetFloatable)
        layout.addWidget(dockwidget)

        treewidget = QTreeWidget()
        dockwidget.setWidget(treewidget)

        label = QLabel("DockWidget is docked")
        layout.addWidget(label)


class WinFrom(QDialog):
    def __init__(self):
        """ formulaire avec QDialog, QFormLayout """
        QFormLayout.__init__(self)
        
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        
class WinComboBox(QWidget):
    def __init__(self):
        """ ComboBox est une liste deroulante """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        combobox = QComboBox()
        combobox.addItem("France")
        combobox.addItem("Angleterre")
        combobox.addItem("Brésil")
        combobox.currentTextChanged.connect(self.combobox_changed)
        layout.addWidget(combobox)

    def combobox_changed(self):
        combo = self.sender()
        print(combo.currentText())


class WinCompleter(QWidget):
    def __init__(self):
        """ proposition de mot dans Entry genre si y'a "S" -> Steven et Samantha propose (comme recherche web) """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        names = ["George", "Marcus", "Samantha", "Steven", "Maria"]

        completer = QCompleter(names)

        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)


class WinCalendarWidget(QWidget):
    def __init__(self):
        """ calendar """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        calendar = QCalendarWidget()
        layout.addWidget(calendar)


class WinDateEdit(QWidget):
    def __init__(self):
        """ input pour une date """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)
        
        dateedit = QDateEdit()
        layout.addWidget(dateedit)
        

class WinTimeEdit(QWidget):
    def __init__(self):
        """ input d'heure avec use QTime """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        time = QTime()
        # time de 13h 15m 40s (HMS)
        time.setHMS(13, 15, 40)

        timeedit = QTimeEdit()
        timeedit.setTime(time)
        layout.addWidget(timeedit, 0, 0)


class WinDateTimeEdit(QWidget):
    def __init__(self):
        """ input date et heure en meme temps """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        datetimeedit = QDateTimeEdit()
        layout.addWidget(datetimeedit)


class WinDialog(QWidget):
    def __init__(self):
        """ formulaire (basique) """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("This is a dialog.")
        layout.addWidget(label, 0, 0)
        
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)


class WinFileDialog(QWidget):
    def __init__(self):
        """ ouverture de fichier a partir d'une fenetre """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Open")
        button.clicked.connect(self.openFile)
        layout.addWidget(button)

    def openFile(self):
        # version visuel windows classique
        options = QFileDialog.Options()

        # version visuel differente
        #options = QFileDialog.DontUseNativeDialog
        file = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()",
                                           "","All Files (*);;Python Files (*.py)", options=options)
        print(file)
        

class WinFontDialog(QFontDialog):
    def __init__(self):
        """ selection d'une police a la Word """
        QFontDialog.__init__(self)
        self.fontSelected.connect(self.on_font_selected)

    def on_font_selected(self):
        font = self.currentFont()

        print("Name :         %s" %(font.family()))
        print("Size :         %i" %(font.pointSize()))
        print("Italic :       %s" %(font.italic()))
        print("Underline :    %s" %(font.underline()))
        print("Strikeout :    %s" %(font.strikeOut()))


class WinFontComboBox(QWidget):
    def __init__(self):
        """ selection de font dans liste deroulante """
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        fontcombobox = QFontComboBox()
        fontcombobox.currentFontChanged.connect(self.on_font_changed)
        layout.addWidget(fontcombobox)

    def on_font_changed(self):
        fontcombobox = self.sender()
        font = fontcombobox.currentFont()

        print("Selected font: %s" %(font.family()))


class Win(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        

def openWin(w):
    app = QApplication(sys.argv)

    window = w()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    openWin(Win)


