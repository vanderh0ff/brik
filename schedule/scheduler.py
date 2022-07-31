# how to schedule
# see how many classes need to be done
# see how many days each class has
# see how many tasks each day can have
# get start date

week = {
        'monday': {'max_tasks':12},
        'tuesday': {'max_tasks':12},
        'wednesday': {'max_tasks':12},
        'thursday': {'max_tasks':12},
        'friday': {'max_tasks':12},
        'saturday': {'max_tasks':12},
        'sunday': {'max_tasks':12}
        } 

def initialize_week():
    # get the db connection
    db.week.insert_many


# differnt ways to schedule
# have a target start and end date and evenly distribute tasks 
# have a start and ideal task density then calculate how long it will take


