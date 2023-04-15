FROM python:3.11

RUN pip install --upgrade pip

# https://pypi.org/project/gradio/
# https://www.gradio.app/quickstart/
RUN pip install gradio

# https://pypi.org/project/openai/
# https://platform.openai.com/docs/quickstart
RUN pip install openai

WORKDIR /app

# 查看全部 python 扩展库列表（包括扩展库版本信息）
CMD [ "pip", "list" ]
