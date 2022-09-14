"""
Snake Problem
=============

Question
--------

Write a program that calculates how many different ways a snake of
length 16 can be laid out on a 4x4 grid.


Example
-------

Given a grid like so::

    +---------+---------+---------+---------+
    |         |         |         |         |
    |    0    |    1    |    2    |    3    |
    |         |         |         |         |
    +---------+---------+---------+---------+
    |         |         |         |         |
    |    4    |    5    |    6    |    7    |
    |         |         |         |         |
    +---------+---------+---------+---------+
    |         |         |         |         |
    |    8    |    9    |   10    |   11    |
    |         |         |         |         |
    +---------+---------+---------+---------+
    |         |         |         |         |
    |   12    |   13    |   14    |   15    |
    |         |         |         |         |
    +---------+---------+---------+---------+


one path would be
``[0, 1, 2, 3, 7, 6, 5, 4, 8, 9, 10, 11, 15, 14, 13, 12]``::

    +---------+---------+---------+---------+
    |  Start  |         |         |         |
    |    0---------1---------2---------3    |
    |         |         |         |    |    |
    +---------+---------+---------+----|----+
    |         |         |         |    |    |
    |    4---------5---------6---------7    |
    |    |    |         |         |         |
    +----|----+---------+---------+---------+
    |    |    |         |         |         |
    |    8---------9---------10-------11    |
    |         |         |         |    |    |
    +---------+---------+---------+----|----+
    |   End   |         |         |    |    |
    |    12-------13--------14--------15    |
    |         |         |         |         |
    +---------+---------+---------+---------+


and another ``[5, 6, 10, 9, 8, 4, 0, 1, 2, 3, 7, 11, 15, 14, 13, 12]``::

    +---------+---------+---------+---------+
    |         |         |         |         |
    |    0---------1---------2---------3    |
    |    |    |         |         |    |    |
    +----|----+---------+---------+----|----+
    |    |    |  Start  |         |    |    |
    |    4    |    5---------6    |    7    |
    |    |    |         |    |    |    |    |
    +----|----+---------+----|----+----|----+
    |    |    |         |    |    |    |    |
    |    8---------9--------10    |   11    |
    |         |         |         |    |    |
    +---------+---------+---------+----|----+
    |  End    |         |         |    |    |
    |   12--------13--------14--------15    |
    |         |         |         |         |
    +---------+---------+---------+---------+

There are many more but what is the total of all possible unique paths?


Rules
-----

* Do not output all the paths, just the total path count.  A single
  number is all that is required as output of this program.

* Diagonal movements are not allowed.

* Use Python 3.8+ and the standard modules only.  No Numpy or any third
  party modules.


Tips
----

* The answers for smaller square grids:

    * 1x1 grid (snake length 1) has 1 path.
    * 2x2 grid (snake length 4) has 8 paths.
    * 3x3 grid (snake length 9) has 40 paths.

* Consider performance when writing your solution.

* We will test your solution with square grids of different sizes.

"""


def find_paths(grid, path):
    """ The functions takes the size of the grid and the path taken by the snake as parameter.
    Grid is an integer, while Path is a list of tuples, where a tuple (i,j) denotes a position in the grid.
    For instance, in a 2x2 grid, the path could be [(0,0),(0,1),(1,1),(1,0)]. """

    # A variable which counts the number of ways the snake can be laid in the grid
    no_paths = 0

    # If the length of the path is equal to the length of the snake (grid^2),
    # then the code returns 1, denoting that the snake has fully been laid in the grid.
    if len(path) == grid ** 2:
        return 1

    # Move UP from the current position (note that path[-1] denotes the current position) -
    # if the new position is not outside the grid and not already in the path
    # If the condition is satisfied, then the function is called again with
    # grid as the size, and the current path with the new position appended to it.
    # This is the same for the other three if-statements below.
    if path[-1][0] - 1 >= 0 and not (path[-1][0] - 1, path[-1][1]) in path:
        no_paths += find_paths(grid, path + [(path[-1][0] - 1, path[-1][1])])

    # Move LEFT from the current position -
    # if the new position is not outside the grid and not already in the path
    if path[-1][1] - 1 >= 0 and not (path[-1][0], path[-1][1] - 1) in path:
        no_paths += find_paths(grid, path + [(path[-1][0], path[-1][1] - 1)])

    # Move DOWN from the current position -
    # if the new position is not outside the grid and not already in the path
    if path[-1][0] + 1 < grid and not (path[-1][0] + 1, path[-1][1]) in path:
        no_paths += find_paths(grid, path + [(path[-1][0] + 1, path[-1][1])])

    # Move RIGHT from the current position -
    # if the new position is not outside the grid and not already in the path
    if path[-1][1] + 1 < grid and not (path[-1][0], path[-1][1] + 1) in path:
        no_paths += find_paths(grid, path + [(path[-1][0], path[-1][1] + 1)])

    # return the total number of paths
    return no_paths

def path_count(edge_length: int) -> int:
    """
    Do not change the name, argument, or return type of this function.

    :param edge_length: The number of cells along the edge of a square
                        grid.
    :return: The sum of all possible unique paths on a square grid of
             size: edge_length x edge_length
    """

    # Initialize the matrix given the edge length.
    matrix = [[0 for x in range(edge_length)] for y in range(edge_length)]

    print(matrix)

    count = 0

    # TODO: Complete this function.  You may add other functions as you
    #  see fit.

    return count


if __name__ == '__main__':

    # assert path_count(edge_length=1) == 1
    # assert path_count(edge_length=2) == 8
    # assert path_count(edge_length=3) == 40

    # print(path_count(edge_length=4))

    n = 4
    no_paths = 0

    # This basically loops through all the possible starting points (i,j) in a nxn grid
    # The results from each of the starting points are added into a variable, no_paths
    for i in range(n):
        for j in range(n):
            no_paths += find_paths(n, [(i, j)])

    # The final result is then printed out
    print(no_paths)