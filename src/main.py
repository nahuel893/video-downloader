import sys
sys.path.insert(0, 'gui/')
from gui.window import MyWindow
from db.database import Data

window = MyWindow()
window.run()
