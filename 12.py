#c=int
#i=int
#def mathematical_action(X,znak,y):

def rede (i,x,i_max):
     i0=i
     while True:    #i in range(c1):
         
         if x[i]=='0'or x[i]=='1'or x[i]=='2'or x[i]=='3'or x[i]=='4'or x[i]=='5'or x[i]=='6'or x[i]=='7'or x[i]=='8'or x[i]=='9':
            if i==i_max-1:
                 znak=None 
                 f=0 
                 i=i_max
                 break  
            else:
                 i=i+1
                 f=1
         else:
             znak=x[i]
             f=1
             break  
     q=int(x[i0:i])      
     mas=[i,q,f,znak] 
     return mas

def sum_(x, znak, y):
      if  znak== '+':
           r=x+y
           print (x,'+',y,"=",r)
      if  znak=='-':
           r=x-y
           print (x,'-',y,"=",r)
      if  znak=='*':
           r=x*y
           print (x,'*',y,"=",r)
      if  znak=='sqrt':
           r=x**0.5
           print (x,'sqrt',y,"=",r)
      if  znak=='^':
           r=x**y
           print (x,'^',y,"=",r)
           print(r)
      return r
print("введите выражение") 
x=input() 
i_max=len(x)
F=1
X_values=[]
Arithmetic_signs=[]
i_body=0
i=0
while F==1:
     x0=x[:] # копирование строки из одной в другую 
     z=rede(i,x0,i_max)
     i=z[0]+1
     X_values.append(z[1])
     F==z[2]
     Arithmetic_signs.append(z[3])
     #print (X_values[i_body], end='')
     #print (Arithmetic_signs[i_body])
     i_body=i_body+1
     #print(i)
     #print(i_max)
     if i>=i_max:
         F=0
print ("работает")
print(X_values)
print(Arithmetic_signs)
try:
     ix_div=Arithmetic_signs.index('/')
     rezalt=X_values[ix_div]/X_values[ix_div+1]
     X_values[ix_div+1]=rezalt
     del(X_values[ix_div])
     print(X_values)
     del (Arithmetic_signs[ix_div])
     print(Arithmetic_signs)
     
except ValueError:
      print(" ")
try:
      ix_multi=Arithmetic_signs.index('*')
      rezalt=X_values[ix_multi]*X_values[ix_multi+1]
      X_values[ix_multi+1]=rezalt
      del(X_values[ix_multi])
      print(X_values)
      print(X_values[ix_multi])
      print(rezalt)
      del (Arithmetic_signs[ix_multi])
except ValueError:
      print("  ")

print(Arithmetic_signs)
for i in range(0,len(Arithmetic_signs)-1,1):
     rezalt_=sum_(X_values[0], Arithmetic_signs[i], X_values[i+1] )
     X_values[0]=rezalt_