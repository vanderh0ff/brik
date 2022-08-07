import datetime
import math
import pprint

fake_tasks = 100
start_date = datetime.date.fromisoformat("2022-05-01")
end_date = datetime.date.fromisoformat("2022-05-30")
number_of_days = end_date - start_date
weeks = math.ceil(number_of_days.days/7.0)

def total_task_span(start_date, end_date, class_week):
    delta_days = end_date - start_date
    week_max_tasks = []
    for weekday in class_week.items():
        week_max_tasks.append(weekday[1]['max_tasks'])
    total_task_value = 0
    for day in range(delta_days.days):
        current_day = start_date + datetime.timedelta(days=day)
        total_task_value += week_max_tasks[current_day.weekday()]
    return total_task_value

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



# i need to take this normailzed week and map it to the entire school range then distribute the tasks

def gen_tasks(number_of_tasks:int):
    tasks = []
    for task_number in range(number_of_tasks):
        tasks.append({
          'id': task_number,
          'weight': 1
        })
    return tasks

def stack_tasks(start_date, class_name):
    tasks_to_schedule = gen_tasks(fake_tasks)
    task_week = list(map((lambda x: x['max_tasks']),class_week.values()))
    current_day = start_date
    current_weight = 0
    for x in range(len(tasks_to_schedule)):
        current_weight += tasks_to_schedule[x]['weight']
        while current_weight > task_week[current_day.weekday()]:
            current_weight -= task_week[current_day.weekday()]
            current_day = current_day + datetime.timedelta(days=1)
        tasks_to_schedule[x]['scheduled_for'] = current_day
    return tasks_to_schedule
    
    pass
def distribute_tasks(start_date, end_date, class_name):
    # get class tasks and class weekday, we are using fake values for testing
    # real one will go and get from the db
    tasks_to_schedule = gen_tasks(fake_tasks)
    # initilize current day and task weight counter for loop
    task_weight_counter = 0
    current_day = start_date
    task_week = list(map((lambda x: x['max_tasks']),class_week.values()))
    # calculate the total available task slots and how many we consume to evenly distribute tasks
    tts = total_task_span(start_date, end_date, class_week)
    task_increment = tts/fake_tasks
    for n in range(len(tasks_to_schedule)):
        tasks_to_schedule[n]['scheduled_for'] = current_day
        task_weight_counter += task_increment
        while task_weight_counter >= task_week[current_day.weekday()]:
            task_weight_counter -= task_week[current_day.weekday()]
            current_day = current_day + datetime.timedelta(days=1)
    return tasks_to_schedule


#final = distribute_tasks(start_date, end_date, 'fake class')
final = stack_tasks(start_date, 'fake class')
pprinter = pprint.PrettyPrinter()
pprinter.pprint(final)