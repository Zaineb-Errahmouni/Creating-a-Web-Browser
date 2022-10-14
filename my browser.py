from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()
        #afichage de la page navigateur
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.navigateur =QWebEngineView()
        #appel le naavigateur github
        self.navigateur.setUrl(QUrl('http://googl.com/'))
        self.setCentralWidget(self.navigateur)
        self.showMaximized()


        #navbar:
        navbar = QToolBar()
        self.addToolBar(navbar)

        #add the submit
        acceuil_btn = QAction('Acceuil', self)
        acceuil_btn.triggered.connect(self.url_acceuil)
        navbar.addAction(acceuil_btn)



        return_btn = QAction('Rtour', self)
        return_btn.triggered.connect(self.navigateur.back)
        navbar.addAction(return_btn)

        rafraichir_btn = QAction('Actualiser', self)
        rafraichir_btn.triggered.connect(self.navigateur.reload)
        navbar.addAction(rafraichir_btn )


        avancer_btn = QAction('Suivant', self)
        avancer_btn.triggered.connect(self.navigateur.forward)
        navbar.addAction(avancer_btn)



        #ajouter recherche

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.url_bar)

        self.navigateur.urlChanged.connect(self.update_url)

    def url_acceuil(self):
        self.navigateur.setUrl(QUrl('http://googl.com/')) 
    

    def navigation(self):
        url = self.url_bar.text()
        self.navigateur.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
fenetre = FenPrincipale()
app.exec()


