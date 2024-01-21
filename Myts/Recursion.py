# def calsum(n):
#     if n <0: 
#         return "INVALID"
#     if n == 1:
#         return 1
#     else:
#         return n + calsum(n-1)
    
# n = int(input("n"))

def multi(n):
    if n < 0: 
        return "INVALID"
    if n == 0:
        return 1
    else: 
        return (2*n+1)*multi(n-1)
