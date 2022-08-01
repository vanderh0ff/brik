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


# differnt ways to schedule
# have a target start and end date and evenly distribute tasks
# have a start and ideal task density then calculate how long it will take


def schedule_class_by_task_weight(start_date:str="TODAY"):
    if start_date == "TODAY":
        start_date = datetime.date.today()
    else:
        start_date = datetime.date.fromisoformat(start_date)
    current_day = 0
    current_weight = 0
    class_tasks = collection.find({'subject': 'MS Physical Science'})
    lw = list(week)
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

def schedule_class_by_target_date(start_date_string: str, target_date_string: str):
    start_date = datetime.date.fromisoformat(start_date_string)
    target_date = datetime.date.fromisoformat(target_date_string)
    pass


def get_this_weeks_schedule():
    query = {
        'scheduled_for': {
            '$lt': datetime.datetime.today() + datetime.timedelta(days=7)
        }
    }
    this_week = db.tasks.find(query)
