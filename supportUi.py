import sys
from PyQt5.QtWidgets import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500,500)
    w.setWindowTitle("Pacman Ai Assignment")
    w.show()
    label = QLabel(w)
    label1 = QLabel(w)
    label1.setText("PACMAN AI")
    label.setText("PLEASE SELECT ANY ONE EXECUTION")
    
    label.move(100,40)
    label.show()
    label1.show()


    
   
    grid = QGridLayout(w)
    grid.addWidget(QPushButton("Pacman Simple Trial Layout"),0,0)
    grid.addWidget(QPushButton("Pacman  Multiplayer Trial Layout"),0,1)
    grid.addWidget(QPushButton("Pacman  Multiplayer With Keyboard For RED"),1,0)
    grid.addWidget(QPushButton("Pacman  Multiplayer With Keyboard For BLUE"),1,1)
    grid.addWidget(QPushButton("Pacman MultiAgent  "),2,0,1,0)
    w.show()
    sys.exit(app.exec_())