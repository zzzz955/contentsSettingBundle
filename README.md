# contentsSettingBundle
주기적으로 세팅이 필요한 이벤트 및 콘텐츠의 운영툴 세팅을 위한 엑셀 파일을 제작하는 앱
각 이벤트/콘텐츠 세팅 시 필요한 시즌 번호 및 시작 일자를 기재할 경우 해당 데이터를 기반으로 엑셀 파일을 자동으로 제작, 운영툴에 추가할 경우 소요 시간은 1분 이내로 수동 세팅 대비 약 95% 이상의 리소스 감소 효과 기대

# mainwindow.py
앱 실행 시 최초로 노출되는 UI, 이벤트/콘텐츠 세팅 자동화에 필요한 위젯과 데이터를 연결 시켜주는 허브 역할

# dialogs.py
추가로 필요한 위젯 or 데이터를 팝업으로 활용하기 위한 모듈

# dataframes.py
데이터프레임, 시간 연산등 주어진 데이터를 가공하고 엑셀 파일로 추출하기 위한 모듈

# custom.xml
qt_material 모듈의 테마로 GUI 변경을 위한 파일
venv\Lib\site-packages\qt_material\themes내 위치 필요

# requiremodules.txt
설치가 필요한 모듈의 집합, 가상환경 생성 후 pip install 필요

# google-calendar.png
QToolbutton 위젯의 아이콘으로 활용
