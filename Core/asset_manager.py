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