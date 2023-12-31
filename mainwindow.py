import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, \
    QMessageBox, QFrame, QLabel, QLineEdit, QToolButton, QGridLayout
from PyQt5.QtGui import QIcon, QIntValidator
from qt_material import apply_stylesheet
import dataframes
from dialogs import *

class contentsSettingBundle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("콘텐츠/이벤트 세팅 파일 제작")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 위젯 선언
        frame1 = QFrame(self)
        frame2 = QFrame(self)
        frame3 = QFrame(self)
        label0 = QLabel("<b>시즌 정보</b>")
        label1 = QLabel("<b>시즌 ID : </b>")
        self.lineedit1 = QLineEdit()
        self.lineedit1.setPlaceholderText("10")
        self.lineedit1.setValidator(QIntValidator())
        label2 = QLabel("<b>시즌 시작 일자 : </b>")
        label3 = QLabel("<b>이벤트 목록</b>")
        label4 = QLabel("<b>전장 콘텐츠 목록</b>")
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
        self.exit_button = QPushButton("종료")

        # 레이아웃 세팅
        frame1_gridlayout = QGridLayout()
        frame2_gridlayout = QGridLayout()
        frame3_gridlayout = QGridLayout()
        layout.addWidget(frame1)
        frame1.setLayout(frame1_gridlayout)
        frame1_gridlayout.addWidget(label0, 0, 0)
        frame1_gridlayout.addWidget(label1, 1, 0)
        frame1_gridlayout.setAlignment(label1, Qt.AlignRight)
        frame1_gridlayout.addWidget(self.lineedit1, 1, 1)
        frame1_gridlayout.addWidget(label2, 2, 0)
        frame1_gridlayout.addWidget(self.lineedit2, 2, 1)
        frame1_gridlayout.addWidget(self.tool_button1, 2, 2)

        layout.addWidget(frame2)
        frame2.setLayout(frame2_gridlayout)
        frame2_gridlayout.addWidget(label3, 0, 0)
        frame2_gridlayout.addWidget(self.event_button1, 1, 0)
        frame2_gridlayout.addWidget(self.event_button2, 1, 1)
        frame2_gridlayout.addWidget(self.event_button3, 2, 0)

        layout.addWidget(frame3)
        frame3.setLayout(frame3_gridlayout)
        frame3_gridlayout.addWidget(label4, 0, 0)
        frame3_gridlayout.addWidget(self.content_button1, 1, 0)
        frame3_gridlayout.addWidget(self.content_button2, 1, 1)
        frame3_gridlayout.addWidget(self.content_button3, 2, 0)
        frame3_gridlayout.addWidget(self.content_button4, 2, 1)
        frame3_gridlayout.addWidget(self.content_button5, 3, 0)
        frame3_gridlayout.addWidget(self.content_button6, 3, 1)
        frame3_gridlayout.addWidget(self.content_button7, 4, 0)

        layout.addWidget(self.exit_button)

        # 시그널 세팅
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
        self.exit_button.clicked.connect(self.close)

        # 미지원 기능
        self.event_button3.setEnabled(False)
        self.content_button6.setEnabled(False)
        self.content_button7.setEnabled(False)

        # 다이얼로그 클래스 변수 선언
        self.cal = calendar_dialog(self)
        self.colosseum = colosseum_val(self)

    def exec_calendar(self):
        # 캘린더 다이얼로그 호출
        self.cal.exec()

    def to_excel_event1(self):
        # 마그나딘 대부호
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            QMessageBox.information(self, '정보', '마그나딘 대부호의 경우 입력 된 시즌 시작 일자 월의 1일 00:00시을 기준 으로 엑셀 파일을 추출 합니다.')
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                result = dataframes.adena_donation(filepath, season_id, start_time_info)
                if result:
                    answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 파일을 열어 보시겠습니까?', QMessageBox.Ok|QMessageBox.No, QMessageBox.Ok)
                    if answer == QMessageBox.Ok:
                        os.startfile(filepath)
        else:
            QMessageBox.warning(self, '경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')

    def to_excel_event2(self):
        # 월드 던전 쟁탈전
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                result = dataframes.global_competition(filepath, season_id, start_time_info)
                if result:
                    answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 파일을 열어 보시겠습니까?', QMessageBox.Ok|QMessageBox.No, QMessageBox.Ok)
                    if answer == QMessageBox.Ok:
                        os.startfile(filepath)
        else:
            QMessageBox.warning(self, '경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')

    def to_excel_event3(self):
        # 접속(일반 푸시)
        pass

    def to_excel_content1(self):
        # 성물 방어전
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            QMessageBox.information(self,'정보', '성물 방어전의 경우 아시아, 유럽, 아메리카 권역 3개의 파일이 일괄 생성 됩니다.'
                                               '\n예) 파일명 : 성물방어전_시즌10 으로 지정했을 경우 생성되는 파일은 다음과 같습니다.'
                                               '\n - 성물방어전_시즌10_아시아'
                                               '\n - 성물방어전_시즌10_유럽'
                                               '\n - 성물방어전_시즌10_아메리카'
                                               '\n ※ 생성 예정인 경로에 동일한 파일 명이 존재할 경우 오류가 발생할 수 있습니다.')
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                result = dataframes.monster_defence(filepath, season_id, start_time_info)
                if result:
                    answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 저장 경로를 열어 보시겠습니까?', QMessageBox.Ok|QMessageBox.No, QMessageBox.Ok)
                    if answer == QMessageBox.Ok:
                        os.startfile(os.path.dirname(filepath))
        else:
            QMessageBox.warning(self, '경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')

    def to_excel_content2(self):
        # 혈맹 고대의 전장
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                result = dataframes.ancient_tournament(filepath, season_id, start_time_info)
                if result:
                    answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 파일을 열어 보시겠습니까?', QMessageBox.Ok|QMessageBox.No, QMessageBox.Ok)
                    if answer == QMessageBox.Ok:
                        os.startfile(filepath)
        else:
            QMessageBox.warning(self, '경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')

    def to_excel_content3(self):
        # 슈페리온 요새대전
        season_id = self.lineedit1.text()
        start_time_info = self.lineedit2.text()
        if season_id and start_time_info:
            filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
            if filepath:
                result = dataframes.global_fortress_siege(filepath, season_id, start_time_info)
                if result:
                    answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 파일을 열어 보시겠습니까?', QMessageBox.Ok|QMessageBox.No, QMessageBox.Ok)
                    if answer == QMessageBox.Ok:
                        os.startfile(filepath)
        else:
            QMessageBox.warning(self, '경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')

    def to_excel_content4(self):
        # 콜로세움
        self.colosseum_min_cps = []
        self.colosseum_server_ids = []
        self.colosseum.exec()
        if self.colosseum_min_cps:
            season_id = self.lineedit1.text()
            start_time_info = self.lineedit2.text()
            if season_id and start_time_info:
                filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
                if filepath:
                    result = dataframes.single_colosseum(filepath, season_id, start_time_info, self.colosseum_min_cps, self.colosseum_server_ids)
                    if result:
                        answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 파일을 열어 보시겠습니까?',
                                                         QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
                        if answer == QMessageBox.Ok:
                            os.startfile(filepath)
            else:
                QMessageBox.warning(self,'경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')
        self.colosseum.table_widget.clear()
        self.colosseum.table_widget.setRowCount(0)

    def to_excel_content5(self):
        # 듀얼 콜로세움
        self.colosseum_min_cps = []
        self.colosseum_server_ids = []
        self.colosseum.exec()
        if self.colosseum_min_cps:
            season_id = self.lineedit1.text()
            start_time_info = self.lineedit2.text()
            if season_id and start_time_info:
                filepath, _ = QFileDialog.getSaveFileName(self, '저장 경로 설정', '', '엑셀 파일(*.xlsx)')
                if filepath:
                    result = dataframes.dual_colosseum(filepath, season_id, start_time_info, self.colosseum_min_cps, self.colosseum_server_ids)
                    if result:
                        answer = QMessageBox.information(self, '알림', '성공적으로 파일 추출을 완료하였습니다. 파일을 열어 보시겠습니까?',
                                                         QMessageBox.Ok | QMessageBox.No, QMessageBox.Ok)
                        if answer == QMessageBox.Ok:
                            os.startfile(filepath)
            else:
                QMessageBox.warning(self,'경고', '시즌 번호 및 시즌 시작 일자가 제대로 입력 되었는지 확인해 주세요.')
        self.colosseum.table_widget.clear()
        self.colosseum.table_widget.setRowCount(0)

    def to_excel_content6(self):
        # 명예의 전장
        pass

    def to_excel_content7(self):
        # 명예의 대전장
        pass

if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='custom.xml')
    window = contentsSettingBundle()
    window.show()
    app.exec_()