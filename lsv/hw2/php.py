import math
import os
import sys

n = 4 if len(sys.argv)<2 else int(sys.argv[1])
m = n + 1

nbvar = m*n # (i,j) = (1,1) (1,2) ... (1,n)
nbclauses = 0
cnf = []
# each pigeon must be in some hole
for i in range(1,m+1):
	clause = []
	for j in range(1,n+1):
		var = (i-1)*n + j
		clause.append(var)
	clause.append(0)
	cnf.append(clause)
	nbclauses += 1
# each hole contains at most one pigeon
for k in range(1,m):
	for l in range(k+1,m+1):
		for j in range(1,n+1):
			var1 = (k-1)*n + j
			var2 = (l-1)*n + j
			clause = [-1*var1, -1*var2, 0]
			cnf.append(clause)
			nbclauses += 1

# file.write
file = open("hw2-7b.dimacs", "w")
file.write("c n = %s, m = %s\n" %(n,m))
file.write("p cnf %s %s\n" %(nbvar, nbclauses))
for clause in cnf:
	for v in clause:
		file.write("%s " % v)
	file.write("\n")
file.close()
# run minisat
print("n=%s, m=%s" %(n,m))
os.system("minisat hw2-7b.dimacs")
