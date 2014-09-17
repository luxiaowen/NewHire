import unittest
import checkurl

class checkurlTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def testNotFound(self):
        notFoundList=('http://www.hust.edu.cn/asdfdf/',
            'http://www.seu.edu.cn/asdd/',
            'http://www.hust.edu.cn/dfd/')
        for weburl in notFoundList:
            self.assertEqual(checkurl.checkurl(weburl),True,'test 404 failed')
##        self.assertEqual(checkurl.checkurl('http://www.hust.edu.cn/asdfdf/'),True,'test 404 failed')
        
    def testFound(self):
        foundList=('http://www.baidu.com',
            'http://www.sohu.com',
            'http://www.sina.com')
        for weburl in foundList:
            self.assertEqual(checkurl.checkurl(weburl),False,'test 200 failed')
##        self.assertEqual(checkurl.checkurl('http://www.baidu.com'),False,'test 200 failed')
        
if __name__=='__main__':
    unittest.main()
