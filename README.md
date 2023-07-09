# Korean-and-English-Address-Converter

## 데이터 준비
[`주소 데이터`](https://drive.google.com/file/d/1VUxr2g-bXbtzt4SVNY6uOcj6phqFT8TR/view?usp=drive_link)를 누르면 다운할 수 있습니다.
압축을 해제하고 English_address와 Korean_address를 English-address-error-correction의 하위 폴더로 위치하세요.
또는 [`주소 DB`](https://business.juso.go.kr/addrlink/attrbDBDwld/attrbDBDwldList.do?cPath=99MD)에서 최신 주소 데이터를 제공받을 수 있습니다. 도로명 주소 한글과 도로명 주소 영문을 다운하시기 바랍니다.
#### 예시
```Korean-and-English-Address-Converter
├── Korean_address
│   ├── rnaddrkor_busan
│   └── rnaddrkor_...
├── English_address
│   ├── rneng_busan
│   └── rneng_...
├── address_translation.py
├── main.py
└── consistency_match.py
```

## 실행
main.py의 코드에서 볼 수 있듯이, English2Korean와 Korean2English 함수를 통해 영어와 한글이 변환된 결과를 얻을 수 있습니다. 입력 형식은 변수 english_address와 korean_address처럼 맞춰주시기 바랍니다.
```
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
## english2korean: 41135107434029900000800000|4113510700|경기도|성남시 분당구|야탑동||0|264|2|411354340299|야탑로205번길|0|8|0|4113564000|야탑3동|13503||20110729|0|||성남세관|
## korean2english: 41135107434029900000800000|4113510700|Gyeonggi-do|Bundang-gu, Seongnam-si|Yatap-dong||411354340299|Yatap-ro 205beon-gil|0|8|0|13503|0|264|2|20110729|
```
