def pressure(parameter_sys,parameter_dia):

    if parameter_sys > 180 or parameter_dia > 120:
        message = 'Hypertension Crisi'
    elif parameter_sys > 140 or parameter_dia > 90:
        message = 'Hypertension Stage 2'
    elif 130 < parameter_sys < 139 or 80 < parameter_dia < 89:
        message = 'Hypertension Stage 1'
    elif 120 < parameter_sys < 129 and parameter_dia < 80:
        message = 'Elevated'
    elif parameter_sys < 120 and parameter_dia < 80:
        message = 'Normal'
    print(f'result = {message}')
while True:
    try:
        parameter_sys = int(input('Please enter your Systolic pressure: '))
        parameter_dia = int(input('Please entery your Diastolic pressure: '))
        pressure(parameter_sys,parameter_dia)
    except:
        print('Error: Please enter your valid number \n')
        