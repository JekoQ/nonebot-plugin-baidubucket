from nonebot import on_command
from nonebot.rule import to_me
from nonebot.params import ArgPlainText

from .baidu_api import func_model, func_translate, func_sentiment_analysis, func_correction, func_keyword

#翻译响应器
translate_to_chinese = on_command("翻译至中文", rule=to_me(), aliases={"to_chinese","2c"}, priority=10, block=True)
translate_to_english = on_command("翻译至英文", rule=to_me(), aliases={"to_english","2e"}, priority=10, block=True)
translate_to_japanese = on_command("翻译至日文", rule=to_me(), aliases={"to_japanese","2j"}, priority=10, block=True)

#大模型响应器
chat_to_ernie = on_command("文心一言", rule=to_me(), aliases={"ernie","ERNIE"}, priority=10, block=True)

#NLP自然语言处理响应器
nlp_to_sentiment_analysis = on_command("情感分析", rule=to_me(), aliases={"sentiment"}, priority=10, block=True)
nlp_to_correction = on_command("文本纠错", rule=to_me(), aliases={"correction"}, priority=10, block=True)
nlp_to_keyword = on_command("关键词提取", rule=to_me(), aliases={"keyword"}, priority=10, block=True)

 

#翻译至中文
@translate_to_chinese.got("text", prompt="请输入原文：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_translate('zh',text)

        if 'error_code' in response.keys():
            await translate_to_chinese.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            await translate_to_chinese.reject(f"翻译结果：\n{response['trans_result'][0]['dst']}")
    else:
        await translate_to_chinese.finish(f"已退出翻译")

#翻译至英文
@translate_to_english.got("text", prompt="请输入原文：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_translate('en',text)

        if 'error_code' in response.keys():
            await translate_to_english.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            await translate_to_english.reject(f"翻译结果：\n{response['trans_result'][0]['dst']}")
    else:
        await translate_to_english.finish(f"已退出翻译")

#翻译至日文
@translate_to_japanese.got("text", prompt="请输入原文：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_translate('jp',text)

        if 'error_code' in response.keys():
            await translate_to_japanese.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            await translate_to_japanese.reject(f"翻译结果：\n{response['trans_result'][0]['dst']}")
    else:
        await translate_to_japanese.finish(f"已退出翻译")

#文心一言
@chat_to_ernie.got("text", prompt="文心一言 ERNIE-Bot-turbo 与您对话：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_model(text)
        if 'error_code' in response.keys():
            await chat_to_ernie.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            await chat_to_ernie.reject(response['result'])
    else:
        await chat_to_ernie.finish(f"已退出文心一言")



#情感分析
@nlp_to_sentiment_analysis.got("text", prompt="请输入需要分析的文本：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_sentiment_analysis(text)
        if 'error_code' in response.keys():
            await nlp_to_sentiment_analysis.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            res = response['items'][0]
            sentiment = {0:"负向",1:"中性",2:"正向"}
            res_text = "%s, 置信度: %.2f%%"%(sentiment[res['sentiment']],res['confidence']*100)
            await nlp_to_sentiment_analysis.reject(res_text)
    else:
        await nlp_to_sentiment_analysis.finish(f"已退出情绪分析")


#文本纠错
@nlp_to_correction.got("text", prompt="请输入需要纠错的文本：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_correction(text)
        if 'error_code' in response.keys():
            await nlp_to_correction.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            res_text = response['item']['correct_query']
            await nlp_to_correction.reject(f"纠错结果：\n{res_text}")
    else:
        await nlp_to_correction.finish(f"已退出文本纠错")


#关键字提取
@nlp_to_keyword.got("text", prompt="请输入需要提取关键词的文本：")
async def _(text: str = ArgPlainText()):

    if text!='esc':
        response = func_keyword(text)
        if 'error_code' in response.keys():
            await nlp_to_keyword.finish(f"错误代码 {int(response['error_code'])}：{response['error_msg']}")
        else:
            res_text = response['results']
            res=[]
            for key_value in res_text:
                res.append(key_value["word"])
                if len(res)==5:
                    break
            res_text = ",".join(res)
            await nlp_to_keyword.reject(f"关键词：\n{res_text}")
    else:
        await nlp_to_keyword.finish(f"已退出关键词提取")

