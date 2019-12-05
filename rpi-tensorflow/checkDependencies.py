print("Checking dependencies")

import sys
print(sys.version)

modules = set(["numpy", "os", "six.moves.urllib", "sys", "tarfile", "tensorflow", "zipfile", "cv2", "collections", "io", "matplotlib", "PIL", "object_detection.utils", "utils"])

for module in modules:
    try:
        __import__(module)
    except ImportError:
        print("{0} not found".format(module))