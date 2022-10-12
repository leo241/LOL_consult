from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QToolTip, QLabel, QTabWidget,QLineEdit,QPushButton, QComboBox, QScrollArea, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont, QPainter,QPen, QPixmap,QCursor,QKeyEvent # 调色板
from PyQt5.QtCore import Qt,QRect
import sys
import qtawesome
from all_dics import *
import re # 用以正则表达式获取版本信息
import os # 用以获取本目录下的文件名称

class PositionWindow(QWidget): # 继承QWidget这个类别

    def __init__(self,position):
        super().__init__() # 继承类
        self.position = position
        self.initUI()


    def initUI(self):
        mini_font = QFont()
        mini_font.setFamily('微软雅黑')
        mini_font.setPointSize(8)
        self.mini_font = mini_font

        # 中文字体格式
        label_font = QFont()
        label_font.setFamily('微软雅黑')
        label_font.setBold(True)
        label_font.setPointSize(10.5) # 字体大小
        # label_font.setWeight(50)
        self.label_font_Chinese = label_font

        # 中文字体格式
        label_font = QFont()
        label_font.setFamily('微软雅黑')
        label_font.setBold(True)
        label_font.setPointSize(11.5)  # 字体大小
        # label_font.setWeight(50)
        self.label_font_Chinese2 = label_font

        # 英文字体格式
        label_font = QFont()
        label_font.setFamily("Roman times")
        # label_font.setBold(True)
        label_font.setPointSize(5)
        # label_font.setWeight(50)
        self.label_font_English = label_font

        placeholder_font = QFont()
        placeholder_font.setFamily('微软雅黑')
        placeholder_font.setPointSize(8)
        placeholder_font.setBold(True)
        self.placeholder_font = placeholder_font

        # QToolTip.setFont(QFont("Roman times", 15))
        QToolTip.setFont(placeholder_font)
        # self.setToolTip('<b>奇怪的吴小志同学</b>')
        # 窗口参数的设定
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255,255,255))  # 背景颜色
        self.setPalette(palette1)
        self.setAutoFillBackground(True)

        # 获取版本信息
        file_names = os.listdir()
        version_list = list()
        for file_name in file_names:
            version_list += re.findall('\d+\.\d+', file_name)
        self.version = max(version_list) # 最近的版本作为最终版本



        self.resize(900, 800)
        self.setWindowOpacity(1)  # 窗口设置为不透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setWindowTitle('韩服查询')
        self.setWindowIcon(QIcon('hero_name/jinx.png'))
        self.add_scroll()
        self.add_input_text()
        self.add_consult_btn()
        self.add_version()



    def add_scroll(self): # 增加下拉条
        '''
        一定要看好这里的包含关系：self(widget)>la(layout)>scroll>a(widget)>btn
        换句话说，想要加入滚动条，需要一个layout作为过度，而想在滚动条里加入零件，又需要把零件放在widget里面过度
        :return:
        '''
        # l1 = QHBoxLayout()

        a = QWidget()
        a.setMinimumSize(1000, 5000) # 这个参数很关键，决定了滚动条的容量
        # a.setStyleSheet("QPushButton{color:black}"
        #                     "QPushButton:hover{color:red}"
        #                     "QPushButton{background-color:rgb(250,250,250)}"
        #                     "QPushButton{border:0.5px}"
        #                     "QPushButton{border-radius:1px}"
        #                     "QPushButton{padding:0.5px 0.5px}"
        #                     "QPushButton{text-align:left}"
        #                     "QPushButton{vertical-align:middle}")
        # a.setLayout(l1)

        version = self.version
        with open(version + f'/{self.position}.txt', encoding='gbk') as file:
            content = file.readlines()
        y_axis = 50
        self.button_list = list()
        for line in content:  # 读取top.txt，获取所有上单名称
            btn = QPushButton(a)

            hero_name = line.split('\t')[0]


            btn.setCursor(QCursor(Qt.PointingHandCursor))  # 手形按钮点击
            # btn.setIcon(QIcon(f'hero_name/{hero_dict[hero_name]}.png')) # 设置图片

            btn.setFont(self.label_font_Chinese)
            btn.setGeometry(QRect(50, y_axis, 900, 60))
            # btn.move(10, y_axis)
            # btn.setMinimumSize(900,10)
            btn.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,255,255)}"
                            "QPushButton{border:0.5px}"
                            "QPushButton{border-radius:1px}"
                            "QPushButton{padding:0.5px 0.5px}"
                            "QPushButton{text-align:left}" 
                            "QPushButton{vertical-align:middle}"
                              )
            # btn.setStyleSheet('text-align:left')
            btn.setText(line)
            btn.clicked.connect(self.detail_info)

            # # 添加图片按钮标签
            btn = QPushButton(a)


            btn.setIcon(QIcon(f'hero_name/{hero_dict[hero_name]}.png'))  # 设置图片

            btn.setGeometry(QRect(20, y_axis + 8, 20, 20))
            btn.setStyleSheet("QPushButton{color:black}"
                              "QPushButton:hover{color:red}"
                              "QPushButton{background-color:rgb(255,255,255)}"
                              "QPushButton{border:0.5px}"
                              "QPushButton{border-radius:1px}"
                              "QPushButton{padding:0.5px 0.5px}"
                              "QPushButton{text-align:left}"
                              "QPushButton{vertical-align:middle}"
                              )

            y_axis += 70
        # l1.addWidget(btn)



        scroll = QScrollArea()
        scroll.setWidget(a)

        la = QHBoxLayout()
        la.addWidget(scroll)

        self.setLayout(la)


    def detail_info(self):
        version = self.version
        sender = self.sender()
        hero_name = sender.text().split('\t')[0]
        self.setWindowIcon(QIcon(f'hero_name/{hero_dict[hero_name]}.png'))
        file_name = f"{version}/{self.position}/{hero_dict[hero_name]}.txt"
        with open(file_name, encoding='gbk') as file:
            content = file.read()
        QMB = QMessageBox()
        # pic = f'hero_name/{hero_dict[hero_name]}.png'
        # print(pic)
        # QMB.setWindowIcon(QIcon(pic))
        QMB.about(self, hero_dict_chinese[hero_dict[hero_name]], content)



    def add_input_text(self):
        '''添加用户输入文本框'''
        self.consult1 =QLineEdit(self)
        self.consult1.setGeometry(QRect(25, 18, 300, 38))
        self.consult1.setFont(self.label_font_Chinese)
        # self.consult1.setPlaceholderText('诺克萨斯之手')

    def add_consult_btn(self):
        btn = QPushButton(qtawesome.icon('fa.search', color='yellow'), "查 询", self)
        btn.setCursor(QCursor(Qt.PointingHandCursor))  # 手形按钮点击

        btn.setFont(self.label_font_Chinese)
        btn.setGeometry(QRect(350,18,120,38))
        btn.setStyleSheet("QPushButton{color:white}"
                          "QPushButton:hover{color:red}"
                          "QPushButton{background-color:rgb(40,40,255)}"
                          "QPushButton{border:2px}"
                          "QPushButton{border-radius:10px}"
                          "QPushButton{padding:2px 4px}")
        btn.clicked.connect(self.consult)

    def consult(self):
        version = self.version
        hero_name = self.consult1.text()
        self.setWindowIcon(QIcon(f'hero_name/{hero_dict[hero_name]}.png'))
        file_name = f"{version}/{self.position}/{hero_dict[hero_name]}.txt"
        with open(file_name, encoding='gbk') as file:
            content = file.read()
        QMB = QMessageBox()
        # pic = f'hero_name/{hero_dict[hero_name]}.png'
        # print(pic)
        # QMB.setWindowIcon(QIcon(pic))
        QMB.about(self, hero_dict_chinese[hero_dict[hero_name]], content)
        # QMessageBox.about(self, hero_dict_chinese[hero_dict[hero_name]], content)
        # QMessageBox.setWindowIcon(QIcon(f'hero_name/{hero_dict[hero_name]}.png'))

    def keyPressEvent(self, QKeyEvent):  # 键盘某个键被按下时调用
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            # key()  是普通键
            self.consult()

    def add_version(self): # 增加版本信息
        # 添加文本标签
        label = QLabel(self)
        # 设置标签的左边距，上边距，宽，高
        label.setGeometry(QRect(750,18,300,38))
        # 设置文本标签的字体和大小，粗细等
        # label.setFont(QFont("微软雅黑", 12))
        label.setFont(self.label_font_Chinese2)
        label.setText(f"版本：{self.version}")
        label.setStyleSheet("color:rgb(255,150,200)")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    PositionList = ['top','jungle','mid','adc','support']
    main = PositionWindow(PositionList[3])
    main.show()
    sys.exit(app.exec_())