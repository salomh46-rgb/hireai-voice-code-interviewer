# 🎯 HireAI — Autonomous Voice & Code Technical Interviewer Platform

<div align="center">

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Web Speech API](https://img.shields.io/badge/Speech%20API-Audio%20Streaming-6366F1?style=for-the-badge&logo=webrtc&logoColor=white)](https://developer.mozilla.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](Dockerfile)
[![License MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-100%25_Passing-brightgreen?style=for-the-badge&logo=pytest&logoColor=white)](tests/)

<p align="center">
  <b>Simulates real-time FAANG & Senior Full-Stack technical mock interviews with live speech-to-text audio interactions, Monaco code editor evaluation, and automated Scorecard analytics.</b>
</p>

</div>

---

## 🌟 Core Architecture & Capabilities

- 🎙️ **Real-Time Voice Interactivity:** Bidirectional speech synthesis & Web Speech recognition allowing candidates to verbally explain architecture and trade-offs.
- 💻 **Live Code Sandbox IDE:** In-browser code editor with syntax evaluation across Full-Stack, Backend Concurrency, and AI/RAG domain problems.
- 🧠 **Algorithmic & Big-O Evaluator:** Evaluates time complexity, memory allocation, and edge case safety in sub-2.5 seconds.
- 📊 **Detailed Candidate Scorecards:** Generates 100-point multi-axis feedback (Algorithms, Code Cleanliness, Verbal Articulation).
- 🐳 **Containerized & Production Ready:** Docker-ready backend with FastAPI test coverage.

---

## 🚀 Quickstart

### 1. Run via Python / FastAPI:
```bash
cd server
pip install -r requirements.txt
uvicorn server.main:app --reload --port 8000
```

### 2. Run via Docker Compose:
```bash
docker build -t hireai-server .
docker run -p 8000:8000 hireai-server
```

### 3. Open Interactive Interview Arena:
Open `client/index.html` directly or deploy to Vercel/Netlify!

---

## 🧪 Automated Testing

Run the test suite:
```bash
python -m unittest discover tests/
```

---

## 👨‍💻 Author

**Javohirbek Asqarov (Jasper)**
- GitHub: [@salomh46-rgb](https://github.com/salomh46-rgb)
- Portfolio: [javohirbek-portfolio.vercel.app](https://javohirbek-portfolio.vercel.app/)
- Telegram: [@Dr_eviluz](https://t.me/Dr_eviluz)
- Email: [salomh46@gmail.com](mailto:salomh46@gmail.com)

---

## 📄 License
MIT © [Javohirbek Asqarov](LICENSE)
