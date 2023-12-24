<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-baidubucket

_✨ NoneBot 百度NLP不全家桶 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/JekoQ/nonebot-plugin-baidubucket.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-baidubucket">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-baidubucket.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>


## 📖 介绍


百度自然语言处理的全家桶（并不全），集合百度翻译/NLP大模型/NLP任务处理等功能
具体涵盖内容：
1. 千帆大模型平台
   - [x] 文心一言 ERNIE
   - [ ] Stable Diffusion
2. 翻译开放平台
   - [x] 文本翻译（任意语种->中/英/日）
   - [ ] 文档翻译（QQ频道似乎不支持文件解析）
   - [ ] 语种识别（这个功能可以识别的语言太少了）
3. AI开放平台
   - [x] 情绪分析
   - [x] 文本纠错
   - [x] 关键词提取
   - [ ] 其他功能（比较鸡肋的..） 

## 💿 安装与配置

1. 首先注册并申请百度平台的API
* 翻译开放平台：http://api.fanyi.baidu.com/product/11 ，之后开启`通用文本翻译功能`
* 千帆大模型平台：https://console.bce.baidu.com/qianfan/overview ，之后找到`应用接入`选项，创建一个应用；应用默认会开启多个大模型功能，确保`ERNIE-Bot-turbo-0922`是开启的
* ![qianfan](https://github.com/JekoQ/nonebot-plugin-baidubucket/blob/main/images/qianfan.png)
* AI开放平台：https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3 ，创建一个应用，确保`情感倾向分析`，`文本纠错`，`关键词提取`三个功能是开启的
* ![nlp](https://github.com/JekoQ/nonebot-plugin-baidubucket/blob/main/images/nlp.png)
2. 在目录`baidu_api.py`中输入三个平台的密钥key
3. 如果需要外接其他功能，可以参考 https://console.bce.baidu.com/tools/#/index 中的`实例代码中心`，配置对应功能API接口
4. 机器人的错误码可以在对应平台的开发者文档中查询，一般是密钥key填写错误


## 🎉 使用
### 指令表
| 指令  | 说明 |
|:----:|:----:|
|  2c | 翻译至中文 |
|  2e | 翻译至英文 |
|  2j | 翻译至日文 |
|  ernie | 开启文心一言对话 |
|  sentiment | 文本情感分析 |
|  correction | 文本纠错 |
|  keyword | 关键词提取 |
|  esc | 退出当前模式 |

### 效果图
可以开始和robot对话
![qq](https://github.com/JekoQ/nonebot-plugin-baidubucket/blob/main/images/qq.png)
