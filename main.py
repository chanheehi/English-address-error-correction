from address_translation import English2Korean, Korean2English

# 주소 데이터 입력
english_address = 'Seongnam Customs, 8, Yatap-ro 205beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do'
korean_address = '경기도, 성남시, 분당구, 야탑로205번길, 8, 성남세관'
english_address_cut_unit = english_address.split(',')
korean_address_cut_unit = korean_address.split(',')
english_address_cut_unit = [tmp.strip() for tmp in english_address_cut_unit]
korean_address_cut_unit = [tmp.strip() for tmp in korean_address_cut_unit]

# 영문주소를 한글주소로 변환====
english2korean = English2Korean(english_address_cut_unit)
korean2english = Korean2English(korean_address_cut_unit)

print(f'english2korean: {english_address}')
print(f'korean2english: {korean_address}')
