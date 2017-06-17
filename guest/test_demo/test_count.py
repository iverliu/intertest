# coding=utf-8
from count import Calculator
import unittest


# 测试类一定要继承unittest.TestCase
class TestAdd(unittest.TestCase):

    # 在每一条用例开始前执行
    def setUp(self):
        print("start test:")
        #dr = webdriver.Firefox()
        #初始化接口测试数据，base_url

    # 在每一条用例结束时执行
    def tearDown(self):
        print("end test.")
        #dr.quit()

    # 测试方法的命名一定要以"test"开头
    def test_add(self):
        c = Calculator(3, 5)
        self.assertEqual(c.add(), 8)
        print("add")

    def test_add2(self):
        c = Calculator(3, 5)
        self.assertEqual(c.add(), 8)
        print("add2")


class TestSub(unittest.TestCase):

    def test_sub(self):
        c = Calculator(3, 5)
        self.assertEqual(c.sub(), -2)
        print("sub")

    def test_sub2(self):
        c = Calculator(3, 5)
        self.assertEqual(c.sub(), -2)
        print("sub2")


if __name__ == "__main__":
    #unittest.main()  # 执行用例的顺序？ 
    
    # 测试套件：运行一组测试的集合
    suit = unittest.TestSuite()
    #suit.addTest(TestSub("test_sub"))
    #suit.addTest(TestSub("test_sub2"))
    suit.addTest(TestAdd("test_add2"))
    suit.addTest(TestAdd("test_add"))
    
    runner = unittest.TextTestRunner()
    runner.run(suit)

