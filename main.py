# hesap makinesi yapma kodu

def toplama (num1,num2):
    print(f"İşlem Sonucunuz: {num1+num2}")
def cıkartma (num1,num2):
    print(f"İşlem Sonucunuz: {num1-num2}")
def carpma (num1,num2):
    print(f"İşlem Sonucunuz: {num1*num2}")
def bolme (num1,num2):
    print(f"İşlem Sonucunuz: {num1/num2}")


num1 = input("İlk sayıyı giriniz: ")
num2 = input("İkinci sayıyı giriniz: ")
myOperator = input("Operatoru giriniz: ")

if myOperator == "+":
    toplama(int(num1),int(num2))
elif myOperator == "*":
    carpma(int(num1),int(num2))
elif myOperator == "/":
    bolme(int(num1),int(num2))
elif myOperator == "-":
    cıkartma(int(num1),int(num2))
else:
    print("İşlem Tanımlı Değil")






