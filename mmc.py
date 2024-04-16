    #usando recursão para calcular o minimo multiplo comum de dois valores 
    def mmcx(m,n,xm,xn):

    if xm == xn :
        return xn 
    if xm < xn :
        return mmcx(m,n, xm+m, xn)
    else :
        return mmcx(m, n, xn+n, xm)
