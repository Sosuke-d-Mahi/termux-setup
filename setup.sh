#!/bin/bash

# Termux Dev Setup Bootstrapper
# This script prepares the environment for the Python automator

echo "🚀 Preparing Termux environment..."

# 1. Update system
pkg update && pkg upgrade -y

# 2. Install core requirements
pkg install git python -y

# 3. Create project directory if it doesn't exist
# (Assuming the user has already cloned or downloaded the files)
# If they are running this script alone, we can clone for them.

# 4. Install Python requirements
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# 5. Launch the main automator
echo "✨ Launching Automator..."
python main.py
