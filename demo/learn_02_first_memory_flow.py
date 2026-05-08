"""
learn_02_first_memory_flow.py
=============================

目标：
1. 跑通 Mem0 的最小“写入 + 检索”闭环
2. 理解 add/search 的输入输出长什么样
3. 学会用最小样例验证配置是否生效

使用方式：
    python demo/learn_02_first_memory_flow.py

学习建议：
- 第一次运行先不追求“最佳结果”，先追求“跑通闭环”。
- 看到结果后，再去看 learn_03 的源码追踪。
"""

from __future__ import annotations

import os
from pprint import pprint

from mem0 import Memory


def build_config() -> dict:
    """
    构建最小配置。

    说明：
    - LLM 使用 DeepSeek V4（显式指定，避免走旧默认值）
    - Embedder 不显式配置时，按仓库默认行为处理
    """
    return {
        "llm": {
            "provider": "deepseek",
            "config": {
                "model": "deepseek-v4-flash",
                "temperature": 0.2,
                "max_tokens": 2000,
                "top_p": 1.0,
            },
        }
    }


def validate_keys() -> None:
    """
    在真正调用前，先做环境变量校验。
    """
    missing = []
    if not os.getenv("DEEPSEEK_API_KEY"):
        missing.append("DEEPSEEK_API_KEY")
    if not os.getenv("OPENAI_API_KEY"):
        missing.append("OPENAI_API_KEY")
    if missing:
        raise RuntimeError(f"缺少环境变量: {', '.join(missing)}")


def run_first_flow() -> None:
    """
    执行最小闭环：
    1) add 两轮对话
    2) search 新问题
    3) 输出结果供你观察
    """
    validate_keys()
    memory = Memory.from_config(build_config())

    user_id = "learn-demo-user"
    messages = [
        {"role": "user", "content": "我喜欢周末跑步，也喜欢简洁风格的工具。"},
        {"role": "assistant", "content": "记住了：你偏好周末跑步和简洁工具。"},
    ]

    print("\n=== STEP 1: ADD ===")
    add_result = memory.add(messages, user_id=user_id, metadata={"lesson": "02"})
    pprint(add_result)

    print("\n=== STEP 2: SEARCH ===")
    search_result = memory.search(
        "我想安排周末计划，怎么结合我的偏好？",
        filters={"user_id": user_id},
        top_k=3,
    )
    pprint(search_result)

    print("\n=== STEP 3: 你要关注什么 ===")
    print("1) add 结果里是否有结构化记忆内容")
    print("2) search 结果是否召回了“周末跑步/简洁风格”")
    print("3) 若结果为空，优先排查 key、网络、模型名")


def main() -> None:
    print("Mem0 学习引导 - 第 2 课：最小可运行记忆流")
    run_first_flow()


if __name__ == "__main__":
    main()

