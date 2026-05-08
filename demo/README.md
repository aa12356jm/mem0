# Mem0 仓库学习与实战指南（DeepSeek V4）

这份文档面向第一次接触本仓库的开发者。目标不是一次性读完所有代码，而是按可验证的小步骤理解 Mem0 的核心概念、跑通最小示例、学会定位代码、配置 DeepSeek V4，并知道后续如何扩展和测试。

> 日期：2026-05-08  
> 仓库路径：`/Volumes/ZhiTaiTiPlus7100-2T/codes/mem0`  
> 推荐主线：先学 Python SDK，再了解 TypeScript SDK、CLI、Server、OpenMemory。

## 0. 新人快速入口（先跑这个）

你可以先运行以下脚本，按编号执行即可：

```bash
python demo/learn_00_index.py
```

如果你偏好直接看文档，也可以先读：

- `demo/README.md`（全景版）
- `demo/learn_01_environment_and_layout.py`（环境与目录）
- `demo/learn_02_first_memory_flow.py`（第一条可运行链路）

## 1. 这个仓库解决什么问题

Mem0 是一个给 AI 应用使用的“记忆层”。普通聊天模型只看当前上下文，Mem0 会把对话中的长期偏好、事实、历史状态抽取成结构化记忆，再在后续对话中检索出来，帮助模型做个性化回答。

核心工作流可以理解为四步：

1. `add`：把对话、文本或事件写入 Mem0。
2. `extract`：LLM 从输入中抽取值得长期保存的事实。
3. `store`：Embedder 把记忆转成向量，Vector Store 保存向量和元数据。
4. `search`：新问题到来时，Mem0 用语义、关键词和实体等信号找回相关记忆。

你学习源码时可以一直带着这个问题：一次 `memory.add(...)` 和一次 `memory.search(...)` 在代码里分别经过了哪些层？

## 2. 仓库地图

先记住这些目录：

| 路径 | 作用 | 学习优先级 |
| --- | --- | --- |
| `mem0/` | Python SDK 核心实现，包含 Memory、LLM、Embedder、Vector Store、Graph、Reranker | 高 |
| `tests/` | Python SDK 单元测试，适合用来理解行为边界 | 高 |
| `docs/` | Mintlify 文档站，包含配置、集成、API 说明 | 高 |
| `mem0-ts/` | TypeScript SDK，包含 hosted client 与 OSS Memory | 中 |
| `cli/python/` | Python CLI，Typer 实现 | 中 |
| `cli/node/` | Node CLI，Commander 实现 | 中 |
| `server/` | 自托管 FastAPI REST Server | 中 |
| `openmemory/` | 自托管完整记忆平台，含 FastAPI API 与 Next.js UI | 后 |
| `examples/`、`cookbooks/` | 示例项目和 Notebook | 后 |

建议先不要从 `openmemory/` 开始。它是完整应用，依赖多，适合你理解 SDK 后再看。

## 3. 准备环境

Python SDK 主线推荐：

```bash
cd /Volumes/ZhiTaiTiPlus7100-2T/codes/mem0
hatch shell dev_py_3_11
```

如果本机还没有 Hatch：

```bash
pip install hatch
hatch shell dev_py_3_11
```

TypeScript 相关包使用 `pnpm`：

```bash
npm install -g pnpm@10
cd mem0-ts
pnpm install
```

本仓库规则：

- Python SDK 用 Ruff，根目录行宽 120。
- TypeScript 包统一使用 `pnpm`，不要用 `npm install` 或 `yarn`。
- 修改某个包后，只运行该包相关的 lint、typecheck、test，避免无谓地跑全仓库。

## 4. 配置 DeepSeek V4

Mem0 仓库已经内置 DeepSeek LLM Provider：

- Python：`mem0/llms/deepseek.py`
- Python 配置：`mem0/configs/llms/deepseek.py`
- TypeScript：`mem0-ts/src/oss/src/llms/deepseek.ts`
- 文档：`docs/components/llms/models/deepseek.mdx`

截至 2026-05-08，DeepSeek 官方 API 文档列出的 V4 模型包括：

- `deepseek-v4-flash`：默认推荐，速度和成本更适合学习、开发、常规记忆抽取。
- `deepseek-v4-pro`：更强的 V4 模型，适合高质量抽取或更复杂推理。

注意：仓库当前 DeepSeek Provider 的默认模型仍是 `deepseek-chat`。如果你明确要使用 DeepSeek V4，请在 config 里显式写 `model`，不要依赖默认值。

环境变量：

```bash
export DEEPSEEK_API_KEY="你的 DeepSeek API Key"
export DEEPSEEK_API_BASE="https://api.deepseek.com"
```

Python SDK 的 DeepSeek V4 配置：

```python
config = {
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
```

如果你要把效果优先于成本，可以改成：

```python
"model": "deepseek-v4-pro"
```

Mem0 还需要 Embedder。最省事的学习路径是继续用 OpenAI embedding：

```bash
export OPENAI_API_KEY="你的 OpenAI API Key"
```

如果你不想使用 OpenAI embedding，后续可以阅读 `docs/components/embedders/overview.mdx`，换成 Ollama、HuggingFace、Together 等 Embedder。第一次学习建议先减少变量，先跑通主流程。

参考链接：

- DeepSeek API 文档：https://api-docs.deepseek.com/
- Mem0 DeepSeek 文档：`docs/components/llms/models/deepseek.mdx`

## 5. 第一个最小 Python 示例

`demo/quickstart_deepseek.py` 已经准备好，你可以直接运行，不需要手动创建文件。

运行：

```bash
cd /Volumes/ZhiTaiTiPlus7100-2T/codes/mem0
hatch shell dev_py_3_11
python demo/quickstart_deepseek.py
```

你应该看到两类输出：

- `ADD RESULT`：Mem0 抽取出来的新记忆，例如用户喜欢科幻电影、不喜欢恐怖片。
- `SEARCH RESULT`：针对新问题检索出的相关记忆。

如果这里失败，优先检查：

- `DEEPSEEK_API_KEY` 是否设置。
- `OPENAI_API_KEY` 是否设置。
- 网络是否能访问 DeepSeek 与 OpenAI API。
- 模型名是否仍是 DeepSeek 官方可用模型。

## 6. 第一次读源码：跟踪 `Memory.from_config`

从这几处开始：

1. `mem0/__init__.py`：看 SDK 对外暴露了哪些类。
2. `mem0/memory/main.py`：搜索 `class Memory` 和 `def from_config`。
3. `mem0/configs/base.py`：理解 `MemoryConfig` 包含 `llm`、`embedder`、`vector_store`。
4. `mem0/utils/factory.py`：理解 Provider Factory 如何把字符串 `deepseek` 映射到具体类。
5. `mem0/llms/deepseek.py`：理解 DeepSeek 为什么可以复用 OpenAI-compatible client。

建议使用这些命令：

```bash
rg -n "class Memory|def from_config|def add\\(|def search\\(" mem0/memory/main.py
rg -n "\"deepseek\"|DeepSeekLLM|DeepSeekConfig" mem0 tests docs mem0-ts -S
rg -n "class .*Factory|def create" mem0/utils mem0/vector_stores mem0/embeddings -S
```

阅读重点：

- `Memory.from_config(config)` 会把 dict 转成 `MemoryConfig`。
- `Memory.__init__` 会创建 LLM、Embedder、Vector Store。
- Provider 名称是字符串，但真正实例化由 Factory 完成。
- DeepSeek Provider 最终调用 `client.chat.completions.create(...)`。

## 7. 理解 `memory.add(...)`

建议你按这个顺序读：

```bash
rg -n "def add\\(|def _add_to_vector_store|extract|insert" mem0/memory/main.py
```

一条记忆写入的大致路径：

1. 外部调用 `memory.add(messages, user_id=...)`。
2. Mem0 规范化 `messages`、`metadata`、`filters`。
3. LLM 根据提示词抽取可保存事实。
4. Embedder 把事实转成向量。
5. Vector Store 保存向量、文本、用户 ID、元数据。
6. 返回本次新增的 memory 列表。

你读代码时要特别注意这些边界：

- `user_id`、`agent_id`、`run_id` 是记忆隔离维度。
- `metadata` 是业务自定义信息，适合放来源、标签、租户、时间等。
- `infer=True` 时会让 LLM 抽取事实；`infer=False` 更接近直接写入。

## 8. 理解 `memory.search(...)`

建议命令：

```bash
rg -n "def search\\(|def _search_vector_store|keyword_search|rerank" mem0/memory/main.py
```

检索的大致路径：

1. 外部调用 `memory.search(query, filters={"user_id": ...}, top_k=...)`。
2. Embedder 把 query 转成向量。
3. Vector Store 做语义搜索。
4. 如果后端支持，叠加关键词搜索。
5. 结果按分数、阈值、`top_k` 过滤。
6. 返回可注入到模型上下文的记忆。

你可以做一个小实验：连续写入三条不同偏好，然后搜索不同问题，观察 `SEARCH RESULT` 里的排序变化。

## 9. 学会看测试

测试是理解预期行为最快的入口。建议先读这些：

```bash
sed -n '1,220p' tests/llms/test_deepseek.py
sed -n '1,240p' tests/test_main.py
```

DeepSeek 测试会告诉你：

- 默认 base URL 是 `https://api.deepseek.com`。
- 可以用 `DEEPSEEK_API_BASE` 覆盖。
- 可以通过 config 传入自定义 `deepseek_base_url`。
- `response_format`、tools 等参数如何转发给 OpenAI-compatible API。

运行 DeepSeek LLM 单元测试：

```bash
hatch shell dev_py_3_11
pytest tests/llms/test_deepseek.py
```

运行核心 Memory 测试：

```bash
pytest tests/test_main.py
```

如果你改了 `mem0/llms/deepseek.py`，至少跑：

```bash
ruff check mem0/llms/deepseek.py mem0/configs/llms/deepseek.py tests/llms/test_deepseek.py
pytest tests/llms/test_deepseek.py
```

## 10. 第二条主线：TypeScript SDK

当 Python SDK 跑通后，再看 TS：

```bash
cd /Volumes/ZhiTaiTiPlus7100-2T/codes/mem0/mem0-ts
pnpm install
pnpm run build
pnpm run test
```

DeepSeek 相关文件：

```bash
rg -n "DeepSeek|deepseek|DEEPSEEK" src tests -S
```

你会看到 TS 的 DeepSeek Provider 也走 OpenAI-compatible 路线：

- 环境变量：`DEEPSEEK_API_KEY`
- base URL：`DEEPSEEK_API_BASE` 或 `https://api.deepseek.com`
- 默认模型：`deepseek-chat`

要用 DeepSeek V4，同样需要显式传入：

```ts
model: "deepseek-v4-flash"
```

## 11. 第一个源码改动练习

建议做一个低风险练习：给 DeepSeek 文档补充 V4 模型说明。

候选文件：

- `docs/components/llms/models/deepseek.mdx`

改动目标：

- 保留已有 `deepseek-chat` 示例。
- 增加一段说明：如果使用 DeepSeek V4，请显式设置 `model` 为 `deepseek-v4-flash` 或 `deepseek-v4-pro`。
- 不改 Provider 默认值，避免破坏向后兼容。

验证：

```bash
python scripts/check-llms-txt-coverage.py
```

如果只改已有文档页，通常不需要改 `docs/llms.txt`。如果新增 `.mdx` 页面，则必须把页面加入 `docs/llms.txt`。

## 12. 常见任务怎么下手

### 新增 LLM Provider

参考 DeepSeek：

1. 新建 `mem0/llms/<provider>.py`。
2. 新建或更新 `mem0/configs/llms/<provider>.py`。
3. 更新 `mem0/llms/configs.py` 或相关注册位置。
4. 更新 `mem0/utils/factory.py`。
5. 新增 `tests/llms/test_<provider>.py`。
6. 新增 `docs/components/llms/models/<provider>.mdx`。
7. 如果新增文档页，更新 `docs/llms.txt`。

### 新增 Vector Store

从已有 provider 复制学习路径：

```bash
ls mem0/vector_stores
rg -n "class .*Vector|def search|def insert|def delete" mem0/vector_stores -S
```

原则：

- 不要把新依赖加到 core dependencies，优先放可选依赖组。
- 保持接口签名和现有 provider 一致。
- 测试里 mock 外部服务，除非是明确的 integration test。

### 修 bug

推荐顺序：

1. 先用 `rg` 定位相关代码和测试。
2. 写一个会失败的回归测试。
3. 最小改动修复。
4. 跑相关测试和 lint。
5. 如果影响公开行为，更新文档。

## 13. 推荐 5 天学习计划

### Day 1：跑通

- 阅读本文件第 1-5 节。
- 配好 DeepSeek V4 与 embedding key。
- 跑通 `demo/quickstart_deepseek.py`。
- 记录 `add` 和 `search` 的输出长什么样。

### Day 2：读 Python SDK 核心链路

- 阅读 `mem0/memory/main.py` 的 `Memory.from_config`、`add`、`search`。
- 阅读 `mem0/utils/factory.py`。
- 阅读 `mem0/llms/deepseek.py`。
- 跑 `pytest tests/llms/test_deepseek.py`。

### Day 3：理解配置与 Provider

- 阅读 `mem0/configs/base.py`。
- 对比 DeepSeek、OpenAI、Ollama 这些 LLM Provider。
- 阅读一个 Embedder Provider 和一个 Vector Store Provider。
- 画出“LLM + Embedder + Vector Store”的依赖图。

### Day 4：看 TS SDK 与 CLI

- 进入 `mem0-ts/` 跑 build/test。
- 对比 TS 的 DeepSeek Provider 和 Python 的 DeepSeek Provider。
- 阅读 `cli/python/README.md` 与 `cli/node/README.md`。

### Day 5：做一个小改动

- 从文档、测试、或 provider 配置说明里选一个小改动。
- 保持 diff 小。
- 跑对应 lint/test。
- 自己写一段总结：改了什么、为什么改、怎么验证。

## 14. 调试清单

遇到问题时按这个顺序排查：

1. 环境变量是否设置：`DEEPSEEK_API_KEY`、`OPENAI_API_KEY`。
2. 当前 Python 环境是否是 Hatch 环境：`which python`。
3. 包是否从本地仓库导入：`python -c "import mem0; print(mem0.__file__)"`。
4. DeepSeek 模型名是否可用。
5. Vector Store 是否有本地持久化旧数据影响测试。
6. 单元测试是否用 mock，还是会真实请求外部 API。
7. 修改 TS 包时是否使用了 `pnpm`。

## 15. 你应该形成的源码心智模型

Mem0 的代码结构不是一个单体大函数，而是多类 Provider 组合：

```text
Application
  |
  v
Memory / AsyncMemory
  |
  +-- LLM Provider        -> 抽取、推理、格式化记忆
  +-- Embedder Provider   -> 文本转向量
  +-- Vector Store        -> 保存和检索向量
  +-- Graph Store         -> 可选，处理关系记忆
  +-- Reranker            -> 可选，重排搜索结果
```

所以学习和改代码时，最重要的是先判断问题属于哪一层：

- 模型输出不对：优先看 LLM Provider、prompt、response parsing。
- 搜不到记忆：优先看 Embedder、Vector Store、filters、limit、threshold。
- 用户隔离不对：优先看 `user_id`、`agent_id`、`run_id`、metadata filters。
- 性能或成本问题：优先看模型选择、embedding、top_k、是否启用额外检索或图。

## 16. 下一步推荐

完成本指南后，建议继续做三个小项目：

1. 用 DeepSeek V4 + Mem0 写一个命令行偏好记忆助手。
2. 把 embedding 从默认 OpenAI 换成一个本地或国产 embedding provider。
3. 给 `docs/components/llms/models/deepseek.mdx` 提交一次 V4 文档更新，并补充验证说明。
