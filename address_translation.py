import os
from solution_plan import Region_English2Lower, Region_Korean2English

# 영문 주소를 한글 주소로 변환
def English2Korean(cut_address_unit: list) -> str:
    english_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'English_address')
    tmp = cut_address_unit.copy()
    path_tmp = Region_English2Lower(tmp)
    english_address_path = os.path.join(english_base_path, f'rneng_{path_tmp[5]}.txt')
    answer_address = ''
    with open(english_address_path, "r", encoding='cp949') as f:
        answer_address = f.readlines()

    # cut_address_unit[1]이 담긴 cut_address_unit[2]가 포함된 라인 찾기
    address_find_number = 0
    for i, line in enumerate(answer_address):
        if cut_address_unit[2] in line:
            if cut_address_unit[1] == line.split('|')[9]:
                address_find_number = i

    # 영문주소를 한글주소로 변환
    korean_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Korean_address')
    korean_address_path = os.path.join(korean_base_path, f'rnaddrkor_{tmp[5]}.txt')    
    with open(korean_address_path, "r", encoding='cp949') as f:
        answer_address = f.readlines()

    address = answer_address[address_find_number]
    return address

# 한글 주소를 영문 주소로 변환
def Korean2English(cut_address_unit: list) -> str:
    korean_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Korean_address')
    tmp = cut_address_unit.copy()
    path_tmp = Region_Korean2English(tmp)
    korean_address_path = os.path.join(korean_base_path, f'rnaddrkor_{path_tmp[0]}.txt')
    answer_address = ''
    with open(korean_address_path, "r", encoding='cp949') as f:
        answer_address = f.readlines()

    # cut_address_unit[1]이 담긴 cut_address_unit[2]가 포함된 라인 찾기
    address_find_number = 0
    for i, line in enumerate(answer_address):
        if cut_address_unit[3] in line:
            if cut_address_unit[4] == line.split('|')[12]:
                address_find_number = i

    # 한글주소를 영문주소로 변환
    english_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'English_address')
    english_address_path = os.path.join(english_base_path, f'rneng_{tmp[0]}.txt')
    with open(english_address_path, "r", encoding='cp949') as f:
        answer_address = f.readlines()

    address = answer_address[address_find_number]
    return address