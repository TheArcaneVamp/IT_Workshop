n = int(input("n="))
r = int(input("r="))
def nCr(n,r):
    r_fact = factrec(r)
    n_fact = factrec(n)
    n_diff_r_fact = factrec(n-r)
    ncr = n_fact/(r_fact*n_diff_r_fact)
    print("nCr=", ncr)

def nPr(n,r):
    r_fact = factrec(r)
    n_fact = factrec(n)
    n_diff_r_fact = factrec(n-r)
    npr = (n_fact/n_diff_r_fact)
    print("nPr=", npr)



def factrec(x):
    if x==1:
        return 1
    else:
        return x*factrec(x-1)
nCr(n,r)
nPr(n,r)
