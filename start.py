import os
import sys
import shutil


def create_batch_file(python_script_path, batch_file_name='start_my_script.bat'):
    # 获取当前脚本所在的目录
    current_dir = os.path.dirname(python_script_path)

    # 创建批处理文件的完整路径
    batch_file_path = os.path.join(current_dir, batch_file_name)

    # 写入批处理文件内容，用于启动当前Python脚本
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write('@echo off\n')
        batch_file.write(f'python "{sys.executable}" "{python_script_path}"\n')

    print(f'Batch file "{batch_file_path}" created.')


def add_to_startup(batch_file_path):
    # 获取当前用户的启动文件夹路径
    startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # 将批处理文件复制到启动文件夹
    startup_batch_file_path = os.path.join(startup_folder, os.path.basename(batch_file_path))
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder)
    shutil.copyfile(batch_file_path, startup_batch_file_path)

    print(f'Added "{startup_batch_file_path}" to startup folder.')


def remove_from_startup(batch_file_path):
    # 获取启动文件夹中的批处理文件路径
    startup_batch_file_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs',
                                           'Startup', os.path.basename(batch_file_path))

    # 如果批处理文件存在，则删除它
    if os.path.exists(startup_batch_file_path):
        os.remove(startup_batch_file_path)
        print(f'Removed "{startup_batch_file_path}" from startup folder.')
    else:
        print(f'"{startup_batch_file_path}" not found in startup folder.')


def run():
    # 创建批处理文件
    create_batch_file(exe_path)

    # 添加到开机启动
    add_to_startup(exe_path)

    # 如果需要移除自启动，取消以下注释
    # remove_from_startup(current_script_path)
