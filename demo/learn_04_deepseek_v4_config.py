"""
learn_04_deepseek_v4_config.py
==============================

目标：
1. 系统化掌握 DeepSeek V4 在 Mem0 里的配置方式
2. 学会在“便宜快速”和“高质量”模型之间切换
3. 学会快速检查当前配置是否与你预期一致

使用方式：
    python demo/learn_04_deepseek_v4_config.py
"""

from __future__ import annotations

import os
from pprint import pprint


def build_flash_config() -> dict:
    """
    开发/学习阶段默认推荐：
    - 成本更可控
    - 延迟更低
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


def build_pro_config() -> dict:
    """
    对抽取质量有更高要求时可切到 pro。
    """
    return {
        "llm": {
            "provider": "deepseek",
            "config": {
                "model": "deepseek-v4-pro",
                "temperature": 0.2,
                "max_tokens": 3000,
                "top_p": 1.0,
            },
        }
    }


def print_env_guidance() -> None:
    """
    输出环境变量说明，帮助你排查“为什么模型没走对”。
    """
    print("DeepSeek 关键环境变量：")
    print("- DEEPSEEK_API_KEY: 必需")
    print("- DEEPSEEK_API_BASE: 可选，默认 https://api.deepseek.com")
    print("- OPENAI_API_KEY: 默认 embedding 常用")

    print("\n当前环境检测：")
    print(f"DEEPSEEK_API_KEY 已设置: {bool(os.getenv('DEEPSEEK_API_KEY'))}")
    print(f"DEEPSEEK_API_BASE: {os.getenv('DEEPSEEK_API_BASE', '<未设置，使用默认>')}")
    print(f"OPENAI_API_KEY 已设置: {bool(os.getenv('OPENAI_API_KEY'))}")


def compare_configs() -> None:
    """
    对比两种配置，帮助你形成“何时切换模型”的判断。
    """
    print("\nFlash 配置：")
    pprint(build_flash_config())
    print("\nPro 配置：")
    pprint(build_pro_config())

    print("\n选择建议：")
    print("1) 学习和日常开发：先用 deepseek-v4-flash")
    print("2) 对抽取准确率更敏感：切换 deepseek-v4-pro 再做对比")
    print("3) 每次切换模型后，固定同一批输入做 A/B 观察")


def main() -> None:
    print("Mem0 学习引导 - 第 4 课：DeepSeek V4 配置策略")
    print_env_guidance()
    compare_configs()
    print("\n下一步：python demo/learn_05_debug_and_tests.py")


if __name__ == "__main__":
    main()

