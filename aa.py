import requests 

english_url = 'https://www.juso.go.kr/addrlink/addrEngApi.do'
doro_url = 'https://business.juso.go.kr/addrlink/addrLinkApi.do'

english_param = { 
    'confmKey':'devU01TX0FVVEgyMDIzMDcwMzE5MDExOTExMzg5NzU=',
    'currentPage':'1', 
     'countPerPage':'5', 
     'keyword':'busan', 
     'resultType': 'json'
}
doro_param = {
    'confmKey':'devU01TX0FVVEgyMDIzMDcwMzE5MjIzMzExMzg5Nzc=',
    'currentPage':'1', 
     'countPerPage':'5', 
     'keyword':'busan', 
     'resultType': 'json'
}

english_req = requests.get(english_url, english_param)
doro_req = requests.get(doro_url, doro_param)

english_data = english_req.json()
doro_data = doro_req.json()

import pandas as pd

english_data_frame = pd.DataFrame ( english_data['results']['juso'] ) 
doro_data_frame = pd.DataFrame ( doro_data['results']['juso'] )
print(english_data_frame)
print(doro_data_frame)