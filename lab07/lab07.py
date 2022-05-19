from pyparsing import empty


def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    # list_link = []
    # link_tmp = link
    # while link_tmp.first is not None:
    #     list_link.append(link_tmp.first)
    #     link_tmp = link_tmp.rest
    # return list_link
    res = []
    while link is not Link.empty:
        res.append(link.first)
        link = link.rest
    return res


def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():
        for b in t.branches:
            cumulative_mul(b)
            t.label *= b.label
    
def label_squarer(t):
    t.label = t.label ** 2
    for branch in t.branches:
        label_squarer(branch)


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    while link is not Link.empty:
        if link not in visited:
            visited.add(link)
        else:
            return True
        link = link.rest
    return False


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    fast = link.rest.rest
    slow = link.rest
    while fast is not Link.empty and fast.rest is not Link.empty:
        if slow is fast:
            return True
        fast = fast.rest.rest
        slow = slow.rest
    return False



def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    if s is not Link.empty and s.rest is not Link.empty:
        if s.rest.rest is Link.empty:
            s.rest = Link.empty
        else:
            every_other(s.rest.rest)
            s.rest = s.rest.rest
    
def height(t):
    """Return the longest length of the path from root to a leaf.
    
    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> height(t)
    1
    """
    if t.is_leaf():
        return 0
    else:
        max_values = []
        for branch in t.branches:
            max_values.append(height(branch))
        return 1 + max(max_values)

def max_path_sum(t):
    """Return the maximum sum of the values along any path in the tree."""
    if t.is_leaf():
        return t.label
    else:
        max_sum = []
        for branch in t.branches:
            max_sum.append(max_path_sum(branch))
        return t.label + max(max_sum)

def reverse_other(t, is_odd=True):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf() and is_odd:
        for i in range(len(t.branches) // 2):
            t.branches[i].label, t.branches[-i - 1].label = t.branches[-i - 1].label, t.branches[i].label
        
    for branch in t.branches:
        reverse_other(branch, not is_odd)

def find_path(t, x):
    """Take in a tree and a value, returns a list of nodes which are contained in the path
    required to get from the root of the tree to a node, whose label is x."""
    if t.label == x:
        return [t.label]
    for b in t.branches:
        path = find_path(b, x)
        if path:
            return [t.label] + path
    # else:
    #     paths = [find_path(b, x) for b in t.branches]
    #     for path in paths:
    #         if path:
    #             return [t.label] + path
    
def prune_small(t, n):
    """Prune the tree mutatively, keep at most n branches on each node
    with the smallest label."""
    while len(t.branches) > n:
        largest = max([b for b in t.branches], key=lambda x: x.label)
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b, n)

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

if __name__ == "__main__":
    t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]),Tree(5, [Tree(3), Tree(4)])])
    prune_small(t3, 2)
    print(t3)