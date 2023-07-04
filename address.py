import os

address = 'Seongnam Customs, 8, Yatap-ro 205beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do'.lower()
cut_address_unit = address.split(',')
cut_address_unit = [tmp.strip() for tmp in cut_address_unit]

# Depth 0의 전처리[일관되게]
if 'seoul' in cut_address_unit[5]:   cut_address_unit[5] = 'seoul'
elif 'gyeonggi' in cut_address_unit[5]:  cut_address_unit[5] = 'gyeonggi'
## 모든 Depth를 일관되게 변경해야함====

english_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'English_address')
english_address_path = os.path.join(english_base_path, f'rneng_{cut_address_unit[5]}.txt')

# depth 3(-ro)의 첫글자 대문자로 변환
cut_address_unit[2] = f'{cut_address_unit[2][0].upper()}{cut_address_unit[2][1:]}'.replace('beon-gil', '')
with open(english_address_path, "r", encoding='cp949') as f:
    notepad_content = f.readlines()

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

aa = notepad_content[address_find_number]
    