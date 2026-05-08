"""
learn_05_debug_and_tests.py
===========================

目标：
1. 帮你把“学习”升级成“可验证学习”
2. 让你掌握最关键的测试命令和调试顺序
3. 避免一上来跑全量测试导致信息噪音

使用方式：
    python demo/learn_05_debug_and_tests.py
"""

from __future__ import annotations

import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def print_test_strategy() -> None:
    """
    给出先窄后宽的验证策略。
    """
    print("Mem0 学习引导 - 第 5 课：调试与测试")
    print("\n建议顺序（先窄后宽）：")
    print("1) DeepSeek provider 定点测试")
    print("2) Memory 主流程测试")
    print("3) 只在需要时扩大范围")


def show_commands() -> None:
    """
    输出建议命令，便于你直接复制执行。
    """
    print("\n可直接执行的命令：")
    print("cd /Volumes/ZhiTaiTiPlus7100-2T/codes/mem0")
    print("hatch shell dev_py_3_11")
    print("pytest tests/llms/test_deepseek.py -q")
    print("pytest tests/test_main.py -q")
    print("ruff check mem0/llms/deepseek.py tests/llms/test_deepseek.py")


def optional_quick_check() -> None:
    """
    可选：快速检查关键测试文件是否存在。

    这个函数不跑测试，只检查路径，避免误会“命令没反应”。
    """
    print("\n关键文件存在性检查：")
    test_files = [
        REPO_ROOT / "tests/llms/test_deepseek.py",
        REPO_ROOT / "tests/test_main.py",
        REPO_ROOT / "mem0/llms/deepseek.py",
    ]
    for path in test_files:
        print(f"- {path}: {'OK' if path.exists() else 'MISSING'}")


def show_debug_checklist() -> None:
    """
    常见故障排查顺序。
    """
    print("\n调试清单（按优先级）：")
    checks = [
        "环境变量是否正确（DEEPSEEK_API_KEY / OPENAI_API_KEY）",
        "是否在正确 python 环境（hatch shell）中运行",
        "模型名是否显式设置为 deepseek-v4-flash 或 deepseek-v4-pro",
        "search 调用是否使用 filters={'user_id': ...}",
        "报错来自网络、鉴权还是参数校验",
    ]
    for item in checks:
        print(f"- {item}")


def main() -> None:
    print_test_strategy()
    show_commands()
    optional_quick_check()
    show_debug_checklist()
    print("\n下一步：python demo/learn_06_mini_project_exercise.py")


if __name__ == "__main__":
    main()

