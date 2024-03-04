import threading
import tkinter as tk
import re
import time
import random

screen_width = 1920
screen_height = 1080

# 读取并解析 LRC 文件
with open("world.lrc", 'r', encoding='utf-8') as file:
    lrc_content = file.read()

times = []
lyrics = []

for line in lrc_content.strip().split('\n'):
    time_match = re.search(r'\[(\d+:\d+\.\d+)\]', line)
    if time_match:
        time_str = time_match.group(1)
        minutes, seconds = time_str.split(':')
        total_seconds = int(minutes) * 60 + float(seconds)
        times.append(total_seconds)
        lyric = line.replace(f'[{time_str}]', '').strip()
        lyrics.append(lyric)


# 为每句歌词创建新窗口的函数
def show_lyric(lyric, delay):
    time.sleep(delay)
    window = tk.Tk()
    window.title("World")
    x = random.randint(0, screen_width - 300)  # 留出足够空间显示窗口
    y = random.randint(0, screen_height - 200)
    # 设置窗口的位置
    window.geometry(f"300x80+{x}+{y}")
    label = tk.Label(window, text=lyric, font=("Microsoft YaHei", 15), fg="black")
    label.pack(pady=20)
    window.mainloop()


# 使用线程为每句歌词创建新窗口
def play():
    threads = []
    start_time = time.time()
    for i in range(len(lyrics)):
        if i == 0:
            delay = 0
        else:
            delay = times[i] - times[i-1]
            time.sleep(delay)
            thread = threading.Thread(target=show_lyric, args=(lyrics[i], delay))
            threads.append(thread)
            thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()