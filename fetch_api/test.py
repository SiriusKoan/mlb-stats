import json
from main import *

r = Updater(2000)
r.insert_to_db()
# with open("test.json", "w") as f:
    # json.dump(r.get_all(), f, indent=4)
