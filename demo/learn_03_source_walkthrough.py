"""
learn_03_source_walkthrough.py
==============================

目标：
1. 带你按“调用链”定位核心源码文件
2. 减少盲目阅读，先抓关键函数入口
3. 建立对 Memory.from_config/add/search 的结构化认知

使用方式：
    python demo/learn_03_source_walkthrough.py
"""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def p(path: str) -> str:
    """将相对路径转成绝对路径字符串，方便你直接打开。"""
    return str(REPO_ROOT / path)


def print_learning_path() -> None:
    """
    输出建议阅读顺序，并解释每一层要看什么。
    """
    print("Mem0 学习引导 - 第 3 课：源码追踪")
    print("\n建议按这个顺序读：")

    steps = [
        ("mem0/__init__.py", "确认对外暴露的核心类（Memory / AsyncMemory 等）"),
        ("mem0/memory/main.py", "定位 Memory 主链路：from_config / add / search"),
        ("mem0/configs/base.py", "理解统一配置模型（llm/embedder/vector_store）"),
        ("mem0/utils/factory.py", "理解 provider 字符串如何映射到具体实现类"),
        ("mem0/llms/deepseek.py", "理解 DeepSeek LLM Provider 的请求参数与默认行为"),
        ("tests/llms/test_deepseek.py", "验证你对 DeepSeek Provider 行为的理解"),
        ("tests/test_main.py", "验证你对 Memory 主流程行为边界的理解"),
    ]

    for idx, (rel, purpose) in enumerate(steps, start=1):
        print(f"{idx}. {p(rel)}")
        print(f"   - 学习目标: {purpose}")


def print_focus_questions() -> None:
    """
    给你一组“阅读问题”，帮助你主动理解，而不是被动浏览。
    """
    print("\n阅读时请回答这些问题：")
    questions = [
        "Memory.from_config 做了哪些配置校验和实例化动作？",
        "add 是如何把 user_id/agent_id/run_id 合并进过滤与元数据的？",
        "search 为什么要求通过 filters 传 user_id，而不是顶层参数？",
        "DeepSeek provider 的默认 model/base_url 是什么？可被哪些方式覆盖？",
        "如果你要新增一个 LLM provider，最少要改哪些文件？",
    ]
    for q in questions:
        print(f"- {q}")


def print_next_step() -> None:
    print("\n下一步：python demo/learn_04_deepseek_v4_config.py")


def main() -> None:
    print_learning_path()
    print_focus_questions()
    print_next_step()


if __name__ == "__main__":
    main()

