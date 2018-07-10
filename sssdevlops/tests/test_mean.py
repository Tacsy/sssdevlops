#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This file is to test the mean function
"""
from sssdevlops import mean


def test_simple():
    num_list = [1,2]
    observed  = mean(num_list)
    expected = 1.5
    assert observed == expected

