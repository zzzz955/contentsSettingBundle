from PyQt5.QtWidgets import QDialog, QCalendarWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QLabel, QTableWidget
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIntValidator

class calendar_dialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("시즌 시작 일정 선택")
        self.setGeometry(500,100,600,600)
        self.main_window = main_window
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.showDate)
        self.val = QLineEdit()
        self.accept_btn = QPushButton("적용")
        self.accept_btn.clicked.connect(self.accept)
        self.reject_btn = QPushButton("취소")
        self.reject_btn.clicked.connect(self.reject)
        layout = QVBoxLayout()
        layout.addWidget(self.cal)
        layout.addWidget(self.val)
        layout.addWidget(self.accept_btn)
        layout.addWidget(self.reject_btn)
        self.setLayout(layout)

    def showDate(self, data):
        self.val.setText(data.toString(Qt.ISODate))

    def accept(self):
        try:
            self.main_window.lineedit2.setText(self.val.text())
            super().accept()
        except Exception as e:
            print(e)

    def reject(self):
        self.val.clear()
        super().reject()

class colosseum_val(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("콜로세움 추가 정보 입력")
        self.main_window = main_window
        self.table_widget = QTableWidget()
        self.accept_btn = QPushButton("적용")
        self.accept_btn.clicked.connect(self.accept)
        self.reject_btn = QPushButton("취소")
        self.reject_btn.clicked.connect(self.reject)
        self.add_btn = QPushButton("추가")
        self.add_btn.clicked.connect(self.add_row)
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        self.setLayout(layout)
        layout.addLayout(grid_layout)
        grid_layout.addWidget(self.add_btn, 0, 0)
        grid_layout.addWidget(self.accept_btn, 0, 1)
        grid_layout.addWidget(self.reject_btn, 0, 2)
        layout.addWidget(self.table_widget)

        self.table_widget.clear()
        header = ['삭제', '제한 전투력', '서버ID']
        self.table_widget.setColumnCount(len(header))
        self.table_widget.setHorizontalHeaderLabels(header)

    def add_row(self):
        del_btn = QPushButton('삭제')
        del_btn.clicked.connect(self.del_row)
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        self.table_widget.setCellWidget(row_count, 0, del_btn)

    def del_row(self):
        sender = self.sender()
        if isinstance(sender, QPushButton):
            index = self.table_widget.indexAt(sender.pos())
            row = index.row()
            self.table_widget.removeRow(row)