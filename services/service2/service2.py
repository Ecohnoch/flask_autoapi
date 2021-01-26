# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : service2.py
# @Function : TODO

from dependencies import add, mul

def service2(param1, param2, param3):
    param1 = int(param1)
    param2 = int(param2)
    param3 = int(param3)

    ans1 = add(param1, param2, param3)
    ans2 = mul(param1, param2, param3)

    return str(ans1), str(ans2)