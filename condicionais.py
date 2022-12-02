def par(x):
    print(x%2==0)
def dentro(x,y,z):
   dentro = x>=y and x<=z
   print(dentro)
def fora(x,y,z):
    fora = x<y or x>z
    print(fora)
def bissexto(ano):
    bissexto = ano%400==0 or (ano%4==0 and ano%100!=0)
    print(bissexto)

#testando as funções:
par(8)
par(1)
dentro(1,3,5)
dentro(1,0,2)
fora(8,1,2)
fora(1,1,2)
bissexto(1900)
bissexto(2000)