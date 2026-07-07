# Ruanyuxi 🌐
### AI Platform & Infrastructure Engineer | Security Researcher

*Building reliable, high-performance, and secure environments for Autonomous Agents.*

---

## 🚀 About Me

I am an **AI Platform & Infrastructure Engineer** and **Security Researcher** specializing in autonomous agent runtimes, sandbox escape prevention, high-performance API gateways, and anti-detection automation.

Unlike traditional developers, I adopt a strictly **AI-Native & Vibe Coding Workflow**, leveraging agentic loops to accelerate engineering iteration while maintaining institutional-grade robustness in testing, sandboxing, and deployment.

- 🏗️ **AI Infrastructure**: Designing sandboxed runtimes (Node.js/Docker) and dual-SQLite messaging conduits.
- ⚡ **Backend Engine**: Creating concurrent, rate-limited FastAPI gateway routers and Redis distributed locking states.
- 🔒 **Offensive Security & Evasion**: Advanced binary program analysis, IDA Pro decompilation, and spoofing browser fingerprinters (TLS/Canvas/WebGL) to bypass cloud WAFs.

---

## 🛠️ Tech Stack & Tooling

```
  Languages         : Python, Go, Node.js/TypeScript, C++, Bash
  AI Engine         : ReAct Loop, MCP (Model Context Protocol), Graph of Agents, Prompt Engineering
  Platform & Cloud  : Docker, Docker Compose, AWS (EC2, VPC, SG), Cloudflare (Workers, WAF, DNS)
  Data & Cache      : Redis (Lua locking, sliding rate-limiters), PostgreSQL, SQLite, SQLAlchemy 2.0
  Security Auditing : IDA Pro, Ghidra, Inline Hooking (Trampoline), Web fingerprint spoofing
```

---

## 🎨 AI-Native Engineering Workflow

I design systems by orchestrating agents and enforcing strict human-in-the-loop verification policies:

```
┌──────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│ Requirement Analysis │ ───> │ Task Decomposition Plan │ ───> │ Claude Code & Cursor    │
└──────────────────────┘      └─────────────────────────┘      └────────────┬────────────┘
                                                                            │
                                                                            v
┌──────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│ Production Deploy    │ <─── │ Multi-Agent E2E Testing │ <─── │ Human Approval Gate     │
│ CF WAF + AWS EC2     │      │ Pytest / Ruff Checks    │      │ (Permission Hooks)      │
└──────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
```

---

## 📁 Featured Projects

### ⚡ [agent-service](https://github.com/Ruanyuxi1337/agent-service)
*Production-grade asynchronous AI ReAct loop gateway service.*
- **Concurrency Safeguard**: Leverages **Redis distributed locks** via Lua scripts to stop race conditions on conversational states.
- **SSE Stream & Connection Reclamation**: Catches `asyncio.CancelledError` on client disconnection to instantly propagate termination signals up to LLM queries and release computing quotas.
- **Observer RAG Evaluation**: Computes real-time token intersection recall indexes dynamically in an asynchronous queue.

### 📦 [nanoclaw (feature-custom-security)](https://github.com/Ruanyuxi1337/nanoclaw)
*Hardened agent container hosting runtime based on Node.js and Docker SDK.*
- **Directory Traversal Fix**: Implemented the `isSafePath` verification method in TypeScript MCP handler to stop arbitrary files from escaping out of `/workspace/agent`.
- **Zero-Contention IPC**: Dual-DB architecture (`inbound.db` / `outbound.db`) separating reader/writer processes to scale container tasks concurrently.

### 🎭 [browser-automation](https://github.com/Ruanyuxi1337/browser-automation)
*Anti-fingerprinting, high-entropy web scraping automation engine.*
- **Low-Level Spoofing**: Rebuilt core Selenium capabilities using Camoufox browser to fake JA3/JA4 TLS handshake states, Canvas renders, and audio entropy.
- **Bezier Trajectory Profiling**: Custom interpolation simulating muscle deceleration to bypass Cloudflare behavioral anomaly WAF checks.

---

## 📈 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=Ruanyuxi1337&show_icons=true&theme=tokyonight&locale=en" alt="Ruanyuxi's GitHub stats" width="48%" />
  <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=Ruanyuxi1337&layout=compact&theme=tokyonight&locale=en" alt="Top Langs" width="48%" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=Ruanyuxi1337&theme=tokyonight" alt="GitHub Streak" width="97%" />
</p>

---

## 📬 Connect With Me

- **Email:** [abyssrift1337@gmail.com](mailto:abyssrift1337@gmail.com)
- **GitHub:** [@Ruanyuxi1337](https://github.com/Ruanyuxi1337)
