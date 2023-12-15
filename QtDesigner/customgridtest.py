import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PySide6.QtCore import QSize


class DynamicGridLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # Add some buttons to the layout for demonstration
        for i in range(10):
            self.grid_layout.addWidget(QPushButton(f"Button {i}"), i // 2, i % 2)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustGridLayout()

    def adjustGridLayout(self):
        # Calculate the new number of rows and columns based on the window size
        width = self.width()
        height = self.height()

        # Simple logic to determine rows and columns (modify as needed)
        num_columns = max(1, width // 500)
        num_rows = max(1, height // 100)

        # Temporarily store the widgets in a list and remove them from the layout
        widgets = []
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            self.grid_layout.removeWidget(widget)
            widgets.append(widget)
            widget.hide()

        # Re-add the widgets in the new positions
        for i, widget in enumerate(widgets):
            self.grid_layout.addWidget(widget, i // num_columns, i % num_columns)
            widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = DynamicGridLayout()
    mainWin.show()
    sys.exit(app.exec())


