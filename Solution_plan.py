

def Depth0_pre(tmp_path: list) -> list:
    # Depth 0의 전처리[일관되게]
    if 'seoul' in tmp_path[5]:   tmp_path[5] = 'seoul'
    elif 'gyeonggi' in tmp_path[5]:  tmp_path[5] = 'gyeonggi'
    elif 'busan' in tmp_path[5]: tmp_path[5] = 'busan'
    elif 'daegu' in tmp_path[5]:  tmp_path[5] = 'daegu'
    elif 'incheon' in tmp_path[5]:   tmp_path[5] = 'incheon'
    elif 'ulsan' in tmp_path[5]: tmp_path[5] = 'ulsan'
    elif 'sejong' in tmp_path[5]:    tmp_path[5] = 'sejong'
    elif 'jeonnam' in tmp_path[5]:   tmp_path[5] = 'jeonnam'
    elif 'jeonbuk' in tmp_path[5]:   tmp_path[5] = 'jeonbuk'
    elif 'jeju' in tmp_path[5]:  tmp_path[5] = 'jeju'
    elif 'gyeongnam' in tmp_path[5]: tmp_path[5] = 'gyeongnam'
    elif 'gyeongbuk' in tmp_path[5]: tmp_path[5] = 'gyeongbuk'
    elif 'gwangju' in tmp_path[5]:   tmp_path[5] = 'gwangju'
    elif 'gangwon' in tmp_path[5]:   tmp_path[5] = 'gangwon'
    elif 'daejeon' in tmp_path[5]:   tmp_path[5] = 'daejeon'
    elif 'chungnam' in tmp_path[5]:  tmp_path[5] = 'chungnam'
    elif 'chungbuk' in tmp_path[5]:  tmp_path[5] = 'chungbuk'

    return tmp_path

def error_check(comparison_results: list, input_data: list):
    depth0_government = [
        'Seoul', 'Gyeonggi-do', 'Busan', 'Daegu', 'Incheon', 'Ulsan', 'Sejong-si', 'Jeollanam-do', 'Jeollabuk-do', 'Jeju-do',
        'Gyeongsangnam-do', 'Gyeongsangbuk-do', 'Gwangju', 'Gangwon-do', 'Daejeon', 'Chungcheongnam-do', 'Chungcheongbuk-do'
        ]
    
    # input_data[-1]에서 depth0_government의 위치를 int로 반환
    # depth0_government_index = depth0_government.index(input_data[-1])
