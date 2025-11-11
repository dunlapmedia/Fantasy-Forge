"""Build script for creating executables."""

import os
import sys
import subprocess
import platform


def build_executable():
    """Build executable for current platform."""
    print("Fantasy Forge - Build Script")
    print("=" * 50)
    print(f"Platform: {platform.system()}")
    print(f"Python: {sys.version}")
    print()

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller found")
    except ImportError:
        print("✗ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed")

    print()
    print("Building executable...")
    print("-" * 50)

    # Build command
    cmd = [
        "pyinstaller",
        "--name=Fantasy-Forge",
        "--windowed",
        "--onefile",
        "--clean",
        "run.py"
    ]

    # Add icon if available
    system = platform.system()
    if system == "Windows" and os.path.exists("icon.ico"):
        cmd.extend(["--icon=icon.ico"])
    elif system == "Darwin" and os.path.exists("icon.icns"):
        cmd.extend(["--icon=icon.icns"])

    # Add hidden imports
    cmd.extend([
        "--hidden-import=PyQt6",
        "--hidden-import=PyQt6.QtCore",
        "--hidden-import=PyQt6.QtWidgets",
        "--hidden-import=PyQt6.QtGui",
        "--hidden-import=requests",
    ])

    try:
        subprocess.check_call(cmd)
        print()
        print("=" * 50)
        print("✓ Build successful!")
        print()
        print(f"Executable location: dist/Fantasy-Forge{'.exe' if system == 'Windows' else ''}")
        print()
        print("To run the application:")
        if system == "Windows":
            print("  dist\\Fantasy-Forge.exe")
        else:
            print("  ./dist/Fantasy-Forge")
        print()
        print("Note: The executable can be distributed to users without Python installed.")
        print("      However, users will still need Ollama installed for AI features.")
        
    except subprocess.CalledProcessError as e:
        print()
        print("✗ Build failed!")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_executable()
