import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = os.environ.get("GMAIL_USERNAME")
password = os.environ.get("GMAIL_PASSWORD")

if not sender or not password:
    print("Error: Missing credentials")
    exit(1)

# List of applications
applications = [
    {
        "to": "peachlandai@gmail.com",
        "subject": "应聘AI伴侣产品对话编排工程师 - Ruanyuxi",
        "body": """您好，我是 Ruanyuxi，在 V2EX 上看到了您招聘“AI伴侣产品对话编排工程师”的帖子，对该岗位非常感兴趣。

我虽然是在校学生（大专大数据专业，2027年毕业），但我过去几年一直在独立开发并上线运营高并发的 AI 应用，时间充裕，支持全职远程或灵活兼职。

我的技术沉淀和编排经验非常契合您的需求：
1. 状态机与剧情控制：我熟悉 LLM 确定性状态机（FSM）的维持。在自研的 Agent 网关（agent-service）中，我通过设计 ReAct 决策主循环的硬性步数拦截（MAX_REACT_STEPS=10）和 Redis Lua 分布式锁，确保并发请求下 Session 状态的强一致性与防御过载。
2. 隔离与安全编排：我是开源 Agent 框架 NanoClaw 的安全贡献者，重构了其 MCP 沙箱安全机制，编写了路径穿越过滤（isSafePath），在隔离运行时（Sandbox）有丰富的开发经验。
3. 成本与背压优化：针对流式 SSE 传输，我通过在 FastAPI 捕获 asyncio.CancelledError，实现对上游 LLM API 的毫秒级断连回收机制，防止长上下文下的 Token 资源浪费。
4. 全栈集成经验：我独立配置过 AWS VPC 安全组、Docker 容器网络，并用 Cloudflare Workers 在边缘端进行动态路由与鉴权。

我的 GitHub 已经更新了相关的代码和架构设计，期待与您进一步交流：
GitHub 主页：https://github.com/Ruanyuxi1337
核心项目：
- 异步 AI 网关：https://github.com/Ruanyuxi1337/agent-service
- 容器 Agent 运行时：https://github.com/Ruanyuxi1337/nanoclaw

方便的话，我们可以加个微信或 TG 聊一下，随时可以进行项目演示。祝好！"""
    },
    {
        "to": "kevin@symbiosis-x.com",
        "subject": "应聘具身智能Web平台全栈工程师 - Ruanyuxi",
        "body": """您好 Kevin，

我是 Ruanyuxi，在 V2EX 上看到了您招聘“具身智能 Web 平台全栈工程师”的帖子，非常兴奋，这与我的技能组合和研发理念完美契合。

关于我与该岗位的契合度：
1. 极致的 AI-native 研发效能：我非常认同“All in AI”的工作理念。我日常深度使用 Claude Code, Cursor 与自研 Agent 流程进行开发。例如，我基于开源 Agent 架构 NanoClaw 和 Python 开发了多套生产级的 Agent 工具链，并自主设计了交互式的 Claude Code 终端客户端（claude-code-cli）。
2. 扎实的全栈与高并发后端：我精通 Python (FastAPI / asyncio) 与 Go。在自研的 AI Gateway 项目中，我利用 Redis Lua 脚本开发了分布式互斥锁，并在 FastAPI 中优雅捕获 asyncio.CancelledError 实现了流式长连接的背压与自动资源回收，达到了极高的稳定标准。
3. 隔离与安全机制：我是 NanoClaw 开源项目（Node.js / Docker）的安全贡献者，独立修复了其路径穿越安全漏洞，编写了 isSafePath 安全过滤器，对 Docker 容器网络及沙箱隔离有深厚积累。
4. Linux 与运维能力：我熟练使用 Docker Compose 部署容器化架构，配置 AWS EC2、VPC 路由与 Cloudflare WAF 安全规则，具备开箱即用的系统部署及运维视野。

我虽然是 2027 届的在校学生，但拥有完整的线上服务研发、商业化与安全对抗闭环经验。我可以提供核心项目的在线演示（Demo）。

GitHub 仓库链接：
- 主页：https://github.com/Ruanyuxi1337
- 异步 AI 网关：https://github.com/Ruanyuxi1337/agent-service
- 容器 Agent 沙箱：https://github.com/Ruanyuxi1337/nanoclaw

期待您的回复，非常希望有机会能够加入团队，和您一起参与具身智能软件生态的建设。谢谢！"""
    }
]

# Sending loop
try:
    print("Connecting to smtp.gmail.com:587...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print("Logging in...")
    server.login(sender, password)
    
    for app in applications:
        msg = MIMEMultipart()
        msg["From"] = f"Ruanyuxi <{sender}>"
        msg["To"] = app["to"]
        msg["Subject"] = app["subject"]
        msg.attach(MIMEText(app["body"], "plain", "utf-8"))
        
        print(f"Sending email to {app['to']}...")
        server.sendmail(sender, app["to"], msg.as_string())
        print(f"Successfully sent to {app['to']}!")
        
    server.close()
    print("All applications sent successfully!")
except Exception as e:
    print("SMTP Error:", e)
    exit(1)
