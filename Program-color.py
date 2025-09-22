import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor(title="เลือกสีพื้นหลัง")
    if color[1]:
        set_bg(color[1])
def set_bg(hex_color):
    root.configure(bg=hex_color)
    current_color_var.set(f"สีปัจจุบัน:{hex_color}")
    label_info.configure(bg=hex_color)
    entry_hex.configure(bg="white")

    for btn in preset_buttons:
        btn.configure(relief="raised")

def apply_hex():
    hex_val = entry_hex.get().strip()
    if hex_val:
        if not hex_val.startswith("#"):
            hex_val = "#" + hex_val

        if len(hex_val) in (4,7):
            try:
                root.winfo_rgb(hex_val)
                set_bg(hex_val)
            except th.TclError:
                current_color_var.set("รูปแบบสีไม่ถูกต้อง")
        else:
            current_color_var.set("รูปแบบสีไม่ถูกต้อง (เช่น #RRGGBB)")
            
root = tk.Tk()
root.title("ตัวอย่าง: เปลี่ยนสีพื้นหลัง (Color Chooser)")
root.geometry("480x260")
root.configure(bg="#f0f0f0")

current_color_var = tk.StringVar(value="สีปัจจุบัน: #f0f0f0")
label_info = tk.Label(root, textvariable=current_color_var, font=("Segoe UI", 12), bg="#f0f0f0")
label_info.pack(pady=(12,8))

btn_choose = tk.Button(root, text="เลือกสีด้วย Color Chooser...", command=choose_color)
btn_choose.pack(pady=6)

frm_hex = tk.Frame(root, bg=root["bg"])
frm_hex.pack(pady=8)
entry_hex = tk.Entry(frm_hex,width=18)
entry_hex.insert(0, "#ffffff")
entry_hex.grid(row=0, column=0, padx=(0,6))
btn_apply = tk.Button(frm_hex, text="ใช้คำนี้เป็นพื้นหลัง", command=apply_hex)
btn_apply.grid(row=0, column=1)

preset_colors = ["#FFFFFF", "#FFCCCC", "#CCE5FF", "#CCFFCC", "#FFF2CC", "#E0CCFF", "#333333"]
preset_frame = tk.LabelFrame(root, text="สีสำเร็จรูป", padx=10, pady=8, bg=root["bg"])
preset_frame.pack(pady=10, fill="x", padx=12)

preset_buttons = []
for i, c in enumerate(preset_colors):
    b = tk.Button(preset_frame, bg=c, width=6, command=lambda col=c:set_bg(col))
    b.grid(row=0, column=i, padx=4)
    preset_buttons.append(b)

def reset_default():
    set_bg("#f0f0f0")
reset_btn = tk.Button(root, text="รีเซ็ตเป็นค่าเริ่มต้น", command=reset_default)
reset_btn.pack(pady=(6,12))
########colorchooser########

root.mainloop()
