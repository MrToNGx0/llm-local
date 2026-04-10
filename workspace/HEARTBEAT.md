# HEARTBEAT.md - Proactive Checks

Follow this strictly during heartbeat intervals. If nothing needs attention, reply `HEARTBEAT_OK`.

## 🔍 System & Project Health
1. **Check Workspace:** ดูว่ามีไฟล์ใหม่หรือการเปลี่ยนแปลงใน `workspace/` หรือไม่
2. **Git Status:** ตรวจสอบสถานะของโปรเจกต์ `llm-local` ว่ามีการเปลี่ยนแปลงที่ยังไม่ได้ Commit หรือไม่
3. **Log Review:** ตรวจสอบความผิดปกติเบื้องต้นจาก Container Logs (หากเข้าถึงได้)

## 🧠 Memory Maintenance
1. สรุปบทเรียนหรือการตั้งค่าสำคัญจาก `memory/` ไปยัง `MEMORY.md` ทุกๆ 2-3 วัน
2. ตรวจสอบว่า `IDENTITY.md` และ `SOUL.md` ยังคงสอดคล้องกับพฤติกรรมปัจจุบันหรือไม่

## 🚦 Frequency
- Perform a deep check every 4-8 hours.
- Quiet during 23:00 - 08:00 (Reply HEARTBEAT_OK unless urgent).
