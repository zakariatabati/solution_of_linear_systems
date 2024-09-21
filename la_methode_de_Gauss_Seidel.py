import numpy as np

def D_j(A):
    D = np.zeros(A.shape)
    for i in range(0,int(A.shape[0])):
        for j in range(0,int(A.shape[0])):
            if(i==j):
                D[i][j] = A[i][j]
    return D 
def E_j(A):
    E = np.tril(-A)
    for i in range(0,int(A.shape[0])):
        for j in range(0,int(A.shape[0])):
            if(i==j):
                E[i][j] = 0
    return E
def F_j(A):
    F = np.triu(-A)
    for i in range(0,int(A.shape[0])):
        for j in range(0,int(A.shape[0])):
            if(i==j):
                F[i][j] = 0
    return F

def method_gauss_seidel(A,b,x0,eps=0.01,max_it=1000):
    x=x0
    it=0
    M = D_j(A)
    E = E_j(A)
    F = F_j(A)
    S = np.linalg.inv((M-E))
    B_GS = np.dot(S,F)
    C_GS = np.dot(S,b)
    va_p = np.linalg.eigvals(B_GS)
    if(max(va_p)>1):
        
        return "the method is divergent"
    while(it<max_it ):
        err = np.linalg.norm(A.dot(x) - b)
        if(err<eps):
            break
        x = np.dot(B_GS,x) + C_GS
        it=it+1
    return x

## unit testing 
'''

def testing(A,b,x0,res):
    if(np.array_equal(method_gauss_seidel(A,b,x0),res)):
        return "valid"
    else:
        print("the solution i found is : " ,method_gauss_seidel(A,b,x0))
        return "invalid" 
## test 1
A =  np.array([[2, 1,2], [6, 4,0] , [8,5,1]])
b = np.array([[10],[26],[35]])
x0= np.array([[0],[0],[0]])
print(testing(A,b,x0,"the method is divergent"))
## test 2
A =  np.array([[2, 4,-4,1], [3, 6,1,-2] , [-1,1,2,3],[1,1,-4,1]])
b = np.array([[0],[-7],[4],[2]])
x0= np.array([[0],[0],[0],[0]])
print(testing(A,b,x0,"the method is divergent"))
## test 3
A =  np.array([[1, 2,-2], [1, 1,1] , [2,2,1]])
b = np.array([[1],[2],[0]])
x0= np.array([[0],[0],[0]])
print(testing(A,b,x0,"the method is divergent"))

## test 4
A =  np.array([[10, 1], [2,10]])
b = np.array([[11],[12]])
x0= np.array([[0],[0]])
print(testing(A,b,x0,np.array([[1.],[1.]])))

## test 5
A =  np.array([[10, -1,0], [-1, 10,-2] , [-2,0,10]])
b = np.array([[9],[10],[7]])
x0= np.array([[0],[0],[0]])
print(testing(A,b,x0,np.array([[1.0284],[1.28398],[0.90568]])))




'''