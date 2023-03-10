import sys
sys.path.insert(0, 'gui/')
from gui.window import MyWindow
from db.database import Data

data = Data()
data.create_connection()
data.insert("https://docs.python.org/3/library/sqlite3.html")
print(data.select())
data.close()
