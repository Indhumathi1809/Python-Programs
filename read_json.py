import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import json

class JsonTableViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('JSON Table Viewer')
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)  # Assuming JSON data has two columns: key and value
        self.table_widget.setHorizontalHeaderLabels(['Key', 'Value'])

        self.load_json_data('data.json')

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def load_json_data(self, file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            self.populate_table(data)

    def populate_table(self, data):
        self.table_widget.setRowCount(len(data))
        row = 0
        for key, value in data.items():
            key_item = QTableWidgetItem(str(key))
            value_item = QTableWidgetItem(str(value))
            self.table_widget.setItem(row, 0, key_item)
            self.table_widget.setItem(row, 1, value_item)
            row += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JsonTableViewer()
    window.show()
    sys.exit(app.exec_())
