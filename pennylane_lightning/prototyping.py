import numpy as np
from lightning_qubit_ops import mvp, test

vec = np.ones(2, dtype="complex")
mat = np.eye(2, dtype="complex")

res = mvp(mat, vec, [0])

print(test())
# print(res)

# vec = np.array([1, 0, 0, 0, 0, 0, 0, 0])
# mat = np.array([[0, 1], [1, 0]])
#
# np.tensordot(mat, vec, [1])
