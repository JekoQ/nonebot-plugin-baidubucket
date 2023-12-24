import requests
import random
import json
from hashlib import md5
from .baidu_config import Config

from nonebot import get_driver

global_config = get_driver().config
baidu_config = Config.parse_obj(global_config)


#百度翻译
def func_translate(to_lang: str, query: str):
    """
    百度翻译开放平台 http://api.fanyi.baidu.com/
    appid: APP ID
    appkey: 密钥
    url: 通用翻译API HTTPS地址
    salt: md5算法加盐
    """

    #百度翻译API
    translate_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

    # md5加密
    salt = random.randint(32768, 65536)
    joint = baidu_config.appid + query + str(salt) + baidu_config.key
    sign = md5(joint.encode('utf-8')).hexdigest()

    
    #POST建立连接
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #建立连接
    payload = {'appid': baidu_config.appid, 'q': query, 'from': 'auto', 'to': to_lang, 'salt': salt, 'sign': sign}
    response = requests.post(translate_url, params=payload, headers=headers)
    
    return response.json()


#千帆大模型文心一言
def func_model(tokens: str):

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": baidu_config.API_KEY, "client_secret": baidu_config.SECRET_KEY}

    model_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + str(requests.post(url, params=params).json().get("access_token"))
   
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": f"{tokens}"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", model_url, headers=headers, data=payload)
    
    return response.json()
    
#情绪分析
def func_sentiment_analysis(tokens: str):

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": baidu_config.nlp_api_key, "client_secret": baidu_config.nlp_secret_key}

    baidu_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=&access_token=" + str(requests.post(url, params=params).json().get("access_token"))
   
    payload = json.dumps({
        "text": f"{tokens}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", baidu_url, headers=headers, data=payload)

    return response.json()
    


#文本纠错
def func_correction(tokens: str):

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": baidu_config.nlp_api_key, "client_secret": baidu_config.nlp_secret_key}

    baidu_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet?charset=&access_token=" + str(requests.post(url, params=params).json().get("access_token"))
   
    payload = json.dumps({
        "text": f"{tokens}"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", baidu_url, headers=headers, data=payload)

    return response.json()
    


#关键词提取
def func_keyword(tokens: str):

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": baidu_config.nlp_api_key, "client_secret": baidu_config.nlp_secret_key}

    baidu_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/txt_keywords_extraction?access_token=" + str(requests.post(url, params=params).json().get("access_token"))
   
    payload = {"text":[f"{tokens}"]}
    payload = str(payload).encode('utf-8')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.request("POST", baidu_url, headers=headers, data=payload)

    return response.json()
    
