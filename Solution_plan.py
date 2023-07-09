def Region_English2Lower(tmp_path: list) -> list:
    tmp_path[5] = tmp_path[5].lower()
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

def Region_Korean2English(tmp_path: list) -> list:
    if '서울' in tmp_path[0]:   tmp_path[0] = 'seoul'
    elif '경기' in tmp_path[0]:  tmp_path[0] = 'gyeonggi'
    elif '부산' in tmp_path[0]: tmp_path[0] = 'busan'
    elif '대구' in tmp_path[0]:  tmp_path[0] = 'daegu'
    elif '인천' in tmp_path[0]:   tmp_path[0] = 'incheon'
    elif '울산' in tmp_path[0]: tmp_path[0] = 'ulsan'
    elif '세종' in tmp_path[0]:    tmp_path[0] = 'sejong'
    elif ('전남' in tmp_path[0]) or ('전라남도' in tmp_path[0]):   tmp_path[0] = 'jeonnam'
    elif ('전북' in tmp_path[0]) or ('전라북도' in tmp_path[0]):   tmp_path[0] = 'jeonbuk'
    elif '제주' in tmp_path[0]:  tmp_path[0] = 'jeju'
    elif ('경남' in tmp_path[0]) or ('경상남도' in tmp_path[0]): tmp_path[0] = 'gyeongnam'
    elif ('경북' in tmp_path[0]) or ('경상북도' in tmp_path[0]): tmp_path[0] = 'gyeongbuk'
    elif '광주' in tmp_path[0]:   tmp_path[0] = 'gwangju'
    elif '강원' in tmp_path[0]:   tmp_path[0] = 'gangwon'
    elif '대전' in tmp_path[0]:   tmp_path[0] = 'daejeon'
    elif ('충남' in tmp_path[0]) or ('충청남도' in tmp_path[0]):  tmp_path[0] = 'chungnam'
    elif ('충북' in tmp_path[0]) or ('충청북도' in tmp_path[0]):  tmp_path[0] = 'chungbuk'

    return tmp_path


        