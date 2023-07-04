import os
from Solution_plan import Depth0_pre, error_check
from address_translation import English2Korean, Korean2English
from compare_similarity import Compare_similarity

# 주소 데이터 입력
address = 'Seongnam Customs, 8, Yatap-ro 205beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do'
cut_address_unit = address.split(',')
cut_address_unit = [tmp.strip() for tmp in cut_address_unit]

# 과정 준비
path_tmp = cut_address_unit.copy()
path_tmp = Depth0_pre(path_tmp)
english_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'English_address')
road_name_tmp = path_tmp[5].lower().split('-')[0]
english_address_path = os.path.join(english_base_path, f'rneng_{road_name_tmp}.txt')
answer_address = ''
with open(english_address_path, "r", encoding='cp949') as f:
    answer_address = f.readlines()

# 문제유무 확인(유사도 비교 단계)====
comparison_results = Compare_similarity(cut_address_unit, answer_address)

# 문제 풀이
if comparison_results[-1] == 'X':
    error_check(comparison_results, path_tmp)
    
error_check(comparison_results, path_tmp)
# elif (comparison_results[-1] == 'O') and (comparison_results[2] == 'O'):
#     korean_address = 
# elif 
# 영문주소를 한글주소로 변환====
# English2Korean(answer_address, cut_address_unit)