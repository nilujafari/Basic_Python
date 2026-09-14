weight = float(input('enter your weight: \n'))
acual_wather = float(input('entery your drink wather: \n'))

recommended = weight * 0.033 ###recommended = tosiye shode
precent = (acual_wather / recommended)*100

if precent <= 70:
    print('Drink Less')
elif 70 < precent <= 120:
    print('Drink Normal')
else:
    print('Drink More')