from PySide6.QtWidgets import QApplication, QMainWindow

# QT application object
app = QApplication([])

# add QT Main Window
window = QMainWindow()
window.show()

# event loop.
app.exec()
