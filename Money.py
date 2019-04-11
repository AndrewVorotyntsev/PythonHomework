def delivery_of_change(x):
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = 0
    while x > 0:
            if x >= 5000:
                k += 1
                x = x-5000
            else:
                if x >= 2000:
                   l += 1
                   x = x-2000
                else:
                    if x >= 1000 :
                        m += 1
                        x=x-1000
                    else:
                        if x >= 500:
                            n += 1
                            x = x-500
                        else :
                            if x >= 200:
                                a += 1
                                x = x-200
                            else:
                                if x >= 100:
                                    b += 1
                                    x = x-100
                                else:
                                    if x >= 50:
                                        c += 1
                                        x = x-50
                                    else:
                                        if x >= 10:
                                            d += 1
                                            x = x-10
                                        else:
                                            if x >= 5:
                                                e += 1
                                                x = x-5
                                            else:
                                                if x >= 1:
                                                    f += 1
                                                    x = x-1
                                                else:
                                                    if x >= 0.5:
                                                        g += 1
                                                        x = x-0.5
                                                    else:
                                                        if x >= 0.1:
                                                            h += 1
                                                            x=x-0.1
                                                        else:
                                                            if x >= 0.05:
                                                                i+=1
                                                                x=x-0.05
                                                            else:
                                                                if x >= 0.01:
                                                                    j+=1
                                                                    x=x-0.01
                                                                else:
                                                                    break

    print("5000=",k,"\n2000=",l,"\n1000",m,"\n500=",n,"\n200=" ,a , "\n100=",b , "\n50=",c , "\n10=" ,d,"\n5=",e,"\n1=",f,"\n0.5=",g,"\n0.1=",h,"\n0.05=",i,"\n0.01=",j)


print("Write money")
x=float(input())
delivery_of_change(x)09
