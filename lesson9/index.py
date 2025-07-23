import box #這樣import，只會去呼叫box package的__init__

def main(): #try也可以放在主function裡
    try:
        play_count = 0  #在root區，一定會執行
        while(True):
            play_count += 1
            box.play_game()  #呼叫play_game()這個function，如果有raise會直接從這個回圈跳出
            is_continue = input("您還要繼續嗎(y,n)?")
            if is_continue == "n":
                break

        print(f"{box.user_name}共玩了{play_count}次")
        print("遊戲結束")
        
    except ValueError:
        print("格式錯誤")
        print("應用程式中斷")
    except Exception as e:
        print(e)
        print("應用程式中斷")
    

# main()  #呼叫main function

if __name__ == "__main__":  #function的名稱(入建變數為__name__)一定是字串-> XXX.py檔的主執行檔名稱為"__main__"，程式的開始執行py檔
    main()