import argparse
import numpy as np
import math


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="inputmatrixpath, pls enter a path")
parser.add_argument("--pam", type=int, help="pamnumber")
parser.add_argument("--output", type=str, help="outputmatrixpath, pls enter a path")
args = parser.parse_args()
print(vars(args))
# Read file
file = open(args.input, "r")
data = file.readlines()
file.close()

# Put the data into a matrix
m = np.zeros((20, 20))
for i in range(2, 22):
    s = data[i].rstrip()
    rowData = s.split()
    del rowData[0]
    for j in range(len(rowData)):
        m[i - 2][j] = int(rowData[j])
        
# Frequencies
f = [0.087, 0.041, 0.040, 0.047, 0.033, 0.038, 0.050, 0.089, 0.034, 0.037, 0.085, 0.081, 0.015, 0.040, 0.051, 0.070, 0.058, 0.010, 0.030, 0.065]

# Input the number x for PAMx
x = args.pam

# Caculate Mx
m = m /10000
mx = m
for i in range(x - 1):
    mx = np.matmul(mx, m)

# Caculate PAMx
pamx = np.zeros((20, 20))
for i in range(20):
    for j in range(20):
        if mx[i][j] == 0:
            pamx[i][j] = 0
        else:
            r = mx[i][j] / f[i]
            pamx[i][j] = 10 * math.log(r, 10)
pamx = np.around(pamx)
pamx = pamx.astype(int)
np.set_printoptions(precision=4)
pamx = pamx.astype(str)

# Add the amino acid into the matrix
aminoAcidR = np.array(["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"])
aminoAcidC = np.array([" ", "A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"])
pamx = np.insert(pamx, 0, aminoAcidR, axis = 0)
pamx = np.insert(pamx, 0, aminoAcidC, axis = 1)

# Write the matrix into the txt file
np.savetxt(args.output, pamx, fmt = '%4s')

    