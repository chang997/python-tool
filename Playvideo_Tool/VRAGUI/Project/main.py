import sys
from PyQt5.QtWidgets import QApplication
from Project.window2 import VRAWindow2
from Project.window import VRAWindow

app = QApplication(sys.argv)
window = VRAWindow()
window.resize(640, 480)
window.show()
sys.exit(app.exec_())




