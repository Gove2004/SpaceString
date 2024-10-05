import tkinter as tk


version = "SpaceString by Gove v1.2"
"""
开发日志:
2024/10/03
    1.0: 完成基本功能, 支持ascii编码.
2024/10/05
    1.1: 支持utf-8编码, 增加右键复制粘贴清除快捷功能.
"""


space_0 = 0x180e  # 6158
space_1 = 0x200b  # 8203
length = 32


def string_to_space(string: str):
    out = ""
    for s in string:
        if s == "\n":
            continue
        o = ord(s)
        s = bin(o)[2:].zfill(length)
        for b in s:
            if b == "0":
                out += chr(space_0)
            elif b == "1":
                out += chr(space_1)
    return out


def space_to_string(space: str):
    out = ""
    b = ""
    for s in space:
        if s == "\n":
            continue
        if s != chr(space_0) and s != chr(space_1):
            out += s
        if s == chr(space_0):
            b += "0"
        elif s == chr(space_1):
            b += "1"
        if len(b) == length:
            out += chr(int("0b"+b, 2))
            b = ""
    return out

  
def main():
    root = tk.Tk()
    root.title(version)
    root.resizable(False, False)

    string_var = tk.StringVar()
    space_var = tk.StringVar()

    tk.Label(root, text="String:").grid(row=0, column=0)
    tk.Label(root, text="Space:").grid(row=1, column=0)

    def on_right_click(event, entry: tk.Entry):
        right_click_menu = tk.Menu(root, tearoff=0)
        right_click_menu.add_command(label="Paste", command=lambda: entry.insert(tk.END, root.clipboard_get()))
        right_click_menu.add_command(label="Copy", command=lambda: entry.clipboard_append(entry.get()))
        right_click_menu.add_command(label="Clear", command=lambda: entry.delete(0, tk.END))
        right_click_menu.post(event.x_root, event.y_root) 

    string_entry = tk.Entry(root, textvariable=string_var)
    string_entry.bind("<Button-3>", lambda event: on_right_click(event, string_entry))
    string_entry.grid(row=0, column=1)

    space_entry = tk.Entry(root, textvariable=space_var)
    space_entry.bind("<Button-3>", lambda event: on_right_click(event, space_entry))
    space_entry.grid(row=1, column=1)

    tk.Button(root, text="Encode", command=lambda: space_var.set(string_to_space(string_var.get()))).grid(row=0, column=2)
    tk.Button(root, text="Decode", command=lambda: string_var.set(space_to_string(space_var.get()))).grid(row=1, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()
