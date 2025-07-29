import sys
sys.path.append("./lec07")

from PyQt6.QtWidgets import QApplication, QDialog
from calculator import Ui_Dialog  # ← This must match the file name and class name



class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.input1.valueChanged.connect(self.update_output)
        self.ui.input2.valueChanged.connect(self.update_output)

    def update_output(self):
        result = self.ui.input1.value() + self.ui.input2.value()
        self.ui.output.setText(str(result))

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())
