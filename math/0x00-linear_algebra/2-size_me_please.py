#!/usr/bin/env python3
"""
dsfa fdsad abjn a  bhd iywg ighwjq mka 0osqn kerl khe pjad hujfee oiewqn hwrekqjn eqwhijleq
"""
def matrix_shape(matrix):
    """
    ga idwuq hkrqj lskjcs oijqwn qpwkoem sjva jgqw khure poytmn ,.mdsn kq   hjb askjdas kwjqe rlkhren qhkeb xkr
    """
    if type(matrix[0]) is not list:
        """
        qwkj oirj ewlrj ckjbqew jhqe  rtkljhnt hoiqwchebn rkcba kqwrqb
        """
        return [len(matrix)]
    else:
        """
        agg hhs jsu jwb hqed ufrjj
        """
        return [len(matrix)] + matrix_shape(matrix[0])
