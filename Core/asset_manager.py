import os, sys, subprocess, threading
proj_root = os.getcwd()
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)
from Utils.qt_utility import displayMessageBox

class AssetManager:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

        from Resources.UI.ui_main_window import Ui_MainWindow
        self.ui: Ui_MainWindow = self.mainWindow.ui

        # self.ui.listWidget.itemClicked.connect(self.onItemClicked)
        # self.ui.listWidget.itemDoubleClicked.connect(self.onItemDoubleClicked)

    def onItemClicked(self, item):
        print(item.text())

    def onItemDoubleClicked(self, item):
        print(item.text())

class Test:
    @staticmethod
    def test():
        # set dir
        bin_folder = r'D:\SteamLibrary\steamapps\common\Call of Duty World at War\bin'
        os.chdir(bin_folder)
        script_path = os.path.join(bin_folder, 'converter.exe')
        

        process = subprocess.Popen(
            [script_path, '-nopause', '-single', r'material', 'test_material'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True,  # Use universal_newlines or text for real-time streaming
            bufsize=1   # Line-buffered output
        )

        def capture_output(stream):
            for line in iter(stream.readline, ''):
                if line:
                    print(line, end='')

        # Start separate threads to capture stdout and stderr
        threading.Thread(target=capture_output, args=(process.stdout,), daemon=True).start()
        threading.Thread(target=capture_output, args=(process.stderr,), daemon=True).start()

        process.wait()  # Wait for the process to complete

if __name__ == '__main__':
    Test.test()