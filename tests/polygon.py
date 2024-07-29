import os
import sys

sys.path.insert(1, os.path.join(os.path.dirname(sys.path[0]), "src"))

from config import settings

print(settings.param_name)
