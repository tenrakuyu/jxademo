# -*- encoding=utf8 -*-
__author__ = "tianle"

from airtest.core.api import *

auto_setup(__file__)

print('swipe=========>')

while 1==1:
    swipe((800, 1800), vector=[0, -0.5], duration=0.3)
    swipe((800, 1800), vector=[0, -0.5], duration=1)
    swipe((800, 1800), vector=[0, -0.5], duration=0.3)
    swipe((800, 1800), vector=[0, -0.5], duration=1)