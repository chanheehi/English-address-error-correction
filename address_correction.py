from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy

english_depth0 = [
    'Seoul', 'Gyeonggi-do', 'Busan', 'Daegu', 'Incheon', 'Ulsan', 'Sejong-si', 'Jeollanam-do', 'Jeollabuk-do', 'Jeju-do',
    'Gyeongsangnam-do', 'Gyeongsangbuk-do', 'Gwangju', 'Gangwon-do', 'Daejeon', 'Chungcheongnam-do', 'Chungcheongbuk-do'
    ]

def English_Address_correction(address: list) -> numpy.ndarray:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    modified_depth0 = Depth0_government(model, address[-1])
    # modified_depth1 = Depth3_government(model, address[2])
    address[-1] = modified_depth0
    print(address)
    pass

def Depth0_government(model, address: str) -> str:
    aaa = model.encode([address])
    bbb = model.encode(english_depth0)
    similarities = cosine_similarity(aaa,bbb).tolist()
    maximum_similarity_num  = similarities[0].index(max(similarities[0]))
    
    modified_address = english_depth0[maximum_similarity_num]
    return modified_address

# def Depth3_government(model, address: str) -> str:
#     answer_address = ''
#     with open(english_address_path, "r", encoding='cp949') as f:
#         answer_address = f.readlines()

    pass

