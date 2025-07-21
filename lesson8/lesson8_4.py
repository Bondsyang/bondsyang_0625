import random

def play_game(): #沒有呼叫就不會執行
    min = 1
    max = 100
    count = 0
    guess_value = random.randint(min,max)
    print(guess_value)
    print("==========猜數字遊戲===========\n")
    while(True):
        try:
            count += 1
            keyin = int(input(f"猜數字範圍{min}~{max}:"))            
            if keyin >= min and keyin <= max:
                if(keyin == guess_value):
                    print(f"賓果!猜對了,答案是:{guess_value}")
                    print(f"您猜了{count}次")
                    break
                elif keyin > guess_value:
                    print("再小一點!")
                    max = keyin - 1
                
                else:
                    print("再大一點")
                    min = keyin + 1

                print(f"您已經猜{count}次")
                
            else:
                print("請輸入提示範圍內的數字")
        except ValueError:
            print("格式錯誤")
        except Exception as e:
            print(e)

def main():
    play_count = 0  #在root區，一定會執行
    while(True):
        play_count += 1
        play_game()  #呼叫play_game()這個function
        is_continue = input("您還要繼續嗎(y,n)?")
        if is_continue == "n":
            break

    print(f"您共玩了{play_count}次")
    print("遊戲結束")

# main()  #呼叫main function

if __name__ == "__main__":  #function的名稱(入建變數為__name__)一定是字串-> XXX.py檔的主執行檔名稱為"__main__"，程式的開始執行py檔
    main()