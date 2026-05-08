> 中文注释：本文件非代码内容已翻译为中文，代码块与配置示例保持原样。

# Mintlify 入门套件

单击“使用此模板”复制 Mintlify 入门工具包。入门套件包含的示例包括

- 指南页面
- 导航
- 定制
- API 参考页面
- 使用流行的组件

### 发展

安装 [Mintlify CLI](https://www.npmjs.com/package/mintlify) 以在本地预览文档更改。要安装，请使用以下命令
```

npm i -g mintlify
```

在文档的根目录（其中 mint.json 所在的位置）运行以下命令
```

mintlify dev

```

### 发布变更

安装我们的 Github 应用程序以自动将更改从您的存储库传播到您的部署。推送到默认分支后，更改将自动部署到生产环境。找到要在仪表板上安装的链接。

#### 故障排除

- Mintlify dev 未运行 - 运行 `mintlify install` 它将重新安装依赖项。
- 页面加载为 404 - 确保您正在包含“mint.json”的文件夹中运行
