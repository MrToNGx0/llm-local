# 🤖 AI Local Home Server (Llama 3.1 / Qwen 2.5 + Open Claw)

[English](#english-guide) | [ภาษาไทย](#คู่มือภาษาไทย)

---

## ภาษาไทย (Thai Guide)

โปรเจกต์สำหรับรัน AI ส่วนตัวในเครื่อง (Local) โดยใช้ **Ollama** ร่วมกับ **Open Claw** (Autonomous AI UI) พร้อมการตั้งค่า Persona ระดับสูง (AI Architect)

### ✨ คุณสมบัติเด่น
- **Multi-Model Support**: รองรับ Llama 3.1 8B และ Qwen 2.5 7B (แนะนำสำหรับภาษาไทย)
- **Open Claw**: หน้าจอใช้งานสำหรับงานเขียนโค้ดและ Autonomous Tasks
- **Master Persona**: ตั้งค่าตัวตน AI เป็น "AI Architect & Digital Strategist"
- **Language Policy**: สื่อสารภาษาไทยและอังกฤษอย่างมืออาชีพ (**Strictly No Chinese**)
- **Auto Model Puller**: ดึงโมเดลให้อัตโนมัติเมื่อเริ่มรัน
- **Monitoring**: ดูสถานะการทำงานผ่าน Dozzle

### 🚀 วิธีเริ่มต้นใช้งาน
1. **เตรียมความพร้อม**: ติดตั้ง Docker และ NVIDIA Container Toolkit (ถ้ามี GPU)
2. **ตั้งค่า**: 
   - คัดลอกไฟล์: `cp .env.example .env`
   - ใส่ API Key ของ Gemini หรือค่ายอื่นๆ ในไฟล์ `.env`
   - แก้ไข `workspace/USER.md` เพื่อให้ AI รู้จักคุณ
3. **เริ่มระบบ**:
   ```bash
   docker-compose up -d
   ```
4. **เข้าใช้งาน**:
   - **Open Claw**: [http://localhost:18789](http://localhost:18789)
   - **Logs (Dozzle)**: [http://localhost:8888](http://localhost:8888)

---

## English Guide

A comprehensive local AI hosting setup featuring **Ollama** and **Open Claw**, pre-configured with a "Master AI Persona" for advanced tasks.

### ✨ Features
- **Local LLMs**: Powered by Ollama (Default: Qwen 2.5 / Llama 3.1).
- **AI Architect Persona**: Expert-level instructions for coding, tech, and strategic tasks.
- **Language Policy**: Professional Thai/English communication (**Strictly No Chinese**).
- **Smart Routing**: Seamlessly switch between local models and Cloud APIs (Gemini).
- **Monitoring**: Real-time container logs with Dozzle.

### 🚀 How to Run
1. **Prerequisites**: Ensure Docker is installed. For GPU support, install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
2. **Configuration**: 
   - `cp .env.example .env`
   - Edit `.env` to add your `GOOGLE_API_KEY` or other provider keys.
   - Update `workspace/USER.md` with your preferences.
3. **Launch**:
   ```bash
   docker-compose up -d
   ```
4. **Access**:
   - **Open Claw**: [http://localhost:18789](http://localhost:18789)
   - **Monitoring (Dozzle)**: [http://localhost:8888](http://localhost:8888)

### 📁 Project Structure
- `docker-compose.yml`: Services orchestration.
- `openclaw.json`: Gateway and agent configuration.
- `workspace/`: **Core AI Logic & Data**
  - `AGENTS.md`: System instructions & expertise.
  - `SOUL.md`: Values and personality.
  - `IDENTITY.md`: Name, role, and language policy.
  - `USER.md`: Your personal context and preferences.
  - `TOOLS.md`: Search and verification strategies.
