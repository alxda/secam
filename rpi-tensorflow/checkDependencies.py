print("Checking dependencies")

modules = set(["numpy", "os", "six.moves.urllib", "sys", "tarfile", "tensorflow", "zipfile", "cv2", "collections", "io", "matplotlib", "PIL", "utils"])

for module in modules:
    try:
        __import__(module)
    except ImportError:
        print("{0} not found".format(module))