# 🗒️ NoteMan

A clean, retro-styled command-line notes manager — made for fun, built in Python.

![NoteMan Screenshot](https://files.catbox.moe/4l1few.png)

---

## 📌 What is NoteMan?

**NoteMan** is a simple terminal-based note tool. It lets you:

- ✍️ Write notes  
- 📄 View your saved notes  
- 📋 List all notes  
- 🧽 Edit or delete specific notes  
- 🚨 Use **panic mode** to clear **everything** in one go  

Your notes are stored locally inside a `storage/` directory.  
No internet. No cloud. No nonsense.

---

## 🔧 Features

| Command      | Description                              |
|--------------|------------------------------------------|
| `note write`      | Create a new note                        |
| `note view`       | View a specific note                     |
| `note list`       | See all saved notes                      |
| `note delete`     | Delete a note by its name                |
| `note edit`       | Edit an existing note                    |
| `panic`      | 💣 Wipe **all** your notes immediately    |
| `setup`      | First-time setup — installs dependencies |

---

## 📸 Screenshots

| Home Page | Write Mode | List Mode |
|------------|-----------|-------|
| ![Home](https://files.catbox.moe/4l1few.png) | ![Write](https://files.catbox.moe/o9flgb.png) | ![List](https://files.catbox.moe/6wolr2.png) |

---

## 🚀 Installation & Usage

> 📌 You only need Python 3 and Git installed initially.

### 1. Clone the repository

```bash
git clone https://github.com/TheDesiignerr/NoteMan
cd NoteMan
```

### 2. Run NoteMan

```bash
python3 main.py
```

### 3. Inside NoteMan, type:

```bash
setup
```

- It will auto-install or update Git (asks for `sudo` if needed).  
- Prepares everything so you're ready to go.  
- Then start writing notes with `note write`, list them with `note list`, etc.

---

## 📁 Local Note Storage

All notes are saved as `.txt` files inside a local `storage/` directory.

You can back it up, or wipe it with `panic` mode if needed.

---

## 🤷 Why?

Honestly? No deep reason.  
Just built for fun, for people who enjoy working in the terminal.

---

## 🧑‍💻 Author

Made by [TheDesiignerr](https://github.com/TheDesiignerr)  
Powered by **Python 3**, `colorama`, and terminal energy ⚡

---

## 🪪 License

MIT License — free to use, fork, modify, or obliterate.
