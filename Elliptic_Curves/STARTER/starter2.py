def add(x1,y1,x2,y2,p,A):
    if x1!=x2 and y1!=y2:
        s=(((y2-y1+p)%p)*pow(x2-x1,-1,p))%p
    else :
        s=((((3*x1*x1)%p+A))%p)*pow(2*y1,-1,p)
    x3=((s*s)%p-x1-x2+p+p)%p
    y3=((s*(x1-x3))%p-y1+p)%p
    return (x3,y3)
x,y=add(493,5564,493,5564,9739,497)
x,y=add(x,y,1539,4742,9739,497)
x,y=add(x,y,4403,5202,9739,497)
print(x,y)

# crypto{4215,2162}