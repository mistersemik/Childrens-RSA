import main
import sympy

#M должно быть не больше N
m = '21412235'
p = sympy.randprime(1,231521241243111)
q = sympy.randprime(1,231512412423111)
N = q*p
f = (p-1)*(q-1)
print('N=',N)
print('f=',f)


cr =''
number = []
for i in m:
    ind = main.abc.index(i)
    number.append(ind)
    cr+=str(ind)
m = int(cr)
print('m=',m)
print('Кодовая последовательность сообщения:\n',number)



e = main.find_e(0,f)
print('e=',e)

d = main.invert(e,f)
print('d =',d)

c = pow(m,e,N)
print('c=',c)

m1 = pow(c,d,N)
print('m`=',m1)

cr = ''
for i in range(len(number)):
    ind = main.abc[number[i]]
    cr+=ind
print(cr)