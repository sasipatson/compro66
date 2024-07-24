import random

def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def main():
    # สร้างรายการคะแนนที่สุ่มมา 5 ค่าในช่วง 30.0 - 50.0
    scores = [random.uniform(30.0, 50.0) for _ in range(5)]
    
    # คำนวณค่าเฉลี่ยคะแนน
    average_score = calculate_average(scores)
    
    # แสดงผลลัพธ์
    print("คะแนนที่สุ่มได้:", scores)
    print(f"ผลรวมคะแนน: {sum(scores):.2f}")
    print(f"ค่าเฉลี่ยคะแนน: {average_score:.2f}")

if __name__ == "__main__":
    main()
