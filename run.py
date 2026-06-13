import platform
import os
import sys
import socket
import subprocess

# Colors
R = '\033[38;5;196m'
W = '\033[97m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
B = '\033[94m'
M = '\033[95m'
N = '\033[0m'

BANNER = f"""
{R}╔{'═'*50}╗
{R}║{W}   ██████╗ ███████╗███╗   ██╗███████╗ ██████╗      {R}║
{R}║{W}   ██╔══██╗██╔════╝████╗  ██║╚══███╔╝██╔═══██╗     {R}║
{R}║{W}   ██████╔╝█████╗  ██╔██╗ ██║  ███╔╝ ██║   ██║     {R}║
{R}║{W}   ██╔══██╗██╔══╝  ██║╚██╗██║ ███╔╝  ██║   ██║     {R}║
{R}║{W}   ██████╔╝███████╗██║ ╚████║███████╗╚██████╔╝     {R}║
{R}║{W}   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝      {R}║
{R}║{W}               ═══ X EDITION ═══                    {R}║
{R}║{G}        Facebook Cracker | File Cracker | Token Tool  {R}║
{R}║{Y}           Author: BENZO | Version: 1.0              {R}║
{R}╚{'═'*50}╝{N}
"""

def check_dependencies():
    """Check and auto-install dependencies."""
    deps = ['requests', 'bs4', 'mechanize', 'rich', 'colorama', 'cloudscraper']
    missing = []
    for d in deps:
        try:
            __import__(d.replace('-', '_'))
        except ImportError:
            missing.append(d)
    
    if missing:
        print(f'{Y}[!] Installing missing dependencies: {", ".join(missing)}{N}')
        for d in missing:
            os.system(f'pip install {d} -q')
    
    print(f'{G}[✓] All dependencies satisfied{N}')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    
    print(f'{C}[i] Checking system...{N}')
    arch = platform.architecture()
    
    # Check for updates (optional, won't fail if no git)
    try:
        os.system('git pull --quiet 2>/dev/null')
    except:
        pass
    
    print(f'{G}[✓] System: {arch[0]}{N}')
    print(f'{C}[i] Loading BENZO-X engine...{N}')
    
    check_dependencies()
    
    # Import and run the main engine
    try:
        from core import engine
        engine.run()
    except ImportError as e:
        print(f'{R}[!] Error loading engine: {e}{N}')
        print(f'{Y}[!] Make sure core/engine.py exists{N}')
        sys.exit(1)
    except Exception as e:
        print(f'{R}[!] Unexpected error: {e}{N}')
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
