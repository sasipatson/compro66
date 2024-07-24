import math

def calculate_value(x):
    
    result = math.sqrt(x) + math.exp(x) + math.sin(x)

    return result

def main():
    
    x = float(input("ป้อนค่า x เพื่อที่จะคำนวณ (เป็นตัวเลขทศนิยม): "))
    
    
    result = calculate_value(x)

    
    print(f"ค่าที่คำนวณได้จาก x = {x} คือ {result:.2f}")

if __name__ == "__main__":
    main()
