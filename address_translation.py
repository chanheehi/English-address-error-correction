import os
from consistency_match import Region_English2Lower, Region_Korean2English

class file_path:
    def __init__(self, address_cut_unit: list):
        self.cut_address_unit = address_cut_unit
        self.english_path = None
        self.korean_path = None
        self.english_tmp = None
        self.korean_tmp = None
        
    def english_filepath(self):
        # 경로 설정
        english_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'English_address')
        self.english_tmp = self.cut_address_unit.copy()
        path_tmp = Region_English2Lower(self.english_tmp)
        self.english_path = os.path.join(english_base_path, f'rneng_{path_tmp[5]}.txt')
        self.korean_path = os.path.join(english_base_path, f'rnaddrkor_{path_tmp[5]}.txt')

    def korean_filepath(self):
        # 경로 설정
        korean_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Korean_address')
        self.korean_tmp = self.cut_address_unit.copy()
        path_tmp = Region_Korean2English(self.korean_tmp)
        self.english_path = os.path.join(korean_base_path, f'rneng_{path_tmp[0]}.txt')
        self.korean_path = os.path.join(korean_base_path, f'rnaddrkor_{path_tmp[0]}.txt')

# 영문 주소를 한글 주소로 변환
    def English2Korean(self, cut_address_unit: list) -> str:
        answer_address = ''
        with open(self.english_path, "r", encoding='cp949') as f:
            answer_address = f.readlines()

        # cut_address_unit[1]이 담긴 cut_address_unit[2]가 포함된 라인 찾기
        address_find_number = 0
        for i, line in enumerate(answer_address):
            if cut_address_unit[2] in line:
                if cut_address_unit[1] == line.split('|')[9]:
                    address_find_number = i

        # 영문주소를 한글주소로 변환
        korean_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Korean_address')
        korean_address_path = os.path.join(korean_base_path, self.korean_path.split('\\')[-1])   
        with open(korean_address_path, "r", encoding='cp949') as f:
            answer_address = f.readlines()

        address = answer_address[address_find_number]
        return address

    # 한글 주소를 영문 주소로 변환
    def Korean2English(self, cut_address_unit: list) -> str:
        answer_address = ''
        with open(self.korean_path, "r", encoding='cp949') as f:
            answer_address = f.readlines()

        # cut_address_unit[1]이 담긴 cut_address_unit[2]가 포함된 라인 찾기
        address_find_number = 0
        for i, line in enumerate(answer_address):
            if cut_address_unit[3] in line:
                if cut_address_unit[4] == line.split('|')[12]:
                    address_find_number = i

        # 한글주소를 영문주소로 변환
        english_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'English_address')
        english_address_path = os.path.join(english_base_path, self.english_path.split('\\')[-1])
        with open(english_address_path, "r", encoding='cp949') as f:
            answer_address = f.readlines()

        address = answer_address[address_find_number]
        return address