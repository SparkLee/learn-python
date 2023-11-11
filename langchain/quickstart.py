# LangChain Quickstart: https://python.langchain.com/docs/get_started/quickstart

import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = OpenAI()
# chat_model = ChatOpenAI() # 默认读取环境变量“OPENAI_API_KEY”
chat_model = ChatOpenAI(openai_api_key=os.getenv('API_KEY_OPENAI'))

text = "我想给一家使用AI生成UGC内容的创业公司取一个名字，你有什么好的建议吗？"
messages = [HumanMessage(content=text)]

out1 = llm.invoke(text)
out2 = chat_model.invoke(messages)

if __name__ == "__main__":
    # print(out1)
    print(out2)
