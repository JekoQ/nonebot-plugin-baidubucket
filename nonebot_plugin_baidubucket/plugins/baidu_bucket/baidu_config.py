from pydantic import BaseModel, Extra
from nonebot import get_driver

class Config(BaseModel, extra=Extra.ignore):
    
    appid: str = ""
    key: str = ""
    """
    百度翻译配置，见 https://fanyi-api.baidu.com/doc/21
    """

    
    API_KEY = ""
    SECRET_KEY = ""
    """
    千帆大模型平台配置，见https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    """

    
    nlp_api_key = ""
    nlp_secret_key = ""
    """
    自然语言处理平台，见 https://console.bce.baidu.com/ai/#/ai/nlp/app/list
    """

plugin_config = Config.parse_obj(get_driver().config.dict())