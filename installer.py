import subprocess
import os
import json
import time

class TermuxInstaller:
    def __init__(self):
        self.home = os.path.expanduser("~")
        self.config_path = "config.json"

    def run(self, cmd, shell=True):
        try:
            print(f"  > Executing: {cmd}")
            subprocess.run(cmd, shell=shell, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error: Command failed with return code {e.returncode}")
            return False

    def update_system(self):
        print("🔄 Updating Termux repositories...")
        self.run("pkg update && pkg upgrade -y")

    def install_packages(self, packages):
        print(f"📦 Installing {len(packages)} packages...")
        for pkg in packages:
            print(f"   Installing {pkg}...")
            self.run(f"pkg install {pkg} -y")

    def setup_zsh(self):
        print("🎨 Setting up Zsh & Oh My Zsh...")
        self.run("pkg install zsh -y")
        
        omz_dir = os.path.join(self.home, ".oh-my-zsh")
        if not os.path.exists(omz_dir):
            print("   Installing Oh My Zsh...")
            self.run('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
        else:
            print("   Oh My Zsh is already installed.")

        print("   Changing default shell to Zsh...")
        self.run("chsh -s zsh")

    def setup_p10k(self):
        print("✨ Setting up Powerlevel10k theme...")
        p10k_dir = os.path.join(self.home, ".oh-my-zsh/custom/themes/powerlevel10k")
        if not os.path.exists(p10k_dir):
            self.run(f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {p10k_dir}")
            zshrc = os.path.join(self.home, ".zshrc")
            if os.path.exists(zshrc):
                with open(zshrc, "r") as f:
                    content = f.read()
                content = content.replace('ZSH_THEME="robbyrussell"', 'ZSH_THEME="powerlevel10k/powerlevel10k"')
                with open(zshrc, "w") as f:
                    f.write(content)
        else:
            print("   Powerlevel10k is already installed.")

    def setup_aliases(self, aliases):
        print("🔗 Setting up aliases...")
        bashrc = os.path.join(self.home, ".bashrc")
        zshrc = os.path.join(self.home, ".zshrc")
        
        alias_str = "\n"
        for alias, cmd in aliases.items():
            alias_str += f"alias {alias}='{cmd}'\n"
        
        for rc in [bashrc, zshrc]:
            if os.path.exists(rc):
                with open(rc, "a") as f:
                    f.write(alias_str)

    def setup_storage(self):
        print("📁 Requesting storage permissions...")
        self.run("termux-setup-storage")

    def install_full_environment(self, config):
        self.update_system()
        self.install_packages(config.get("packages", []))
        
        if config.get("extras", {}).get("oh_my_zsh"):
            self.setup_zsh()
            if config.get("extras", {}).get("powerlevel10k"):
                self.setup_p10k()
        
        if "aliases" in config.get("extras", {}):
            self.setup_aliases(config["extras"]["aliases"])
        
        self.setup_storage()
        print("\n✅ Full Environment Setup Complete!")

def install_packages(packages):
    installer = TermuxInstaller()
    installer.install_packages(packages)

def setup_zsh():
    installer = TermuxInstaller()
    installer.setup_zsh()
