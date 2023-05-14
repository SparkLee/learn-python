FROM python:3.11

ENV TERM xterm

RUN pip install --upgrade pip

# https://pypi.org/project/openai/
# https://platform.openai.com/docs/quickstart
RUN pip install openai

RUN pip install -U python-dotenv

WORKDIR /app

# 查看全部 python 扩展库列表（包括扩展库版本信息）
CMD [ "top", "-b" ]
