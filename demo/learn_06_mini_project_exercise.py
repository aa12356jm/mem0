"""
learn_06_mini_project_exercise.py
=================================

目标：
1. 带你做一个“能持续迭代”的小练习项目
2. 把前面学到的配置、调用、排错、测试串起来
3. 给你一个可执行的进阶任务清单

使用方式：
    python demo/learn_06_mini_project_exercise.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ExerciseStep:
    """
    一个学习步骤的数据模型。

    这么写的目的：
    - 结构清晰：每个步骤都有目标、动作、验证
    - 方便后续扩展：你可以继续加 week2/week3 任务
    """

    title: str
    objective: str
    action: str
    verify: str


def build_curriculum() -> List[ExerciseStep]:
    """
    定义从基础到进阶的 7 步 mini project 路线。
    """
    return [
        ExerciseStep(
            title="Step 1 - 初始化最小脚手架",
            objective="建立一个可反复运行的本地脚本入口",
            action="创建 demo/my_memory_assistant.py，先只初始化 Memory.from_config",
            verify="脚本启动不报错，且能打印当前模型配置",
        ),
        ExerciseStep(
            title="Step 2 - 接入 add/search",
            objective="跑通最小功能闭环",
            action="支持输入一句偏好并写入，再用问题检索历史偏好",
            verify="search 结果可召回刚写入的偏好",
        ),
        ExerciseStep(
            title="Step 3 - 设计 metadata",
            objective="让记忆有可筛选维度",
            action="为每次写入增加 category/source/session 标签",
            verify="不同 category 的检索结果可被正确过滤",
        ),
        ExerciseStep(
            title="Step 4 - 加入错误处理",
            objective="从 demo 升级为可用工具",
            action="捕获 key 缺失、网络失败、参数错误并给出可执行提示",
            verify="人为制造错误时，提示清晰可定位",
        ),
        ExerciseStep(
            title="Step 5 - 写回归测试",
            objective="锁定关键行为防回归",
            action="给关键函数写 2~3 个 pytest 用例（mock 外部依赖）",
            verify="pytest 能稳定通过，且失败时能准确指出问题",
        ),
        ExerciseStep(
            title="Step 6 - 做模型 A/B 对比",
            objective="建立模型选择的工程判断",
            action="同一批输入分别跑 deepseek-v4-flash 与 deepseek-v4-pro",
            verify="记录成本/延迟/效果差异并形成结论",
        ),
        ExerciseStep(
            title="Step 7 - 文档化决策",
            objective="形成可复用的团队资产",
            action="在 demo/ 写一份实验记录（配置、结果、结论）",
            verify="别人只看文档就能复现实验",
        ),
    ]


def print_curriculum(steps: List[ExerciseStep]) -> None:
    """
    以一致格式输出学习计划，便于你按步骤打卡。
    """
    print("Mem0 学习引导 - 第 6 课：综合实战任务")
    for step in steps:
        print("\n" + "-" * 80)
        print(step.title)
        print(f"目标: {step.objective}")
        print(f"行动: {step.action}")
        print(f"验收: {step.verify}")


def print_final_advice() -> None:
    """
    给你进阶时最容易忽略的三个原则。
    """
    print("\n" + "=" * 80)
    print("进阶建议")
    print("=" * 80)
    print("1) 每次只改一个变量（模型、prompt、top_k 选其一）")
    print("2) 每次改动都要有可对比输入，避免主观判断")
    print("3) 先补测试再重构，保证你能快速回退")


def main() -> None:
    steps = build_curriculum()
    print_curriculum(steps)
    print_final_advice()


if __name__ == "__main__":
    main()

