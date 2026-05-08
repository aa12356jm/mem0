"""
learn_07_typescript_track.py
============================

目标：
1. 给新人一条与 Python 对称的 TypeScript 学习路径
2. 明确 mem0-ts 中 DeepSeek 相关代码入口
3. 给出从构建到测试再到源码阅读的最小闭环

使用方式：
    python demo/learn_07_typescript_track.py
"""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TS_ROOT = REPO_ROOT / "mem0-ts"


def print_path_overview() -> None:
    """显示 TS 路径和关键文件。"""
    print("Mem0 学习引导 - 第 7 课：TypeScript 学习路线")
    print(f"\nmem0-ts 路径: {TS_ROOT}")
    print(f"路径存在: {TS_ROOT.exists()}")

    key_files = [
        "src/oss/src/llms/deepseek.ts",
        "src/oss/src/utils/factory.ts",
        "src/oss/tests/deepseek.test.ts",
        "src/oss/tests/factory.unit.test.ts",
    ]
    print("\n关键文件：")
    for rel in key_files:
        path = TS_ROOT / rel
        print(f"- {path} | {'OK' if path.exists() else 'MISSING'}")


def print_commands() -> None:
    """输出建议命令序列。"""
    print("\n建议命令（按顺序）：")
    print("cd /Volumes/ZhiTaiTiPlus7100-2T/codes/mem0/mem0-ts")
    print("pnpm install")
    print("pnpm run build")
    print("pnpm run test")
    print("rg -n \"DeepSeek|deepseek|DEEPSEEK\" src tests -S")


def print_reading_questions() -> None:
    """输出带问题的阅读路线，帮助主动学习。"""
    print("\n阅读问题：")
    questions = [
        "deepseek.ts 如何读取 DEEPSEEK_API_KEY / DEEPSEEK_API_BASE？",
        "TS 默认模型是否仍是 deepseek-chat？",
        "factory.ts 如何把 provider='deepseek' 映射到 DeepSeekLLM？",
        "测试里如何 mock OpenAI-compatible client？",
        "如果要切 V4，代码里需要改默认值还是只改调用侧配置？",
    ]
    for q in questions:
        print(f"- {q}")


def main() -> None:
    print_path_overview()
    print_commands()
    print_reading_questions()
    print("\n完成后可回到 Python/TS 对照总结：demo/README.md 第 10 节。")


if __name__ == "__main__":
    main()

