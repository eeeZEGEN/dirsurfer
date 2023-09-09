from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor
import sys as s


class CommonItem(QStandardItem):
	'''
	Common item class
	'''
	def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
		super().__init__()

		fnt = QFont('Open Sans', font_size)
		fnt.setBold(set_bold)

		self.setEditable(False)
		self.setForeground(color)
		self.setFont(fnt)
		self.setText(txt)


class Dirsurfer(QMainWindow):
	'''
	Main app class
	''' 
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Dirsurfer')
		self.resize(500, 900)

		treeView = QTreeView()
		treeView.setHeaderHidden(True)

		treeModel = QStandardItemModel()
		rootNode = treeModel.invisibleRootItem()

		some_dir = CommonItem('home', 16, set_bold=True)
		some_sec_dir = CommonItem('roman', 14)
		some_dir.appendRow(some_sec_dir)

		rootNode.appendRow(some_dir)

		treeView.setModel(treeModel)
		treeView.expandAll()
		self.setCentralWidget(treeView)

app = QApplication(s.argv)


dirsurfer = Dirsurfer()
dirsurfer.show()

s.exit(app.exec_())