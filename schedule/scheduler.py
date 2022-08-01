import datetime

# how to schedule
# see how many classes need to be done
# see how many days each class has
# see how many tasks each day can have
# get start date


def initialize_week():
    week = {
        'monday': {'max_tasks': 12},
        'tuesday': {'max_tasks': 12},
        'wednesday': {'max_tasks': 12},
        'thursday': {'max_tasks': 12},
        'friday': {'max_tasks': 12},
        'saturday': {'max_tasks': 12},
        'sunday': {'max_tasks': 12}
    }
    # get the db connection
    for day in week:
        db.week.insert_one({day: week[day]})


def get_class_week(class_name:str):
    this_class = db.classes.find_one({"name":class_name})
    return this_class['week']

# differnt ways to schedule
# have a target start and end date and evenly distribute tasks
# have a start and ideal task density then calculate how long it will take


def schedule_class_by_task_weight(class_name:str, start_date:str="TODAY"):
    if start_date == "TODAY":
        start_date = datetime.date.today()
    else:
        start_date = datetime.date.fromisoformat(start_date)
    current_day = 0
    current_weight = 0
    class_tasks = collection.find({'subject': class_name})
    lw = get_class_week(class_name)
    while True:
        try:
            task = class_tasks.next()
            current_weight += task['weight']
            if current_weight > week[lw[current_day % 7]]['max_tasks']:
                current_day += 1
                current_weight = task['weight']
            query = {'_id': task['_id']}
            update = {"$set":
                      {'scheduled_for': datetime.datetime.combine(
                          start_date + datetime.timedelta(
                              days=current_day
                          ),
                          datetime.time.min)
                       }
                      }
            db.tasks.update_one(query, update)
        except:
            break

def normalize_week(class_week):
    total_tasks = sum(map((lambda x: int(x['max_tasks'])),class_week))
    normalized_week = list(map((lambda x: float(x['max_tasks'])/total_tasks),class_week))
    return normalized_week

def schedule_class_by_target_date(class_name: str, start_date_string: str, target_date_string: str):
    start_date = datetime.date.fromisoformat(start_date_string)
    target_date = datetime.date.fromisoformat(target_date_string)
    class_week = get_class_week(class_name)
    # since we cant just use the values in the schedule we get an idea of the
    # workload wanted on each day by dividing the max tasks per day against
    # the sum of the weeks max tasks
    normalized_week = normalize_week(class_week)
    # we then get the number of days we want to finish in
    schedule_time_delta = target_date - start_date
    number_of_days = schedule_time_delta.days
    # then for each day we look up the normalized task weight for and add
    # it to a total so we can distribute the tasks to the weighted days
    # of the week
    normalized_task_total = 0.0
    for x in range(number_of_days):
        normalized_task_total += normalized_week[x%7]
    class_tasks = collection.find({'$and':[{'subject': class_name},{'completed':False}]})
    num_tasks = class_tasks.retrieved






def get_this_weeks_schedule():
    query = {
        'scheduled_for': {
            '$lt': datetime.datetime.today() + datetime.timedelta(days=7)
        }
    }
    this_week = db.tasks.find(query)
