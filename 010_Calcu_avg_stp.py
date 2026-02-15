from datetime import datetime
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
def calculate_avg_in_range(
        fitness_data,
        start_date,
        end_date,
        start_time,
        end_time
):
    total_step = 0
    count_step = 0
    start_dt = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
    end_dt = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M")

    for i in fitness_data:
        i_fit_date = datetime.strptime(f"{i['date']} {i['time']}", "%Y-%m-%d %H:%M")
        if start_dt <= i_fit_date <= end_dt:
            total_step += i["steps"]
            count_step += 1

        if count_step == 0:
            print("Error zero divition")
            return 0
    return total_step / count_step
avg = calculate_avg_in_range(fitness_data, "2025-01-01","2025-01-04","06:30","22:40")
print(avg)



#Second Method
def calculate_avg_in_range(
    fitness_data,
    start_date,
    end_date,
    start_time,
    end_time
):
    start_time = f"{start_date} {start_time}"
    end_time = f"{end_date} {end_time}"
    start_time_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_time_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
    total_steps = 0
    count_steps = 0
    for item in fitness_data:
        item_date = f"{item['date']} {item['time']}"
        item_time_dt = datetime.strptime(item_date, "%Y-%m-%d %H:%M")

        if start_time_dt <= item_time_dt <= end_time_dt:
            total_steps += item['steps']
            count_steps += 1
            
    if count_steps == 0:
        print("Error zero divition")
        return 0
    return total_steps / count_steps
avg = calculate_avg_in_range(fitness_data,"2025-01-01","2025-01-04","06:30","23:59")
print(avg)
