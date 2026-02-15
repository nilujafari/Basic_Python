import datetime as dt

fitness_data = [
    {"date": "2025-01-01", "time": "06:30", "steps": 800},
    {"date": "2025-01-01", "time": "08:00", "steps": 1200},
    {"date": "2025-01-01", "time": "11:45", "steps": 3400},
    {"date": "2025-01-01", "time": "15:20", "steps": 2200},
    {"date": "2025-01-01", "time": "19:10", "steps": 1800},

    {"date": "2025-01-02", "time": "07:15", "steps": 950},
    {"date": "2025-01-02", "time": "09:30", "steps": 1600},
    {"date": "2025-01-02", "time": "12:10", "steps": 3100},
    {"date": "2025-01-02", "time": "17:25", "steps": 2700},
    {"date": "2025-01-02", "time": "21:00", "steps": 1300},

    {"date": "2025-01-03", "time": "06:50", "steps": 700},
    {"date": "2025-01-03", "time": "10:00", "steps": 2000},
    {"date": "2025-01-03", "time": "14:30", "steps": 2600},
    {"date": "2025-01-03", "time": "18:15", "steps": 2900},
    {"date": "2025-01-03", "time": "22:40", "steps": 1500},

    {"date": "2025-01-04", "time": "07:05", "steps": 1100},
    {"date": "2025-01-04", "time": "09:50", "steps": 1700},
    {"date": "2025-01-04", "time": "13:20", "steps": 2500},
    {"date": "2025-01-04", "time": "16:45", "steps": 3000},
    {"date": "2025-01-04", "time": "20:30", "steps": 2100},
]

def average_steps(
    fitness_data, 
    start_date = None,
    end_date = None,
    start_time = None,
    end_time = None
):
    if start_date is None:
        current_date = str(dt.datetime.now().strftime("%Y-%m-%d"))
        start_date = current_date
    if end_date is None:
        gap_days = 1
        end_date = dt.datetime.now() + dt.timedelta(days=gap_days)
        end_date = str(end_date.strftime("%Y-%m-%d"))

    if start_time is None:
        start_time = dt.datetime.now().strftime("%H:%M")
    print(start_date, end_date)
    total_steps = 0
    count_steps = 0 
    for i in fitness_data:
        if start_date <= i["date"] <= end_date and start_time <= i["time"] <= end_time:
            total_steps += i["steps"]
            #print(total_steps)
            count_steps += 1
    
    if count_steps == 0:
        return 0
    return total_steps / count_steps
print(average_steps(fitness_data))





# UTC
# test1 = "2025-12-26 14:30:00"
# test2 = dt.datetime.now()
# test3 = dt.replace(tzinfo=dt.timezone.utc)
# # test2_tmrw = test2 + dt.timedelta(hours=1)
# print(test1)
# print(test2)
# print(test3)
# import pytz
# from datetime import datetime, timezone

# dt = datetime(2024, 1, 25, 12, 0, 0)
# print(dt)
# res = dt.replace(tzinfo=pytz.timezone('Asia/Shanghai'))
# print(res)
# test = "2025-01-04"
# test_time = "06:32"
# test_dt = datetime.now()
# print(type(test_dt))
# print(type(test))
# print(test_dt.strftime("%A %Y-%m-%d %H:%M:%S"))


# def calculate_avg_in_range(
#     data,
#     start_date,
#     end_date,
#     start_time,
#     end_time
# ):
#     start_time = f"{start_date} {start_time}"
#     end_time = f"{end_date} {end_time}"
#     start_time_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
#     end_time_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

#     total_steps = 0
#     count_steps = 0
#     for item in data:
#         item_date = f"{item['date']} {item['time']}"
#         item_time_dt = datetime.strptime(item_date, "%Y-%m-%d %H:%M")

#         if start_time_dt <= item_time_dt <= end_time_dt:
#             total_steps += item['steps']
#             count_steps += 1

    
#     if count_steps == 0:
#         print("No data in the range")
#         return 0

#     return total_steps / count_steps