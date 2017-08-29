import unittest
from ooptask2 import Node, LinkedList, MyValueError


class LinkedListTest(unittest.TestCase):
    
    def setUp(self):       
        self.lists = [ LinkedList(), LinkedList() ]
        for n in range(7, 0, -1):
            self.lists[0].add_front(n)
            
        for c in ('e', 'd', 'c', 'b', 'a'):
            self.lists[1].add_front(c)

        print ("setUp executed!")

    def testAdd_front(self):
        self.assertEqual(self.lists[0].get(0), 1)
        self.assertEqual(self.lists[1].get(0), 'a')
        
    def testAppend(self):
        self.lists[0].append(8)
        self.lists[1].append("f")
        self.assertEqual(self.lists[0].get(7), 8)
        self.assertEqual(self.lists[1].get(5), 'f')
        
    def testGet(self):
        self.assertEqual(self.lists[0].get(2), 3)
        self.assertEqual(self.lists[1].get(4), 'e')
        
    def testPut(self):
        self.lists[0].put(1, 0)
        self.assertEqual(self.lists[0].get(1), 0)
        self.assertEqual(self.lists[0].get(0), 1)
        self.assertEqual(self.lists[0].get(2), 2)
        
        self.assertRaises(MyValueError, self.lists[1].put, 0, 'a')
        
    def testSize(self):
        self.assertEqual(self.lists[0].size(), 7)
        self.assertEqual(self.lists[1].size(), 5)
        
    def testIndexOf(self):
        self.assertEqual(self.lists[0].indexOf(4), 3)
        self.assertEqual(self.lists[1].indexOf("c"), 2)
        
    def testDelete(self):
        self.lists[0].delete(3)
        self.assertEqual(self.lists[0].get(2), 3)
        self.assertEqual(self.lists[0].get(3), 5)

    def tearDown(self):
        self.lists = None
        print ("tearDown executed!")






if __name__ == "__main__": 
    unittest.main()
