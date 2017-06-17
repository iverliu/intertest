#coding=utf-8
import unittest


suit = unittest.defaultTestLoader.discover("./ccc", "*_aaa.py")


runner = unittest.TextTestRunner()
runner.run(suit)


#  discover() == unittest.main()