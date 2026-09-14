walk_step = float(input('enter your walk step: \n'))
activity_day = int(input('enter your activity day: \n')) #minute
sitting_hours = float(input('enter your sitting hour: \n')) # colock

if walk_step > 10000 and activity_day > 30 and sitting_hours < 6:
    print('active')
elif (600 < walk_step < 10000) or (15 < activity_day < 30) or (6 < sitting_hours < 8):
    print('moderate')
else:
    print('sedentary')