import random
from langchain_openai import ChatOpenAI

num = random.randint(0, 9)  # 生成0-9的随机整数

llm = ChatOpenAI(
    base_url="http://127.0.0.1:60630/v1",
    api_key="sk-noauth",
    model="Qwen/Qwen3-Coder-30B-A3B-Instruct",
)

print(llm.invoke(f"现有0-9范围内的一个整数，请猜测这个整数是几，只回答数字").content)