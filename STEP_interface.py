import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget


class FolderContainerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Folder Container Example")
        self.setGeometry(100, 100, 800, 600)

        # Create the file system model
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath("/")

        # Create the tree view
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setRootIndex(self.file_system_model.index("/"))

        # Create the main container widget
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(self.tree_view)

        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderContainerApp()
    window.show()
    sys.exit(app.exec_())