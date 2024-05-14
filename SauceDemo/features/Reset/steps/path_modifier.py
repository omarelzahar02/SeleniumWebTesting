import os
import sys

def modify_sys_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while os.path.basename(current_dir) != "SeleniumWebTesting":
        current_dir = os.path.dirname(current_dir)

    sys.path.append(current_dir)