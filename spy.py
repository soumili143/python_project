numbe = 1125
strnumbe = str(numbe)
sumOfDigit = 0
productOfDigit = 1
listdigits = list(map(int, strnumbe))
for elemen in listdigits:
    sumOfDigit = sumOfDigit+elemen
    productOfDigit = productOfDigit*elemen
if(sumOfDigit == productOfDigit):
    print('The given number', strnumbe, 'is spy number')

else:
    print('The given number', strnumbe, 'is not spy number')