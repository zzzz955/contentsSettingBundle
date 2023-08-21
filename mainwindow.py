from functools import wraps
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, \
    QMessageBox, QFrame, QLabel, QLineEdit, QToolButton, QGridLayout
from PyQt5.QtGui import QIcon, QIntValidator
from qt_material import apply_stylesheet
import dataframes
from dialogs import *
from dataframes import *

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            QMessageBox.warning(args[0], '예외 발생', f'요청 처리 중 예외가 발생하였습니다. 예외 정보: {e}')
            raise
    return wrapper

class contentsSettingBundle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("콘텐츠/이벤트 세팅 파일 제작")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        frame1 = QFrame(self)
        frame2 = QFrame(self)
        frame3 = QFrame(self)
        label1 = QLabel("시즌 번호 : ")
        self.lineedit1 = QLineEdit()
        self.lineedit1.setPlaceholderText("10")
        self.lineedit1.setValidator(QIntValidator())
        label2 = QLabel("시즌 시작 일자 : ")
        self.lineedit2 = QLineEdit()
        self.lineedit2.setPlaceholderText("YYYY-MM-DD")
        self.lineedit2.setReadOnly(True)
        self.tool_button1 = QToolButton(self)
        self.tool_button1.setIcon(QIcon("google-calendar.png"))
        self.event_button1 = QPushButton("마그나딘 대부호")
        self.event_button2 = QPushButton("월드 던전 쟁탈전")
        self.event_button3 = QPushButton("접속(일반 푸시)")
        self.content_button1 = QPushButton("성물 방어전")
        self.content_button2 = QPushButton("혈맹 고대의 전장")
        self.content_button3 = QPushButton("슈페리온 요새대전")
        self.content_button4 = QPushButton("콜로세움")
        self.content_button5 = QPushButton("듀얼 콜로세움")
        self.content_button6 = QPushButton("명예의 전장")
        self.content_button7 = QPushButton("명예의 대전장")

        frame1_gridlayout = QGridLayout()
        frame2_gridlayout = QGridLayout()
        frame3_gridlayout = QGridLayout()
        layout.addWidget(frame1)
        frame1.setLayout(frame1_gridlayout)
        frame1_gridlayout.addWidget(label1, 0, 0)
        frame1_gridlayout.addWidget(self.lineedit1, 0, 1)
        frame1_gridlayout.addWidget(label2, 1, 0)
        frame1_gridlayout.addWidget(self.lineedit2, 1, 1)
        frame1_gridlayout.addWidget(self.tool_button1, 1, 2)

        layout.addWidget(frame2)
        frame2.setLayout(frame2_gridlayout)
        frame2_gridlayout.addWidget(self.event_button1, 0, 0)
        frame2_gridlayout.addWidget(self.event_button2, 0, 1)
        frame2_gridlayout.addWidget(self.event_button3, 1, 0)

        layout.addWidget(frame3)
        frame3.setLayout(frame3_gridlayout)
        frame3_gridlayout.addWidget(self.content_button1, 0, 0)
        frame3_gridlayout.addWidget(self.content_button2, 0, 1)
        frame3_gridlayout.addWidget(self.content_button3, 1, 0)
        frame3_gridlayout.addWidget(self.content_button4, 1, 1)
        frame3_gridlayout.addWidget(self.content_button5, 2, 0)
        frame3_gridlayout.addWidget(self.content_button6, 2, 1)
        frame3_gridlayout.addWidget(self.content_button7, 3, 0)

        self.tool_button1.clicked.connect(self.exec_calendar)
        self.event_button1.clicked.connect(self.to_excel_event1)
        self.event_button2.clicked.connect(self.to_excel_event2)
        self.event_button3.clicked.connect(self.to_excel_event3)
        self.content_button1.clicked.connect(self.to_excel_content1)
        self.content_button2.clicked.connect(self.to_excel_content2)
        self.content_button3.clicked.connect(self.to_excel_content3)
        self.content_button4.clicked.connect(self.to_excel_content4)
        self.content_button5.clicked.connect(self.to_excel_content5)
        self.content_button6.clicked.connect(self.to_excel_content6)
        self.content_button7.clicked.connect(self.to_excel_content7)

        self.event_button3.setEnabled(False)
        self.content_button6.setEnabled(False)
        self.content_button7.setEnabled(False)

        self.cal = calendar_dialog(self)
        self.colosseum = colosseum_val(self)

    def exec_calendar(self):
        self.cal.exec()

    @exception_handler
    def to_excel_event1(self):
        # 마그나딘 대부호
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            QMessageBox.information(self, '정보', '마그나딘 대부호의 경우 입력 된 시즌 시작 일자 월의 1일 00:00시을 기준 으로 엑셀 파일을 추출 합니다.')
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                dataframes.adena_donation(filepath, season_id, start_time_info)

    @exception_handler
    def to_excel_event2(self):
        # 월드 던전 쟁탈전
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                dataframes.global_competition(filepath, season_id, start_time_info)

    @exception_handler
    def to_excel_event3(self):
        # 접속(일반 푸시)
        pass

    @exception_handler
    def to_excel_content1(self):
        # 성물 방어전
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                dataframes.monster_defence(filepath, season_id, start_time_info)

    @exception_handler
    def to_excel_content2(self):
        # 혈맹 고대의 전장
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                dataframes.ancient_tournament(filepath, season_id, start_time_info)

    @exception_handler
    def to_excel_content3(self):
        # 슈페리온 요새대전
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                dataframes.global_fortress_siege(filepath, season_id, start_time_info)

    def to_excel_content4(self):
        # 콜로세움
        self.colosseum.exec()

    @exception_handler
    def to_excel_content5(self):
        # 듀얼 콜로세움
        pass

    @exception_handler
    def to_excel_content6(self):
        # 명예의 전장
        pass

    @exception_handler
    def to_excel_content7(self):
        # 명예의 대전장
        pass

if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='custom.xml')
    window = contentsSettingBundle()
    window.show()
    app.exec_()