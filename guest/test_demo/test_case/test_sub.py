# coding=utf-8
from count import Calculator
import unittest


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
    suit.addTest(TestSub("test_sub"))
    suit.addTest(TestSub("test_sub2"))
    
    runner = unittest.TextTestRunner()
    runner.run(suit)


# 单元/百盒测试的不难点不再“单元测试框架”本身
# 你能不能读懂开发的代码   