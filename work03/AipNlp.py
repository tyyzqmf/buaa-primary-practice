from aip import AipNlp
import const


# https://cloud.baidu.com/doc/NLP/s/tk6z52b9z
class Nlp:
    def __init__(self):
        self.client = AipNlp("", "", "")

    # 登陆AI平台，获取client
    def login(self, appid, apikey, secretkey):
        self.client = AipNlp(appid, apikey, secretkey)
        # 校验密钥是否正确
        try:
            authObj = self.client._auth()
            params = self.client._getParams(authObj)
            return True
        except Exception as e:
            return False

    def lexer(self, text):
        """ 调用词法分析 """
        res = self.client.lexer(text)
        index = 1
        data = []
        for item in res["items"]:
            data.append(
                [
                    str(index),
                    item["item"],
                    const.POS[item["pos"]],
                    ",".join(item["basic_words"])
                ]
            )
            index += 1
        return data

    def depParser(self, text):
        """ 调用依存句法分析 """
        res = self.client.depParser(text)
        words = {}
        for item in res["items"]:
            words[item['id']] = item['word']
        data = []
        for item in res["items"]:
            data.append(
                [
                    str(item['id']),
                    item["word"],
                    const.POS[item["postag"]],
                    words[item['head']] if item['head'] != 0 else '无',
                    const.DEPRE[item['deprel']]
                ]
            )
        return data

    def dnnlm(self, text):
        """ 调用DNN语言模型 """
        res = self.client.dnnlm(text)
        data = []
        index = 1
        for item in res["items"]:
            data.append(
                [
                    str(index),
                    item["word"],
                    item["prob"],
                ]
            )
            index += 1
        return data, res["ppl"]

    def simnet(self, text1, text2):
        """ 调用短文本相似度 """
        res = self.client.simnet(text1, text2)
        return res["score"]

    def commentTag(self, text, type):
        """ 调用评论观点抽取 """
        """ 如果有可选参数 """
        options = {}
        options["type"] = const.COMMENTTYPE[type]
        res = self.client.commentTag(text, options)
        data = ""
        for item in res["items"]:
            data += f"{item['prop']}, {item['adj']}"
        return data

    def sentimentClassify(self, text):
        """ 调用情感倾向分析 """
        res = self.client.sentimentClassify(text)
        sentiments = {
            0: "负向",
            1: "中性",
            2: "正向"
        }
        data = f"情感极性分类结果: {sentiments[res['items'][0]['sentiment']]},"
        data += f"分类的置信度: {res['items'][0]['confidence']},"
        data += f"属于积极类别的概率: {res['items'][0]['positive_prob']},"
        data += f"属于消极类别的概率: {res['items'][0]['negative_prob']}"
        return data

    def wordEmbedding(self, word):
        """ 调用词向量表示 """
        res = self.client.wordEmbedding(word)
        vec = [str(v) for v in res['vec']]
        data = ','.join(vec)
        return data

    def wordSimEmbedding(self, word1, word2):
        """ 调用词义相似度 """
        res = self.client.wordSimEmbedding(word1, word2)
        return res["score"]

    def keyword(self, title, content):
        """ 调用文章标签 """
        res = self.client.keyword(title, content)
        data = ""
        for item in res["items"]:
            data += f"{item['tag']}: {item['score']}\n"
        return data

    def topic(self, title, content):
        """ 调用文章分类 """
        res = self.client.topic(title, content)
        data = "一级分类结果:\n"
        for item in res["item"]["lv1_tag_list"]:
            data += f"{item['tag']}: {item['score']}\n"
        data += "二级分类结果:\n"
        for item in res["item"]["lv2_tag_list"]:
            data += f"{item['tag']}: {item['score']}\n"
        return data
