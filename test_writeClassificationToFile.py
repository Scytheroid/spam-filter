#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test the write_classification_to_file() function."""

import os
import unittest
import random
from contextlib import contextmanager
import builtins
import warnings
import io

from utils import write_classification_to_file

FNAME_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'
REFERENCENAME = '!delete_this_reference.txt'
FILENAME = '!delete_me.txt'
HAM_TAG = 'OK'
SPAM_TAG = 'SPAM'
EMAIL_CLASSES = (HAM_TAG, SPAM_TAG)

class WriteClassificationTest(unittest.TestCase):

    def test_returnEmptyFile_forEmptyDict(self):
        input = dict()
        save_classification_to_file(input, REFERENCENAME)

        with replaced_open():
            write_classification_to_file(input, FILENAME)

        # Validate results
        self.assertListEqual(
            list(io.open(REFERENCENAME)),
            list(io.open(FILENAME)),
            'Items in written files are not equal.')

    def test_correctlyFormattedDict(self):
        input = create_classification()
        save_classification_to_file(input, REFERENCENAME)

        with replaced_open():
            write_classification_to_file(input, FILENAME)

        # Validate results
        self.assertListEqual(
            list(io.open(REFERENCENAME)),
            list(io.open(FILENAME)),
            'Items in written files are not equal.')

    def tearDown(self):
        """Delete the classification file if it exists."""
        try:
            os.unlink(FILENAME)
            os.unlink(REFERENCENAME)
        except:
            pass

def save_classification_to_file(d, fname):
    """Save the classification dictionary to a file."""
    with open(fname, 'wt', encoding='utf-8') as f:
        for key, value in d.items():
            f.write(key + ' ' + value + '\n')

def create_classification(n_items=20, n_spams=None):
    """Create a random dictionary of classified email filenames."""
    n_spams = n_spams if n_spams else n_items // 2
    classes = [SPAM_TAG] * n_spams + [HAM_TAG] * (n_items - n_spams)
    random.shuffle(classes)
    d = {}
    for i in range(n_items):
        d[random_filename()] = classes.pop()
    return d

def random_filename(fnamelength=8, ext_prob=1):
    """Create a filename as a random sequence of letters and numbers, possibly with an extension."""
    fname = random_string(fnamelength)
    ext = ''
    if random.random() < ext_prob:
        ext = '.' + random_string(3)
    return fname + ext

def random_string(strlength=8, chars=FNAME_CHARS):
    """Create a string as a random sequence of the given chars."""
    sampled_chars = [random.choice(chars) for i in range(strlength)]
    return ''.join(sampled_chars)

@contextmanager
def replaced_open(warning_only=False):
    """Replace original open() with ours that raises if the encoding is not set to utf-8."""

    def my_open(*args, **kwargs):
        # If opening in binary mode, call the true open function
        if (len(args) > 1 and ('b' in args[1].lower())
                or ('mode' in kwargs and ('b') in kwargs['mode'].lower())):
            return orig_open(*args, **kwargs)        
        # If encoding set properly, call the true open function
        if 'encoding' in kwargs and kwargs['encoding'].lower() == 'utf-8':
            return orig_open(*args, **kwargs)
        # Else raise an error or issue a warning
        if warning_only:
            warnings.warn('When opening a file, you forgot to set the encoding to utf-8.')
        else:
            raise RuntimeError('When opening a file, you forgot to set the encoding to utf-8.')

    orig_open = builtins.open
    builtins.open = my_open
    yield
    builtins.open = orig_open

if __name__ == "__main__":
    unittest.main()