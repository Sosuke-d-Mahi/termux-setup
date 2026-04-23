#!/bin/bash

echo "🚀 Preparing Termux environment..."

pkg update && pkg upgrade -y

pkg install git python -y

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "✨ Launching Automator..."
python main.py
