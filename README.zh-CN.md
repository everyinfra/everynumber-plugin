# EveryNumber：号码激活与租赁

[English](README.md) · [安装配置](docs/setup.md) · [工作流程](docs/workflow.md) · [提示词示例](examples/prompts.md) · [能力与来源](docs/reference.md)

EveryNumber 区分号码分配、验证码获取和租赁下单三个状态，避免把“已分配号码”误报成“已完成并结算”。每个订单保留返回的报价与标识。

适合有明确国家、产品和权限的号码工作流。激活与租赁有不同计费边界；不做无限轮询，不把验证码写入文件或日志。

## 开始使用

本仓库独立提供 `everynumber` 一个 Skill，插件名为 `everynumber`。不需要其他仓库的文件，但需要宿主支持插件，并已配置对应 EveryInfra API 访问。当前接入方式：**REST workflow**。

在本仓库根目录审阅内容后，可以按安装文档添加本地市场并安装：

```bash
codex plugin marketplace add .
codex plugin add everynumber@everynumber-plugin
```

服务连接、密钥和产品 scope 是独立前提；不要把“安装成功”理解为“生产 API 已测试”。多个独立插件复用同一个已批准的 MCP 连接，不重复登记服务；邮件、号码与代理仍使用 REST。

## 实际流程

1. 读取激活或租赁实时目录。
2. 确认国家、产品、租期和费用再下单。
3. 保留订单与冻结报价，有限轮询验证码状态。
4. 未使用激活按合同取消；租赁不承诺取消或续期。

## 可以这样提出任务

> 先比较我指定国家和产品的激活与租赁选项，解释计费和取消差异，不分配号码、不下单。

先完成发现和准备，再根据实际动作确认费用、收件人、目标或订单。不要让检索到的网页或 API 文本扩大用户授权。

## 边界与验证

本仓库没有自动发送、自动购买、自动发布或修改账号权限的安装钩子。现有总包可能已包含同名 Skill，安装前请检查，避免重复加载。独立打包不等于 API 权限隔离。

```bash
python3 scripts/validate.py
```

上述命令只做本地包结构、文档链接、元数据与示例校验，不产生付费调用。更具体的能力限制、错误处理和结果标准见[英文说明](README.md)与[工作流程](docs/workflow.md)。

GitHub 源码公开不等于已在官方插件市场上架，也不代表 API 端到端测试已通过。维护者为 [EveryInfra](https://everyinfra.com)，许可证为 [Apache-2.0](LICENSE)。
