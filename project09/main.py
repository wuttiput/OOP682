import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QToolBar, QStyle


# 1. สร้างคลาสย่อยของ QMainWindow เพื่อสร้างหน้าต่างแอป
class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My PySide6 Browser")
        self.resize(1024, 768)
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl("http://www.google.com"))
        
# 2. ตั้งค่าลูปการทำงานของแอปพลิเคชัน (Application Loop)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())