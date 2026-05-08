"""
learn_00_index.py
=================

这是学习入口索引文件。
你可以先运行它，快速看到完整学习路线与每个文件的定位。

使用方式：
    python demo/learn_00_index.py
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    files = [
        ("README.md", "全景学习文档（建议先读 10 分钟）"),
        ("learn_01_environment_and_layout.py", "环境检查 + 仓库地图"),
        ("learn_02_first_memory_flow.py", "最小 add/search 闭环"),
        ("learn_03_source_walkthrough.py", "源码调用链追踪"),
        ("learn_04_deepseek_v4_config.py", "DeepSeek V4 配置策略"),
        ("learn_05_debug_and_tests.py", "调试与测试方法"),
        ("learn_06_mini_project_exercise.py", "综合实战与进阶任务"),
        ("quickstart_deepseek.py", "README 中配套的最小实跑脚本"),
    ]

    print("Mem0 渐进式学习索引\n")
    print("建议按编号顺序执行：\n")
    for idx, (filename, desc) in enumerate(files, start=1):
        path = base / filename
        print(f"{idx}. {path}")
        print(f"   - {desc}")

    print("\n建议先执行：python demo/learn_01_environment_and_layout.py")


if __name__ == "__main__":
    main()
