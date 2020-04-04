import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import subprocess
import tempfile
from subprocess import call
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Assignment : Pacman Ai'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.initUI()
    
    def initUI(self):

        
        #f2 = open("cmd.txt", "r")
        #contents =f2.read()
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        #creaing title
        self.titleLable = QLabel(self)
        self.titleLable.setText("Run Options")
        self.titleLable.move(30,10)
        

        self.titleOutput = QLabel(self)
        self.titleOutput.setText("Console Pacman")
        self.titleOutput.move(200,10)




        # Create textbox
        self.textbox = QTextEdit(self)
        self.textbox.move(150, 50)
        self.textbox.resize(200,300)
        self.textbox.setStyleSheet("color: #90EE90;  background-color: black;padding:10px")
        #self.textbox.setText(contents)

        
        
        # Create a button in the window
        self.button = QPushButton('Pacman Trial Run', self)
        
        self.button.resize(150,50)
        self.button2 = QPushButton('Pacman MultiPlayer',self)
        
        self.button2.resize(150,50)

        self.button3 = QPushButton('Pacman Keyboard',self)
        
        self.button3.resize(150,50)

        self.button4 = QPushButton('Stop Execution',self)
        
        self.button4.resize(120,30)
        self.button4.setStyleSheet("color: black;  background-color: red")



        self.comboBox = QComboBox(self)
        self.comboBox.setObjectName(("monsterSel"))
        self.comboBox.setGeometry(QRect(40, 40, 150, 50))
        self.comboBox.addItem("Blue Monster Keys")
        self.comboBox.addItem("Blue Monster 2 Keys")
        self.comboBox.addItem("Red Monster Keys")
        self.comboBox.addItem("Red Monster 2 Keys")
        



        #alignment
        self.button.move(0,50)
        self.button2.move(0,100)
        self.button3.move(0,200)
        self.comboBox.move(0,150)
        self.button4.move(10,300)


        
        # connect button to function on_click
        self.button.clicked.connect(self.on_clickTrial)
        self.button3.clicked.connect(self.on_clickKeyboard)
        self.button4.clicked.connect(self.stopMain)
        self.button2.clicked.connect(self.on_clickMultiplayer)
        self.show()

        stringmain = self.textbox.toPlainText()
        f= open("cmd.txt","a+")
        f.write(stringmain)
    
    @pyqtSlot()
    def on_clickTrial(self):
        self.textbox.setText("Pacmac Trial Will Run -- This makes A TIE Between both")
        call(["python", "capture.py" , "-l" ,"testCapture.lay"])
       
        

    def on_clickKeyboard(self):
        index = self.comboBox.currentIndex()
        if index == 0:
            #python capture.py -r BaselineAgents -b BaselineAgents --blueOpts first=keys
            self.textbox.setText("Pacmac With Blue Monster As Keywboard will run")
            result = subprocess.run(['python', 'capture.py' , '-r' , 'BaselineAgents' ,'-b' ,'BaselineAgents' , '--blueOpts','first=keys' ], stdout=subprocess.PIPE)
            
        elif index == 1: 
            self.textbox.setText("Pacmac With Blue Monster 2 As Keywboard will run")
            result = subprocess.run(['python', 'capture.py' , '-r' , 'BaselineAgents' ,'-b' ,'BaselineAgents' , '--blueOpts','second=keys' ], stdout=subprocess.PIPE)
            
        elif index == 2: 
            self.textbox.setText("Pacmac With Red Monster As Keywboard will run")
            result = subprocess.run(['python', 'capture.py' , '-r' , 'BaselineAgents' ,'-b' ,'BaselineAgents' , '--redOpts','first=keys' ], stdout=subprocess.PIPE)
            
        elif index == 3: 
            self.textbox.setText("Pacmac With Red Monster 2 As Keywboard will run")
            result = subprocess.run(['python', 'capture.py' , '-r' , 'BaselineAgents' ,'-b' ,'BaselineAgents' , '--redOpts','second=keys' ], stdout=subprocess.PIPE)
            

    def on_clickMultiplayer(self):
        self.textbox.setText("Pacmac With no Keyboard input will run and have Automatic Play")
        result = subprocess.run(['python', 'capture.py' , '-r' , 'BaselineAgents' ,'-b' ,'BaselineAgents' ], stdout=subprocess.PIPE)
               

    
    def stopMain(self):
        sys.exit(0)    
    

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    

    ex = App()
    sys.exit(app.exec_())