from PyQt5.QtWidgets import QApplication, QWidget,  QMessageBox, QToolTip, QLabel, QTabWidget, QPushButton,QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont, QPixmap, QCursor # 调色板
from PyQt5.QtCore import Qt,QRect
import sys
from PositionWindow import *
import qtawesome
from warnings import filterwarnings
filterwarnings("ignore")

# 虚拟环境：C:\Users\e\.virtualenvs\selenium-C9YVgdxR

class main_window(QWidget): # 继承QWidget这个类别

    def __init__(self,client1,client2,client3,client4,client5):
        super().__init__() # 继承类
        self.client1 = client1
        self.client2 = client2
        self.client3 = client3
        self.client4 = client4
        self.client5 = client5
        self.initUI()

    def initUI(self):
        mini_font = QFont()
        mini_font.setFamily('微软雅黑')
        mini_font.setPointSize(8)
        self.mini_font = mini_font

        label_font = QFont()
        label_font.setFamily('微软雅黑')
        label_font.setBold(True)
        label_font.setPointSize(12)
        # label_font.setWeight(50)
        self.label_font = label_font

        placeholder_font = QFont()
        placeholder_font.setFamily('微软雅黑')
        placeholder_font.setPointSize(10)
        self.placeholder_font = placeholder_font

        # QToolTip.setFont(QFont("Roman times", 15))
        QToolTip.setFont(placeholder_font)
        # self.setToolTip('<b>奇怪的吴小志同学</b>')
        # 窗口参数的设定
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255,255,255))  # 背景颜色
        self.setPalette(palette1)
        self.setAutoFillBackground(True)

        self.resize(1000, 800)
        self.setWindowOpacity(1)  # 窗口设置为不透明
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框

        self.setWindowTitle('韩服查询')
        self.setWindowIcon(QIcon('lol_logo.png'))
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.loadTabWidgets()) # 添加分窗口
        self.setLayout(self.main_layout)
        self.add_picture()

        # self.add_close_btn()


    def add_picture(self):
        '''为界面添加图像'''
        label = QLabel(self)
        label.setGeometry(QRect(725, 550, 200, 200))
        label.setText('')
        label.setPixmap(QPixmap('zeo2.png'))
        label.setScaledContents(True) # 开启自适应大小


    def closeEvent(self, event):
        '''关闭时的弹框设置'''
        reply = QMessageBox.question(self, '退出提示',
                                     "确定退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def loadTabWidgets(self):
        tabWidgets = QTabWidget()
        tabWidgets.setGeometry(0,0,400,10)
        tabWidgets.setFont(self.label_font)
        tabWidgets.addTab(self.client1, "上路")

        tabWidgets.addTab(self.client2, "打野")
        tabWidgets.addTab(self.client3, "中路")
        tabWidgets.addTab(self.client4, "下路")
        tabWidgets.addTab(self.client5, "辅助")
        tabWidgets.show()
        return tabWidgets

    # def add_close_btn(self):
    #     self.abutton = QPushButton("", self)
    #     self.abutton.setCursor(QCursor(Qt.PointingHandCursor))  # 手形按钮点击
    #
    #     self.abutton.setGeometry(QRect(1400, 4, 45, 42))
    #     self.abutton.setStyleSheet("QPushButton{color:white}"
    #                                "QPushButton:hover{color:white}"
    #                                "QPushButton{background-color:rgb(255,255,255)}"
    #                                "QPushButton{border:0px}"
    #                                # "QPushButton{border-radius:10px}"
    #                                # "QPushButton{padding:2px 4px}"
    #                                )
    #     self.abutton.setIcon(QIcon("pix/close.png"))
    #     self.abutton.clicked.connect(self.close)
    #     self.abutton.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c1 = PositionWindow('top')
    c2 = PositionWindow('jungle')
    c3 = PositionWindow('mid')
    c4 = PositionWindow('adc')
    c5 = PositionWindow('support')
    main = main_window(c1,c2,c3,c4,c5)
    main.show()
    sys.exit(app.exec_())