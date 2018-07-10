"""
Miscelllaneous list manipulation
"""

def split(num_lst, index):
    '''

    Parameters
    ----------
    num_lst: list
    index: int

    Returns
    -------
    Two lists, splitting num_lst by 'index'

    Examples
    --------
    >>> split(['a','b','c','d'],3)
    (['a', 'b', 'c'], ['d'])
    '''

    list1 = num_lst[:index]
    list2 = num_lst[index:]

    return list1, list2

