#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for simple filters."""

import unittest
import test_filterbase

from simplefilters import (
    NaiveFilter,
    ParanoidFilter,
    RandomFilter)


class NaiveFilterTest(test_filterbase.BaseFilterTestCase):
    
    def setUp(self):
        super().setUp()
        # Set an instance of the NaiveFilter class for the test
        self.filter = NaiveFilter()


class ParanoidFilterTest(test_filterbase.BaseFilterTestCase):
    
    def setUp(self):
        super().setUp()
        # Set an instance of the ParanoidFilter class for the test
        self.filter = ParanoidFilter()


class RandomFilterTest(test_filterbase.BaseFilterTestCase):
    
    def setUp(self):
        super().setUp()
        # Set an instance of the RandomFilter class for the test
        self.filter = RandomFilter()


if __name__ == '__main__':
    unittest.main(exit=False)