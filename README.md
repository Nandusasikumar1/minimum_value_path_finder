# minimum_value_path_finder

This program will find the path of minimum values in a 2D matrix.

for example consider the matrix
[[ 2,  8, 11,  5, 12],
[ 6, 16, 22, 15,  3],
[23,  4, 14, 10,  7],
[18, 13, 17, 19, 25],
[21,  1, 20, 24,  9]]

when we input the index [1,1] of this  matrix to the program the output will be path of indices and values:
('indices are :[1, 1]-->[0, 0]-->[1, 0]-->[2, 1]-->[3, 1]-->[4, 1]-->[3, 2]-->[2, 3]-->[1, 4]-->[0, 3]-->[0, 2]-->[0, 1]-->[1, 2]-->[2, 2]-->[1, 3]-->[2, 4]-->[3, 3]-->[4, 4]-->[4, 3]-->[4, 2]', 'values are :16-->2-->6-->4-->13-->1-->17-->10-->3-->5-->11-->8-->22-->14-->15-->7-->19-->9-->24-->20')

# Duplicate values are not allowed.
For example, when the path reaches 6 at index [1,0] the  minimum value around 6 is 2,but 2 is already in the path.Hence the program will find the next minimum value which is 4 at index [2,1]
When all the minvals are used the program stops.
