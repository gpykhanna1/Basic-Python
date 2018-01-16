import numpy as np
#
# x = np.array([[1,2], [3,4]])
# print(x)    # Prints "[[1 2]
#             #          [3 4]]"
#
# print("")
#
# print(x.T)  # Prints "[[1 3]
#             #          [2 4]]"
#
# print("")

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"


# ... the transpose of a 1x3 matrix should be a 3x1 matrix
# See Mathematica Notebook
# So what is the difference in Python between np.array([1,2,3]) and np.array([ [1,2,3] ])

print("")
v_1 = np.array([ [1,2,3] ])
print(v_1)
print(v_1.T)

print("")

v_2 = np.array([ [1],[2],[3] ] )
print(v_2)
print(v_2.T)

print(np.linalg.matrix_rank(v))
print(np.linalg.matrix_rank(v_1))
print(np.linalg.matrix_rank(v_2))
