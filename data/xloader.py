from pymongo import MongoClient
import urllib.parse
from openpyxl import load_workbook

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('schooltime')

client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
db = client.brik
collection = db.tasks

wb = load_workbook(filename = "test-data/bf65d610-e3a5-4870-ab7d-d01db2419fff.xlsx", read_only=True)
ws = wb.active

tasks = []
total_tasks = 0
in_chapter = False
last_lesson = None
last_chapter = None
for row in ws.rows:
    if "Grade" in repr(row[0].value):
        total_tasks += int(row[0].value.split(':')[2])
    if "Chapter" in repr(row[0].value):
        if "Test" not in row[0].value:
            last_chapter = row[0].value
            in_chapter = True
            continue
    if in_chapter:
        if row[0].value == "Worksheet":
            continue
        if "Lesson:" in repr(row[0].value):
            last_lesson = row[0].value
            continue
        elif "Week of:" in repr(row[0].value):
            in_chapter = False
        else:
            tasks.append({"task":row[0].value,
                          "lesson":last_lesson,
                          "chapter":last_chapter})
