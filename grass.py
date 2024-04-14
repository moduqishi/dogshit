import requests
import pyaes
from base64 import b64encode

def password_encode(plain_text):
    key = b'pigxpigxpigxpigx'  # 密钥
    iv = b'pigxpigxpigxpigx'  # 初始化向量
    plain_text = plain_text.encode()  # 将字符串转换为字节串

    # 计算 padding 长度
    pad_len = 16 - (len(plain_text) % 16)

    # 添加 padding
    plain_text += b'\x00' * pad_len

    # 创建一个 AES CBC cipher
    cipher = pyaes.AESModeOfOperationCBC(key, iv)

    # 加密
    cipher_text = b"".join([cipher.encrypt(plain_text[i:i+16]) for i in range(0, len(plain_text), 16)])

    return b64encode(cipher_text).decode('utf-8')  # 将字节串转换为字符串

def get_access_token(username, password):
    global access_token, studentId
    password = password_encode(password)
    data = {'username': username,'password': password}
    headers = {'Authorization': 'Basic c3R1ZGVudDpzdHVkZW50', 'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post('https://www.wtjy.com/auth/oauth/token?grant_type=password', headers=headers, data=data)
    response.raise_for_status()  # 检查请求是否成功
    json_response = response.json()
    studentId = json_response['user_info']['studentId']
    access_token = json_response['access_token']
    return {'access_token': access_token, 'studentId': studentId}

def get_answer_paper(access_token, id, studentId, subjectId):
    url = "https://www.wtjy.com/report/statappstudentreport/getanswerpaper/v2"
    params = {'id': id, 'studentId': studentId, 'subjectId': subjectId}
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # 检查请求是否成功
    json_response = response.json()
    return json_response['data']['answerSheetUrl']
    
def fetch_exams_info(access_token):
    try:
        url = 'https://www.wtjy.com/report/stat/reportpage'
        headers = {
        	'Authorization': f'Bearer {access_token}',
        	'SCHOOL-ID': '20125',
        	'Content-Type': 'application/json'
        	}
        data = {
        	"current": 1,
        	"size": 5
        	}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        exams = response.json().get('data', {}).get('records', [])
        
        formatted_exams = [
            {exam['name']: {'id': exam['id'], 'statTime': exam['statTime'], 'excelUrl': exam['excelUrl']}}
            for exam in exams
        ]
        return formatted_exams
    except requests.exceptions.HTTPError as err:
        print ("HTTP Error:", err)
    except requests.exceptions.RequestException as err:
        print ("Oops: Something went wrong", err)


def exam_details(exams, access_token):
    # 定义请求头
    headers = {
        'SCHOOL-ID': '20125',
        'Authorization': f'Bearer {access_token}'
    }

    # 用来存储最终结果的列表
    results = []

    # 对exams列表中的每一项进行处理
    for exam in exams:
        for exam_name, exam_info in exam.items():
            # 准备请求参数
            params = {
                'id': exam_info['id'],
                'studentId': 3124646,
                'subjectId': 0
            }
            
            # 发送GET请求
            response = requests.get('https://wtjy.com/report/statstudentreport/getsrscoreoverview', headers=headers, params=params)

            # 检查响应状态码
            if response.status_code != 200:
                print("请求失败，状态码：", response.status_code)
                continue

            # 解析响应的JSON数据
            data = response.json().get('data')
            
            # 检查响应数据是否为空
            if not data:
                print("请求数据为空或格式不正确，请检查API响应")
                continue
            
            # 初始化结构
            exam_result = {exam_name: {
                'id': exam_info['id'],
                'excelUrl': exam_info['excelUrl'],
                'totalscore': None,
                'totalclassrank': None,
                'totalschoolrank': None,
                'scores': []
            }}
            
            # 遍历返回的科目数据
            for subject in data:
                # 检查是否为总分
                if subject['subjectId'] == 0:
                    exam_result[exam_name]['totalscore'] = subject['score']
                    exam_result[exam_name]['totalclassrank'] = subject['classRank']
                    exam_result[exam_name]['totalschoolrank'] = subject['schoolRank']
                else:
                    # 如果answerSheetUrl不是null则分离URL
                    answer_urls = subject['answerSheetUrl'].split('，') if subject['answerSheetUrl'] else ['', '']
                    
                    subject_results = {
                        'subject': subject['subjectName'],
                        'score': subject['score'],
                        'classrank': subject['classRank'],
                        'schoolrank': subject['schoolRank'],
                        'answerpaperA': answer_urls[0],
                        'answerpaperB': answer_urls[1] if len(answer_urls) > 1 else ''
                    }
                    # 添加到科目得分列表
                    exam_result[exam_name]['scores'].append(subject_results)
            
            # 添加到结果列表
            results.append(exam_result)
    
    return results


