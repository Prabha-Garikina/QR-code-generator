# QR Code Generator 🔗📱

A simple desktop GUI application built with **Python** and **Tkinter** that generates QR codes from any URL or text input, previews them instantly, and lets you save them as image files.

This repository includes two versions of the tool:

| File | Description |
|------|-------------|
| `generate_qrcode1.py` | Basic QR code generator — enter a URL, generate and preview the QR code, and save it as an image. |
| `generte_qrcoe.py` | Extended version that additionally **shortens the URL** (via TinyURL) before encoding it into the QR code, making the generated code cleaner and easier to scan. |

---

## ✨ Features

- 🖥️ Simple, clean Tkinter GUI
- 🔗 Generate a QR code from any URL or text
- 🔗 (v2) Automatic URL shortening using TinyURL before QR generation
- 🖼️ Live preview of the generated QR code inside the app
- 💾 Save the QR code as a `.png` image anywhere on your system

---

## 📦 Requirements

- Python 3.7+
- [`qrcode`](https://pypi.org/project/qrcode/)
- [`Pillow`](https://pypi.org/project/Pillow/) (PIL)
- [`pyshorteners`](https://pypi.org/project/pyshorteners/) — required only for `generte_qrcoe.py`

Install dependencies:

```bash
pip install qrcode[pil] Pillow pyshorteners
```

---

## 🚀 Usage

### Basic version

```bash
python generate_qrcode1.py
```

1. Enter a URL or text in the input field.
2. Click **Generate QR Code** to create and preview it.
3. Click **Save as Image** to save the QR code as a `.png` file.

### Version with URL shortening

```bash
python generte_qrcoe.py
```

Works the same way, but the entered URL is first shortened via TinyURL before being encoded into the QR code.

> **Note:** URL shortening requires an active internet connection.

---

## 🗂️ Project Structure

```
.
├── generate_qrcode1.py   # Basic QR code generator
├── generte_qrcoe.py      # QR code generator with URL shortening
└── README.md
```

---

## 🛠️ Possible Improvements

- Merge both versions into a single app with a toggle for URL shortening.
- Add input validation for empty fields or invalid URLs.
- Add support for custom QR code colors, logos, or error-correction levels.
- Fix the unused scrollbar widget in `generte_qrcoe.py`.
- Rename `generte_qrcoe.py` to fix the typo for clarity (`generate_qrcode2.py`).

---

## 📄 License

This project is open source — feel free to use, modify, and distribute it.
