from PyQt5.QtWidgets import QDialog, QCalendarWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout, QTableWidget, QMessageBox
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
        self.val.setReadOnly(True)
        self.accept_btn = QPushButton("적용")
        self.accept_btn.clicked.connect(self.accept)
        self.reject_btn = QPushButton("취소")
        self.reject_btn.clicked.connect(self.reject)
        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        layout.addWidget(self.cal)
        layout.addWidget(self.val)
        layout.addLayout(h_layout)
        h_layout.addWidget(self.accept_btn)
        h_layout.addWidget(self.reject_btn)
        self.setLayout(layout)

    def showDate(self, data):
        # 선택된 캘린더 데이터 노출
        self.val.setText(data.toString(Qt.ISODate))

    def accept(self):
        # 선택한 날짜 적용 및 다이얼로그 닫기
        self.main_window.lineedit2.setText(self.val.text())
        super().accept()

    def reject(self):
        # 반환값 없이 다이얼로그 닫기
        self.val.clear()
        super().reject()

class colosseum_val(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setGeometry(500,100,500,500)
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

        header = ['삭제', '제한 전투력', '서버ID']
        self.table_widget.setColumnCount(len(header))
        self.table_widget.setHorizontalHeaderLabels(header)
        self.table_widget.resizeColumnsToContents()

    def add_row(self):
        # tablewidget의 행 추가
        del_btn = QPushButton('삭제')
        del_btn.clicked.connect(self.del_row)
        lineedit1 = QLineEdit()
        lineedit2 = QLineEdit()
        lineedit1.setValidator(QIntValidator())
        lineedit2.setValidator(QIntValidator())

        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        self.table_widget.setCellWidget(row_count, 0, del_btn)
        self.table_widget.setCellWidget(row_count, 1, lineedit1)
        self.table_widget.setCellWidget(row_count, 2, lineedit2)

    def del_row(self):
        # tablewidget의 행 삭제
        sender = self.sender()
        if isinstance(sender, QPushButton):
            index = self.table_widget.indexAt(sender.pos())
            row = index.row()
            self.table_widget.removeRow(row)

    def accept(self):
        # 테이블 정보 저장 및
        rows = self.table_widget.rowCount()
        if rows:
            for row in range(rows):
                cp_min = self.table_widget.cellWidget(row, 1)
                server_id = self.table_widget.cellWidget(row, 2)
                if cp_min.text() and server_id.text():
                    self.main_window.colosseum_min_cps.append(cp_min.text())
                    self.main_window.colosseum_server_ids.append(server_id.text())
                else:
                    QMessageBox.warning(self, '경고', '입력 데이터를 확인해 주세요.')
                    break
            if len(self.main_window.colosseum_min_cps) and len(self.main_window.colosseum_server_ids) == rows:
                super().accept()
        else:
            self.main_window.colosseum_min_cps = []
            self.main_window.colosseum_server_ids = []
            super().reject()

    def reject(self):
        self.main_window.colosseum_min_cps = []
        self.main_window.colosseum_server_ids = []
        super().reject()