import json
from main import *

r = Updater(2021)
with open("test.json", "w") as f:
    json.dump(r.get_all(), f, indent=4)
