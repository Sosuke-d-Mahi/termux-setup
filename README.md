# 🚀 Termux Dev Setup Automator

![Termux Setup Hero](https://raw.githubusercontent.com/Sosuke-d-Mahi/termux-setup/main/assets/hero.png)

**Transform your Termux into a professional-grade development environment with a single command.**

Tired of manually installing packages, configuring shells, and setting up themes every time you reset Termux? This automator handles the heavy lifting, giving you a beautiful, functional, and ready-to-code terminal in minutes.

---

## ✨ Features

- **⚡ One-Command Bootstrap:** Run `setup.sh` and watch the magic happen.
- **🎨 Aesthetic Zsh:** Automatically installs Zsh + Oh My Zsh with the stunning Powerlevel10k theme.
- **📦 Pre-configured Packages:** Installs Python, Node.js, Git, C/C++, and essential utilities out of the box.
- **🔗 Smart Aliases:** Includes productivity-boosting aliases like `update`, `ll`, and `gs`.
- **🛠 Fully Customizable:** Modify `config.json` to select exactly what you need.
- **📂 Storage Access:** Automatically handles `termux-setup-storage` permissions.

---

## ⚡ Quick Start

Open Termux and paste the following command:

```bash
pkg update && pkg upgrade -y && pkg install git -y && git clone https://github.com/Sosuke-d-Mahi/termux-setup.git && cd termux-setup && chmod +x setup.sh && ./setup.sh
```

---

## 🔧 Project Structure

| File | Purpose |
| :--- | :--- |
| `setup.sh` | The entry point script to bootstrap the environment. |
| `main.py` | The interactive menu and user interface. |
| `installer.py` | Core logic for package and environment setup. |
| `config.json` | Your personal setup configuration. |
| `requirements.txt`| Python dependencies for the beautiful CLI. |

---

## ⚙️ Customization

You can tailor the installation by editing `config.json` before running the setup:

```json
{
  "packages": [
    "git", "python", "nodejs", "zsh", "vim"
  ],
  "extras": {
    "oh_my_zsh": true,
    "powerlevel10k": true,
    "aliases": {
      "update": "pkg update && pkg upgrade -y"
    }
  }
}
```

---

## 📸 Screenshots

*(Mockup of the Interactive Menu)*
```text
+------------------------------------------+
|      🚀 Termux Dev Setup Automator       |
| Transform your Termux into a powerhouse  |
+------------------------------------------+
| 1. [Basic]   - Essentials only           |
| 2. [Full]    - Complete environment      |
| 3. [Custom]  - Load selective config     |
| 4. [Exit]    - Exit                      |
+------------------------------------------+
Select an option (1-4): _
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for new tool suggestions.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="center">
  Made with ❤️ for the Termux Community
</p>
