#!/usr/bin/python3
""" create a pascal triangle of n dimension """


def pascal_triangle(n):
    """ adds 1 at begining and 1 at end alwayts,
    iterates given amount of sums"""
    if n <= 0:
        return []
    else:
        triangle = [[1], [1, 1]]
        for i in range(1, n - 1):
            line = [1]
            for j in range(0, len(triangle[i]) - 1):
                line.extend([triangle[i][j] + triangle[i][j+1]])
            line += [1]
            triangle.append(line)
        return triangle
