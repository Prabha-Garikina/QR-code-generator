import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
import pyshorteners

def generate_qr_code():
    url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(short_url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("qrcode.png")
    load = Image.open("qrcode.png")
    render = ImageTk.PhotoImage(load)
    img_label = tk.Label(image=render)
    img_label.image = render
    img_label.pack(pady=30)

def save_as_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png")
    img = qrcode.make(entry.get())
    img.save(filename)

root =tk.Tk()
root.title("QR Code Generator")
root.configure(bg="#f0f0f0")

heading = tk.Label(root, text="QR Code Generator", bg="#f0f0f0", fg="#000000", font=("Arial", 20))
heading.pack(pady=20)

label = tk.Label(root, text="Enter URL:", bg="#f0f0f0", fg="#000000")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=30)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

generate_button = tk.Button(button_frame, text="Generate QR Code", command=generate_qr_code, bg="#4CAF50", fg="#ffffff")
generate_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(button_frame, text="Save as Image", command=save_as_image, bg="#4CAF50", fg="#ffffff")
save_button.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()