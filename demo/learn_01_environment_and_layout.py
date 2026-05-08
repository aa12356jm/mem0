"""
learn_01_environment_and_layout.py
==================================

目标：
1. 帮你快速确认当前开发环境是否符合 Mem0 学习要求
2. 帮你理解仓库目录结构和每个目录的职责
3. 给出“今天下一步该做什么”的明确行动清单

使用方式：
    cd /Volumes/ZhiTaiTiPlus7100-2T/codes/mem0
    python demo/learn_01_environment_and_layout.py

预期学习结果：
- 你知道从哪里开始看代码
- 你知道后续每个学习脚本对应哪个能力层
"""

from __future__ import annotations

import os
import platform
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def print_header(title: str) -> None:
    """统一输出分节标题，便于你扫描终端输出。"""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def check_environment() -> None:
    """
    检查最关键的学习前置项。

    说明：
    - 这里只做“轻量检查”，不做依赖安装。
    - 如果某项缺失，脚本会告诉你下一步命令。
    """
    print_header("1) 环境检查")
    print(f"Python 版本: {platform.python_version()}")
    print(f"系统: {platform.system()} {platform.release()}")
    print(f"仓库根目录: {REPO_ROOT}")
    print(f"hatch 可用: {bool(shutil.which('hatch'))}")
    print(f"pnpm 可用: {bool(shutil.which('pnpm'))}")

    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    print(f"DEEPSEEK_API_KEY 已设置: {bool(deepseek_key)}")
    print(f"OPENAI_API_KEY 已设置: {bool(openai_key)}")

    print("\n如果没设置 key，先执行：")
    print('  export DEEPSEEK_API_KEY="你的-key"')
    print('  export OPENAI_API_KEY="你的-key"')
    print("\n如果 hatch/pnpm 不可用，先安装再继续后续课程。")


def explain_layout() -> None:
    """
    输出最核心目录，减少你“该看哪里”的犹豫成本。
    """
    print_header("2) 核心目录地图")
    core_paths = [
        ("mem0/", "Python SDK 核心实现（必看）"),
        ("tests/", "Python 测试（理解行为边界）"),
        ("docs/", "官方文档源文件（配置与概念）"),
        ("mem0-ts/", "TypeScript SDK"),
        ("cli/python/", "Python CLI"),
        ("cli/node/", "Node CLI"),
        ("server/", "FastAPI 自托管服务"),
        ("openmemory/", "完整平台（API + UI）"),
    ]
    for rel, desc in core_paths:
        abs_path = REPO_ROOT / rel
        exists = "存在" if abs_path.exists() else "缺失"
        print(f"- {rel:<15} | {desc:<32} | 状态: {exists}")


def next_actions() -> None:
    """
    给出明确下一步，避免“读完不知道做什么”。
    """
    print_header("3) 下一步行动")
    print("按顺序运行这些脚本：")
    print("1. python demo/learn_02_first_memory_flow.py")
    print("2. python demo/learn_03_source_walkthrough.py")
    print("3. python demo/learn_04_deepseek_v4_config.py")
    print("4. python demo/learn_05_debug_and_tests.py")
    print("5. python demo/learn_06_mini_project_exercise.py")


def main() -> None:
    """脚本入口。"""
    print_header("Mem0 学习引导 - 第 1 课")
    check_environment()
    explain_layout()
    next_actions()


if __name__ == "__main__":
    main()
