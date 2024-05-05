import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDateTimeEdit
from PyQt5.QtCore import QDateTime, QTimer
import schedule
import time

class TaskScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Task Scheduler')
        self.setGeometry(100, 100, 400, 200)

        self.task_name_label = QLabel('Task Name:')
        self.task_name_edit = QLineEdit()
        
        self.task_time_label = QLabel('Task Time:')
        self.task_time_edit = QDateTimeEdit()
        self.task_time_edit.setDateTime(QDateTime.currentDateTime())

        self.add_task_button = QPushButton('Add Task')
        self.add_task_button.clicked.connect(self.add_task)

        self.task_list_label = QLabel('Task List:')
        self.task_list = QLabel()

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_tasks)
        self.timer.start(1000)  # Check tasks every second

        layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        form_layout.addWidget(self.task_name_label)
        form_layout.addWidget(self.task_name_edit)
        form_layout.addWidget(self.task_time_label)
        form_layout.addWidget(self.task_time_edit)
        form_layout.addWidget(self.add_task_button)
        layout.addLayout(form_layout)
        layout.addWidget(self.task_list_label)
        layout.addWidget(self.task_list)
        self.setLayout(layout)

    def add_task(self):
        task_name = self.task_name_edit.text()
        task_time = self.task_time_edit.dateTime().toPyDateTime()
        schedule.every().day.at(task_time.strftime('%H:%M')).do(self.notify_task, task_name)
        self.update_task_list()

    def notify_task(self, task_name):
        current_time = time.strftime('%H:%M:%S')
        self.task_list.setText(f'Task "{task_name}" scheduled for {current_time}')

    def check_tasks(self):
        schedule.run_pending()
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
        self.task_list.setText(f'Current Time: {current_time}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TaskScheduler()
    window.show()
    sys.exit(app.exec_())
