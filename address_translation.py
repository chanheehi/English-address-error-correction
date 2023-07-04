import os

# 영문 주소를 한글 주소로 변환
def English2Korean(notepad_content: str, cut_address_unit: list) -> str:
    # cut_address_unit[1]이 담긴 cut_address_unit[2]가 포함된 라인 찾기
    address_find_number = 0
    for i, line in enumerate(notepad_content):
        if cut_address_unit[2] in line:
            if cut_address_unit[1] == line.split('|')[9]:
                address_find_number = i

    # 영문주소를 한글주소로 변환
    korean_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Korean_address')
    kreaon_address_path = os.path.join(korean_base_path, f'rnaddrkor_{cut_address_unit[5]}.txt')
    with open(kreaon_address_path, "r", encoding='cp949') as f:
        notepad_content = f.readlines()

    korean_address = notepad_content[address_find_number]
    return korean_address

# 한글 주소를 영문 주소로 변환
def Korean2English(korean_address_path: str, cut_address_unit: list) -> str:
    pass
