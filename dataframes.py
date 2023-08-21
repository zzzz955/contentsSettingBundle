import pandas as pd
import calendar
from datetime import datetime, timedelta

def adena_donation(filepath, season_id, start_time_info):
    date = datetime.strptime(start_time_info, "%Y-%m-%d")
    start_time = date.replace(day=1)
    _, last_day = calendar.monthrange(date.year, date.month)
    end_time = start_time + timedelta(days=last_day-1, hours=23, minutes=30)
    season_status = 1

    col = ['season_id',	'start_time',	'end_time',	'season_status']
    df = pd.DataFrame(columns=col)

    df.loc[0] = ['','','','']
    df.loc[1] = ['시즌 아이디', '시작시간', '종료시간', '시즌 상태']
    df.loc[2] = ['', '2022-01-01- 00:00:00', '2022-01-01- 00:00:00', '']
    df.loc[3] = [season_id, start_time, end_time, season_status]
    df = df.applymap(str)
    df.to_excel(filepath, sheet_name="아데나 기부", index=False)

def global_competition(filepath, season_id, start_time_info):
    date = datetime.strptime(start_time_info, "%Y-%m-%d")
    type1_start = date + timedelta(hours=19)
    type1_end = date + timedelta(days=14 ,hours=23, minutes=59)
    type2_start = date + timedelta(hours=19)
    type2_end = date + timedelta(hours=21, minutes=20)
    type3_start = date + timedelta(hours=21, minutes=30)
    type3_end = date + timedelta(hours=22)
    type4_start = date + timedelta(hours=23)
    type4_end = date + timedelta(days=14 ,hours=23, minutes=59)

    data = {
        'schedule_type': ['','스케줄 타입','',1,2,3,4],
        'season_id' : ['','시즌 아이디','',season_id,season_id,season_id,season_id],
        'start_time' : ['','시작시간','2022-01-01 00:00:00', type1_start, type2_start, type3_start, type4_start],
        'end_time' : ['','종료시간','2022-01-01 00:00:00', type1_end, type2_end, type3_end, type4_end],
        'start_status' : ['','시작 수행여부',0,0,0,0,0],
        'end_status' : ['','종료 수행여부',0,0,0,0,0]
    }

    df = pd.DataFrame(data).applymap(str)
    df.to_excel(filepath, sheet_name="월드 던전 쟁탈전", index=False)

def ancient_tournament(filepath, season_id, start_time_info):
    date = datetime.strptime(start_time_info, "%Y-%m-%d")
    application_start_time = date
    application_end_time = date + timedelta(days=1 ,hours=21)
    group_stage_8_start_time = date + timedelta(days=2 ,hours=22)
    group_stage_8_end_time = date + timedelta(days=2 ,hours=22, minutes=10)
    group_stage_4_start_time = date + timedelta(days=2 ,hours=22, minutes=15)
    group_stage_4_end_time = date + timedelta(days=2 ,hours=22, minutes=25)
    group_stage_2_start_time = date + timedelta(days=2 ,hours=22, minutes=30)
    group_stage_2_end_time = date + timedelta(days=2 ,hours=22, minutes=40)
    champion_stage_8_start_time = date + timedelta(days=9 ,hours=22)
    champion_stage_8_end_time = date + timedelta(days=9 ,hours=22, minutes=10)
    champion_stage_4_start_time = date + timedelta(days=9 ,hours=22, minutes=15)
    champion_stage_4_end_time = date + timedelta(days=9 ,hours=22, minutes=25)
    champion_stage_2_start_time = date + timedelta(days=9 ,hours=22, minutes=30)
    champion_stage_2_end_time = date + timedelta(days=9 ,hours=22, minutes=40)
    total_schd_end_time = date + timedelta(days=9 ,hours=23, minutes=59)

    data = {
        'season_id' : ['','시즌 아이디','',season_id],
    'application_start_time' : ['','참가신청 시작 시간','2021-01-01 00:00:00', application_start_time],
    'application_end_time' : ['','참가신청 종료 시간','2021-01-01 00:00:00', application_end_time],
    'group_stage_8_start_time' : ['','조별리그 8강 시작 시간','2021-01-01 00:00:00', group_stage_8_start_time],
    'group_stage_8_end_time' : ['','조별리그 8강 종료 시간','2021-01-01 00:00:00', group_stage_8_end_time],
    'group_stage_4_start_time' : ['','조별리그 4강 시작 시간','2021-01-01 00:00:00', group_stage_4_start_time],
    'group_stage_4_end_time' : ['','조별리그 4강 종료 시간','2021-01-01 00:00:00', group_stage_4_end_time],
    'group_stage_2_start_time' : ['','조별리그 결승전 시작 시간','2021-01-01 00:00:00', group_stage_2_start_time],
    'group_stage_2_end_time' : ['','조별리그 결승전 종료 시간','2021-01-01 00:00:00', group_stage_2_end_time],
    'champion_stage_8_start_time' : ['','챔피언리그 8강 시작 시간','2021-01-01 00:00:00', champion_stage_8_start_time],
    'champion_stage_8_end_time' : ['','챔피언리그 8강 종료 시간','2021-01-01 00:00:00', champion_stage_8_end_time],
    'champion_stage_4_start_time' : ['','챔피언리그 4강 시작 시간','2021-01-01 00:00:00', champion_stage_4_start_time],
    'champion_stage_4_end_time' : ['','챔피언리그 4강 종료 시간','2021-01-01 00:00:00', champion_stage_4_end_time],
    'champion_stage_2_start_time' : ['','챔피언리그 결승전 시작 시간','2021-01-01 00:00:00', champion_stage_2_start_time],
    'champion_stage_2_end_time' : ['','챔피언리그 결승전 종료 시간','2021-01-01 00:00:00', champion_stage_2_end_time],
    'total_schd_end_time' : ['','시즌 종료 시간','2021-01-01 00:00:00', total_schd_end_time],
    }

    df = pd.DataFrame(data).applymap(str)
    df.to_excel(filepath, sheet_name="혈맹 고대의 전장", index=False)

def monster_defence(filepath, season_id, start_time_info):
    date = datetime.strptime(start_time_info, "%Y-%m-%d")
    start_time = date + timedelta(hours=18)
    end_time_701 = date + timedelta(days=4 ,hours=22, minutes=59)
    start_time_702 = date + timedelta(days=6, hours=20)
    end_time_702 = date + timedelta(days=6 ,hours=21)
    is_pre_season = 0
    season_number = season_id
    matching_group_info_id = 0
    round = 8
    enable = 0
    repeated_time_701 = '{"times":[{ "start_time": "'+ str(start_time) + '", "end_time": "'+str(end_time_701)+'" }]}'
    repeated_time_702 = '{"times":[{ "start_time": "'+str(start_time_702)+'", "end_time": "'+str(end_time_702)+'" }]}'
    col = ['start_time','end_time_701',	'end_time_702',	'is_pre_season',	'season_number',	'matching_group_info_id',	'round',	'enable',	'repeated_time_701',	'repeated_time_702']
    commondf = pd.DataFrame(columns=col)
    commondf.loc[0] = ['','','','','','','','','','']
    commondf.loc[1] = ['시작시간','생존전 종료시간','경쟁전 종료시간',	'프리시즌 여부','시즌 번호',	'매칭그룹 Info ID',	'진출 상태',	'활성화 여부',	'생존전 시간 상세',	'경쟁전 시간 상세']
    commondf.loc[2] = ['2022-01-01 00:00:00',	'2022-01-01 00:00:00',	'2022-01-01 00:00:00','1[O] , 0[X]','','','',				'1[O] , 0[X]',	'{"times":[{ "start_time": "2022-09-02 14:10:00", "end_time": "2022-09-02 14:20:00" }, { "start_time": "2022-09-02 14:30:00", "end_time": "2022-09-02 14:40:00" }]}',	'{"times":[{ "start_time": "2022-09-02 14:10:00", "end_time": "2022-09-02 14:20:00" }, { "start_time": "2022-09-02 14:30:00", "end_time": "2022-09-02 14:40:00" }]}']
    commondf.loc[3] = [start_time, end_time_701, end_time_702, is_pre_season,season_number,matching_group_info_id,round,enable,repeated_time_701,repeated_time_702]
    commondf = commondf.applymap(str)
    df_asia = commondf.copy()
    df_fr = commondf.copy()
    df_vi = commondf.copy()
    df_asia['servers'] = ['','서버목록','1002,1003','1305,1306,1307,1308,1309,1310,1900,1901']
    df_fr['servers'] = ['', '서버목록', '1002,1003', '1002,1427,1432,1436,1438']
    df_vi['servers'] = ['', '서버목록', '1002,1003', '1001,1431,1435,1437']
    df_asia.to_excel("asia_"+filepath, sheet_name="성물방어전 일괄추가",index=False)
    df_fr.to_excel("fr_"+filepath, sheet_name="성물방어전 일괄추가",index=False)
    df_vi.to_excel("vi_"+filepath, sheet_name="성물방어전 일괄추가",index=False)

def global_fortress_siege(filepath, season_id, start_time):
    date = datetime.strptime(start_time, "%Y-%m-%d")
    application_start_time= date + timedelta(hours=22, minutes=30)
    application_end_time= date + timedelta(days=1, hours=12)
    group_stage_8_start_time= date + timedelta(days=1, hours=20, minutes=5)
    group_stage_8_end_time= date + timedelta(days=1, hours=20, minutes=12)
    group_stage_4_start_time= date + timedelta(days=1, hours=20, minutes=20)
    group_stage_4_end_time= date + timedelta(days=1, hours=20, minutes=27)
    group_stage_2_start_time= date + timedelta(days=1, hours=20, minutes=35)
    group_stage_2_end_time= date + timedelta(days=1, hours=21)
    total_schd_end_time= date + timedelta(days=1, hours=21, minutes=59)

    col = ['season_id',	'application_start_time',	'application_end_time',	'group_stage_8_start_time',	'group_stage_8_end_time',	'group_stage_4_start_time',	'group_stage_4_end_time',	'group_stage_2_start_time',	'group_stage_2_end_time',	'total_schd_end_time']
    df = pd.DataFrame(columns=col)
    df.loc[0] = ['','','','','','','','','','']
    df.loc[1] = ['시즌 아이디',	'참가신청 시작 시간',	'참가신청 종료 시간',	'조별리그 8강 시작 시간',
                 '조별리그 8강 종료 시간',	'조별리그 4강 시작 시간',	'조별리그 4강 종료 시간',
                 '조별리그 결승전 시작 시간',	'조별리그 결승전 종료 시간',	'시즌 종료 시간']
    df.loc[2] = ['','2021-01-01 00:00:00','2021-01-01 00:00:00','2021-01-01 00:00:00','2021-01-01 00:00:00',
                 '2021-01-01 00:00:00','2021-01-01 00:00:00','2021-01-01 00:00:00','2021-01-01 00:00:00','2021-01-01 00:00:00']
    df.loc[3] = [season_id, application_start_time, application_end_time, group_stage_8_start_time,
                 group_stage_8_end_time, group_stage_4_start_time, group_stage_4_end_time, group_stage_2_start_time,
                 group_stage_2_end_time, total_schd_end_time]
    df = df.applymap(str)
    df.to_excel(filepath, sheet_name="전서버 요새전",index=False)

