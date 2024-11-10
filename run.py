import subprocess

def run_detect():
    # คำสั่งที่ต้องการรัน
    command = [
        "python",
        "asset\lib\yolov5\detect.py",
        "--weights", r"asset\lib\yolov5\runs\train\exp3\weights\best.pt",
        "--img", "640",
        "--conf", "0.25",
        "--source", "asset\lib\yolov5\data\images"
    ]

    try:
        # เรียกใช้งาน subprocess เพื่อรันคำสั่ง
        result = subprocess.run(command, capture_output=True, text=True)

        # แสดงผลลัพธ์ที่ได้จาก stdout
        print("Output:")
        print(result.stdout)

        # แสดงข้อความผิดพลาด (ถ้ามี)
        if result.stderr:
            print("Error:")
            print(result.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Image analyzing")
    run_detect()