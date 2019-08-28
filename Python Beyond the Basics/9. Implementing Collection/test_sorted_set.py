# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:37:02 2019

@author: Saravanakumar
"""

import unittest

from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):
    
    def test_empty(self):
        s = SortedSet([])
        
    def test_from_sequence(self):
        s = SortedSet([12,31,23,123])
        
    def test_with_duplicates(self):
        s = SortedSet([1,2,1,2,2,1])
    
    def test_from_iterable(self):
        def gen():
            yield 4
            yield 5
            yield 6
            yield 7
            g = gen()
            s = SortedSet(g)
    
    def test_default_empty(self):
        s = SortedSet()
        
class TestContainerProtocol(unittest.TestCase):
    
    def setUp(self):
        self.s = SortedSet([2,5,3,4,9,47])
        
    def test_positive_contained(self):
        self.assertTrue(3 in self.s)
        
    def test_negative_contained(self):
        self.assertFalse(54 in self.s)
        
    def test_positive_not_contained(self):
        self.assertTrue(54 not in self.s)
        
    def test_negative_not_contained(self):
        self.assertFalse(5 not in self.s)
        
class TestSizedProtocol(unittest.TestCase):
    
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)
        
    def test_one(self):
        s = SortedSet([23])
        self.assertEqual(len(s), 1)
        
    def test_with_duplicates(self):
        s = SortedSet([1,1,3,12,12])
        self.assertEqual(len(s), 3)
        
    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)
        
class TestIterableProtocol(unittest.TestCase):
    
    def setUp(self):
        self.s = SortedSet([23,4,234,2,234,23])
        
    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 4)
        self.assertEqual(next(i), 23)
        self.assertEqual(next(i), 234)
        self.assertRaises(StopIteration, lambda:next(i))
        
    def test_for_loop(self):
        index = 0
        expected = [2,4,23,234]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1
        
class TestIndexProtocol(unittest.TestCase):
    
    def setUp(self):
        self.s = SortedSet([1,6,9,23,33])
        
    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)
        
    def test_index_four(self):
        self.assertEqual(self.s[4], 33)
        
    def test_index_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]
    
    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 33)
        
    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)
        
    def test_index_one_before_the_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]
    
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1,6,9]))
        
    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedSet([23,33]))
        
    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet([]))
        
    def test_slice_arbitary(self):
        self.assertEqual(self.s[1:3], SortedSet([6,9]))
        
    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)
        
    def test_reversed(self):
        s = SortedSet([1,3,5,7])
        r = reversed(s)
        self.assertEqual(next(r), 7)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 1)
        with self.assertRaises(StopIteration):
            next(r)
            
    def test_index_positive(self):
        s = SortedSet([1,5,8,9])
        self.assertEqual(s.index(8), 2)
        
    def test_index_negative(self):
        s = SortedSet([1,5,8,9])
        with self.assertRaises(ValueError):
            s.index(34)
        
    def test_count_zero(self):
        s = SortedSet([1, 5, 7, 9])
        self.assertEqual(s.count(11), 0)
        
    def test_count_one(self):
        s = SortedSet([1,5,7,9])
        self.assertEqual(s.count(7), 1)
        
        
    
class TestReprProtocol(unittest.TestCase):
    
    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), 'SortedSet()')

    def test_repr_some(self):
        s = SortedSet([23,4,234])
        self.assertEqual(repr(s), 'SortedSet([4, 23, 234])')
    
class TestEqualityProtocol(unittest.TestCase):
    
    def test_positive_equal(self):
        self.assertTrue(SortedSet([4,5,6]) == SortedSet([6,5,4]))
    
    def test_negative_equal(self):
        self.assertFalse(SortedSet([23,4,234]) == SortedSet([23,4,23,4]))
        
    def test_type_mismatch(self):
        self.assertFalse(SortedSet([4,5,6]) == [4,5,6])
        
    def test_identical(self):
        s = SortedSet([23,4,234])
        self.assertTrue(s == s)
        
    
        
if __name__ == '__main__':
    unittest.main()
