#!/usr/bin/env python3
"""let's duck type an iterable object"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return tuple of value and len of each element in a list"""
    return [(i, len(i)) for i in lst]
