# MouseCenterDrag

鼠标自动化小工具：运行后把光标移到屏幕水平中心、当前 Y 位置，按下左键并向下拖拽半个屏幕高度。
基于 Python/PyAutoGUI/Tkinter，带 GUI 与全局热键。

## Features
- 一键/热键触发自动拖拽
- 自动计算：center_x = screen_w//2，target_y = current_y + screen_h//2（限制在屏幕内）
- 3 秒倒计时、平滑移动（easeInOutQuad）
- GUI 日志窗口；置顶显示
- 全局热键 Ctrl+Alt+Space 启动
- PyAutoGUI failsafe：鼠标急移到屏幕角落可中止自动化

## Requirements
- Python 3.8+
- pyautogui
- keyboard
- Tkinter（标准库；Linux 可能需 python3-tk）
- screeninfo（获取显示器信息，失败时回退 pyautogui.size）

## Install
git clone https://github.com/berserkross/MouseCenterDrag.git
cd MouseCenterDrag
pip install -r requirements.txt
# 最低依赖：pip install pyautogui keyboard screeninfo

## Usage
python MouseCenterDrag.py
- 点 “Start (Ctrl+Alt+Space)” 或按全局热键
- 程序倒计时 3 秒后自动：移到中心 → 左键按下 → 向下拖半屏 → 松开
- 失控时快速把鼠标移到屏幕左上角触发 PyAutoGUI FailSafe 中止

## Platform notes
- Windows：通常直接可用，全局热键需以普通用户运行；如控制管理员窗口可能需管理员权限。
- macOS：需“系统设置 → 隐私与安全性 → 辅助功能”授权运行脚本的 Python/终端/IDE；
  全局键盘热键另可能受权限与后台事件限制。[9](@ref)
- Linux：X11 下通常可用；需 python3-xlib、python3-tk，部分发行版补 scrot。
  Wayland 下鼠标/热键可能受限，建议切 X11 或声明实验性支持。[6,14](@ref)
- PyAutoGUI 默认只稳定控制主显示器，多屏绝对坐标可能偏移。[2](@ref)

## Safety
仅用于自己桌面的可控自动化；不要在远程桌面、锁屏、或无人工监督时跑未知拖拽脚本。

## Use cases
UI 自动化演示、拖拽操作复盘、辅助测试“下拉/拖拽区”交互原型。
