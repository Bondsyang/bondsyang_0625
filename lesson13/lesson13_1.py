#有一個names.txt
#讀取names.txt
#請隨機取出3個名字
import random



random.seed(4561)

# 定義科目常數
SUBJECTS = ["國文", "英文", "數學"]

def sample_names_from_file(file_name: str, nums: int = 1) -> list[str]:
    """
    從指定的檔案中讀取所有姓名，並隨機取出指定數量的姓名。

    參數:
        file_name (str): 檔案名稱，檔案內容為姓名，每行一個。
        nums (int): 要隨機取出的姓名數量，預設為1。

    回傳:
        list[str]: 隨機取出的姓名列表。
    """
    try:
        with open(file_name, encoding="utf-8") as file:
            content: str = file.read()
            names: list[str] = content.split()
            if nums > len(names):
                raise ValueError("取樣數量超過檔案中的姓名數量。")
            return random.sample(names, nums)
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 '{file_name}'。")
        return []
    except ValueError as e:
        print(f"錯誤: {e}")
        return []

def generate_scores_for_names(names: list[str]) -> list[dict]:
    """
    為每個姓名生成3個隨機分數。

    參數:
        names (list[str]): 姓名列表。

    回傳:
        list[dict]: 包含姓名和3個隨機分數的2維列表。
    """
    result_list = []
    for person_name in names:
        student_scores:dict = {"姓名":person_name}
        for subject in ["國文", "英文", "數學"]:
            student_scores[subject] = random.randint(50, 100) 
        result_list.append(student_scores)

    return result_list


def print_student_scores(students: list[dict]):
    '''列印學生姓名和分數，並計算平均分數。
    參數:
        students (list[dict]): 包含學生姓名和分數的列表。
    
    回傳:
        None
    '''    
    print("學生成績表:")
    print(f"{'姓名':<10}{'國文':<8}{'英文':<8}{'數學':<8}{'平均':<8}")
    for student in students:
        name = student["姓名"]
        scores: list[int] = [student[subject] for subject in SUBJECTS]
        average = sum(scores) / len(scores)
        print(f"{name:<10}{scores[0]:<8}{scores[1]:<8}{scores[2]:<8}{average:.2f}")


def analyze_scores(students: list[dict]) -> None:
    """
    列印成績分析資訊，包括全班平均成績、最高分學生及最低分學生。

    參數:
        students (list[dict]): 包含學生姓名和分數的列表。

    回傳:
        None
    """
    if not students:
        print("成績分析: 無學生資料")
        return

    total_scores = []
    for student in students:
        scores = [student[subject] for subject in SUBJECTS]
        total_scores.append(sum(scores) / len(scores))

    class_average = sum(total_scores) / len(total_scores)
    max_score = max(total_scores)
    min_score = min(total_scores)

    max_student = students[total_scores.index(max_score)]["姓名"]
    min_student = students[total_scores.index(min_score)]["姓名"]

    print("成績分析:")
    print(f"- 全班平均成績: {class_average:.1f}分")
    print(f"- 最高分學生: {max_student}({max_score:.1f}分)")
    print(f"- 最低分學生: {min_student}({min_score:.1f}分)")


def main():
    print("=== 學生成績管理系統 ===\n\n")
    names: list[str] = sample_names_from_file("names.txt", nums=3)
    students: list[dict] = generate_scores_for_names(names)
    print_student_scores(students)
    analyze_scores(students)

if __name__ == "__main__":
    main()