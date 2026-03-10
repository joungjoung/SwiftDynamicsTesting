## การสั่งรันโปรแกรม

### เตรียมความพร้อมของระบบ (มี Python และ venv ติดตั้งแล้ว)
1. เปิด Terminal หรือ Command Prompt
2. สร้าง virtual environment (ถ้ายังไม่มี)
```bash
python -m venv .venv
```
3. เปิดใช้งาน virtual environment
```bash
.venv\Scripts\activate  # สำหรับ Windows
```
4. ติดตั้ง dependencies
```bash
pip install -r requirements.txt
```

### เตรียมฐานข้อมูล
1. สร้างฐานข้อมูล (ถ้ายังไม่มี)
```bash
python manage.py makemigrations
python manage.py migrate
```

2. สร้าง superuser (ถ้ายังไม่มี)
```bash
python manage.py createsuperuser
```

### รันเซิร์ฟเวอร์
```bash
python manage.py runserver
```
