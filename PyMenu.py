#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from PyQt4 import QtCore, QtGui, uic

PATH = os.getcwd()

class Example(QtGui.QWidget):
	def __init__(self, uiFile = ""):
		QtGui.QWidget.__init__(self)
		self.ui = uic.loadUi(PATH + "/ui/example.ui", self)
		
		self.btnExample.clicked.connect(self.Ex)

	def Ex(self):
		QtGui.QMessageBox.about(self, QtCore.QString("This is an example function"), QtCore.QString("This is an example function"))

class Principal(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = uic.loadUi(PATH + "/ui/principal.ui", self)

		self.Actions = {"Menu A": [
										("A1",self.say, 0),
										("A2",self.say, 0),
									],
					    "Menu B": [
					    				("Example A",lambda:self.load(Example(),0)),
					    				("Example B",lambda:self.load(Example(),1)),


					    			],
					    "Menu C": [
					    				("C1", lambda:self.say("Menu C1")),
					    				("C2", lambda:self.say("Menu C2")),
					    				("C4", lambda:self.say("Menu C3")),
					    				("C4", lambda:self.say("Menu C4")),
									],					    			
					    "Direct action":lambda:self.say("Direct action")
					    }
		
		self.cstMenu()
		self.show()

		self.Blank = QtGui.QWidget(self)
		self.pilaW.setCurrentIndex( self.pilaW.addWidget( self.Blank) )

	def cstMenu(self):
		for x in self.Actions.keys()[::-1]:
			if type(self.Actions[x]) == list:
				item = self.menuBar().addMenu("&"+x)        
				for y in self.Actions[x]:
					item.addAction(y[0], y[1])
			else:
				self.menuBar().addAction(x, self.Actions[x])
	

	def load(self, wdg, tipo = 0):
		self.pilaW.removeWidget(self.pilaW.currentWidget())
		if tipo == 0:
			self.pilaW.setCurrentIndex( self.pilaW.addWidget(wdg) )
		else:
			wdg.show()


	def say(self,txt = "Nothing"):
		print "Say:",txt

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	SimpleMenu = Principal()
	sys.exit(app.exec_())
