# 🤖 AI Local Home Server (Llama 3.1 + Gemini)

[English](#english-guide) | [ภาษาไทย](#คู่มือภาษาไทย)

---

## ภาษาไทย (Thai Guide)

โปรเจคสำหรับรัน AI ส่วนตัวในเครื่อง (Local) โดยใช้ **Ollama** ร่วมกับหน้าจอใช้งานที่สวยงามอย่าง **Open WebUI** พร้อมรองรับการเชื่อมต่อกับ **Google Gemini API**

### ✨ คุณสมบัติเด่น
- **Llama 3.1 8B (Q4_K_M)**: รันในเครื่องตัวเอง เร็ว แรง และเป็นส่วนตัว
- **Gemini Integration**: สลับไปใช้ Gemini ได้ทันทีเมื่อต้องการงานที่ซับซ้อน
- **Auto Model Puller**: ดึงโมเดลให้อัตโนมัติเมื่อเริ่มรัน ไม่ต้องพิมพ์คำสั่งเอง
- **GPU Support**: รองรับการใช้งานการ์ดจอ NVIDIA เพื่อความรวดเร็ว
- **Monitoring**: ดูสถานะการทำงานผ่าน Dozzle Dashboard

### 🚀 วิธีเริ่มต้นใช้งาน
1. **เตรียมความพร้อม**: ติดตั้ง Docker และ NVIDIA Container Toolkit (ถ้ามี GPU)
2. **ตั้งค่า**: ใส่ Gemini API Key ในไฟล์ `.env` (ถ้ามี)
3. **เริ่มระบบ**:
   ```bash
   docker-compose up -d --build
   ```
4. **เข้าใช้งาน**:
   - **หน้าแชท**: [http://localhost:3000](http://localhost:3000)
   - **ดู Logs**: [http://localhost:8888](http://localhost:8888)

---

## English Guide

A comprehensive local AI hosting setup featuring **Ollama** and **Open WebUI**, with seamless **Google Gemini API** integration.

### 🚀 How to Run
1. **Prerequisites**: Ensure Docker is installed. For GPU support, install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
2. **Configuration**: Edit `.env` to add your `GOOGLE_API_KEY`.
3. **Launch**:
   ```bash
   docker-compose up -d --build
   ```
4. **Access**:
   - **Web UI**: [http://localhost:3000](http://localhost:3000)
   - **Monitoring (Dozzle)**: [http://localhost:8888](http://localhost:8888)

### 🛠️ GPU Verification
Check if your GPU is recognized:
```bash
docker exec -it ollama nvidia-smi
```

### 💡 Choosing the Right Model / การเลือกใช้งาน
- **Privacy (ข้อมูลส่วนตัว)** ➡️ 🏠 **Llama 3.1 (Local)**
- **Complex Logic (งานซับซ้อน)** ➡️ ☁️ **Gemini (Cloud)**
- **Image/File Analysis (วิเคราะห์ภาพ/ไฟล์)** ➡️ ☁️ **Gemini (Cloud)**

### 📁 Project Structure
- `docker-compose.yml`: Main services configuration.
- `.env`: Ports, API keys, and security settings.
- `agent/`: Custom Python API (FastAPI) for future AI tasks.
- `workspace/`: Shared folder for AI files and data.
