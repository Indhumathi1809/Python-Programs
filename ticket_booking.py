import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton

class TicketBookingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ticket Booking App')
        self.setGeometry(100, 100, 400, 200)

        self.movie_label = QLabel('Select Movie:')
        self.movie_combo = QComboBox()
        self.movie_combo.addItems(['Movie A', 'Movie B', 'Movie C'])

        self.seat_label = QLabel('Select Seat:')
        self.seat_combo = QComboBox()
        self.seat_combo.addItems(['Seat 1', 'Seat 2', 'Seat 3', 'Seat 4'])

        self.book_button = QPushButton('Book Ticket')
        self.book_button.clicked.connect(self.book_ticket)

        layout = QVBoxLayout()
        movie_layout = QHBoxLayout()
        movie_layout.addWidget(self.movie_label)
        movie_layout.addWidget(self.movie_combo)
        layout.addLayout(movie_layout)

        seat_layout = QHBoxLayout()
        seat_layout.addWidget(self.seat_label)
        seat_layout.addWidget(self.seat_combo)
        layout.addLayout(seat_layout)

        layout.addWidget(self.book_button)
        self.setLayout(layout)

    def book_ticket(self):
        selected_movie = self.movie_combo.currentText()
        selected_seat = self.seat_combo.currentText()
        print(f'Booked ticket for {selected_movie}, Seat: {selected_seat}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicketBookingApp()
    window.show()
    sys.exit(app.exec_())
