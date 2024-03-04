# README.md
## 莉莉丝 - 虚拟助手
莉莉丝是一个有趣的虚拟助手，她会以弹出窗口的形式与用户互动，提供音乐播放功能，并有一些隐藏的“惊喜”。用户每天首次运行程序时，莉莉丝会根据不同的天数展示不同的对话内容，模拟与用户建立联系的过程。
### 功能特点
- **互动对话**：莉莉丝会根据程序运行的天数与用户进行不同内容的对话。
- **音乐播放**：莉莉丝会询问用户是否愿意一起听歌，并播放预定的音乐文件。
- **隐藏功能**：在特定条件下，莉莉丝会触发特殊事件，如模拟意外重启电脑。
### 使用说明
1. 确保你的系统中安装了Python，以及以下Python库：
   - `tkinter`
   - `requests`
   - `playsound`
2. 克隆或下载此仓库到你的电脑上。
3. 运行`main.py`文件以启动莉莉丝。
4. 根据弹出窗口的提示进行互动。
### 注意事项
- 程序设计为每天运行时展示不同的对话，具体逻辑在代码中通过读取`data.txt`文件来控制。
- 程序中包含的`lilis.mp3`、`1.wav`、`2.wav`和`3.wav`是用于播放的音乐文件，请确保这些文件与`main.py`位于同一目录下。
- 程序在第一次运行时会创建一个批处理文件，并尝试将自己添加到Windows的开机启动项中。
### 许可证
本项目采用[MIT许可证](LICENSE)，你可以自由地使用、修改和分发。
### 作者
- [tamikip](https://github.com/tamikip)
### 贡献
欢迎提出问题和建议，也欢迎贡献代码。
---
_最后更新于: 2024年3月4日_

# README.md
## Lilith - Your Virtual Assistant
Lilith is an interactive virtual assistant that engages with the user through pop-up windows, offers music playback, and includes some hidden "surprises." Depending on the day count since the program was first run, Lilith will display different dialogues, simulating the process of building a relationship with the user.
### Features
- **Interactive Dialogue**: Lilith will have different conversations with the user based on the day count of the program.
- **Music Playback**: Lilith will ask the user if they want to listen to music together and play a preset music file.
- **Hidden Features**: Under specific conditions, Lilith will trigger special events, such as simulating an accidental restart of the computer.
### Usage Instructions
1. Ensure you have Python installed on your system, along with the following Python libraries:
   - `tkinter`
   - `requests`
   - `playsound`
2. Clone or download this repository to your computer.
3. Run the `main.py` file to launch Lilith.
4. Interact with the pop-up windows as prompted.
### Notes
- The program is designed to display different dialogues each day it runs, with the logic controlled by reading the `data.txt` file within the code.
- The included `lilis.mp3`, `1.wav`, `2.wav`, and `3.wav` are music files for playback. Make sure these files are in the same directory as `main.py`.
- The program will create a batch file on the first run and attempt to add itself to the Windows startup items.
### License
This project is licensed under the [MIT License](LICENSE), allowing you to use, modify, and distribute it freely.
### Author
- [Your Name](https://github.com/your_username)
### Contributions
Issues and suggestions are welcome, as well as contributions to the code.
---
_Last updated: March 4, 2024_
