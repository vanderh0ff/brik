from data import db,xloader
import os
import sys

collection = db.db.tasks

data_path = 'test-data'
data_files = os.listdir(data_path)
for data_file in data_files:
    tasks = xloader.extract_with_preprocess(os.path.join(data_path, data_file))
    collection.insert_many(tasks)


