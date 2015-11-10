import sys, os, re, unittest


def regressiontest():
    path = os.getcwd()
    sys.path.append(path)
    files = os.listdir(path)
