# 🤖 AI Local Home Server (Llama 3.1 + Open Claw)

[English](#english-guide) | [ภาษาไทย](#คู่มือภาษาไทย)

---

## ภาษาไทย (Thai Guide)

โปรเจคสำหรับรัน AI ส่วนตัวในเครื่อง (Local) โดยใช้ **Ollama** ร่วมกับ **Open Claw** (Autonomous AI UI) พร้อมรองรับการเชื่อมต่อกับ **Google Gemini API** และ Cloud AI อื่นๆ

### ✨ คุณสมบัติเด่น
- **Llama 3.1 8B**: รันในเครื่องตัวเองผ่าน Ollama
- **Open Claw**: หน้าจอใช้งานสำหรับงานเขียนโค้ดและ Autonomous Tasks (รองรับการทำหน้าที่เป็น Router)
- **Gemini Integration**: เชื่อมต่อ Cloud AI เพื่อความฉลาดสูงสุด
- **Auto Model Puller**: ดึงโมเดลให้อัตโนมัติเมื่อเริ่มรัน (Llama 3.1)
- **Monitoring**: ดูสถานะการทำงานผ่าน Dozzle

### 🚀 วิธีเริ่มต้นใช้งาน
1. **เตรียมความพร้อม**: ติดตั้ง Docker และ NVIDIA Container Toolkit (ถ้ามี GPU)
2. **ตั้งค่า**: 
   - คัดลอกไฟล์: `cp .env.example .env`
   - ใส่ API Key ของ Gemini หรือค่ายอื่นๆ ในไฟล์ `.env`
3. **เริ่มระบบ**:
   ```bash
   docker-compose up -d
   ```
4. **เข้าใช้งาน**:
   - **Open Claw**: [http://localhost:8080](http://localhost:8080)
   - **Logs (Dozzle)**: [http://localhost:8888](http://localhost:8888)

---

## English Guide

A comprehensive local AI hosting setup featuring **Ollama** and **Open Claw**, with seamless integration for **Google Gemini**, **Anthropic**, and **OpenAI**.

### ✨ Features
- **Local LLMs**: Powered by Ollama (Default: Llama 3.1).
- **Open Claw UI**: An autonomous AI assistant interface designed for coding and complex tasks.
- **Smart Routing**: Use Open Claw to route between local models and cloud APIs (Gemini, Claude, GPT).
- **Auto Model Pulling**: Automatically downloads the required model on startup.
- **Monitoring**: Real-time container logs with Dozzle.

### 🚀 How to Run
1. **Prerequisites**: Ensure Docker is installed. For GPU support, install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
2. **Configuration**: 
   - `cp .env.example .env`
   - Edit `.env` to add your `GOOGLE_API_KEY` or other provider keys.
3. **Launch**:
   ```bash
   docker-compose up -d
   ```
4. **Access**:
   - **Open Claw**: [http://localhost:8080](http://localhost:8080)
   - **Monitoring (Dozzle)**: [http://localhost:8888](http://localhost:8888)

### 🛠️ GPU Verification
Check if your GPU is recognized by Ollama:
```bash
docker exec -it ollama nvidia-smi
```

### 📁 Project Structure
- `docker-compose.yml`: Services orchestration.
- `.env`: Ports, API keys, and security settings.
- `workspace/`: Shared folder for AI files and data.
