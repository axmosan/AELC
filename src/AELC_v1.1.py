import os
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk  # Pillowを使用して画像を読み込む

# ドキュメントフォルダのパス
documents_path = os.path.expanduser("~/Documents")
japanese_file = os.path.join(documents_path, "ae_force_japanese.txt")
english_file = os.path.join(documents_path, "ae_force_english.txt")

# Japaneseボタンが押されたときの処理
def set_japanese():
    if not os.path.exists(japanese_file):
        open(japanese_file, 'w').close()
    if os.path.exists(english_file):
        os.remove(english_file)
        open(japanese_file, 'w').close()
    root.destroy()

# Englishボタンが押されたときの処理
def set_english():
    if not os.path.exists(english_file):
        open(english_file, 'w').close()
    if os.path.exists(japanese_file):
        os.remove(japanese_file)
        open(english_file, 'w').close()
    root.destroy()

# メインウィンドウの設定
root = Tk()
root.title("AELC")  # ウィンドウタイトルを"AELC"に設定
root.geometry("300x200")
root.configure(bg='#1f1f1f')  # 背景色を#1f1f1fに設定

# アイコンの設定
icon_path = "C:/Users/axmo/Desktop/VSC/AX_Python/AELC/AELC_256x256.ico"
root.iconbitmap(icon_path)

# ウィンドウの最小サイズを設定（300x200に固定）
root.minsize(300, 200)

# ロゴ画像の読み込みと配置
logo_path = "C:/Users/axmo/Desktop/VSC/AX_Python/AELC/logo_100x100.png"
img = Image.open(logo_path)
img = img.resize((33, 33), Image.Resampling.LANCZOS)  # 画像サイズを1/3にリサイズ
logo_img = ImageTk.PhotoImage(img)

# ウィンドウサイズに応じてロゴを右下に配置する関数
def place_logo():
    logo_label.place(x=root.winfo_width() - 33, y=root.winfo_height() - 33)  # 右下に配置

# ロゴを配置するためのラベル
logo_label = Label(root, image=logo_img, bg='#1f1f1f')  # 背景色を合わせる
root.update_idletasks()  # ウィンドウのサイズを正確に取得
place_logo()  # ロゴを配置

# ウィンドウサイズ変更時にもロゴが常に右下に配置されるようにする
root.bind('<Configure>', lambda event: place_logo())

# ボタンのスタイル設定（アウトラインとボタン全体の設定）
button_style = {
    "bg": "#1f1f1f",
    "fg": "#EBEBEB",
    "width": 20,
    "height": 2,
    "relief": "flat",  # フラットな外観
    "highlightthickness": 2,  # アウトラインの太さを2pxに設定
    "highlightbackground": "#EBEBEB",  # アウトラインの色をEBEBEBに設定
    "highlightcolor": "#EBEBEB"  # ボタンがフォーカスされたときのアウトラインの色
}

# Japaneseボタンの配置
btn_japanese = Button(root, text="Japanese", command=set_japanese, **button_style)
btn_japanese.place(relx=0.5, rely=0.4, anchor='center')

# Englishボタンの配置
btn_english = Button(root, text="English", command=set_english, **button_style)
btn_english.place(relx=0.5, rely=0.6, anchor='center')

# GUIのループを開始
root.mainloop()
