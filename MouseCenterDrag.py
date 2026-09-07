"""
Automatic Mouse Drag Program
Function: After running, move cursor to screen center, then press left mouse button and drag down half screen distance
"""

import pyautogui
import time
import screeninfo
import tkinter as tk
from threading import Thread
import keyboard


class MouseDragGUI:
    """GUI class for displaying mouse drag status"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Drag Control")
        self.root.geometry("600x400+100+100")
        self.root.wm_attributes("-topmost", 1)
        self.root.resizable(False, False)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.start_button = tk.Button(
            self.button_frame, 
            text="▶ Start (Ctrl+Alt+Space)", 
            command=self.start_drag,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            height=2,
            width=25
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.shortcut_label = tk.Label(
            self.button_frame,
            text="Shortcut:\nCtrl+Alt+Space",
            font=("Arial", 9),
            fg="#666"
        )
        self.shortcut_label.pack(side=tk.LEFT, padx=10)
        
        self.text_widget = tk.Text(self.root, font=("Consolas", 10), wrap=tk.WORD, state=tk.NORMAL)
        self.text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.running = True
        self.is_dragging = False
        
        self.setup_global_hotkey()
        
        self.print_message("=" * 50)
        self.print_message("Automatic Mouse Drag Program")
        self.print_message("=" * 50)
        self.print_message("")
        self.print_message("Press 'Start' button or use global shortcut:")
        self.print_message("  🔥 Ctrl + Alt + Space")
        self.print_message("")
        self.print_message("WARNING: This program will control the mouse!")
        self.print_message("To exit, quickly move mouse to screen corner (safety protection)")
        self.print_message("")
        
    def setup_global_hotkey(self):
        """Setup global keyboard shortcut"""
        try:
            keyboard.add_hotkey('ctrl+alt+space', self.start_drag)
            self.print_message("✓ Global hotkey registered: Ctrl+Alt+Space")
        except Exception as e:
            self.print_message(f"⚠ Hotkey setup failed: {e}")
    
    def start_drag(self):
        """Start drag operation when button clicked or hotkey pressed"""
        if self.is_dragging:
            self.print_message("")
            self.print_message("⚠ Drag operation already in progress...")
            return
        
        self.is_dragging = True
        self.start_button.config(state=tk.DISABLED, text="⏳ Running...")
        
        drag_thread = Thread(target=self.execute_drag)
        drag_thread.daemon = True
        drag_thread.start()
    
    def print_message(self, message):
        """Print message to text widget"""
        self.text_widget.insert(tk.END, message + "\n")
        self.text_widget.see(tk.END)
        self.root.update_idletasks()
    
    def clear_text(self):
        """Clear all text in widget"""
        self.text_widget.delete(1.0, tk.END)
    
    def close(self):
        """Close GUI window"""
        self.running = False
        self.root.destroy()
    
    def run(self):
        """Start GUI main loop"""
        self.root.mainloop()
    
    def execute_drag(self):
        """Execute mouse drag operation"""
        try:
            time.sleep(0.5)
            
            self.print_message("")
            self.print_message("=" * 50)
            self.print_message("Starting drag operation...")
            self.print_message("=" * 50)
            self.print_message("")
            self.print_message("Countdown: 3 seconds...")
            
            for i in range(3, 0, -1):
                self.print_message(f"  {i}...")
                time.sleep(1)
            
            screen_width, screen_height = pyautogui.size()
            half_screen_distance = screen_height // 2
            
            center_x = screen_width // 2
            current_y = pyautogui.position()[1]
            target_y = min(current_y + half_screen_distance, screen_height - 10)
            
            self.print_message("")
            self.print_message(f"Screen Resolution: {screen_width} x {screen_height}")
            self.print_message(f"Drag Distance: {half_screen_distance} pixels")
            self.print_message("")
            self.print_message(f"Step 1: Move to center ({center_x}, {current_y})")
            pyautogui.moveTo(center_x, current_y, duration=0.5, tween=pyautogui.easeInOutQuad)
            time.sleep(0.2)
            
            self.print_message(f"Step 2: Press left mouse button")
            pyautogui.mouseDown(button='left')
            time.sleep(0.1)
            
            self.print_message(f"Step 3: Drag down to ({center_x}, {target_y})")
            pyautogui.moveTo(center_x, target_y, duration=1.0, tween=pyautogui.easeInOutQuad)
            
            time.sleep(0.1)
            pyautogui.mouseUp(button='left')
            
            self.print_message("")
            self.print_message("✓ Drag completed!")
            self.print_message(f"Final position: {pyautogui.position()}")
            self.print_message("")
            self.print_message("=" * 50)
            self.print_message("Operation finished successfully!")
            self.print_message("=" * 50)
            
        except Exception as e:
            self.print_message("")
            self.print_message(f"❌ Error occurred: {str(e)}")
            self.print_message("")
            self.print_message("Please ensure you have necessary permissions.")
        
        finally:
            self.is_dragging = False
            self.root.after(100, self.reset_button)
    
    def reset_button(self):
        """Reset button state after operation completes"""
        self.start_button.config(state=tk.NORMAL, text="▶ Start (Ctrl+Alt+Space)")


def get_screen_height():
    """Get screen height"""
    try:
        sctx = screeninfo.get_monitors()[0]
        return sctx.height
    except:
        return pyautogui.size().height


def main():
    gui = MouseDragGUI()
    gui.run()


if __name__ == "__main__":
    main()
