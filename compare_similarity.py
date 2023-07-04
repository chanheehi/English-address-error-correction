from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def Compare_similarity(input_data: list, answer_data: list) -> list:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # input_data[1]이 담긴 input_data[2]의 찾기
    address_find_number = 0
    for i, line in enumerate(answer_data):
        if input_data[2] in line:
            if input_data[1] == line.split('|')[9]:
                address_find_number = i
    
    cut_address = answer_data[address_find_number].split('|')
    cut_address = [tmp.strip() for tmp in cut_address]
    
    pre_answer_data = []
    pre_answer_data.append('')
    pre_answer_data.append(cut_address[9])
    pre_answer_data.append(cut_address[7])
    pre_answer_data.append(cut_address[3].split(', ')[0])
    pre_answer_data.append(cut_address[3].split(', ')[1])
    pre_answer_data.append(cut_address[2])
    

    for i in range(len(input_data)):
        input_data[i] = input_data[i].lower()
    for i in range(len(pre_answer_data)):
        pre_answer_data[i] = pre_answer_data[i].lower()
    pre_answer_data[-1] = pre_answer_data[-1]
    input = model.encode(input_data)
    answer = model.encode(pre_answer_data)
    similarities = cosine_similarity(input,answer)
    

    # Depth별 유사도 확인
    comparison_results = []
    for i in range(len(similarities)):
        if similarities[i][i] > 0.99:
            comparison_results.append('O')
        else:   comparison_results.append('X')
    
    return comparison_results