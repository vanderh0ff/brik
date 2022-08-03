import datetime
import math

fake_tasks = 100
start_date = datetime.date.fromisoformat("2022-05-01")
end_date = datetime.date.fromisoformat("2022-10-09")
number_of_days = end_date - start_date
weeks = math.ceil(number_of_days.days/7.0)

def normalize_week(class_week):
    total_tasks = 0
    for day in class_week.items():
        print(day)
        total_tasks += day[1]['max_tasks']
    total_tasks = float(total_tasks)
    for day in class_week:
        class_week[day]['normalized_tasks'] = class_week[day]['max_tasks'] / total_tasks
    return class_week

class_week = {
    'monday': {"max_tasks": 12},
    'tuesday': {"max_tasks": 12},
    'wednesday': {"max_tasks": 12},
    'thursday': {"max_tasks": 12},
    'friday': {"max_tasks": 12},
    'saturday': {"max_tasks": 0},
    'sunday': {"max_tasks": 0}
}

nw = normalize_week(class_week)
tpw = fake_tasks/weeks
print(tpw, weeks)

# i need to take this normailzed week and map it to the entire school range then distribute the tasks