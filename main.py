import sys

sys.path.append('/Users/rion/Github/new_tools')


from PySide2.QtWidgets import *
from NukeInfo import Ui_Form
import  nukescripts 

username = os.getlogin()
v_string = nuke.NUKE_VERSION_STRING


class window(Ui_Form, QWidget):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(("QrCode v1.0.5 using by ({x})").format(x=username))
        self.pushButton_welcome.released.connect(self.Welcome)
        self.pushButton_date.released.connect(self._date)
        self.pushButton_root.released.connect(self._force_update_all)
        self.pushButton_nk_version.released.connect(self._version)
        
          
    # Button Welcome

    def Welcome(self):
        print("You pressed pushButton_welcome")

    # Button Welcome

    def _date(self):
        print("You pressed date")

# Button Root
    def _root(self):
        root_path = nuke.root().name()
        root_path = root_path.split('/')[-1]
        print(root_path)
    # Button Version

    def _version(self):
        print("{u} you are running Nuke{v} version".format(u=username, v=v_string))

    def _force_update_all(self):
        with nuke.root():
            node_count = 0
            for node in nuke.allNodes():
                if node.Class() == "Copy":
                    node_count += 1

            nuke.message("Updated : %s Copy Node In this Script." % node_count) 

# Added into Nuke Panel
nukescripts.registerWidgetAsPanel('window', 'Nuke info Panel', 'uk.co.thefoundry.window', True)


# For widgets
if __name__ == '__main__':
    widgets = window()
    widgets.show()

