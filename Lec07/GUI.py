from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
import sys


#def on_click():
#    print("Button clicked!")

# Construct a simple PyQt6 application with a window, label, and button
app = QApplication(sys.argv)
window = QWidget()

# Create layouts
v_layout = QVBoxLayout()
h_layout = QHBoxLayout()

# Create buttons
btn1 = QPushButton("Top")
btn2 = QPushButton("Left")
btn3 = QPushButton("Right")

# Add buttons to horizontal layout
h_layout.addWidget(btn2)
h_layout.addWidget(btn3)

# Add top button and horizontal layout to vertical layout
v_layout.addWidget(btn1)
v_layout.addLayout(h_layout)

window.setLayout(v_layout)

window.setWindowTitle("Nested Layout Example")
window.resize(300, 400)
window.show()  # Show the window with settings of Title and Size

sys.exit(app.exec())

# Alt + Shift + E : Run highlighted codes
