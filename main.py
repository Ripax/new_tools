import sys

sys.path.append('/Users/rion/Github/new_tools')


from PySide2.QtWidgets import *
from NukeInfo import Ui_Form
import  nukescripts 
import datetime


username = os.getlogin()
v_string = nuke.NUKE_VERSION_STRING



class window(Ui_Form, QWidget):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(("Nuke Script Information for TD : ({x})").format(x=username))
        self.pushButton_welcome.released.connect(self.Welcome)
        self.pushButton_date.released.connect(self._date)
        self.pushButton_root.released.connect(self._root)
        self.pushButton_nk_version.released.connect(self._version)
        
          
    # Button Welcome

    def Welcome(self):
        self.label.setText('')
        self.label.setText('You pressed pushButton_welcome')

    # Button Welcome

    def _date(self):
        time = datetime.datetime.now()
        self.label.setText('')
        self.label.setText('Now Time is : {}'.format(time))

# Button Root

    def _root(self):
        userinput = self.lineEdit_class.text()
        with nuke.root():
            node_count = 0
            for node in nuke.allNodes():
                if node.Class() == userinput:
                    node_count += 1
            return node_count   
        nodes_Name = node_count()
        self.label.setText('')
        self.label.setText('Updated : {} Copy Node In this Script. '.format(nodes_Name) )

    # Button Version

    def _version(self):
        self.label.setText('')
        self.label.setText("{u} you are running Nuke{v} version".format(u=username, v=v_string))

# Added into Nuke Panel
nukescripts.registerWidgetAsPanel('window', 'Nuke Script Information for TD : ({x})'.format(x=username), 'uk.co.thefoundry.window', True)


# For widgets
#if __name__ == '__main__':
#    widgets = window()
#    widgets.show()

