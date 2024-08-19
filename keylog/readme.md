python -m venv myenv
source myenv/bin/activate  # (trên Linux/macOS)
myenv\Scripts\activate      # (trên Windows)

pip install pyinstaller
pip install pynput


<!-- python3 -m PyInstaller main.py -->

<!-- python3 setup.py py2app -->

pyinstaller --onefile --noconsole main.py