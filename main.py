from address_translation import file_path

# 주소 데이터 입력
english_address = 'Seongnam Customs, 8, Yatap-ro 205beon-gil, Bundang-gu, Seongnam-si, Gyeonggi-do'
korean_address = '경기도, 성남시, 분당구, 야탑로205번길, 8, 성남세관'
english_address_cut_unit = english_address.split(',')
korean_address_cut_unit = korean_address.split(',')
english_address_cut_unit = [tmp.strip() for tmp in english_address_cut_unit]
korean_address_cut_unit = [tmp.strip() for tmp in korean_address_cut_unit]

# 클래스 선언
english_address_class = file_path(english_address_cut_unit)
english_address_class.english_filepath()
korean_address_class = file_path(korean_address_cut_unit)
korean_address_class.korean_filepath()

# 주소 변환
english2korean = english_address_class.English2Korean(english_address_cut_unit)
korean2english = korean_address_class.Korean2English(korean_address_cut_unit)

print(f'english2korean: {english2korean}')
print(f'korean2english: {korean2english}')
