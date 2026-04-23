import os
import json
import sys
import time
from installer import TermuxInstaller

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich.table import Table
    from rich import print as rprint
    USE_RICH = True
    console = Console()
except ImportError:
    USE_RICH = False

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "packages": ["git", "python", "curl"],
            "extras": {"oh_my_zsh": True}
        }

def show_banner():
    if USE_RICH:
        console.print(Panel.fit(
            "[bold blue]🚀 Termux Dev Setup Automator[/bold blue]\n"
            "[italic cyan]Transform your Termux into a powerhouse[/italic cyan]",
            border_style="magenta"
        ))
    else:
        print("=" * 40)
        print("  Termux Dev Setup Automator")
        print("=" * 40)

def show_menu():
    if USE_RICH:
        table = Table(title="Menu Options", show_header=True, header_style="bold green")
        table.add_column("Option", style="dim", width=6)
        table.add_column("Setup Type")
        table.add_column("Description")
        
        table.add_row("1", "Basic", "Essentials only (Git, Python)")
        table.add_row("2", "Full", "Complete environment (Node, Zsh, Theme)")
        table.add_row("3", "Custom", "Load from config.json")
        table.add_row("4", "Exit", "Close the automator")
        
        console.print(table)
    else:
        print("1. [Basic]   - Essentials only")
        print("2. [Full]    - Complete environment")
        print("3. [Custom]  - Load selective config")
        print("4. [Exit]    - Exit")

def play_animation():
    if not os.path.exists("ascii-animation.txt"):
        return

    try:
        with open("ascii-animation.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        frames = []
        for i in range(0, len(lines), 100):
            frames.append("".join(lines[i:i+100]))

        for frame in frames:
            sys.stdout.write("\033[H") # Move cursor to top-left
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(0.05)
        
        time.sleep(0.5)
        os.system("clear")
    except Exception as e:
        pass

def main():
    play_animation()
    config = load_config()
    installer = TermuxInstaller()
    
    while True:
        os.system("clear")
        show_banner()
        show_menu()
        
        if USE_RICH:
            choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4"], default="1")
        else:
            choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            rprint("[yellow]Starting Basic Setup...[/yellow]") if USE_RICH else print("Starting Basic...")
            installer.install_packages(["git", "python", "curl"])
        
        elif choice == "2":
            rprint("[green]Starting Full Setup... This may take a while.[/green]") if USE_RICH else print("Starting Full Setup...")
            installer.install_full_environment(config)
        
        elif choice == "3":
            rprint(f"[cyan]Installing custom packages from config: {', '.join(config['packages'])}[/cyan]") if USE_RICH else print("Installing Custom...")
            installer.install_packages(config["packages"])
        
        elif choice == "4":
            rprint("[bold red]Exiting... Happy coding![/bold red]") if USE_RICH else print("Exiting...")
            break
        
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
