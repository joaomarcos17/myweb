# imported modules for Qt5 web engine
from PyQt5.QtWidgets import *  
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

# this a very simple web browser built in python !!
class MyWebBrowesr(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWebBrowesr, self).__init__(*args, **kwargs)

                                    # title of the browser
        self.window = QTabWidget()
        self.window.setWindowTitle("FreeWeb Web browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView() # function of the browser

        # functions of the buttons

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        
        self.back_btn.clicked.connect(self.browser.back)

        self.forward_btn.clicked.connect(self.browser.forward)

       # end of functions
            #   layout of the browser
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        #   defaut url
        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))



app = QApplication([])

window = MyWebBrowesr()

app.exec_()




