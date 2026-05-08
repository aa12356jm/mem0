"""
quickstart_deepseek.py
======================

这是 README 中引用的最小可运行脚本。

目标：
1. 用最少代码跑通 add + search
2. 验证 DeepSeek V4 配置在本仓库中可用
3. 让新同学快速获得“我已经跑通了”的反馈
"""

from __future__ import annotations

import os
from pprint import pprint

from mem0 import Memory


def build_config() -> dict:
    """返回默认学习配置（DeepSeek V4 Flash）。"""
    return {
        "llm": {
            "provider": "deepseek",
            "config": {
                "model": "deepseek-v4-flash",
                "temperature": 0.2,
                "max_tokens": 2000,
                "top_p": 1.0,
            },
        },
    }


def ensure_env() -> None:
    """在调用前做必要环境变量检查。"""
    missing = []
    if not os.getenv("DEEPSEEK_API_KEY"):
        missing.append("DEEPSEEK_API_KEY")
    if not os.getenv("OPENAI_API_KEY"):
        missing.append("OPENAI_API_KEY")
    if missing:
        raise RuntimeError(f"缺少环境变量: {', '.join(missing)}")


def main() -> None:
    try:
        ensure_env()
        memory = Memory.from_config(build_config())
        user_id = "demo-user"

        messages = [
            {"role": "user", "content": "我喜欢科幻电影，不喜欢恐怖片。"},
            {"role": "assistant", "content": "明白，以后推荐电影时优先考虑科幻，避开恐怖片。"},
        ]

        print("ADD RESULT:")
        add_result = memory.add(messages, user_id=user_id, metadata={"source": "demo-quickstart"})
        pprint(add_result)

        print("\nSEARCH RESULT:")
        search_result = memory.search(
            "我今晚想看电影，应该推荐什么类型？",
            filters={"user_id": user_id},
            top_k=3,
        )
        pprint(search_result)
    except Exception as exc:
        print("\nquickstart 运行失败，排查顺序：")
        print("1) 设置 DEEPSEEK_API_KEY 与 OPENAI_API_KEY")
        print("2) 检查外网访问 DeepSeek/OpenAI 是否可达")
        print("3) 确认在 hatch 环境执行")
        print("4) 模型名保持 deepseek-v4-flash 或 deepseek-v4-pro")
        print(f"\n原始错误: {exc}")


if __name__ == "__main__":
    main()
