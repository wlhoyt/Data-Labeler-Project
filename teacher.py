import sys
import json
from os import path
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,  QMainWindow, QAction, QMenu, QTextEdit,QFontDialog,QColorDialog, QFileDialog, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import QPoint

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title  = 'Teacher Version'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.image = 'ay.jpg'
        if path.exists(self.image) == False:
            sys.exit("Error: Missing image name ay.jpg")
        self.flag = 0
        self.show()
        self.index = 0
        self.labels =[]



    #Creates the image and allows for the image to be drawn on
    def paintEvent(self, event):
        label = QLabel(self)
        pixmap = QPixmap(self.image)
        label.setPixmap(pixmap)

        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(255, 0, 255, 60))
        self.resize(pixmap.width(),pixmap.height())
        qp.drawPixmap(self.rect(),pixmap)
        qp.setBrush(br)
        qp.drawRect(QtCore.QRect(self.begin, self.end))
        if self.index > 0:
            for num in self.labels:
                first = QPoint(num['b_x'],num['b_y'])
                second = QPoint(num['e_x'],num['e_y'])
                qp.drawRect(QtCore.QRect(first,second))
    


    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newBox = contextMenu.addAction("New Box")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            f = open('infromation.txt','w')
            for num in self.labels:
                f.write(json.dumps(num))
                f.write("\n")
            f.close()
            self.close()
        # Resets the positions for the box
        if action == newBox:
            self.begin = event.pos()
            self.end = event.pos()
            self.flag = 1
            self.update()
    #Creates the end point of the boxint(
    def mouseReleaseEvent(self, event):
        if self.flag == 1:
            self.end = event.pos()
            #Save information here  
            self.addEntry()
            self.flag = 0
        self.update()

    def addEntry(self):
        entry = {
            "index":self.index,
            "name": "",
            "b_x":self.begin.x(),
            "b_y":self.begin.y(),
            "e_x":self.end.x(),
            "e_y":self.end.y()
        }
        self.choiceMessageBox(entry)

    def choiceMessageBox(self, diction):
            # message = QMessageBox.question(self, "Label Name", "DO NOT CLICK (X) YOUR LABEL WILL NOT BE SAVED",
            #                             QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
            msgBox = QMessageBox()
            msgBox.setText("Please Choose Label Name")
            msgBox.setInformativeText("DO NOT CLICK (X) YOUR LABEL WILL NOT BE SAVED")
            msgBox.addButton("Star",QMessageBox.ActionRole)
            msgBox.addButton("Planet",QMessageBox.ActionRole)
            msgBox.addButton("Sun",QMessageBox.ActionRole)
            msgBox.addButton("Dust",QMessageBox.ActionRole)
            msgBox.addButton("Galaxy",QMessageBox.ActionRole)
            msgBox.addButton("Comet",QMessageBox.ActionRole)
            ret = msgBox.exec()
            if ret == 0:
                diction["name"] = "Star"
            if ret == 1:
                diction["name"] = "Planet"
            if ret == 2:
                diction["name"] = "Sun"
            if ret == 3:
                diction["name"] = "Dust"
            if ret == 4:
                diction["name"] = "Galaxy"
            if ret == 5:
                diction["name"] = "Comet"
            self.index = self.index + 1
            self.labels.append(diction)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

