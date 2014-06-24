import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        self.create_hello_layout()
        self.stacked_layout.setCurrentIndex(0)
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)

    def create_initial_layout(self):
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("Submit")

        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.text_box)
        self.initial_layout.addWidget(self.submit_button)

        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.initial_layout)
        
        self.stacked_layout.addWidget(self.initial_widget)

        self.submit_button.clicked.connect(self.switch_layout)

    def create_hello_layout(self):
        self.label = QLabel()
        self.back_button = QPushButton("Back")

        self.hello_layout = QVBoxLayout()
        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)

        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.hello_layout)

        self.stacked_layout.addWidget(self.hello_widget)

        self.back_button.clicked.connect(self.switch_layout)

    def switch_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.label.setText("Hello {0}".format(name))
    

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
