def MERGE(A,start,mid,end):
    L=[0]*(mid - start + 1)
    for i in range(len(L) - 1):
        L[i] = A[start+i]
    L[len(L) - 1] = 100000 # centinel, (fix)
    R=[0]*(end - mid + 2)
    for j in range(len(R) - 1):
        R[j] = A[mid+j]

    R[len(R) - 1] = 100000
    i = 0
    j = 0
    k = start
    for l in range(k,end):
        if(L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1   

def mergeSort(A,p,r):
    if p < r:
        mid = int((p+r)/2)
        mergeSort(A,p,mid)
        mergeSort(A,mid+1,r)
        MERGE(A,p,mid,r) 

A  = [20, 30, 15, 21, 42, 45, 31, 0, 9]
mergeSort(A,0,len(A))
